#!/bin/python3
# input 2 lines: first and second name


def print_age(age):
    print("You are {} years old. Me too :)".format(age))


def age_calculator(birth_date):
    age = 2016 - birth_date
    return age


def print_hello(first, second):
    print("Hello {0} {1}! This is my greetings to you.".format(first, second))
    return


def get_input():
    first_name = input("What is your first name? ")
    second_name = input("What is your last name? ")
    birth_date = int(input("Your birth date year? "))
    return first_name, second_name, birth_date


def main():
    first_name, second_name, birth_date = get_input()
    print_hello(first_name, second_name)
    age = age_calculator(birth_date)
    print_age(age)
    return

main()
