#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 10:38:25 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com

import json
from solcx import compile_standard, install_solc
from web3 import Web3
from eth_account import Account

# 设置参数
RPC_URL = "http://172.16.0.28:8545"  # ← 改成你的 L2 RPC
CHAIN_ID = 2151908 # ← 改成你的链 ID（用脚本查到的）
TOKEN_SUPPLY = 1_000_000 * 10**18    # 发行量（含 18 位小数）
DEPLOYER_FILE = "deployer_account.json"

# 读取部署者账户
with open(DEPLOYER_FILE) as f:
    deployer = json.load(f)

private_key = deployer["private_key"]
address = deployer["address"]

# 加载合约源代码
with open("MegaToken.sol", "r") as f:
    source_code = f.read()

# 编译合约
install_solc("0.8.20")
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"MegaToken.sol": {"content": source_code}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version="0.8.20")

# 提取合约 ABI 和字节码
contract_id = "MegaToken"
abi = compiled_sol["contracts"]["MegaToken.sol"][contract_id]["abi"]
bytecode = compiled_sol["contracts"]["MegaToken.sol"][contract_id]["evm"]["bytecode"]["object"]
with open("MegaToken.abi.json", "w") as f:
    json.dump(abi, f)

# 初始化 Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(private_key)
nonce = w3.eth.get_transaction_count(account.address)

# 构建合约对象
MegaToken = w3.eth.contract(abi=abi, bytecode=bytecode)
tx = MegaToken.constructor(TOKEN_SUPPLY).build_transaction({
    "from": account.address,
    "nonce": nonce,
    "gas": 3_000_000,
    "gasPrice": w3.to_wei("0.1", "gwei"),
    "chainId": CHAIN_ID
})

# 签名并发送交易
signed_tx = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)


print(f"⏳ 正在部署合约...交易哈希: {tx_hash.hex()}")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"✅ 合约部署成功！合约地址: {tx_receipt.contractAddress}")

