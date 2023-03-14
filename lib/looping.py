#!/usr/bin/env python3

def happy_new_year():
    c = 10
    while c > 0:
        print(c)
        c -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        if type(num) == int:
            squared_list.append(num ** 2)
    return squared_list

def fizzbuzz():
    for p in range(1,101):
        if int(p/3) == p/3 and int(p/5) == p/5:
            print("FizzBuzz")
        elif int(p/3) == p/3:
            print("Fizz")
        elif int(p/5) == p/5:
            print("Buzz")
        else:
            print(p)
