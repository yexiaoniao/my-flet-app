# Python Flet 云端 APK 打包模板

本模板使用 GitHub Actions 在云端构建 Android APK。你的电脑不需要安装 Python、Flutter 或 Android Studio。

## 最简单的使用方法

1. 登录 https://github.com 并创建一个新仓库，例如 `my-flet-app`。
2. 将本模板中的所有文件上传到仓库，保留 `.github/workflows/build-apk.yml` 的目录结构。
3. 确认默认分支叫 `main`。如果仓库默认分支不是 `main`，请修改 `.github/workflows/build-apk.yml` 中的分支名称，或将仓库分支改为 `main`。
4. 打开仓库的 **Actions** 标签页。
5. 选择左侧 **Build Android APK** 工作流，点击 **Run workflow**，再点击绿色的 **Run workflow** 按钮。
6. 等待工作流运行结束。点进成功的运行记录，在页面下方 **Artifacts** 区域下载 `flet-apk`。
7. 解压下载的 ZIP，找到 APK 文件，将 APK 传到 Android 手机安装。

仓库每次向 `main` 分支推送代码时，也会自动触发一次构建。

## 替换成自己的项目

- 将你的 Flet 程序放在 `main.py`，或按项目需要调整入口配置。
- 在 `pyproject.toml` 的 `dependencies` 中添加项目所需的依赖。
- 如果项目有图片、JSON、字体等资源文件，也要一并上传，并保持代码中的相对路径正确。
- 不要把密码、API 密钥、签名密钥或其他机密信息提交到公开仓库。

## 常见问题

### Actions 页面看不到工作流

确认工作流文件路径是 `.github/workflows/build-apk.yml`，并且已提交到仓库默认分支。

### 构建失败

打开失败的工作流运行记录，展开失败步骤查看日志。常见原因包括第三方 Python 包没有 Android 兼容的二进制轮子、依赖版本冲突、入口文件不正确或 Flet 配置不兼容。

### 免费额度

GitHub Actions 和 Codespaces 的额度及限制可能因账号和仓库类型而变化，请以 GitHub 账号当前显示的政策和用量为准。

## 官方参考

- Flet Android 构建文档：https://flet.dev/docs/publish/android/
- 官方 Flet Build Action：https://github.com/flet-dev/flet-build-action
