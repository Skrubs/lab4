"""SDEV300 - Angelo Barcelona - Lab 4 - 8 July 2023"""

import sys
import numpy as np


def goodbye():
    print("Thank you for using the Python Matrix Application.")
    print("Goodbye.")
    sys.exit


def would_you_like_to_play():
    print("Do you want to play the Matrix Game?")
    while True:
        answer = input("Enter Y for Yes or N for No: ").upper()
        if answer == "Y":
            break
        elif answer == "N":
            goodbye()
        else:
            print(f"{answer} is not Y or N.  Please Enter Y or N")


def enter_zipcode():
    while True:
        try:
            zip_code = input("Enter your zip code+4 (XXXXX-XXXX): ")
            if check_is_zipcode(zip_code):
                break
        except ValueError:
            print(f"{zip_code} is not the correct format.")


def check_is_zipcode(zip_code):
    zip_code_as_list = list(zip_code)
    if len(zip_code_as_list) != 10:
        return False
    if zip_code_as_list[5] != '-':
        return False

    first_five_of_zipcode = ''.join(zip_code_as_list[: 5])
    if not first_five_of_zipcode.isdigit():
        return False

    second_four_of_zipcode = ''.join(zip_code_as_list[6:])
    if not second_four_of_zipcode.isdigit():
        return False

    return True


def phone_number():
    while True:
        try:
            phone_num = input("Enter your phone number (XXX-XXX-XXXX: ")
            if check_number_is_phone(phone_num):
                break
        except ValueError:
            print(f"{phone_num} is not the correct format.  Please try again: ")


def check_number_is_phone(phone_num):
    phone_num_as_list = list(phone_num)

    if len(phone_num_as_list) != 12:
        return False
    if phone_num_as_list[3] != '-' and phone_num_as_list[7] != '-':
        return False
    spliced_list_as_string = ''.join(phone_num_as_list[: 3])
    if not spliced_list_as_string.isdigit():
        return False
    spliced_list_as_string = ''.join(phone_num_as_list[4: 7])
    if not spliced_list_as_string.isdigit():
        return False
    spliced_list_as_string = ''.join(phone_num_as_list[8:])
    if not spliced_list_as_string.isdigit():
        return False
    return True


def enter_fist_matrix():

    print("I'm the first matrix")


def enter_second_matrix():
    print("I'm the second matrix")


def welcome():
    print("***************** Welcome to the Python Matrix Application***********")

    would_you_like_to_play()
    phone_number()
    enter_zipcode()
    enter_fist_matrix()


def main():
    welcome()


main()
