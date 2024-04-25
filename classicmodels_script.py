import mysql.connector
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_to_database(username, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='classicmodels',
            user=username,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Exception as e:
        print(f"An error occurred: {e}")

def get_executives(connection):
    query = """
    SELECT employeeNumber, lastName, firstName, email, jobTitle
    FROM employees
    WHERE jobTitle LIKE '%VP%' OR jobTitle LIKE 'President'
    """
    cursor = connection.cursor()
    cursor.execute(query)
    for (employeeNumber, lastName, firstName, email, jobTitle) in cursor:
        print(f"ID: {employeeNumber}, Last Name: {lastName}, First Name: {firstName}, Email: {email}, Position: {jobTitle}")
    cursor.close()

def get_top_customers(connection):
    query = """
    SELECT customerNumber, customerName, SUM(amount) AS totalPayments
    FROM customers
    JOIN payments USING (customerNumber)
    GROUP BY customerNumber
    ORDER BY totalPayments DESC
    LIMIT 10
    """
    cursor = connection.cursor()
    cursor.execute(query)
    for (customerNumber, customerName, totalPayments) in cursor:
        print(f"Customer ID: {customerNumber}, Name: {customerName}, Total Payments: {totalPayments}")
    cursor.close()

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    connection = connect_to_database(username, password)
    if connection:
        while True:
            print("\nMenu:")
            print("1. Show Executives")
            print("2. Show Top 10 Customers")
            print("3. Clear Screen")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                get_executives(connection)
            elif choice == '2':
                get_top_customers(connection)
            elif choice == '3':
                clear_screen()
            elif choice == '4':
                connection.close()
                break
            else:
                print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
