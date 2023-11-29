#MOD7Q1
import tkinter as tk
from app.functions import StudentReportFunctions

class StudentReportApp:
    # Initialization of the application class
    def __init__(self, master, load_button, calculate_button, display_button, listbox):
        self.master = master  # Main window
        self.load_button = load_button  # Button to load CSV
        self.calculate_button = calculate_button  # Button to calculate average
        self.display_button = display_button  # Button to display report
        self.listbox = listbox  # Listbox to display data
        self.data = []  # List to hold data

    # Function to load CSV data
    def load_csv(self):
        try:
            StudentReportFunctions.load_csv(self.data)  # Load data from CSV
            self.update_listbox()  # Update the listbox with new data
        except Exception as e:
            print(f"Error loading data: {e}")  # Print any error that occurs

    # Function to update the listbox with data
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear existing entries in the listbox
        for item in self.data:  # Loop through the data
            self.listbox.insert(tk.END, item)  # Insert each item into the listbox

    # Function to calculate average scores
    def calculate_average(self):
        StudentReportFunctions.calculate_average(self.data)  # Calculate averages
        self.update_listbox()  # Update the listbox to show updated data

    # Function to display the report
    def display_report(self):
        StudentReportFunctions.display_report(self.data, self.listbox)  # Display the report
        self.update_listbox()  # Update the listbox to show the report

# Main function to set up the GUI
def main():
    root = tk.Tk()  # Create the main window
    root.title("Student Report Application")  # Set title of the main window

    # Create GUI components (buttons and listbox)
    load_button = tk.Button(root, text="Load CSV")
    calculate_button = tk.Button(root, text="Calculate Average")
    display_button = tk.Button(root, text="Display Report")
    listbox = tk.Listbox(root, height=10, width=40)

    # Pack (place) GUI components in the main window
    load_button.pack(pady=10)
    calculate_button.pack(pady=10)
    display_button.pack(pady=10)
    listbox.pack(pady=10)

    # Create an instance of the application class with GUI components
    app = StudentReportApp(root, load_button, calculate_button, display_button, listbox)

    # Configure buttons to execute respective functions when clicked
    load_button.config(command=app.load_csv)
    calculate_button.config(command=app.calculate_average)
    display_button.config(command=app.display_report)

    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Execute the main function
