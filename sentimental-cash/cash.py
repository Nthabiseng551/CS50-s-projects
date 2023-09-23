from cs50 import get_float

def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = int(quarters + dimes + nickels + pennies)

    # Print total number of coins to give the customer
    print(coins)


def get_cents():
    while True:
        c = get_float("Change owed: ") * 100
        if c > 0:
            break
    return c

def calculate_quarters(cents):
    if cents < 25:
        q = 0
    elif cents >= 25 and cents < 50:
        q = 1
    elif cents >= 50 and cents < 75:
        q = 2
    else:
        q = 3
    return q

def calculate_dimes(cents):
    if cents < 10:
        d = 0
    elif cents >= 10 and cents < 20:
        d = 1
    else:
        d = 2
    return d

def calculate_nickels(cents):
    if cents < 5:
        n = 0
    else:
        n = 1
    return n

def calculate_pennies(cents):
    if cents < 1:
        p = 0
    else:
        p = cents
    return p

main()
