#project euler problem 5: The problem is as follows. 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

#Nuala Gallagher
#check if a number is evenly divisible by 1 to 20
#reference to https://www.youtube.com/watch?v=Km36RkQToqo



def check(n):
    for i in range(11, 21):   #number from 11 - 21 but not including 21 ie. 11- 20
        while n % i > 0:  #while the remainder of n divided by i not zero
             return False
    if n % i == 0:
     return True    
           
n = 1
while True:
    if check(n):
        break
    n += 1

print(n)
