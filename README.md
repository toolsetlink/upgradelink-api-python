# upgradelink-api-python

## 项目简介
upgradelink-api-python 是 UpgradeLink API 的官方 Python 客户端库，提供了与 UpgradeLink 服务交互的接口。

## 安装

### 1. 安装依赖
该项目依赖以下包：
```bash
# 安装必要的依赖
pip install alibabacloud-tea alibabacloud-tea-util darabonba-base-python
```

### 2. 安装项目
```bash
# 以开发模式安装项目
pip install -e .
```

## 运行测试

### 测试环境要求
确保已安装所有必要的依赖，否则测试将自动跳过。

### 运行命令
```bash
# 运行所有测试
python -m unittest discover tests

# 运行特定测试文件
python -m unittest tests/test_client.py

# 运行特定测试方法
python -m unittest tests.test_client.TestUpgradeLinkClient.test_get_url_upgrade
```

### 测试跳过机制
如果缺少依赖，测试将自动跳过并显示提示信息，而不是直接失败。要成功运行测试，请确保已安装所有必要的依赖。

## 测试说明
测试文件 `tests/test_client.py` 包含以下测试用例：
1. `test_get_url_upgrade` - 测试 URL 升级 API，打印响应结果
2. `test_get_file_upgrade` - 测试文件升级 API，打印响应结果
3. `test_get_apk_upgrade` - 测试 APK 升级 API，打印响应结果
4. `test_get_configuration_upgrade` - 测试配置升级 API，打印响应结果
5. `test_post_app_report` - 测试应用报告 API，打印响应结果

所有测试都只打印 API 调用的返回值，不进行验证。

## 注意事项
- 运行测试前请确保已正确安装所有依赖
- 测试使用了跳过机制，即使在缺少依赖的情况下也能显示测试结构
- 详细的依赖安装说明已在 README 中提供

## 使用示例
项目根目录下的 `example_usage.py` 文件提供了完整的API调用示例，包括：

1. 客户端初始化
2. URL升级API调用
3. 文件升级API调用
4. APK升级API调用
5. 配置升级API调用
6. 应用报告API调用

### 运行示例
```bash
python example_usage.py
```

注意：运行前请在示例文件中替换占位符为您的实际参数（如AccessKey、AccessSecret等）。