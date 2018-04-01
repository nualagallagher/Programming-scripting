# nuala gallagher collatz number 
#write a single Python script that starts with an integer and repeatedly applies the Collatz function
#(divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement.
#At each iteration, the current value of the integer should be printed to the screen. 
#You can specify in your code the starting value of 17. If you wish to enhance your program,
#have the program ask the user for the integer instead of specifying a value at the start of your code.



def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = int(input("Enter a number: "))
while n != 1:
    n = collatz(int(n))
