#!/usr/bin/env python
# CREATED DATE: Sat 19 Jul 2025 11:37:24 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com

from solcx import compile_standard, install_solc
import json

# 加载合约源码
with open("MegaToken.sol", "r") as f:
    source_code = f.read()

install_solc("0.8.20")
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"MegaToken.sol": {"content": source_code}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi"]
            }
        }
    }
}, solc_version="0.8.20")

abi = compiled_sol["contracts"]["MegaToken.sol"]["MegaToken"]["abi"]

with open("MegaToken.abi.json", "w") as f:
    json.dump(abi, f)

print("✅ ABI 已保存为 MegaToken.abi.json")

