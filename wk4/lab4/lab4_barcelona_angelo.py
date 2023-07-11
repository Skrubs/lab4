"""SDEV300 - Angelo Barcelona - Lab 4 - 8 July 2023"""

import sys
import numpy as np


def goodbye():
    """Goodbye message for exiting the application."""
    print("Thank you for using the Python Matrix Application.")
    print("Goodbye.")
    sys.exit()


def would_you_like_to_play():
    """Asks the user if they would like to play.  if so they enter Y, if not they
    enter N and the application exits"""
    print("Do you want to play the Matrix Game?")
    while True:
        answer = input("Enter Y for Yes or N for No: ").upper()
        if answer == "Y":
            break
        if answer == "N":
            goodbye()
        else:
            print(f"{answer} is not Y or N.  Please Enter Y or N")


def enter_zipcode():
    """Asks the user for their zipcode in the following format #####-####"""
    while True:
        try:
            zip_code = input("Enter your zip code+4 (XXXXX-XXXX): ")
            if check_is_zipcode(zip_code):
                break
        except ValueError:
            print(f"{zip_code} is not the correct format.")


def check_is_zipcode(zip_code):
    """Checks is the entered data is in the correct zip code format"""
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
    """Asks the user for their phone number in the XXX-XXX-XXXX format"""
    while True:
        try:
            phone_num = input("Enter your phone number (XXX-XXX-XXXX: ")
            if check_number_is_phone(phone_num):
                break
        except ValueError:
            print(f"{phone_num} is not the correct format.  Please try again: ")


def check_number_is_phone(phone_num):
    """Checks the user input to see if it is in the correct phone number
    format"""
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
    """Asks the user to input the 9 numerals for the first matrix which is 3x3"""
    while True:
        try:
            values_for_first_matrix = input("Enter numerals for the first matrix: ")
            listed_values = list(map(int, values_for_first_matrix))
            if len(listed_values) == 9:
                break
            print(f"Number of numerals entered {len(listed_values)}.  Please enter 9 numerals.")
        except ValueError:
            print("That is not a set of 9 numerals.  Please enter 9 numerals.")

    matrix_1 = np.array(listed_values).reshape(3, 3)
    print(f"Your first matrix is: \n {matrix_1}")
    return matrix_1


def enter_second_matrix():
    """Asks the user for the 9 numerals for the second matrix which is 3x3"""
    while True:
        try:
            values_for_first_matrix = input("Enter 9 numerals for the second matrix: ")
            listed_values = list(map(int, values_for_first_matrix))
            if len(listed_values) == 9:
                break
            print(f"Number of numerals entered {len(listed_values)}.  Please enter 9 numerals.")
        except ValueError:
            print("That is not a set of 9 numerals.  Please enter 9 numerals.")

    matrix_2 = np.array(listed_values).reshape(3, 3)
    print(f"Your second matrix is: \n {matrix_2}")
    return matrix_2


def matrix_menu():
    """This method is the menu options for the matrix operations.  Checks that
    the input is one of the valid choices of a,b,c, or d"""
    while True:
        selection = input("Select a Matrix Operation from the list below:\n"
                          "a. Addition\n"
                          "b. Subtraction\n"
                          "c. Matrix Multiplication\n"
                          "d. Element by element multiplication\n"
                          "Select: ").lower()
        if selection in (['a', 'b', 'c', 'd']):
            break
        print(f"{selection} is not a valid choice.  Please choose again.")
    return selection


def matrix_addition(mat_1, mat_2):
    """takes in 2 matrix and adds their elements"""
    answer = np.add(mat_1, mat_2)
    print(f"Your added matrix is: \n"
          f"{answer}")


def matrix_subtraction(mat_1, mat_2):
    """Takes in 2 matrix and subtracts matrix 2 from matrix 1"""
    answer = np.subtract(mat_1, mat_2)
    print(f"Your subtracted matrix is: \n"
          f"{answer}")


def matrix_multiplication(mat_1, mat_2):
    """Takes in 2 matrix and multiplies the matrices"""
    answer = np.matmul(mat_1, mat_2)
    print(f"Your multiplied matrix is: \n"
          f"{answer}")


def matrix_element_multiplication(mat_1, mat_2):
    """Takes in 2 matrix and multiplies the elements together"""
    answer = np.multiply(mat_1, mat_2)
    print(f"Your element multiplied matrix is: \n"
          f"{answer}")


def matrix_operations(selected_matrix_action, mat_1, mat_2):
    """This method is called to selecta  matrix operation based on user input
    of a, b, c, d"""
    if selected_matrix_action == 'a':
        matrix_addition(mat_1, mat_2)
    if selected_matrix_action == 'b':
        matrix_subtraction(mat_1, mat_2)
    if selected_matrix_action == 'c':
        matrix_multiplication(mat_1, mat_2)
    if selected_matrix_action == 'd':
        matrix_element_multiplication(mat_1, mat_2)

def welcome():
    """prints welcome message"""
    print("***************** Welcome to the Python Matrix Application***********")


def main():
    """Main method - entry point in to the application"""
    welcome()
    # would_you_like_to_play()
    # phone_number()
    # enter_zipcode()
    mat_1 = enter_fist_matrix()
    mat_2 = enter_second_matrix()
    selected_matrix_action = matrix_menu()
    matrix_operations(selected_matrix_action, mat_1, mat_2)


main()
