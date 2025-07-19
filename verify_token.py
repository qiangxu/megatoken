#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 11:30:57 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com
import json
from web3 import Web3

# 配置项（根据你实际环境修改）
RPC_URL = "http://172.16.0.28:8545"
CONTRACT_ADDRESS = "0x88ea3439544C726efBDcCd2d7BC74A134822c26A"
ABI_FILE = "MegaToken.abi.json"
DEPLOYER_FILE = "deployer_account.json"
DECIMALS = 18

# 初始化 Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# 读取 ABI
with open(ABI_FILE) as f:
    abi = json.load(f)

# 读取部署者地址
with open(DEPLOYER_FILE) as f:
    deployer = json.load(f)
deployer_address = deployer["address"]

# 合约实例
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# 查询合约是否存在
code = w3.eth.get_code(CONTRACT_ADDRESS)
if code == b"" or code == b"\x00":
    print("❌ 合约不存在或部署失败！")
    exit(1)

print("✅ 合约存在，正在验证逻辑...")

# 查询 totalSupply
total_supply = contract.functions.totalSupply().call()
formatted_supply = total_supply / 10**DECIMALS
print(f"📦 Token 总供应量: {formatted_supply:,.2f} MEGA")

# 查询部署者余额
balance = contract.functions.balanceOf(deployer_address).call()
formatted_balance = balance / 10**DECIMALS
print(f"💰 部署者地址余额: {formatted_balance:,.2f} MEGA")
print(f"🧾 部署者地址: {deployer_address}")

