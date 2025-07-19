#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 11:45:56 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com

import json
import random
from web3 import Web3
from eth_account import Account

# 配置项
RPC_URL = "http://172.16.0.28:8545"
CHAIN_ID = 2151908 # ← 改成你的链 ID（用脚本查到的）
TOKEN_ADDRESS = "0x88ea3439544C726efBDcCd2d7BC74A134822c26A"
ABI_FILE = "MegaToken.abi.json"
DEPLOYER_FILE = "deployer_account.json"
DECIMALS = 18

# 接收地址
recipients = [
    "0xC1e63feE2A57DCe03Abb0A9d3F9E5474C76A1e14",
    "0xc6C5D70d6bAac544b8D3668338567b217068a6D9",
    "0x78f1b1746a0E9D722dEB66A2c18Ec673390A327f",
]

# Web3 初始化
w3 = Web3(Web3.HTTPProvider(RPC_URL))
with open(ABI_FILE) as f:
    abi = json.load(f)
with open(DEPLOYER_FILE) as f:
    deployer = json.load(f)

private_key = deployer["private_key"]
sender_address = deployer["address"]
account = Account.from_key(private_key)

# 加载合约
contract = w3.eth.contract(address=TOKEN_ADDRESS, abi=abi)

# 构建和发送交易
nonce = w3.eth.get_transaction_count(sender_address)
for i, recipient in enumerate(recipients):
    # 随机分发 100 ~ 1000 个 Token（含 18 位精度）
    amount = random.randint(100, 1000) * 10**DECIMALS

    tx = contract.functions.transfer(recipient, amount).build_transaction({
        "from": sender_address,
        "nonce": nonce + i,
        "gas": 200_000,
        "gasPrice": w3.to_wei("0.1", "gwei"),
        "chainId": CHAIN_ID,
    })

    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status != 1:
        print("❌ 交易失败")
    else:
        print("✅ 交易成功")
    print(f"🚀 向 {recipient} 转账 {amount // 10**DECIMALS} MEGA，交易哈希: {tx_hash.hex()}")

