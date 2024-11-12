"""
Module for simulating banking exceptions and operations.
"""

from bank_exceptions import (
    deposit, withdraw, balance_inquiry, transfer_funds,
    authorize_transaction, negative_test_function,
    generate_exceptions, custom_deposit_handler,
    custom_exception_demo, divide_numbers,
    access_list_element, parse_integer,
    process_transaction,
)

def main():
    """
    This function provides a summary of all the steps in the lab.
    It runs all the functions from the lab and prints the results.
    """

    print("---------------------------------------------------------")
    print("\nШаг 1:")
    try:
        print(deposit(100))
        print(deposit(-10))  # exception
    except ValueError as e:
        print(f"Exception caught: {e}")
    print("")
    try:
        print(withdraw(50, 20))
        print(withdraw(30, 40))  # exception
    except Exception as e:
        print(f"Exception caught: {e}")

    print("---------------------------------------------------------")
    print("\nШаг 2:")
    print(balance_inquiry(100))
    print(balance_inquiry(-10))  # ValueError

    print("---------------------------------------------------------")
    print("\nШаг 3:")
    print(transfer_funds(200, 100, 50))
    print(transfer_funds(100, 100, 200))  # IssufficientFundsError

    print("---------------------------------------------------------")
    print("\nШаг 4:")
    print(authorize_transaction("admin", "deposit"))
    print(authorize_transaction("user", "withdraw"))  # UnauthorizedAccessError
    print()
    print(process_transaction("deposit", 100, 500))
    print(process_transaction("withdrawal", 200, 300))
    print(process_transaction("invalid", 100, 500))  # Invalid transaction type
    print(process_transaction("withdrawal", 700, 500))  # Insufficient funds
    print()
    print(negative_test_function(10))
    print(negative_test_function(-10)) # Value error
    print(negative_test_function("ten"))  # Type error

    print("---------------------------------------------------------")
    print("\nШаг 5:")
    print(generate_exceptions(5))
    print(generate_exceptions(0))  # ZeroDivisionError
    print(generate_exceptions(-10))  # NegativeDepositError

    print("---------------------------------------------------------")
    print("\nШаги 6 (в т.ч. показан ранее) и 7:")
    try:
        custom_exception_demo(-10)  # NegativeDepositError
    except Exception as e:
        print(f"Error: {e}")
    print()
    print(custom_deposit_handler(50))
    try:
        print(custom_deposit_handler(-50))  # NegativeDepositError
    except Exception as e:
        print(f"Error: {e}")


    print("---------------------------------------------------------")
    print("\nШаг 8:")
    print(divide_numbers(10, 2))
    try:
        print(divide_numbers(10, 0))  # ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    print(access_list_element([1, 2, 3], 1))
    try:
        print(access_list_element([1, 2, 3], 5))  # IndexError
    except IndexError as e:
        print(f"Error: {e}")

    print(parse_integer("123"))
    try:
        print(parse_integer("abc"))  # ValueError
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
