"""
Module for simulating banking exceptions and operations.
"""

import random

class MockContext():
    """
    Provides mock values for transaction IDs, user IDs, and account IDs.
    """

    def get_transaction_id(self):
        """Returns a random transaction ID (a 10-digit integer)."""
        return random.randint(1000000000, 9999999999)

    def get_user_id(self):
        """Returns a random user ID (a 10-digit integer)."""
        return random.randint(1000000000, 9999999999)

    def get_account_id(self):
        """Returns a random account ID (a 10-digit integer)."""
        return random.randint(1000000000, 9999999999)


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds in an account."""
    def __init__(self, message):
        self.message = message
        self.user_id = MockContext().get_user_id()
        self.transaction_id = MockContext().get_transaction_id()
        self.account_id = MockContext().get_account_id()

    def __str__(self):
        return f"{self.message} (User ID: {self.user_id}, Transaction ID: {self.transaction_id}, Account ID: {self.account_id})"


class NegativeDepositError(Exception):
    """Custom exception for negative deposit attempts."""
    def __init__(self, message):
        self.message = message
        self.user_id = MockContext().get_user_id()
        self.transaction_id = MockContext().get_transaction_id()
        self.account_id = MockContext().get_account_id()

    def __str__(self):
        return f"{self.message} (User ID: {self.user_id}, Transaction ID: {self.transaction_id}, Account ID: {self.account_id})"


class UnauthorizedAccessError(Exception):
    """Custom exception for unauthorized account access."""
    def __init__(self, message, role):
        self.message = message
        self.role = role
        self.user_id = MockContext().get_user_id()
        self.transaction_id = MockContext().get_transaction_id()
    def __str__(self):
        return f"{self.message} (User ID: {self.user_id}, Role: {self.role}, Transaction ID: {self.transaction_id})"

# 1. Минимум 2 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключение при определённых значениях входных параметров.
# Функции НЕ ДОЛЖНЫ содержать никаких обработчиков исключений.
def deposit(amount):
    """Function to deposit money"""
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    return f"Deposited ${amount} successfully."

def withdraw(balance, amount):
    """Function to withdraw money"""
    if amount > balance:
        raise InsufficientFundsError("Cannot withdraw more than the current balance.")
    return f"Withdrawn ${amount} successfully."

# 2. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик НЕ ДОЛЖЕН содержать блок finally.
def balance_inquiry(balance):
    """Function to check balance"""
    try:
        if balance < 0:
            raise ValueError("Account balance cannot be negative.")
        return f"Current balance is ${balance}."
    except Exception as e:
        return f"Error: {e}"

# 3. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception). Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def transfer_funds(source_balance, target_balance, amount):
    """Function to transfer funds"""
    try:
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > source_balance:
            raise InsufficientFundsError("Not enough balance to transfer.")
        source_balance -= amount
        target_balance += amount
        return f"Transferred ${amount} successfully. Source balance: ${source_balance}"
    except Exception as e:
        return f"Error during transfer: {e}"
    finally:
        print("Transfer operation attempted.")

# 4. Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.
# Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений). Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def authorize_transaction(account_role, action):
    """Function with multiple exception handlers"""
    try:
        if account_role != "admin":
            raise UnauthorizedAccessError("Only admin can authorize this transaction.", account_role)
        if action not in ["deposit", "withdraw"]:
            raise ValueError("Invalid transaction type.")
        return f"Transaction '{action}' authorized."
    except UnauthorizedAccessError as ua:
        return f"Unauthorized Access: {ua}"
    except ValueError as ve:
        return f"Value Error: {ve}"
    except Exception as e:
        return f"Unexpected Error: {e}"
    finally:
        print("Authorization check completed.")

def negative_test_function(value):
    """Example demonstrating exceptions and multiple handlers with finally block"""
    try:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        if value < 0:
            raise ValueError("Negative values not allowed.")
        result = 100 / value
        return f"Result is {result}"
    except ValueError as ve:
        return f"Value Error: {ve}"
    except TypeError as te:
        return f"Type Error: {te}"
    except ZeroDivisionError as zde:
        return f"Zero Division Error: {zde}"
    finally:
        print("Negative test function executed.")

def process_transaction(transaction_type, amount, account_balance):
    """Function to process a transaction"""
    try:
        if transaction_type not in ["deposit", "withdrawal"]:
            raise ValueError("Invalid transaction type.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if transaction_type == "withdrawal" and amount > account_balance:
            raise InsufficientFundsError("Not enough balance to withdraw.")
        if transaction_type == "deposit":
            account_balance += amount
        else:
            account_balance -= amount
        return f"Transaction processed successfully. New balance: ${account_balance}"
    except ValueError as ve:
        return f"Value Error: {ve}"
    except InsufficientFundsError as ife:
        return f"Insufficient Funds Error: {ife}"
    except Exception as e:
        return f"Unexpected Error: {e}"
    finally:
        print("Transaction processing completed.")

# 5. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).
# Функция ДОЛЖНА содержать обрабоnчики всех исключений, которые генерируются внутри этой функции. Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.
def generate_exceptions(value):
    """Function to generate and handle exceptions"""
    try:
        if value == 0:
            raise ZeroDivisionError("Value cannot be zero.")
        if value < 0:
            raise NegativeDepositError("Negative values are not allowed for deposits.")
        result = 100 / value
        return f"Processed value successfully, result is {result}"
    except ZeroDivisionError as zde:
        return f"Zero Division Error: {zde}"
    except NegativeDepositError as nde:
        return f"Negative Deposit Error: {nde}"
    finally:
        print("Exception generation process completed.")

# 6. Минимум 3 разных пользовательских исключения и примеры их использования
def custom_exception_demo(value):
    """Function demonstrating use of custom exceptions"""
    if value < 0:
        raise NegativeDepositError("Attempted to deposit a negative amount.")

# 7. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик МОЖЕТ содержать блок finally.
def custom_deposit_handler(amount):
    """Function to demonstrate custom exception handling"""
    try:
        custom_exception_demo(amount)
        return f"Deposited ${amount} successfully."
    except NegativeDepositError as nde:
        return f"Handling custom exception: {nde}"
    finally:
        print("Custom deposit operation completed.")

# 8. Минимум 3 функции, демонстрирующие работу исключений.
# Алгоритм функций необходимо придумать самостоятельно
def divide_numbers(a, b):
    """Divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    finally:
        print("Division operation attempted.")

def access_list_element(lst, index):
    """Access an element from a list by index"""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."
    finally:
        print("List access attempted.")

def parse_integer(value):
    """Parse string to integer"""
    try:
        return int(value)
    except ValueError:
        return "Invalid input: Not an integer."
    finally:
        print("Integer parsing attempted.")
