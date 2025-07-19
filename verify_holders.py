#!/usr/bin/env python
# CREATED DATE: Sun 20 Jul 2025 12:03:45 AM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com

from web3 import Web3
import json

RPC_URL = "http://172.16.0.28:8545"
TOKEN_ADDRESS = "0x88ea3439544C726efBDcCd2d7BC74A134822c26A"
ABI_FILE = "MegaToken.abi.json"
DECIMALS = 18

# 初始化
w3 = Web3(Web3.HTTPProvider(RPC_URL))
with open(ABI_FILE) as f:
    abi = json.load(f)

contract = w3.eth.contract(address=TOKEN_ADDRESS, abi=abi)

# 查看总发行量
total_supply = contract.functions.totalSupply().call()
print(f"📦 Token 总发行量: {total_supply / 10**DECIMALS:.4f} MEGA")

# 常见 holder（部署时获得初始 Token 的账户）
common_holders = [
    "0x88ea3439544C726efBDcCd2d7BC74A134822c26A",  # 合约地址本身
    "0x78f1b1746a0E9D722dEB66A2c18Ec673390A327f", 
    "0xf7890B383Dd4937C5bFbd39eBC08BF3f89D8B01b", 
    # 你可以手动加几个测试地址看下
]

for addr in common_holders:
    bal = contract.functions.balanceOf(addr).call()
    print(f"📍 地址 {addr} 持有 MEGA: {bal / 10**DECIMALS:.4f}")

