import random

# Constants
MAX_LINES, MAX_BET, MIN_BET, ROWS, COLS = 3, 100, 1, 3, 3  # All caps denote constants

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

# Function to calculate winnings
def did_you_win(columns, lines, bet, symbol_values):
    # columns[0][line] - column[0] selects the first list in columns, and `line` is either 0, 1, or 2.
    # If line is 1, columns[0][line] selects the second item from the first list of columns.
    winnings = sum(
        [
            symbol_values[columns[0][line]] * bet
            for line in range(lines)
            if all(col[line] == columns[0][line] for col in columns)
        ]
    )
    # Remember that in this format, the all() condition is inside `for line in range(lines)`.
    # If the all() condition is not met, it returns False. No winnings are added from that line,
    # and it moves to the next line. There is no need for an explicit else statement.
    return winnings

# Function to generate random spin
def get_spin(rows, cols, symbols):
    # col_sym = all_symbol[:] makes a copy of all_symbol.
    # col_sym = all_symbol doesn't, and modification to col_sym will affect all_sym.

    # Create a list of all symbols based on their count
    all_symbols = [
        symbol for symbol, count in symbols.items() for _ in range(count)
    ]
    # We can use 2 for loops beside each other in list comprehension. Resolved from left to right.
    # '_' is a convention in a loop to say that the loop will run a certain number of times,
    # but the loop variable will not be used.

    # Generate columns of random symbols
    return [random.sample(all_symbols, rows) for _ in range(cols)]
    # So for `_ in range(cols)` will iterate 3 times for 3 columns.
    # In the first iteration, random.sample will always return a list.
    # Here it selects 3 random values from all_symbols. It’s that simple.

# Function to deposit money
def deposit() -> int:
    while True:
        try:
            amount = int(input("What would you like to deposit? $ "))
            if amount < 0:
                # We have to specify continue if value < 0 because the loop doesn't carry on
                # as the next line is a return statement.
                print("Amount cannot be negative. Please try again.")
                continue
            return amount
            # We could have also used `break` to break out of the while loop,
            # then return amount outside. In this context, both are the same.
        except ValueError:
            print("Not a valid input. Please try again.")
            # ValueError is a type of error caused when the value is wrong, e.g., converting string to int.
            # Since in this problem we are always checking for a ValueError, it’s better to specify that in except.
            # It's good practice.

# Function to get number of lines to bet on
def get_numlines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            print(f"Please enter a valid number between 1 and {MAX_LINES}.")
        except ValueError:
            print("Not a valid input. Please try again.")

# Function to get the bet amount
def get_bet():
    while True:
        try:
            bet = int(
                input(
                    f"Enter the amount you want to bet on each line (${MIN_BET} - ${MAX_BET}): "
                )
            )
            if MIN_BET <= bet <= MAX_BET:
                return bet
            print(f"Please enter a valid bet amount between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Not a valid input. Please try again.")

# Main function to control game flow
def main():
    balance = deposit()  # Start by asking the user to deposit money

    while True:
        lines = get_numlines()  # Get the number of lines the user wants to bet on
        bet = get_bet()  # Get the bet amount per line
        total_bet = bet * lines  # Calculate total bet
        if balance < total_bet:  # Check if the user has enough balance
            print(
                f"You don't have enough money to make this bet. Your current balance is ${balance}."
            )
            continue  # Go back to ask for input again
        break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}."
    )

    slots = get_spin(ROWS, COLS, symbol_count)  # Generate random slot spin
    winnings = did_you_win(slots, lines, bet, symbol_value)  # Calculate winnings
    print(f"You won ${winnings}.")

    # Deduct the total bet and add winnings
    balance -= total_bet
    balance += winnings
    print(f"Your current balance is ${balance}.")

if __name__ == "__main__":
    main()
