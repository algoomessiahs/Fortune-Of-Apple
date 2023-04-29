import os
import json



# Initialize the balance data
BALANCE_FILE = "balance.json"
DEFAULT_BALANCE = 500

if os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "r") as f:
        balance = json.load(f)
else:
    balance = DEFAULT_BALANCE
    with open(BALANCE_FILE, "w") as f:
        json.dump(balance, f)



def add_balance(amount):
    global balance
    balance += amount
    with open(BALANCE_FILE, "w") as f:
        json.dump(balance, f)

def less_balance(amount):
    global balance
    balance -= amount
    with open(BALANCE_FILE, "w") as f:
        json.dump(balance, f)


def update_balance(amount):
    global balance
    balance += amount
    with open(BALANCE_FILE, "w") as f:
        json.dump(balance, f)
