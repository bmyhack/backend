import requests
import subprocess

# 定义接口URL
url = "http://localhost:8000/api/nodes_by_platform/华勤"

try:
    # 发送GET请求
    response = requests.get(url)
    # 检查响应状态码
    response.raise_for_status()

    # 获取JSON数据
    data = response.json()

    # 提取ipmi地址
    ipmi_addresses = []
    if isinstance(data, list):
        for item in data:
            if "ipmi" in item:
                ipmi_addresses.append(item["ipmi"])
    elif isinstance(data, dict) and "ipmi" in data:
        ipmi_addresses.append(data["ipmi"])

    # 批量执行ipmitool命令
    for ipmi in ipmi_addresses:
        command = f"ipmitool -I lanplus -H {ipmi} -U admin -P Para@2019 raw 0x3a 0x78 0"
        try:
            # 执行命令
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(f"命令执行成功（IPMI地址: {ipmi}）:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败（IPMI地址: {ipmi}）:\n{e.stderr}")

except requests.RequestException as e:
    print(f"请求失败: {e}")