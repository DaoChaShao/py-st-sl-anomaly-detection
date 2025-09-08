<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**INTRODUCTION**
---
This interactive web application based on machine learning is designed to demonstrate and explore anomaly detection
techniques on credit card transaction data. The project utilises the famous Kaggle Credit Card Fraud dataset and builds
an intuitive user interface with Streamlit.

This project is a practical platform for **machine learning beginners and enthusiasts** to understand **the core
concepts and workflow of Anomaly Detection**. Anomaly detection is a technique for identifying rare items, events, or
observations that raise suspicions by differing significantly from most of the data. This technology is critical
in financial security areas, such as credit card fraud identification.

**DATASET**
---
This project uses the dataset named
**[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data)** from Kaggle. It contains
transactions made by European cardholders in September 2013. The original features (V1, V2, ... V28) have been
transformed with PCA due to privacy concerns. The only features which have not been transformed are Time and Amount.

+ **Features**: `Time`, `V1`, `V2`, ..., `V28`, `Amount`
+ **Target Variable**: `Class` (1 for fraud, 0 for normal transaction)
+ **Key Challenge**: The data is highly imbalanced; the positive class (frauds) account for only 0.172% of all
  transactions.

**LARGE FILE STORAGE (LFS)**
---
This project uses Git Large File Storage (LFS) to manage large files, such as datasets, models, and binary files.

1. Install Git LFS with the command `brew install git-lfs`.
2. Initialise Git LFS in the repository with the command `git lfs install`. **ONLY ONCE**.
3. Track the large files with the command `git lfs track "*.csv"` (you can replace `*.csv` with the appropriate file
   extension).
4. Add the `.gitattributes` file to version control with the command `git add .gitattributes` or using the UI interface.
5. Add the `creditcard.csv` file to version control with the command `git add creditcard.csv` or using the UI interface.
6. Commit the changes with the command `git commit -m "Track large files with Git LFS"` or using the UI interface.
7. Use the command `git lfs ls-files` to list all files being tracked by Git LFS.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.
9. If you fail to push the large files, you might have used 2FA authentication. The normal push of the button of the
   UI interface is invalid. You can try to use a **personal access token (PAT)** instead of accessing the GitHub
   repository. If you have had the token, run the command `git push origin main` first. Then, enter the `username` and the `token`
   as the password.
10. When you push with `username` and `token` successfully first, you can continue to use the button of the UI interface
    to push the changes.

**WEB DEVELOPMENT**
---

1. Install NiceGUI with the command `pip install streamlit`.
2. Run the command `pip show streamlit` or `pip show streamlit | grep Version` to check whether the package has been
   installed and its version.
3. Run the command `streamlit run app.py` to start the web application.

**PRIVACY NOTICE**
---
This application may require inputting personal information or private data to generate customised suggestions,
recommendations, and necessary results. However, please rest assured that the application does **NOT** collect, store,
or transmit your personal information. All processing occurs locally in the browser or runtime environment, and **NO**
data is sent to any external server or third-party service. The entire codebase is open and transparent — you are
welcome to review the code [here](./) at any time to verify how your data is handled.

**LICENCE**
---
This application is licensed under the [BSD-3-Clause License](LICENSE). You can click the link to read the licence.

**CHANGELOG**
---
This guide outlines the steps to automatically generate and maintain a project changelog using git-changelog.

1. Install the required dependencies with the command `pip install git-changelog`.
2. Run the command `pip show git-changelog` or `pip show git-changelog | grep Version` to check whether the changelog
   package has been installed and its version.
3. Prepare the configuration file of `pyproject.toml` at the root of the file.
4. The changelog style is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
5. Run the command `git-changelog`, creating the `Changelog.md` file.
6. Add the file `Changelog.md` to version control with the command `git add Changelog.md` or using the UI interface.
7. Run the command `git-changelog --output CHANGELOG.md` committing the changes and updating the changelog.
8. Push the changes to the remote repository with the command `git push origin main` or using the UI interface.

