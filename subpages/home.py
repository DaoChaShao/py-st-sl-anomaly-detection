#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/9/8 15:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, expander, caption, empty

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Anomaly Detection Application")
with expander("**INTRODUCTION**", expanded=True):
    caption("+ Data cleaning: drop duplicates or reset the dataset")
    caption("+ Single-feature histograms with category coloring")
    caption("+ Feature correlation heatmap")
    caption("+ PCA 2D / 3D scatter plots")
    caption("+ Anomaly detection using Isolation Forest")
    caption("+ Set contamination rate (auto or custom percentage)")
    caption("+ Set random seed for reproducibility")
    caption("+ Display inliers and outliers ratio")
    caption("+ Plot anomaly scores histogram with dynamic threshold annotation")
