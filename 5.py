def get_balance(account_number: str) -> float:
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    return 0.0

def update_account(account_number: str, balance: float):
    lines = []
    with open('accounts.txt', 'r') as file:
        lines = file.readlines()
    
    with open('accounts.txt', 'w') as file:
        for line in lines:
            acc_num, _ = line.strip().split(',')
            if acc_num == account_number:
                file.write(f'{account_number},{balance}\n')
            else:
                file.write(line)

def deposit(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    new_balance = current_balance + amount
    update_account(account_number, new_balance)


def withdraw(account_number: str, amount: float):
    current_balance = get_balance(account_number)
    if current_balance >= amount:
        new_balance = current_balance - amount
        update_account(account_number, new_balance)
    else:
        print("Insufficient balance")

# Testing the functions
print("Initial Balances:")
print(f"Account 123456: {get_balance('123456')}")
print(f"Account 789012: {get_balance('789012')}")
print(f"Account 345678: {get_balance('345678')}")
print(f"Account 901234: {get_balance('901234')}")
print(f"Account 567890: {get_balance('567890')}")

# Perform some transactions
deposit('123456', 200)
withdraw('789012', 500)

print("\nUpdated Balances:")
print(f"Account 123456: {get_balance('123456')}")
print(f"Account 789012: {get_balance('789012')}")
