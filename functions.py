import tkinter as tk
from tkinter import filedialog
import csv
from operator import itemgetter


class StudentReportFunctions:
    @staticmethod
    def load_csv(data):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            with open(file_path, 'r') as file:
                csv_reader = csv.DictReader(file)

                # Print header names
                print("Headers:", csv_reader.fieldnames)

                # Read and process each row
                data.clear()
                for row in csv_reader:
                    print("Row:", row)
                    # Convert numeric values to integers
                    row_data = {
                        'Name': row.get('Name', ''),
                        'Math': int(row.get('Math', 0)),
                        'English': int(row.get('English', 0)),
                        'History': int(row.get('History', 0))
                    }

                    data.append(row_data)

            print("Loaded data:")
            for row in data:
                print(row)

    @staticmethod
    def calculate_average(data):
        for student in data:
            math = student.get('Math', 0)
            english = student.get('English', 0)
            history = student.get('History', 0)

            # Calculate average only if all values are numeric
            if all(isinstance(value, (int, float)) for value in [math, english, history]):
                average = (math + english + history) / 3
                student['Average'] = average
            else:
                student['Average'] = 0

        # Sort data by average scores in descending order
        data.sort(key=itemgetter('Average'), reverse=True)
        print("Sorted data:", data)

    @staticmethod
    def display_report(data, listbox):
        listbox.delete(0, tk.END)  # Clear previous content

        # Add headers to the listbox
        listbox.insert(tk.END, "{:<15} {:<10}".format("Name", "Average"))
        listbox.insert(tk.END, "-" * 25)

        # Add student names and average scores to the listbox
        for student in data:
            name = student.get('Name', '')
            average = student.get('Average', 0.0)
            listbox.insert(tk.END, "{:<15} {:>10.2f}".format(name, average))
