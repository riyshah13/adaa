import tkinter as tk
from tkinter import messagebox

class BusReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Reservation System")
        self.root.geometry("800x600")

        # Login Credentials
        self.credentials = {
            "Mukund": "password1",
            "Riya": "password2",
            "Viraj": "password3"
        }

        self.logged_in = False
        self.current_user = None

        # Initialize variables
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_login_interface()

    def create_login_interface(self):
        login_label = tk.Label(self.root, text="Welcome to Bus Ticket Reservation System", font=("Arial", 16))
        login_label.pack(pady=10)

        username_label = tk.Label(self.root, text="Username:", font=("Arial", 12))
        username_label.pack()

        username_entry = tk.Entry(self.root, textvariable=self.username_var, font=("Arial", 12))
        username_entry.pack()

        password_label = tk.Label(self.root, text="Password:", font=("Arial", 12))
        password_label.pack()

        password_entry = tk.Entry(self.root, textvariable=self.password_var, show="*", font=("Arial", 12))
        password_entry.pack()

        login_button = tk.Button(self.root, text="Log In", command=self.login, font=("Arial", 12))
        login_button.pack(pady=10)

    def create_reservation_interface(self):
        self.root.geometry("800x600")

        # Destroy login interface widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        welcome_label = tk.Label(self.root, text=f"Welcome, {self.current_user}!", font=("Arial", 16))
        welcome_label.pack(pady=10)

        route_label = tk.Label(self.root, text="Select Route:", font=("Arial", 12))
        route_label.pack()

        self.routes = ["Route 1", "Route 2", "Route 3"]
        self.selected_route = tk.StringVar(value=self.routes[0])

        route_dropdown = tk.OptionMenu(self.root, self.selected_route, *self.routes)
        route_dropdown.config(font=("Arial", 12))
        route_dropdown.pack()

        self.create_seats_grid()

        self.total_price = 0
        self.price_label = tk.Label(self.root, text=f"Ticket Price: ${self.total_price:.2f}", font=("Arial", 12))
        self.price_label.pack()

        logout_button = tk.Button(self.root, text="Log Out", command=self.logout, font=("Arial", 12))
        logout_button.pack(pady=10)

    def create_seats_grid(self):
        num_rows = 5
        num_columns = 4
        seat_frame = tk.Frame(self.root)
        seat_frame.pack(pady=20)

        self.seat_buttons = [[None] * num_columns for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_columns):
                row = i + 1
                col = j + 1
                button_text = f"({row}, {col})"
                self.seat_buttons[i][j] = tk.Button(seat_frame, text=button_text, font=("Arial", 12))
                self.seat_buttons[i][j].config(command=lambda r=row, c=col: self.reserve_seat(r, c))
                self.seat_buttons[i][j].grid(row=i, column=j, padx=10, pady=10)

    def update_price_label(self):
        self.price_label.config(text=f"Ticket Price: ${self.total_price:.2f}")

    def reserve_seat(self, row, col):
        selected_route = self.selected_route.get()
        price = self.calculate_ticket_price(row, col)
        self.total_price += price
        self.update_price_label()
        self.seat_buttons[row - 1][col - 1].config(state="disabled")
        self.seat_buttons[row - 1][col - 1].config(text=f"Reserved")
        messagebox.showinfo("Seat Reserved", f"Seat ({row}, {col}) on {selected_route} is reserved.\nTicket Price: ${price:.2f}")

    def calculate_ticket_price(self, row, col):
        # You can implement your own logic to calculate ticket price based on row, col, route, etc.
        return 25.0

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username in self.credentials and self.credentials[username] == password:
            self.current_user = username
            self.logged_in = True
            self.create_reservation_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    def logout(self):
        self.root.destroy()
        self.show_thank_you_message()

    def show_thank_you_message(self):
        thank_you_window = tk.Tk()
        thank_you_window.title("Thank You!")
        thank_you_label = tk.Label(thank_you_window, text="Thank you for using our bus ticket reservation system!", font=("Arial", 16))
        thank_you_label.pack(pady=20)
        thank_you_window.geometry("400x200")
        thank_you_window.mainloop()

def main():
    root = tk.Tk()
    bus_system = BusReservationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
