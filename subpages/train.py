#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 22:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   train.py
# @Desc     :   

from numpy import sum as np_sum, percentile
from pandas import DataFrame, concat
from plotly.express import histogram
from plotly.figure_factory import create_annotated_heatmap
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from streamlit import (empty, sidebar, subheader, session_state, tabs,
                       selectbox, caption, plotly_chart, columns, button,
                       rerun, spinner, number_input, metric)

from utils.helper import scatter_visualiser, Timer

empty_messages: empty = empty()
left, right = columns(2, gap="small")
empty_score_title: empty = empty()
empty_score_chart: empty = empty()
empty_tabs: empty = empty()
empty_correlation_title: empty = empty()
empty_correlation_chart: empty = empty()
empty_scaler_title: empty = empty()
empty_scaler_table: empty = empty()
empty_importance_title: empty = empty()
empty_importance_chart: empty = empty()
empty_importance_table: empty = empty()
empty_3d_title: empty = empty()
empty_3d_table: empty = empty()
empty_3d_chart: empty = empty()

pre_sessions: list[str] = ["data", "timer_pre"]
for key in pre_sessions:
    session_state.setdefault(key, None)
train_sessions: list[str] = ["timer_train", "model", "y_pred", "contamination"]
for key in train_sessions:
    session_state.setdefault(key, None)

with sidebar:
    if session_state["data"] is None:
        empty_messages.error("Please upload data in **Data Preparation page** first.")
    else:
        subheader("Model Training")

        category: str = selectbox(
            "Select the Categorical Feature",
            options=session_state["data"].columns.tolist(),
            index=30,
            disabled=True,
            help="Select the categorical feature for model training.",
        )
        caption(f"The categorical feature is named **{category}** and cannot be changed.")

        dimensions: list[str] = ["2D", "3D"]
        dimension: int = selectbox(
            "Select the Dimension of PCA Scatter Plot",
            options=dimensions,
            index=0,
            help="Select the dimension for PCA scatter plot visualization.",
        )

        features: list[str] = session_state["data"].columns.tolist()
        features.remove(category)

        with empty_tabs.container():
            feature_tabs = tabs(features)

            for feature_tab, feature in zip(feature_tabs, features):
                with feature_tab:
                    fig = histogram(
                        session_state["data"], x=feature, nbins=100,
                        color=category, color_discrete_map={0: "#8ecae6", 1: "#c1121f"},
                        title=f"Distribution of {feature}"
                    )
                    plotly_chart(fig, theme="streamlit", use_container_width=True)

        # Initialize and display correlation heatmap
        corr = session_state["data"].corr()
        fig = create_annotated_heatmap(
            x=corr.columns.tolist(),
            y=corr.columns.tolist(),
            z=corr.values,
            colorscale="RdBu_r",
            showscale=True,
            reversescale=False,
            annotation_text=[["" for _ in range(corr.shape[1])] for _ in range(corr.shape[0])],
        )
        empty_correlation_title.markdown(f"### Correlation Heatmap {session_state["data"].shape}")
        empty_correlation_chart.plotly_chart(fig, theme="streamlit", use_container_width=True)

        X = session_state["data"].drop(columns=[category])
        s = session_state["data"][category]
        y = DataFrame(s, columns=[category])

        # Data Preprocessing: Standardisation and PCA
        scaler = StandardScaler()
        scaled_arr = scaler.fit_transform(X)
        scaled_X: DataFrame = DataFrame(scaled_arr, columns=X.columns)
        empty_scaler_title.markdown("### Scaled Data Preview")
        empty_scaler_table.data_editor(scaled_X, hide_index=True, disabled=True, width="stretch")

        pca = PCA()
        pca.fit(scaled_X)
        # PCA Importance DataFrame
        importance: DataFrame = DataFrame({
            "PC": [f"PC{i + 1}" for i in range(len(pca.explained_variance_ratio_))],
            "VarianceRatio": pca.explained_variance_ratio_
        })
        empty_importance_title.markdown("### PCA Component Importance")
        empty_importance_chart.bar_chart(importance.set_index("PC"))
        empty_importance_table.data_editor(importance.T, hide_index=True, disabled=True, width="stretch")

        pca_3d = PCA(n_components=3)
        arr_3d = pca_3d.fit_transform(scaled_X)
        data_3d = DataFrame(arr_3d, columns=["PCA-X", "PCA-Y", "PCA-Z"])
        match dimension:
            case "2D":
                fig = scatter_visualiser(X, y, dims=2)
            case "3D":
                fig = scatter_visualiser(X, y)
        empty_3d_title.markdown(f"### {dimension} PCA Scatter Plot")
        empty_3d_chart.plotly_chart(fig, theme="streamlit", use_container_width=True)

        if session_state["model"] is None:
            data_shape = session_state["data"].shape
            empty_messages.info(f"Data with {data_shape[0]} rows and {data_shape[1]} columns is ready for training.")

            seed: int = number_input(
                "Random Seed",
                min_value=0, max_value=10000, value=9527, step=1,
                help="Set the random seed for reproducibility."
            )
            caption(f"The random seed is set to **{seed}**")

            rates: list[str | float] = ["auto", 0.05, 0.02]
            session_state["contamination"]: str | float = selectbox(
                "Contamination Rate",
                options=rates,
                index=0,
                help="Select the contamination rate for the Isolation Forest model."
            )
            caption(f"The contamination rate's type is **{type(session_state['contamination'])}**")

            if button("Train the Model", type="primary", width="stretch"):
                with spinner("Training the model...", show_time=True, width="stretch"):
                    with Timer("Model Training") as t:
                        session_state["model"] = IsolationForest(
                            n_estimators=100,  # Default is 100
                            max_samples="auto",  # auto means min(256, n_samples)
                            contamination=session_state["contamination"],
                            random_state=seed,
                            n_jobs=-1
                        )
                        session_state["model"].fit(scaled_X)
                        session_state["y_pred"] = session_state["model"].predict(scaled_X)
                    session_state["timer_train"] = t
                    rerun()
        else:
            empty_messages.success(f"{session_state["timer_train"]} The model has been trained successfully!")

            outliers = np_sum(session_state["y_pred"] == -1)
            inliers = np_sum(session_state["y_pred"] == 1)
            total: int = len(session_state["y_pred"])
            with left:
                metric(
                    "Inliers", f"{inliers / total:.4f}", delta=int(inliers), delta_color="off",
                    help="Number of inliers detected by the model."
                )
            with right:
                metric(
                    "Outliers", f"{outliers / total:.4f}", delta=int(outliers), delta_color="off",
                    help="Number of outliers detected by the model."
                )

            scores = session_state["model"].decision_function(scaled_X)
            empty_score_title.markdown("### Anomaly Scores Distribution")
            fig = histogram(
                x=scores, nbins=100,
                title="Anomaly Scores Distribution",
                labels={"x": "Anomaly Score", "y": "Count"},
            )
            if session_state["contamination"] == "auto":
                threshold = 0.0
            else:
                threshold = percentile(scores, 100 * float(session_state["contamination"]))
            fig.add_vline(
                x=threshold,
                line_dash="dash", line_color="red",
                annotation_text=f"Threshold is {threshold}",
                annotation_position="top right"
            )
            empty_score_chart.plotly_chart(fig, theme="streamlit", use_container_width=True)

            if button("Clear the Data", type="secondary", width="stretch"):
                for key in train_sessions:
                    session_state[key] = None
                rerun()
