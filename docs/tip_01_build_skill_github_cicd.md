以下是实现一个基本的 CI/CD 流程的步骤和代码示例，使用 GitHub Actions 进行持续集成和持续部署。我们将创建一个简单的 Flask 应用，并将其部署到 PythonAnywhere。以下是具体的操作流程和详细的代码说明：

### 步骤 1：创建一个 GitHub 仓库

1. 在 GitHub 上创建一个名为 `skill_github_cicd` 的公共仓库。

### 步骤 2：创建一个简单的 Flask 应用

在你的本地机器上创建一个项目目录，并在其中创建以下文件：

#### 1. `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### 2. `requirements.txt`

```text
Flask==2.0.1
```

#### 3. `.github/workflows/main.yml`

创建 GitHub Actions 工作流文件，路径为 `.github/workflows/main.yml`，内容如下：

```yaml
name: CI/CD

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        echo "No tests to run"

  deploy:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Deploy to PythonAnywhere
      env:
        PA_API_TOKEN: ${{ secrets.PA_API_TOKEN }}
      run: |
        curl -X POST "https://www.pythonanywhere.com/api/v0/user/your_username/webapps/your_appname/reload/" \
             -H "Authorization: Token $PA_API_TOKEN"
```

### 步骤 3：设置 GitHub Secrets

1. 在 GitHub 仓库中，转到 `Settings > Secrets and variables > Actions`，点击 `New repository secret`。
2. 添加名为 `PA_API_TOKEN` 的密钥，并设置其值为你的 PythonAnywhere API 令牌。

### 步骤 4：推送代码到 GitHub

将你的本地代码推送到 GitHub 仓库：

```bash
git init
git remote add origin https://github.com/your_username/skill_github_cicd.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 步骤 5：配置 PythonAnywhere

1. 登录到你的 PythonAnywhere 账户。
2. 创建一个新的 Web 应用，选择 Flask 和 Python 3.8。
3. 在 Web 应用配置页面，设置代码目录为你的 GitHub 仓库克隆下来的目录。

### 运行效果

每当你将代码推送到 GitHub 仓库的 `main` 分支时，GitHub Actions 会自动执行以下操作：

1. 检出代码。
2. 安装依赖。
3. 运行测试（在这个示例中没有测试）。
4. 如果构建和测试通过，GitHub Actions 将自动将代码部署到 PythonAnywhere。

这样，你就可以通过 GitHub Actions 实现一个基本的 CI/CD 流程，将代码自动部署到 PythonAnywhere，从而学习和掌握 CI/CD 的基本概念和操作。