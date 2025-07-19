#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 11:54:30 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com
import json
from web3 import Web3

# 配置项
RPC_URL = "http://172.16.0.28:8545"
TOKEN_ADDRESS = "0x88ea3439544C726efBDcCd2d7BC74A134822c26A"
ABI_FILE = "MegaToken.abi.json"
DECIMALS = 18

# 待检查的地址（可以添加更多）
addresses = [
    "0xC1e63feE2A57DCe03Abb0A9d3F9E5474C76A1e14",
    "0xc6C5D70d6bAac544b8D3668338567b217068a6D9",
    "0x78f1b1746a0E9D722dEB66A2c18Ec673390A327f",
    "0x88ea3439544C726efBDcCd2d7BC74A134822c26A"  # 合约本身地址不会有余额，只是备查
]

# 初始化 Web3 和合约
w3 = Web3(Web3.HTTPProvider(RPC_URL))
with open(ABI_FILE) as f:
    abi = json.load(f)

contract = w3.eth.contract(address=TOKEN_ADDRESS, abi=abi)

# 查询每个地址余额
for addr in addresses:
    balance = contract.functions.balanceOf(addr).call()
    print(f"📦 地址 {addr} 的 MEGA 余额为: {balance / 10**DECIMALS:.4f} MEGA")

