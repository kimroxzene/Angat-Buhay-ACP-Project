import tkinter as tk
from tkinter import PhotoImage, simpledialog, ttk, messagebox
from PIL import Image, ImageTk
from login import RegisterForm, LoginForm
from database import insert_donation, get_all_donations, update_donation, delete_donation
import sqlite3

class DonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Donation Dashboard")
        self.root.geometry("1100x600")
        self.root.config(bg="#f7f7ec")
        self.root.resizable(False, False) 
    
        # database connection 
        self.db = sqlite3.connect("Angat_Buhay.db")
        self.donations = get_all_donations() 

        # Create a header 
        self.create_header()
        self.content_frame = tk.Frame(self.root, bg="#f7f7ec", padx=20, pady=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Create a grid layout with 2 columns
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)  # Left side (image)
        self.content_frame.grid_columnconfigure(1, weight=3)  # Right side (form)

        self.load_register_form()

        self.users_db = {}  # store username and password

    def create_header(self):
        """Create a blue header at the top of the window."""
        header_frame = tk.Frame(self.root, bg="#14afbc", height=50)
        header_frame.pack(side=tk.TOP, fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Donation Dashboard",
            font=("Arial", 16, "bold"),
            bg="#14afbc",
            fg="white"
        )
        title_label.pack(side=tk.LEFT, padx=20)

    def load_register_form(self):
        """Load the register form on the right side."""
        self.clear_right_frame()
        RegisterForm(self.content_frame, self)

    def load_login_form(self):
        """Load the login form on the right side."""
        self.clear_right_frame()
        LoginForm(self.content_frame, self)

    def load_main_menu(self):
        """Load the main menu after login."""
        self.clear_right_frame()
        # Display the image with buttons over it
        self.display_image(self.content_frame)

    def clear_right_frame(self):
        """Clear the right side of the content frame for dynamic updates."""
        for widget in self.content_frame.grid_slaves(row=0, column=1):
            widget.destroy()

    def display_image(self, parent_frame):
        """Load and display the logo image on the left side of the content area."""
        try:
            logo_image = Image.open("main_menu.png")  
            logo_image = logo_image.resize((520, 500))  
            logo_photo = ImageTk.PhotoImage(logo_image)

            # Label widget to display the image
            logo_label = tk.Label(parent_frame, image=logo_photo, bg="#f7f7ec")
            logo_label.image = logo_photo  
            logo_label.grid(row=0, column=0, padx=250, pady=20, sticky="nsew")  

            self.add_buttons_over_image(parent_frame)

        except Exception as e:
            print(f"Error loading image: {e}")

    def add_buttons_over_image(self, parent_frame):
        """Add buttons on top of the image in different positions."""

        # donate
        button1 = tk.Button(parent_frame, text="Donate", command=self.button1_action, font=("Arial", 12, "bold"), bg="#ff4081", fg="white")
        button1.place(relx=0.5, rely=0.01, anchor="n") 

        # update
        button2 = tk.Button(parent_frame, text="Update Donation", command=self.button2_action, font=("Arial", 12, "bold"), bg="#ff4081", fg="white")
        button2.place(relx=0.13, rely=0.5, anchor="w")  # Positioned on the left

        # view dashboard
        button3 = tk.Button(parent_frame, text="View Dashboard", command=self.button3_action, font=("Arial", 12, "bold"), bg="#ff4081", fg="white")
        button3.place(relx=0.85, rely=0.5, anchor="e")  # Positioned on the right

        # exit
        button4 = tk.Button(parent_frame, text="Exit", command=self.button4_action, font=("Arial", 12, "bold"), bg="#ff4081", fg="white")
        button4.place(relx=0.5, rely=1, anchor="s")  # Positioned at the bottom center

        top_button = tk.Button(
            self.root, text="Top Button", command=self.button1_action, 
            font=("Arial", 14), bg="#0078D7", fg="white"
        )
        top_button.pack(pady=20)

    def button1_action(self):
        """Action for Top Button."""
        self.show_donation_window()

    def show_donation_window(self):
        """Create and display the entire donation form in one window."""
        # Clear the window for the donation form
        for widget in self.root.winfo_children():
            widget.destroy()

        # Donor Name
        name_label = tk.Label(self.root, text="Enter Your Name", font=("Lilita One", 14), bg="#f7f7ec", fg = "#15afbc")
        name_label.pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        # Cause selection
        cause_label = tk.Label(self.root, text="Select for a Cause", font=("Lilita One", 14), bg="#f7f7ec", fg = "#15afbc")
        cause_label.pack(pady=20)

        # list for causes
        causes = [
            "Climate Action Sustainability",
            "Nutrition and Food Security",
            "Public Education"
        ]
        self.cause_var = tk.StringVar()
        cause_dropdown = tk.OptionMenu(self.root, self.cause_var, *causes)
        cause_dropdown.config(font=("Arial", 14), width=30, fg = "#15afbc")
        cause_dropdown.pack(pady=10)

        # Quantity
        quantity_label = tk.Label(self.root, text="Enter Donation Quantity", font=("Lilita One", 14), bg="#f7f7ec", fg = "#15afbc")
        quantity_label.pack(pady=10)
        self.quantity_entry = tk.Entry(self.root, font=("Arial", 12))
        self.quantity_entry.pack(pady=10)

         # Unit selection
        unit_label = tk.Label(self.root, text="Enter Unit (kg/pcs)", font=("Lilita One", 14), bg="#f7f7ec", fg = "#15afbc")
        unit_label.pack(pady=10)
        self.unit_var = tk.StringVar()
        unit_dropdown = tk.OptionMenu(self.root, self.unit_var, "kg", "pcs")
        unit_dropdown.config(font=("Arial", 12), width=30)
        unit_dropdown.pack(pady=10)

        # Description
        description_label = tk.Label(self.root, text="Enter Donation Details/Description", font=("Lilita One", 14), bg="#f7f7ec", fg = "#15afbc")
        description_label.pack(pady=10)
        self.description_entry = tk.Entry(self.root, font=("Arial", 12))
        self.description_entry.pack(pady=10)

        # Donate
        submit_button = tk.Button(self.root, text="Donate", command=self.submit_donation, bg="#ff4081", fg="white", font=("Lilita One", 14))
        submit_button.pack(pady=20)

    def submit_donation(self):
        """Submit the donation after entering quantity."""
        name = self.name_entry.get()
        cause = self.cause_var.get()
        quantity = self.quantity_entry.get()
        unit = self.unit_var.get()
        description = self.description_entry.get()

        # Validation
        if not name.strip():
            messagebox.showwarning("Missing Name", "Please enter your name.")
            return
        if not cause.strip():
            messagebox.showwarning("Missing Cause", "Please select a cause.")
            return
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")
            return
        if not unit.strip():
            messagebox.showwarning("Missing Unit", "Please select a unit (kg/pcs/boxes).")
            return
        if not description.strip():
            messagebox.showwarning("Missing Details", "Please provide donation details.")
            return

        # Get the cause_id from the selected cause
        cause_id_mapping = {
            "Climate Action Sustainability": 1,
            "Nutrition and Food Security": 2,
            "Public Education": 3
        }
        cause_id = cause_id_mapping.get(cause)

        if cause_id is None:
            messagebox.showerror("Error", "Invalid cause selected.")
            return

        # Insert the donation into the database
        insert_donation(name, cause_id, int(quantity), unit, description)

        # Refresh the donations list after insertion
        self.donations = get_all_donations()  # Reload donations from the database

        # Confirmation message
        messagebox.showinfo(
            "Donation Successful",
            f"Thank you {name}!\nYou donated {quantity} {unit} of {description} for {cause}."
        )

        # Clear the donation window and reload the main menu
        for widget in self.root.winfo_children():
            widget.destroy()

        self.content_frame = tk.Frame(self.root, bg="#f7f7ec", padx=20, pady=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        self.load_main_menu()

    def button2_action(self):
        """Action for the 'Update Donation' button."""
        # Refresh the donations list from the database to ensure it’s up-to-date
        self.donations = get_all_donations()

        # Display the donation dashboard first
        donation_list = "\n".join(
            [f"ID: {donation[0]} | Donor: {donation[1]} | Cause: {donation[2]} | "
            f"Quantity: {donation[3]} {donation[4]} | Description: {donation[5]}"
            for donation in self.donations]
        )

        if not donation_list:
            messagebox.showerror("Error", "No donations available to display.", parent=self.root)
            return

        # Show the dashboard with all donations
        donation_view = f"Current Donations:\n{donation_list}\n\nPlease choose a donation ID to update."
        donation_id = simpledialog.askinteger("Update Donation", donation_view, parent=self.root)

        if not donation_id:
            return

        # Search for the donation by ID
        donation = next((donation for donation in self.donations if donation[0] == donation_id), None)

        if donation is None:
            messagebox.showerror("Error", f"No donation found with ID {donation_id}.", parent=self.root)
            return

        # Show all current details of the donation and ask for the field to update
        current_details = (
            f"Donor Name: {donation[1]}\n"   # donation[1] is 'donor_name'
            f"Cause: {donation[2]}\n"         # donation[2] is 'cause'
            f"Quantity: {donation[3]}\n"      # donation[3] is 'quantity'
            f"Unit: {donation[4]}\n"          # donation[4] is 'unit'
            f"Description: {donation[5]}\n"   # donation[5] is 'description'
        )

        update_choice = simpledialog.askstring(
            "Update Donation",
            f"Current Donation Details:\n{current_details}\n\n"
            "Which field would you like to update? (donor_name, cause, quantity, unit, description):",
            parent=self.root
        )

        if not update_choice:
            return

        update_choice = update_choice.lower()  # Convert to lowercase to standardize input

        new_value = None
        if update_choice == "donor_name":
            new_value = simpledialog.askstring("Update Donor Name", "Enter new donor name:", parent=self.root)
            if new_value:
                # Update the donation record in the database
                update_donation(donation[0], new_value, donation[2], donation[3], donation[4], donation[5])

        elif update_choice == "cause":
            new_value = simpledialog.askstring("Update Cause", "Enter new cause:", parent=self.root)
            cause_id_mapping = {
                "Climate Action Sustainability": 1,
                "Nutrition and Food Security": 2,
                "Public Education": 3
            }
            if new_value in cause_id_mapping:
                cause_id = cause_id_mapping[new_value]
                # Update the donation record in the database
                update_donation(donation[0], donation[1], cause_id, donation[3], donation[4], donation[5])
            else:
                messagebox.showerror("Error", "Invalid cause selected.")
                return

        elif update_choice == "quantity":
            new_value = simpledialog.askinteger("Update Quantity", "Enter new quantity:", parent=self.root)
            if new_value:
                # Update the donation record in the database
                update_donation(donation[0], donation[1], donation[2], new_value, donation[4], donation[5])

        elif update_choice == "unit":
            new_value = simpledialog.askstring("Update Unit", "Enter new unit:", parent=self.root)
            if new_value:
                # Update the donation record in the database
                update_donation(donation[0], donation[1], donation[2], donation[3], new_value, donation[5])

        elif update_choice == "description":
            new_value = simpledialog.askstring("Update Description", "Enter new description:", parent=self.root)
            if new_value:
                # Update the donation record in the database
                update_donation(donation[0], donation[1], donation[2], donation[3], donation[4], new_value)

        else:
            messagebox.showerror(
                "Error",
                "Invalid choice. Please choose one of the following: donor_name, cause, quantity, unit, description.",
                parent=self.root
            )
            return

        # Refresh the donations list after the update
        self.donations = get_all_donations()  # Reload donations after the update

        # Confirm the update
        messagebox.showinfo("Success", f"Donation ID {donation_id} updated successfully!", parent=self.root)

    def button3_action(self):
        """Action for the 'View Donations' button to show a table of donations."""
        # Create a new window for the donation table
        table_window = tk.Toplevel(self.root)
        table_window.title("Donation Transactions")

        # Create a table
        tree = ttk.Treeview(
            table_window,
            columns=("Donation ID", "Donor Name", "Cause", "Quantity", "Unit", "Description"),
            show="headings"
        )

        # Define columns and headings
        tree.heading("Donation ID", text="Donation ID")
        tree.heading("Donor Name", text="Donor Name")
        tree.heading("Cause", text="Cause")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Unit", text="Unit")
        tree.heading("Description", text="Description")

        # Set column widths
        tree.column("Donation ID", width=100)
        tree.column("Donor Name", width=150)
        tree.column("Cause", width=150)
        tree.column("Quantity", width=100)
        tree.column("Unit", width=100)
        tree.column("Description", width=250)

        # Fetch donations from the database
        def refresh_table():
            for row in tree.get_children():
                tree.delete(row)
            donations = get_all_donations()
            for donation in donations:
                tree.insert(
                    "",
                    "end",
                    values=(
                        donation[0],  # Donation ID
                        donation[1],  # Donor Name
                        donation[2],  # Cause
                        donation[3],  # Quantity
                        donation[4],  # Unit
                        donation[5]   # Description
                    )
                )

        refresh_table()

        # Add a scrollbar to the table
        scroll_y = ttk.Scrollbar(table_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")

        tree.pack(padx=20, pady=20, fill="both", expand=True)

        # Add a Delete button
        def delete_selected_record():
            selected_item = tree.selection()
            if selected_item:
                item_values = tree.item(selected_item, "values")
                donation_id = item_values[0]  # Get the Donation ID from the selected row
                delete_donation(donation_id)  # Delete the record from the database
                refresh_table()  # Refresh the table after deletion
            else:
                tk.messagebox.showwarning("Warning", "Please select a record to delete.")

        delete_button = tk.Button(table_window, text="Delete", command=delete_selected_record)
        delete_button.pack(pady=10)


    def button4_action(self):
        """Action for Bottom Button (Exit)."""
        confirm_exit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm_exit:
            self.root.quit()

class MainMenu:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # Access to app methods

        self.main_menu_frame = tk.Frame(self.root, bg="#f7f7ec")
        self.main_menu_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.main_title_label = tk.Label(self.main_menu_frame, text="Main Menu", font=("Lilita One", 20, "bold"), bg="#f7f7ec")
        self.main_title_label.pack(pady=15)

        # Add buttons or other widgets as needed
        self.donate_button = tk.Button(self.main_menu_frame, text="Make a Donation", font=("Arial", 14), command=self.app.show_donation_window)
        self.donate_button.pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = DonationApp(root)
    root.mainloop()