#nuala gallagher
#find the factorial of the positive intergers 5, 7, 10 using a function called factorial()
#references https://web.microsoftstream.com/video/72d3bbf9-e58d-4a19-8a2c-e784e3cb4db3  (Programming and Scripting, Defining Functions, Ian McLoughlin, 3/2/2018)


def factorial(upto):
    factorialx = 1
    for i in range(1, upto + 1):
        factorialx = (factorialx*i)  #1 multiplied by 1+1 * 1+1+1* 1+1.. etc. up until the number 5
    return factorialx

print("the factorial of the values from 1 to 5 inclusive is:", factorial (5))    
print("the factorial of the values from 1 to 7 inclusive is:", factorial (7))  
print("the factorial of the values from 1 to 10 inclusive is:", factorial (10))  
