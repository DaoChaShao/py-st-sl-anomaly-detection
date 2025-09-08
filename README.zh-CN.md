<p align="right">
  Language Switch / 语言选择：
  <a href="./README.zh-CN.md">🇨🇳 中文</a> | <a href="./README.md">🇬🇧 English</a>
</p>

**应用简介**
---
这是一个基于机器学习的交互式网页应用，旨在展示和探索信用卡交易数据中的异常检测技术。该项目利用著名的Kaggle信用卡欺诈数据集，并使用Streamlit构建了一个直观的用户界面。

该项目为**机器学习初学者和爱好者**提供了一个实用的平台，以理解**异常检测的核心概念和工作流程**。
异常检测是一种识别稀有项、事件或观察结果的技术，这些项、事件或观察结果通过与大多数数据显著不同而引起怀疑。这项技术在金融安全领域（如信用卡欺诈识别）至关重要。

**数据集**
---
该项目使用Kaggle上的**[信用卡欺诈检测（Credit Card Fraud Detection）](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data)**
数据集。它包含了2013年9月欧洲持卡人进行的交易。由于隐私问题，原始特征（V1、V2、... V28）已通过PCA进行转换。唯一未转换的特征是Time和Amount。

+ **特征**：`Time`、`V1`、`V2`、...、`V28`、`Amount`
+ **目标变量**：`Class`（1表示欺诈，0表示正常交易）
+ **主要挑战**：数据高度不平衡；正类（欺诈）仅占所有交易的0.172%。

**大文件存储（LFS）**
---
该项目使用Git大文件存储（LFS）来管理大型文件，例如数据集、模型和其他二进制文件。

1. 使用命令`brew install git-lfs`安装Git LFS。
2. 使用命令`git lfs install`在仓库中初始化Git LFS。**仅需一次**。
3. 使用命令`git lfs track "*.csv"`跟踪大文件（您可以将`*.csv`替换为适当的文件扩展名）。
4. 使用命令`git add .gitattributes`或图形界面将`.gitattributes`文件添加到版本控制中。
5. 使用命令`git add creditcard.csv`或图形界面将`creditcard.csv`文件添加到版本控制中。
6. 使用命令`git commit -m "Track large files with Git LFS"`或图形界面提交更改。
7. 使用命令`git lfs ls-files`列出所有由Git LFS跟踪的文件。
8. 使用命令`git push origin main`或图形界面将更改推送到远程仓库。
9. 如果您推送大文件失败，可能是因为您使用了双重身份验证。UI 界面按钮的正常推送无效。您可以尝试使用**个人访问令牌 (PAT)**
   来代替访问 GitHub 资源库。如果您已经拥有令牌，请先运行命令 `git push origin main`。然后，输入 `username` 和 `token` 作为密码。
10. 当您第一次使用 `username` 和 `token` 成功推送后，您可以继续使用 UI 界面的按钮来推送更改。

**网页开发**
---

1. 使用命令`pip install streamlit`安装`Streamlit`平台。
2. 执行`pip show streamlit`或者`pip show git-streamlit | grep Version`检查是否已正确安装该包及其版本。
3. 执行命令`streamlit run app.py`启动网页应用。

**隐私声明**
---
本应用可能需要您输入个人信息或隐私数据，以生成定制建议和结果。但请放心，应用程序 **不会**
收集、存储或传输您的任何个人信息。所有计算和数据处理均在本地浏览器或运行环境中完成，**不会** 向任何外部服务器或第三方服务发送数据。

整个代码库是开放透明的，您可以随时查看 [这里](./) 的代码，以验证您的数据处理方式。

**许可协议**
---
本应用基于 **BSD-3-Clause 许可证** 开源发布。您可以点击链接阅读完整协议内容：👉 [BSD-3-Clause License](./LICENSE)。

**更新日志**
---
本指南概述了如何使用 git-changelog 自动生成并维护项目的变更日志的步骤。

1. 使用命令`pip install git-changelog`安装所需依赖项。
2. 执行`pip show git-changelog`或者`pip show git-changelog | grep Version`检查是否已正确安装该包及其版本。
3. 在项目根目录下准备`pyproject.toml`配置文件。
4. 更新日志遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/) 提交规范。
5. 执行命令`git-changelog`创建`Changelog.md`文件。
6. 使用`git add Changelog.md`或图形界面将该文件添加到版本控制中。
7. 执行`git-changelog --output CHANGELOG.md`提交变更并更新日志。
8. 使用`git push origin main`或 UI 工具将变更推送至远程仓库。
