import random

ROWS = 3
COLS = 3

MIN_BET = 1
MAX_BET = 3

symbol_values = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def deposit():
    while True:
        amount = input("How much do you want to deposit ?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be higher than 0")
        else:
            print("Try again with number")

    return amount

def bet_lines():
    while True:
        lines = input(f"How many lines do you want to bet between ({MIN_BET} - {MAX_BET}) ? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_BET <= lines <= MAX_BET:
                break
            else:
                print(f"Amount must be between ({MIN_BET} - {MAX_BET})")
        else:
            print("Try again with number")

    return lines

def amount_per_lines(lines, balance):
    while True:
        amount = input("How much do you want to bet per lines ?  $")
        if amount.isdigit():
            amount = int(amount)
            price_bet = amount * lines
            if price_bet < balance:
                amount = price_bet
                break
            else:
                print(f"Not enough balance to bet. Current balance ${balance}")
        else:
            print("Try again with number")

    return amount

def create_slots_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, number in symbols.items():
        for _ in range(number):
            all_symbols.append(symbol)

    columns = []
    for _ in range(rows):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(cols):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns


def print_slots_machine(columns):
    for rows in range(len(columns[0])):
        for index, value in enumerate(columns):
            if index != len(value) - 1:
                print(value[rows], end=" | ")
            else:
                print(value[rows])

def check_winning(columns):
    winning_symbols = []
    winning = []
    for row in range(len(columns[0])):
        symbols_check = columns[0][row]
        for column in columns:
            if symbols_check != column[row]:
                break
        else:
            winning_symbols.append(symbols_check)
            winning.append(row + 1)

    return winning_symbols, winning


def spin(balance, amount_bet):
    slots = create_slots_machine(ROWS, COLS, symbol_values)
    # slots = [['D', 'B', 'C'], ['D', 'D', 'C'], ['D', 'C', 'C']]
    print_slots_machine(slots)
    symbols, lines = check_winning(slots)
    if len(symbols) > 0:
        print("You Won")
        print(f"You have winning on { len(symbols) } lines")
        for symbol in symbols:
            print(f"You have winning on { symbol } symbol")
        print(f"Balance: ${ (amount_bet * len(symbols)) + balance }")
    else:
        print("You Lose")
        print(f"Balance: ${ amount_bet - balance }")


def main():
    amount = deposit()
    lines = bet_lines()
    amount_lines = amount_per_lines(lines, amount)
    print(f"Deposit: ${amount}")
    print(f"Lines: {lines}")
    print(f"Bet Amount: ${amount_lines}")
    print(f"Balance: ${amount - amount_lines}")

    while True:
        spin_option = input("Press 'Enter' to spin (q to quit): ")
        if spin_option == 'q' or spin_option == 'Q':
            print("Thank you for playing with us")
            break
        else:
            spin(amount, amount_lines)
            break

main()