
Project Title
Bill Generator
Overview of the Project
The Bill Generator is a command-line interface (CLI) application designed to create sales receipts or invoices quickly and efficiently. The tool guides the user through interactively entering product details and then leverages the fpdf library to generate a structured, printable PDF document named Bill.pdf.
This project showcases fundamental Python programming concepts, including modular design, basic input validation, complex data structure management (lists of dictionaries), and the integration of external libraries for file output.
________________________________________
Features
The generator provides the following core capabilities:
•	Interactive Data Input: Collects the store name, product name, price, and quantity directly from the user via the console.
•	Dynamic Calculation: Automatically computes the total price for each item and aggregates all items to calculate the final Grand Total Cost.
•	Structured PDF Output: Creates a professional, table-based invoice (Bill.pdf) suitable for printing, ensuring a consistent format.
•	Modular Design: Code is logically separated into two primary functions: basic (input/calculation) and text_to_pdf (PDF generation).
•	Robust Error Handling: Recovers gracefully from common user input mistakes (e.g., entering text instead of a number for price/quantity) by prompting the user to re-enter data without losing previously added items.
________________________________________
Technologies/Tools Used
Technology	Purpose
Python 3	The core programming language.
FPDF	External library used for creating and formatting the final PDF document.
Standard Input/Output (I/O)	Used for the console-based user interface (CLI).
________________________________________
Steps to Install & Run the Project
1. Prerequisites
You must have Python 3 installed on your system.
2. Install Dependencies
The project relies on the fpdf library. Open your terminal or command prompt and execute the following command:
Bash
pip install fpdf
3. Run the Script
1.	Save the provided code as a file named Bill Generator.py.
2.	Navigate to the directory containing the file in your terminal.
3.	Execute the script using the Python interpreter:
Bash
python "Bill Generator.py"
4.	The program will immediately prompt you to enter the Store Name to begin.
________________________________________
Instructions for Testing
Follow these two scenarios to confirm the project is fully functional and robust.
Scenario 1: Successful Bill Generation
This confirms the core functionality of calculation and PDF creation.
1.	Run the script and enter the Store Name.
2.	When prompted (ADD items press Y...), enter Y to add an item.
3.	Enter valid input for Product Name, Price, and Quantity.
4.	Repeat Step 2 and 3 for additional items.
5.	Enter R to finish the input phase.
6.	Expected Outcome: The console displays the final Total Cost, prints the success message ([SUCCESS]BILL is successfully created Bill.pdf), and a file named Bill.pdf is generated in the same directory.
Scenario 2: Error Recovery Testing
This confirms the robust error handling by deliberately causing a ValueError.
1.	Run the script.
2.	Successfully add at least one item (e.g., "Pencil", 5.0, 10).
3.	Enter Y to add a second item.
4.	When prompted for "Price in Rs.:", intentionally enter non-numeric text, such as twenty.
5.	Expected Behavior (Correct): The script should print: "Give valid input". It must not crash or exit. It will then loop and prompt you again (ADD items press Y...).
6.	Verification: Enter R to stop. The script should successfully generate the Bill.pdf file containing only the item(s) entered before the error.
________________________________________
 











Output:
  
