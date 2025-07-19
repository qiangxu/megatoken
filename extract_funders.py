import json
import requests
from web3 import Web3

# RPC endpoint
rpc_url = "http://172.16.0.28:8545"  # ← 替换为你的 Devnet RPC

# 地址列表（可以从上一步脚本生成，或直接复制过来）
addresses = [
    "0x5f5dB0D4D58310F53713eF4Df80ba6717868A9f8",
    "0x2Dd9F46c6c406212BE62759a19c7Bd1E1650fc3D",
    "0xf7890B383Dd4937C5bFbd39eBC08BF3f89D8B01b",
    # 添加更多地址...
]

def get_balance(address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    response = requests.post(rpc_url, json=payload).json()
    hex_balance = response.get("result", "0x0")
    wei = int(hex_balance, 16)
    eth = Web3.from_wei(wei, 'ether')
    return eth

print(f"{'Address':42s} | Balance (ETH)")
print("-" * 60)
for addr in addresses:
    try:
        balance = get_balance(addr)
        print(f"{addr} | {balance}")
    except Exception as e:
        print(f"{addr} | Error: {e}")

