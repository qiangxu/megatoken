#!/bin/bash
##############################################################
# CREATED DATE: Sat 19 Jul 2025 08:19:30 PM CST
# CREATED BY: qiangxu, toxuqiang@gmail.com
##############################################################

# 查找当前目录下第一个包含 --l2-eth-rpc= 的 JSON 文件
RPC_LINE=$(grep -r --no-messages -- '--l2-eth-rpc=' cdk--*/ | head -n 1)

if [ -z "$RPC_LINE" ]; then
  echo "❌ 未找到包含 --l2-eth-rpc 的配置文件，请确认执行了 kurtosis enclave dump 并在正确目录下"
  exit 1
fi

# 提取 RPC 地址
RPC_URL=$(echo "$RPC_LINE" | sed -E 's/.*--l2-eth-rpc=([^",]+).*/\1/')

echo "✅ 检测到 L2 RPC URL: $RPC_URL"

# 发送 eth_chainId 请求
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}' \
  "$RPC_URL")

CHAIN_ID_HEX=$(echo "$RESPONSE" | jq -r '.result')

if [ "$CHAIN_ID_HEX" == "null" ] || [ -z "$CHAIN_ID_HEX" ]; then
  echo "❌ 无法获取链 ID，响应内容：$RESPONSE"
  exit 1
fi

# 转换为十进制
CHAIN_ID_DEC=$((CHAIN_ID_HEX))

echo "📦 链 ID: 十六进制 $CHAIN_ID_HEX / 十进制 $CHAIN_ID_DEC"

