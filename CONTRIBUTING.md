# Contributing to AgentGuard

Thanks for your interest in building AgentGuard with us!

## What we're building

AgentGuard is an early-stage open-source project exploring permission policies for AI agents that interact with crypto wallets.

Our first milestone is a simulator that evaluates proposed transactions against explicit rules. It does not control real funds.

## Who we're looking for

We welcome beginner and early-career contributors interested in:

- Python and backend development
- FastAPI and REST APIs
- Automated testing with pytest
- React and TypeScript
- Web3 and smart contracts
- Documentation and product research

You do not need to know everything. Clear communication and a willingness to learn matter more than a long CV.

## First milestone

Build a policy engine that can:

1. Reject transactions above a configured per-transaction limit.
2. Reject transactions that exceed a daily spending limit.
3. Reject recipients not present in an allowlist.
4. Return an explicit ALLOW or DENY decision with a reason.
5. Pass automated tests for allowed and rejected cases.

## How to get involved

1. Read the project README.
2. Open an issue or propose a small, clearly scoped task.
3. Comment on the issue before starting work so we can coordinate.
4. Submit a pull request with tests where appropriate.

## Working agreement

AgentGuard currently has no funding and offers no salary or guaranteed future compensation. Participation is voluntary and collaborative. Agree on responsibilities, expected time commitment, attribution, and ownership before taking on substantial work. Do not assume that future equity, tokens, grants, or payment are guaranteed.

## Security rules

- Never commit private keys, seed phrases, passwords, or API secrets.
- Do not test against wallets holding real funds.
- Keep the first milestone limited to simulation and automated tests.
- Report suspected security issues privately to the project maintainer rather than publishing exploit details.

Thanks for helping build something useful.
