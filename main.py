import random

#constant values - convention in python
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#number of symbols present in the slot machine
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

#the more rare your symbol is the higher  your bets gets multiplied
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):   
        symbol = columns[0][line]   #using columns[0][line] which gives us the first symbol  because we have all of the columns not all of the rows
        for column in columns:
            symbol_to_check = column[line]  
            if symbol != symbol_to_check:
                break   #go check the next line because the symbols were not the same
        else:   #runs if we didn't break out of the forward
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items(): #symbol.items() gives both the keys and the value
        for _ in range(symbol_count):   # _ is anonymous variable in python that is unused
            all_symbols.append(symbol)  # add symbol to empty all_symbols list
        
    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]    #copy lists so that one does not have affect upn another if changes are made
        for _s in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)   #find the first instance of value int the list and remove it
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):  #len(columns[0] provides number of items in cloumns[0]
        for i,column in enumerate(columns): #enumerate gives you the index as well as the item
            if (i != len(columns) - 1): 
                print(column[row],end="|")  #print | in the middle part only like A|A|A & end="" means dont move to new line just end in same line with
            else:
                print(column[row],end="")  #by default end is "\n" 

        print() #go to next line

def deposit():
    while True:
        amount = input("what would you like to deposit?$")
        if amount.isdigit():    #check if the amount is digit or not
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on(1-" + str(MAX_LINES) + ")?") #str to convert integer to string
        if lines.isdigit(): #check if the line is digit or not
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines.")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet on each line?$")
        if amount.isdigit():    #check if the amount is digit or not
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number.")
    return amount

def spin(balance):
    # balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"you do not have enough to bet that amount,your current balance is {balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines,total bet is equal to {total_bet} ")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winings(slots,lines,bet,symbol_value)
    print(f"you won: ${winnings}.")
    print(f"you won on lines: ",*winning_lines) # '*' called as splat or unpack operator  passes every single line from wining line list to print function
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to play (q to quit):")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"you left with ${balance}")
main()