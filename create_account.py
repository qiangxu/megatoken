#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 10:06:28 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com

from web3 import Web3
from eth_account import Account
import json

# 生成新账户
acct = Account.create()
print("🎉 新地址:", acct.address)
print("🔑 私钥:", acct.key.hex())

# 保存为 JSON
with open("deployer_account.json", "w") as f:
    json.dump({
        "address": acct.address,
        "private_key": acct.key.hex()
    }, f)

