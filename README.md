# ✨ Angat-Buhay-Management-System ✨

## 📝 Overview
The Angat Buhay Donation Management System is a system designed to manage and update various types of donations for multiple causes. 
It supports a wide range of donation categories, including food, water, clothes, books, school supplies, toiletries, and monetary contributions. 
The system allows users to add, update, and view donations, along with their associated details such as the cause, quantity, unit of measurement, 
and details. Each donation type is represented by a specific class, ensuring proper management of item-specific details. The project also offers 
a user-friendly interface for updating donation information, such as cause, quantity, unit, and additional details. This helps streamline the 
process of collecting and managing charitable donations, providing efficient tracking and updating functionalities for both donors and 
administrators. Angat Buhay Donation tracker tracks the donation of the donors.

## 📚 Python Concepts and Libraries Used
The application integrates several key Python concepts and libraries to build its graphical user interface and manage user interactions:

- **Object-Oriented Programming (OOP)**: The application uses OOP principles by organizing functionalities within a `DonationApp` class, with methods for displaying forms, submitting donations, and managing user interactions.
  
- **Tkinter**: The graphical user interface (GUI) is created using Tkinter, which provides interactive widgets like buttons, labels, entry fields, and menus for user engagement.

- **Error Handling**: To ensure smooth user interactions, error handling is implemented using **if-else statements** to validate user inputs such as name, cause, quantity, and unit. Warning messages are displayed if any fields are missing or incorrect, ensuring that the user is aware of any issues.

- **Data Management with Lists and Dictionaries**: 
  - A **list** (`self.donations`) stores all donations, with each donation represented as a dictionary containing fields like "donation_id", "donor_name", "cause", "quantity", "unit", and "description". This structure allows easy manipulation and access to donation data.
  - A **dictionary** (`self.users_db`) stores user credentials, with usernames as keys and passwords as values, facilitating efficient user authentication and management.

These data structures enable dynamic updates and effective management of user inputs and donation records.

## 🌍 Integration with SDGs (Sustainable Development Goals)
The **Angat Buhay Donation Management System** aligns with **🎯 SDG 2: Zero Hunger** and **🎯 SDG 4: Quality Education** by supporting the collection and distribution of resources to address food security and educational access.

- Donations of food, water, and toiletries contribute directly to **SDG 2: Zero Hunger**, addressing nutritional needs and food security.
- Donations of books and school supplies help promote educational access, supporting **SDG 4: Quality Education** by ensuring that underprivileged children and communities have the resources needed for learning.

Through these efforts, the system fosters both nutritional security and educational opportunities for those in need.

## 🗂️ Instructions for Running the Program

### I. Donate
When the system starts, the **Donate** option is presented. The user is prompted to:
1. Select a cause: **Climate Action Sustainability**, **Nutrition and Food Security**, or **Public Education**.
2. Select a donation type based on the chosen cause:
   - **Climate Action**: Food, Water, Clothes, Monetary, or Toiletries
   - **Nutrition and Food Security**: Food, Water, or Monetary
   - **Public Education**: Books, School Supplies, or Monetary
3. Enter donor details including name, selected cause, quantity, unit, and any additional details. Once this information is provided, the donation is successfully added to the system.

### II. Update Donation
To update a donation:
1. The system first displays all donations made by various donors.
2. The user selects the donor ID corresponding to the donation they wish to update.
3. The user can then choose to update specific details such as the cause, quantity, unit, or donation details.

This feature allows users to update their donation information based on their preferences.

### III. View Dashboard
The **View Dashboard** option displays a table containing the following columns for each donation:
- Donor ID
- Donor Name
- Cause of Donation
- Quantity
- Unit
- Donation Details

This allows the user to quickly and easily view all donation information.

### IV. Exit
Once the user selects **Exit**, the program will terminate, stopping its execution.
