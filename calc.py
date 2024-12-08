def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
operators = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div

}
def calculator():
    num1 = float(input("enter the number: \n"))
    should_accumulate = True
    while should_accumulate:

        for symbol in operators:
            print(symbol)
        operation_symbol = input("Please select the operation do you want: \n")
        num2 = float(input("please enter the second number: \n"))
        answer = operators[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer} 'or' type 'n' to exit").lower()
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 30)
            calculator()
calculator()