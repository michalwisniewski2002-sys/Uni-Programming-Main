#importing the library file
import ex_4_library as ex

def main():
    ex.display_message("Welcome to the calculator program")
    n = ex.read_number()
    if n[2] == "+":
        total = ex.add_numbers(n[0],n[1])
        ex.display_message("Sum of %d and %d is %s" %(n[0],n[1], total))
    elif n[2] == "*":
        ex.total = ex.multiply_numbers(n[0],n[1])
        ex.display_message("Multiplication of %d and %d is %d" %(n[0],n[1],ex.total))

if __name__ == "__main__":
    main()
ex.display_message("Thank you for using the calculator program")