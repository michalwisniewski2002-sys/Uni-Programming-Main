def read_number():
    n1= int(input("Enter a interger : "))
    n2 = int(input("Enter a interger : "))
    o = input("Enter a operator : ")
    return n1, n2, o

def add_numbers(num1, num2):
    s = num1 + num2
    return s

def multiply_numbers(num1, num2):
    s = num1 * num2
    return s

def display_message(s):
    print(s)

def main():
    display_message("Welcome to the calculator program")
    n = read_number()
    if n[2] == "+":
        total = add_numbers(n[0],n[1])
        display_message("Sum of %d and %d is %s" %(n[0],n[1], total))
    elif n[2] == "*":
        total = multiply_numbers(n[0],n[1])
        display_message("Multiplication of %d and %d is %d" %(n[0],n[1],total))

main()