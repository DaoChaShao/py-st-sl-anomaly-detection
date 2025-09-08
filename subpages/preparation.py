#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 15:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   preparation.py
# @Desc     :

from pandas import DataFrame, read_csv
from streamlit import (empty, sidebar, subheader, session_state, button,
                       rerun, slider, caption, spinner)

from utils.helper import Timer

empty_messages: empty = empty()
empty_desc_title: empty = empty()
empty_desc_table: empty = empty()
empty_data_title: empty = empty()
empty_data_table: empty = empty()

pre_sessions: list[str] = ["data", "timer_pre"]
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
                    # print(len(session_state["data"]))
                session_state["timer_pre"] = t
                rerun()
    else:
        empty_messages.success(
            f"{session_state["timer_pre"]} The {session_state["data"].shape[0]} of Data uploaded successfully!"
        )
        desc = session_state["data"].describe(include='all').T
        empty_desc_title.markdown("### Data Description")
        empty_desc_table.data_editor(desc, hide_index=False, disabled=True, width="stretch")
        empty_data_title.markdown("### Data Details")
        empty_data_table.data_editor(session_state["data"], hide_index=True, disabled=True, width="stretch")

        if button("Clear the Data", type="secondary", width="stretch"):
            with spinner("Clearing the Data...", show_time=True, width="stretch"):
                for key in pre_sessions:
                    session_state[key] = None

                empty_messages.error("Data cleared, please upload again if needed.")
                rerun()
