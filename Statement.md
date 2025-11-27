1. Problem Statement
Small retail businesses, vendors, and service providers often rely on manual, handwritten invoices or generic, inflexible spreadsheet software to generate receipts for customers. This process is time-consuming, prone to calculation errors, and produces unprofessional or non-standardized documentation. The primary problem is the lack of an accessible, free, and robust digital tool that can quickly convert itemized sales data into a formal, printable invoice format.

2. Scope of the Project
The scope of this project is to develop a functional Command-Line Interface (CLI) application in Python that fulfills the entire lifecycle of a basic sales transaction documentation.

The project encompasses:

User Interface: Handling interactive console input for item details.

Business Logic: Performing accurate calculation of individual item totals and the final grand total.

Output Generation: Utilizing the fpdf library to structure and save the final bill as a Bill.pdf file.

Quality Control: Implementing basic input validation and error handling to ensure the application is robust against typical user input errors.

The project does not include: advanced features such as database persistence (saving past bills), tax/discount calculation, inventory management, or a Graphical User Interface (GUI).

3. Target Users
The primary target users are individuals or entities needing quick, one-off formal documentation for sales:

Small Retail Business Owners: Shopkeepers who need receipts for customers without investing in full POS systems.

Independent Contractors/Freelancers: Individuals who require simple, itemized invoices for services rendered.

Home-Based Businesses: Sellers of crafts, baked goods, or small items who need professional-looking receipts.

Educational Demonstrations: Students or educators needing a clear example of modular programming, calculation, and PDF file generation.

4. High-Level Features
Interactive Item Entry: Allows the user to add multiple products sequentially.

Automated Totaling: Calculates line-item totals and the grand total cost.

Store Naming: Permits customization of the bill with the store's name.

PDF Formatting: Generates a structured PDF with a clear table layout for easy reading.

Input Robustness: Prevents application failure due to invalid data types (e.g., non-numeric input for price or quantity).
