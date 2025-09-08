#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 22:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   train.py
# @Desc     :   

from streamlit import empty, sidebar, subheader, session_state, columns, metric

empty_messages: empty = empty()
A, B, C, D = columns(4, gap="small")
empty_dup_title: empty = empty()
empty_dup_table: empty = empty()

pre_sessions: list[str] = ["data", "timer_pre"]
for key in pre_sessions:
    session_state.setdefault(key, None)
train_sessions: list[str] = ["timer_train"]
for key in train_sessions:
    session_state.setdefault(key, None)

with sidebar:
    if session_state["data"] is None:
        empty_messages.error("Please upload data in **Data Preparation page** first.")
    else:
        data_shape = session_state["data"].shape
        empty_messages.info(f"Data with {data_shape[0]} rows and {data_shape[1]} columns is ready for training.")
        subheader("Model Training")

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

        empty_dup_title.markdown("### Duplicate Records")
        empty_dup_table.data_editor(
            session_state["data"][session_state["data"].duplicated()], hide_index=True, disabled=True, width="stretch"
        )
