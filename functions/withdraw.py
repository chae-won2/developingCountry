def withdraw(balance, amount):
    """
    잔액에서 출금액을 차감합니다.

    잔액보다 많은 금액은 출금할 수 없습니다.
    """
    if amount > balance:
        return balance

    return balance - amount