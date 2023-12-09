import heapq
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk  # Import the ttk module for themed Tkinter

class RoleAuthenticationGUI:
    def __init__(self):
        # Variable Passcodes
        self.Chief_Executive_Officer_password = 641341
        self.Board_Director_password = 654924

        # Roles and priorities
        self.roles_priorities = {
            "C.E.O": 1,
            "Transporter": 4,
            "Software Programmer": 3,
            "Accountant": 4,
            "Assistant Chief Officer": 2,
            "Project Manager": 2,
            "Assistant Engineer Officer": 3,
            "Account Coordinator": 3,
            "Board of Directors": 1,
            "Vice President": 2,
            "Security": 4
        }

        # Priority queue
        self.priority_queue = []

        # Populate the priority queue
        for role, priority in self.roles_priorities.items():
            heapq.heappush(self.priority_queue, (priority, role))

        # GUI
        self.root = tk.Tk()
        self.root.title("Role Authentication")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=(10, 5, 10, 5), font='Helvetica 10')
       
        self.label = ttk.Label(self.root, text="Enter your role:")
        self.label.grid(row=0, column=0, pady=10, padx=10)

        self.role_entry = ttk.Entry(self.root)
        self.role_entry.grid(row=0, column=1, pady=10, padx=10)

        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)

        self.authenticate_button = ttk.Button(self.root, text="Authenticate", command=self.run_authentication)
        self.authenticate_button.grid(row=2, column=1, pady=10, padx=10)

    def authenticate_user(self, role, password):
        """Authenticate the user based on role and password."""
        role_lower = role.lower()

        if role_lower == "c.e.o" and password == self.Chief_Executive_Officer_password:
            return True
        elif role_lower == "board of directors" and password == self.Board_Director_password:
            return True
        else:
            return False

    def print_priority_queue(self):
        "Print the priority queue of roles."
        result = "\nPriority Queue of Roles:\n"
        while self.priority_queue:
            priority, role_number = heapq.heappop(self.priority_queue)
            result += f"Priority: {priority}\t{role_number}\n"
        return result

    def run_authentication(self):
        """Run the user authentication process."""
        role = self.role_entry.get()
        password = self.password_entry.get()

        if role.lower() == "c.e.o" or role.lower() == "board of directors":
            try:
                password = int(password)
                if self.authenticate_user(role, password):
                    result = f"\nYou have gained access.\n{self.print_priority_queue()}"
                else:
                    result = "\nAccess Denied."
            except ValueError:
                result = "\nInvalid input. Please enter a valid integer for the password."
        else:
            result = "\nAccess Denied. You have no permission to access this level."

        # Display the result in a messagebox
        messagebox.showinfo("Authentication Result", result)

# Create an instance of the RoleAuthenticationGUI class
gui = RoleAuthenticationGUI()

# Run the GUI main loop
gui.root.mainloop()
