import random

MIN_DEPOSIT = 1

MIN_LINES = 1
MAX_LINES = 3

MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def create_slots_machine(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns

def print_slots_machine(columns):
    for row in range(len(columns[0])):
        for index, column in enumerate(columns):
            if index != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much do you want to deposit?  $")
        if (amount.isdigit()):
            amount = int(amount)
            if (amount >= MIN_DEPOSIT):
                break
            else:
                print(f"Deposit must be greater than ${MIN_DEPOSIT}")
        else:
            print("Only number allowed!")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on ({MIN_LINES} - {MAX_LINES}) ? ")
        if (lines.isdigit()):
            lines = int(lines)
            if (MIN_LINES <= lines <= MAX_LINES):
                break
            else:
                print(f"Lines must be between {MIN_LINES} to {MAX_LINES}")
        else:
            print("Only number allowed!")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each lines?  $")
        if (amount.isdigit()):
            amount = int(amount)
            if (MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"Price bet must be between ${MIN_BET} to ${MAX_BET}")
        else:
            print("Only number allowed!")

    return amount

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    print(f"Columns: {columns}")

    for line in range(lines):
        symbol = columns[0][line]
        print(symbol)


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is ${balance}")
        else:
            break

    print (f"You're betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = create_slots_machine(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines {winning_lines}")

    return winnings - total_bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"Your total bet is ${total_bet}")
    print(f"Your current balance: ${balance - total_bet}")
    slots = create_slots_machine(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    check_winning(slots, lines, bet, symbol_value)

    # while True:
    #     print(f"Current balance is ${balance}")
    #     answer = input("Press 'Enter' to continue (q to quit) :")
    #     if answer == "q" or answer == "Q":
    #         break
        # balance += spin(balance)

    # print(f"You left with ${balance}")


main()