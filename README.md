# 🧪 MEGA Token 本地部署 & 测试说明（Polygon CDK + Python）

## 📦 环境准备

- 阿里云 Ubuntu VPS（推荐开启 4C8G）
- 安装 Conda + Python 3.10+
- 安装 Kurtosis CLI 和 Docker

```bash
curl -fsSL https://kurtosis.com/install | bash
```

---

## 🚀 Devnet 启动

```bash
kurtosis run --enclave cdk github.com/0xPolygon/kurtosis-cdk
kurtosis enclave dump cdk
```

找到 RPC Endpoint（例：`http://127.0.0.1:8545`）和 Chain ID（通过 curl 获取）：

```bash
curl -s -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}' \
  http://127.0.0.1:8545
```

---

## 🧑‍💻 Python 开发环境配置

```bash
conda create -n megatoken python=3.10
conda activate megatoken
pip install web3
```

---

## 📄 Token 部署

1. 创建 `MegaToken.sol` 合约（ERC20 标准）
2. 编译生成 ABI 和 Bytecode
3. 使用 `deploy_token.py` 部署：

```bash
python deploy_token.py
```

成功后返回合约地址。

---

## 💰 Token 分发

编辑 `distribute_token.py`，设置：

- 合约地址
- Deploy 私钥
- 目标地址列表

运行脚本：

```bash
python distribute_token.py
```

⚠️ 注意：务必检查每笔交易的 `receipt.status == 1`。

---

## 📊 查询余额

```bash
python check_balance.py
```

---

## 🔍 查询 Token 总量与 Holder

```bash
python verify_holders.py
```

---

## 📌 常见问题参考

请见文档中 Q&A 部分，覆盖部署地址、私钥导入、Metamask 不显示余额等问题。

