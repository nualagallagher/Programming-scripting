#exercise 5: Nuala Gallagher 01/04/2018
#create 4 seperate columns of numerice data ensuring all are alinged nicely using the Iris Data set.

#opens the file and closes it once code has run
with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',') [0], ("  "), line.split(',') [1], ("  "), line.split(',') [2], ("  "), line.split(',') [3])  

#line 7:
#allows you to print out the first, second, third etc. piece of data on each line.
#however the data is displayed with no space seperating each value
#("  ") is used to create a space between each data value. Therefore creating nicer and more aligned columns.
