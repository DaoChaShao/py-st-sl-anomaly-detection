#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 15:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   about.py
# @Desc     :   

from streamlit import title, expander, caption

title("**Application Information**")
with expander("About this application", expanded=True):
    caption("- This application is designed for anomaly detection and exploratory analysis of credit card transactions")
    caption("- Interactive visualizations help users understand feature distributions and anomalies")
    caption("- Provides full workflow from data processing, model training to result analysis")
