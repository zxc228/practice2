# practice2
# Python Script for Classicmodels Database

## Overview
This script provides an interface to access and query the `classicmodels` database. It allows users to authenticate, perform specific queries, and interact with the database effectively.

### Features
- **Authentication:** Users can log in with their username and password.
- **Database Connection:** Connects to the `classicmodels` database hosted on `localhost`.
- **Interactive Menu:** Users can select options to execute specific operations.
- **Clear Screen:** Clears the terminal screen for better readability.
- **Exit:** Allows users to exit the application.

## Menu Options

1. **List of Executives**
   - Displays the employee ID, last name, first name, email, and position of executives in the company.

2. **Top 10 Customers**
   - Shows the top 10 customers based on the total payments made to the company, sorted from highest to lowest.

3. **Clear Screen**
   - Clears the terminal screen to keep the interface clean.

4. **Exit**
   - Exits the application.

## Usage
To use this script, execute it from a command line. Ensure Python and required packages (`mysql-connector-python`) are installed.

1. Start the script:
```bash
python classicmodels_script.py
```
3. Follow the on-screen prompts to log in and select an option from the menu.

## Installation

### Requirements
- Python 3.x
- mysql-connector-python
```bash
pip install mysql-connector-python
```


### Setup
- Ensure MySQL is running on `localhost` with the `classicmodels` database loaded.
- Update the script with the correct database credentials if different from defaults.

## Additional Notes
- The script assumes that all users have at least query privileges on the relevant tables.
- No advanced error handling is implemented; the script is designed for basic demonstration purposes.
