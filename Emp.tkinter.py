import tkinter as tk
from tkinter import ttk
import csv

class MovieAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("تحليل بيانات الموظفين")

        self.movies = []

        self.category_label = tk.Label(self.root, text="اختر فئة الموظف:")
        self.category_label.pack()

        self.category_combobox = ttk.Combobox(self.root, values=["HR", "الاداريين", "المهندسين","المبرمجين","المحاسبين","الفنيين"])
        self.category_combobox.pack()

        self.load_button = tk.Button(self.root, text="تحميل البيانات", command=self.load_data)
        self.load_button.pack()

        self.movies_listbox = tk.Listbox(self.root, width=60)
        self.movies_listbox.pack()

        self.root.mainloop()

    def load_data(self):
        category = self.category_combobox.get()
        self.movies_listbox.delete(0, tk.END)

        try:
            with open("movies.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == category:
                        self.movies_listbox.insert(tk.END, row[0])
        except FileNotFoundError:
            tk.messagebox.showerror("خطأ", "لا يمكن العثور على ملف البيانات")

if __name__ == "__main__":
    analyzer = MovieAnalyzer()
