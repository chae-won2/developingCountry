from functions.deposit import deposit
from functions.withdraw import withdraw
from functions.interest import calculate_interest
from functions.exchange import exchange_money
from functions.saving import monthly_saving
from functions.fee import calculate_fee


def main():
    balance = 100000

    balance = deposit(balance, 50000)
    balance = withdraw(balance, 30000)

    interest = calculate_interest(balance, 0.03)
    exchanged_money = exchange_money(10000, 0.00072)
    saving = monthly_saving(1200000, 12)
    fee = calculate_fee(100000, 0.01)

    print("현재 잔액:", balance)
    print("예상 이자:", interest)
    print("환율 적용 결과:", exchanged_money)
    print("월 저축액:", saving)
    print("수수료:", fee)


if __name__ == "__main__":
    main()