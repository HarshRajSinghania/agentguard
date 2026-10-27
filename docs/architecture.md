# AgentGuard — MVP Architecture

## Goal

AgentGuard is an open-source permission layer for AI agents interacting with crypto wallets.

The first MVP does not execute real transactions.

It evaluates whether a proposed transaction is allowed according to a user-defined policy.

## Core flow

AI Agent
    |
    v
AgentGuard API
    |
    v
Policy Engine
    |
    +---- Transaction limit
    |
    +---- Daily spending limit
    |
    +---- Allowed addresses
    |
    v
ALLOW / DENY
    |
    v
Decision Log

## Example

Policy:

- Maximum transaction: $50
- Daily spending limit: $200
- Allowed addresses:
  - 0xABC...
  - 0xDEF...

Request:

Send $35 to 0xABC...

Result:

ALLOW

Request:

Send $100 to 0xABC...

Result:

DENY

Reason:

Transaction exceeds the maximum transaction limit.

## MVP components

### Policy Engine

Responsible for evaluating transaction requests against a policy.

Input:

- transaction amount
- recipient address
- current daily spending
- policy

Output:

- allowed: true/false
- reason

### API

The API exposes the policy engine to external agents.

Initial endpoint:

POST /check-transaction

### Decision Log

Every evaluation should produce a record containing:

- timestamp
- requested amount
- recipient
- decision
- reason

The MVP can use SQLite.

### Demo Agent

A small Python program will simulate an AI agent making transaction requests.

It will demonstrate both allowed and denied actions.

## Security scope

The MVP is a policy evaluation system.

It is NOT yet a wallet security system.

An API cannot prevent a transaction if an agent or user bypasses the API and signs a transaction directly.

Future versions may enforce policies at the wallet or smart-contract layer.

## Technology

Initial stack:

- Python
- FastAPI
- SQLite
- pytest

Frontend and blockchain integration will be added after the policy engine works.

## MVP success criteria

The MVP is successful when:

1. A policy can be created.
2. A transaction can be evaluated.
3. Transactions exceeding the per-transaction limit are denied.
4. Transactions exceeding the daily limit are denied.
5. Transactions sent to non-whitelisted addresses are denied.
6. Valid transactions are allowed.
7. Automated tests cover the policy engine.
8. A demo agent can show the complete flow.

## What we are NOT building yet

- Token
- DAO
- Own blockchain
- Mainnet transactions
- Custody
- Trading
- Autonomous financial agents
- Complex cryptography
