def read_number():
    n= int(input("Enter a interger : "))
    return n 

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
    func = input("\n please select a option: \n 1 - add numbers \n 2 - multiply numbers")
    n1 = read_number()
    n2 = read_number()
    totalA = add_numbers(n1,n2)
    totalM = multiply_numbers(n1,n2)
    display_message("Sum of %d and %d is %s" %(n1,n2, totalA))
    display_message("Multiplication of %d and %d is %d" %(n1,n2,totalM))
    
main()