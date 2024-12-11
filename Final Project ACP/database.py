import sqlite3

def connect_db():
    conn = sqlite3.connect("Angat_Buhay.db")
    return conn

def initialize_database():
    try:
        # Connect to the SQLite database
        conn = connect_db()
        cursor = conn.cursor()

        # Cause table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cause (
            cause_id INTEGER PRIMARY KEY,
            cause_type VARCHAR(100) NOT NULL
        )
        """)

        # Donor table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Donor (
            donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
        """)

        # Donation table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Donation (
            donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_name VARCHAR(255) NOT NULL,
            cause_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit VARCHAR(50) NOT NULL,
            description VARCHAR(255) NOT NULL,
            date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cause_id) REFERENCES Cause(cause_id)
        )
        """)

        # Insert predefined causes
        causes = [
            (1, "Climate Action Sustainability"),
            (2, "Nutrition and Food Security"),
            (3, "Public Education")
        ]
        cursor.executemany("""
            INSERT OR IGNORE INTO Cause (cause_id, cause_type) VALUES (?, ?)
        """, causes)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        if conn:
            conn.rollback()
        if conn:
            conn.close()

# Function to insert a donation into the Donation table
def insert_donation(donor_name, cause_id, quantity, unit, description):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Donation (donor_name, cause_id, quantity, unit, description)
            VALUES (?, ?, ?, ?, ?)
        """, (donor_name, cause_id, quantity, unit, description))
        conn.commit()
        conn.close()
        print(f"Donation Added: {donor_name} - {cause_id} - {quantity} {unit} - {description}")  # Debug print

    except sqlite3.Error as e:
        print(f"Error inserting donation: {e}")
        if conn:
            conn.rollback()
        if conn:
            conn.close()

# Function to retrieve all donations from the database
def get_all_donations():
    """Fetch all donations from the database."""
    try:
        conn = sqlite3.connect("Angat_Buhay.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Donation")
        donations = cursor.fetchall()
        conn.close()
        return donations
    except sqlite3.Error as e:
        print(f"Error fetching donations: {e}")
        return []

# Function to retrieve a single donation by ID
def get_donation_by_id(donation_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Donation.donation_id, Donation.donor_name, Cause.cause_type, 
                   Donation.quantity, Donation.unit, Donation.description
            FROM Donation
            JOIN Cause ON Donation.cause_id = Cause.cause_id
            WHERE Donation.donation_id = ?
        """, (donation_id,))
        donation = cursor.fetchone()
        conn.close()
        return donation

    except sqlite3.Error as e:
        print(f"Error retrieving donation by ID: {e}")
        if conn:
            conn.close()
        return None

# Function to update a donation
def update_donation(donation_id, donor_name, cause_id, quantity, unit, description):
    """Update a donation record in the database."""
    try:
        conn = sqlite3.connect("Angat_Buhay.db") 
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Donation
            SET donor_name = ?, cause_id = ?, quantity = ?, unit = ?, description = ?
            WHERE donation_id = ?
        """, (donor_name, cause_id, quantity, unit, description, donation_id))
        
        conn.commit()
        
        if cursor.rowcount == 0:
            print(f"Warning: No rows were updated for donation ID {donation_id}")
        
        conn.close()

    except sqlite3.Error as e:
        print(f"Error updating donation: {e}")
        if conn:
            conn.rollback()
        if conn:
            conn.close()

# Function to delete a donation by ID
def delete_donation(donation_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM Donation WHERE donation_id = ?
        """, (donation_id,))
        conn.commit()
        conn.close()
        print(f"Donation with ID {donation_id} deleted successfully!")

    except sqlite3.Error as e:
        print(f"Error deleting donation: {e}")
        if conn:
            conn.rollback()
        if conn:
            conn.close()
