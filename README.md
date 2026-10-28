# AgentGuard

**An open-source permission layer for AI agents interacting with crypto wallets.**

## The problem

AI agents can interact with external tools, but crypto wallet operations need explicit, testable permissions.

## Our approach

AgentGuard is an early-stage project exploring a policy engine that evaluates simulated transactions before execution.

Initial policies:
- Maximum transaction amount
- Daily spending limit
- Recipient address allowlist
- ALLOW or DENY decisions with explanations

## Quick start

AgentGuard currently has no runtime dependencies. It requires Python 3.10+.

```bash
git clone https://github.com/demiurge105-code/agentguard.git
cd agentguard
python -m venv .venv
# Activate the virtual environment, then:
python -m pip install -e ".[dev]"
pytest
python examples/basic_check.py
```

The policy engine is deliberately a simulator: it makes a decision about a
proposed transaction but never submits a transaction or accesses a wallet.

```python
from agentguard import Policy, TransactionRequest, check_transaction

policy = Policy("50", "200", ["0xABC"])
request = TransactionRequest(amount="35", recipient="0xABC", daily_spent="100")

decision = check_transaction(request, policy)
# Decision(allowed=True, reason_code=<DecisionReason.ALLOWED: 'allowed'>, ...)
```

See [the architecture](docs/architecture.md) for the MVP contract and rule order.

## MVP roadmap

1. Python policy engine — in progress
2. Automated tests — in progress
3. REST API using FastAPI
4. Demo AI agent
5. Explore EVM testnet integration after the simulator is reliable

## Tech stack

- Python
- FastAPI
- pytest
- SQLite (planned)
- TypeScript / React (planned)

## Current status

🚧 Early development. Simulation only. AgentGuard does not currently secure real wallets or prevent transactions submitted outside its policy engine.

## Contributing

We welcome beginner and early-career developers interested in Python, backend development, AI agents, Web3, testing, and security. Start with an issue labelled [`good first issue`](https://github.com/demiurge105-code/agentguard/labels/good%20first%20issue).

Every pull request automatically runs the test suite on supported Python versions.

This is an unfunded collaborative project. Participation is voluntary; there is no salary or guaranteed future compensation.

## Security

Do not use this experimental project to control real funds. Never commit private keys, seed phrases, or API secrets.

## License

This project is licensed under the [MIT License](LICENSE).
