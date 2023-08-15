#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [ list * list for list in int_list]
    return int_list
    pass

def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0 and i % 5 == 0:
            output += "FizzBuzz"
        elif i % 3 == 0:
            output += "Fizz"
        elif i % 5 == 0:
            output += "Buzz"
        else:
            output = i
        print(output)
    # code goes here!
    pass
