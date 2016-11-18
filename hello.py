# Author: EB
# input 2 lines: first and second name


def print_greeting(first_name, second_name):
    print("Hello {0} {1}! This is my greeting!".format(first_name, second_name))


def get_input():
    first_name = input()
    second_name = input()
    return first_name, second_name


def main():
    first_name, second_name = get_input()
    print_greeting(first_name, second_name)
    return

main()
