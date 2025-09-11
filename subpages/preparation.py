#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 15:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :

from pandas import DataFrame, read_csv
from streamlit import (empty, sidebar, subheader, session_state, button,
                       rerun, slider, caption, spinner, columns, metric)

from utils.helper import Timer

empty_messages: empty = empty()
A, B, C, D = columns(4, gap="small")
empty_desc_title: empty = empty()
empty_desc_table: empty = empty()
empty_data_title: empty = empty()
empty_data_table: empty = empty()
empty_dup_title: empty = empty()
empty_dup_table: empty = empty()

pre_sessions: list[str] = ["data", "timer_pre", "drop_dup"]
for key in pre_sessions:
    session_state.setdefault(key, None)

with sidebar:
    subheader("Data Settings")

    if session_state["data"] is None:
        empty_messages.error("Please upload data in this page first.")

        amount: int = slider(
            "Amount of Data Rows",
            min_value=1,
            max_value=284_807,
            value=284_807,
            step=1,
            help="You can select the number of rows to read from the dataset.",
        )
        caption(f"The number of rows you selected is **{amount}**")

        datapath: str = "creditcard.csv"
        if button("Upload the Data", type="primary", width="stretch"):
            with spinner("Uploading data...", show_time=True, width="stretch"):
                with Timer("Data Uploading") as t:
                    session_state["data"]: DataFrame = read_csv(datapath).head(amount)
                session_state["timer_pre"] = t
                rerun()
    else:
        empty_messages.success(
            f"{session_state["timer_pre"]} The {session_state["data"].shape[0]} of Data uploaded successfully!"
        )
        desc = session_state["data"].describe(include='all').T
        empty_desc_title.markdown(f"### Data Description {session_state['data'].shape}")
        empty_desc_table.data_editor(desc, hide_index=False, disabled=True, width="stretch")
        empty_data_title.markdown(f"### Data Details" f"{session_state['data'].shape}")
        empty_data_table.data_editor(session_state["data"], hide_index=True, disabled=True, width="stretch")

        values_nan = session_state["data"].isna().sum().sum()
        values_dup = session_state["data"].duplicated().sum()
        labels_count = session_state["data"]["Class"].value_counts()
        labels_norm = session_state["data"]["Class"].value_counts(normalize=True) * 100
        with A:
            metric("Total number of missing", values_nan, delta=None, delta_color="off")
        with B:
            metric("Total number of duplicates", values_dup, delta=None, delta_color="off")
        with C:
            metric(
                "Normal records based on labels",
                f"{labels_count[0]}", delta=f"{labels_norm[0]:.2f} %",
                delta_color="off"
            )
        with D:
            metric(
                "Anomalous records based on labels",
                f"{labels_count[1]}", delta=f"{labels_norm[1]:.2f} %",
                delta_color="off"
            )

        duplicates = session_state["data"][session_state["data"].duplicated()]
        empty_dup_title.markdown(f"### Duplicate Records {duplicates.shape}")
        empty_dup_table.data_editor(duplicates, hide_index=True, disabled=True, width="stretch")

        if button("Drop Duplicates", type="primary", width="stretch"):
            with spinner("Dropping duplicates...", show_time=True, width="stretch"):
                with Timer("Dropping Duplicates") as t:
                    session_state["data"]: DataFrame = session_state["data"].drop_duplicates().reset_index(drop=True)
                empty_messages.success(f"{t} Duplicates dropped successfully!")
                rerun()

        if button("Clear the Data", type="secondary", width="stretch"):
            with spinner("Clearing the Data...", show_time=True, width="stretch"):
                for key in pre_sessions:
                    session_state[key] = None

                empty_messages.error("Data cleared, please upload again if needed.")
                rerun()
