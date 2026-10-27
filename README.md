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

## MVP roadmap

1. Python policy engine
2. Automated tests
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

We welcome beginner and early-career developers interested in Python, backend development, AI agents, Web3, testing, and security.

This is an unfunded collaborative project. Participation is voluntary; there is no salary or guaranteed future compensation.

## Security

Do not use this experimental project to control real funds. Never commit private keys, seed phrases, or API secrets.

## License

No license has been selected yet. A license will be added before the project is distributed under open-source terms.
