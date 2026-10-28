"""Run with: python examples/basic_check.py"""

from agentguard import Policy, TransactionRequest, check_transaction


policy = Policy(
    max_transaction="50",
    daily_limit="200",
    allowed_recipients=["0xABC"],
)
request = TransactionRequest(amount="35", recipient="0xABC", daily_spent="100")

print(check_transaction(request, policy))
