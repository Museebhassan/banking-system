:::writing{variant=“standard” id=“48291”}

🏦 Simple Banking System (Python)

📌 Project Overview

This is a basic command-line banking system written in Python. It allows users to create accounts, deposit money, withdraw money, and check account balances.

The project demonstrates core programming concepts such as:
	•	Classes & Objects (OOP)
	•	Dictionaries for data storage
	•	Conditional statements
	•	Loops
	•	User input handling

⸻

⚙️ Features

✅ Create a new bank account
✅ Deposit money
✅ Withdraw money
✅ Check account balance
✅ Multiple account support

⸻

🧠 How It Works
	•	Each account is represented using the BankAccount class.
	•	All accounts are stored in a dictionary (accounts) using the account number as the key.
	•	The system runs in a loop until the user chooses to exit.

⸻

🏗️ Class Structure

BankAccount

Method	Description
__init__(name, account_number)	Initializes account with name and number
deposit(amount)	Adds money to the account
withdraw(amount)	Withdraws money if sufficient balance
check_balance()	Displays account details


⸻

🚀 How to Run
	1.	Make sure Python is installed on your system.
	2.	Save the file as:

banking_system.py


	3.	Run the program:

python banking_system.py



⸻

💻 Menu Options

----- BANKING SYSTEM -----
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit


⸻

📷 Example Usage

Enter your choice: 1
Enter Name: Museeb
Enter Account Number: 12345
Account Created Successfully!

Enter your choice: 2
Enter Account Number: 12345
Enter Amount to Deposit: 5000
Amount Deposited Successfully!

Enter your choice: 4
Account Holder: Museeb
Account Number: 12345
Current Balance: ₹ 5000


⸻

⚠️ Limitations
	•	Data is not saved permanently (resets after program ends)
	•	No authentication or security
	•	No file/database storage

⸻

🔥 Future Improvements
	•	Add file/database storage (SQLite / JSON)
	•	Implement login authentication
	•	Add transaction history
	•	Create GUI using Tkinter or web app using Flask

⸻

👨‍💻 Author

Museeb Hassan

⸻

📌 Note

This project is great for beginners to understand how real-world systems like banking work at a basic level.

