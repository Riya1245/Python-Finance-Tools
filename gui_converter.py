import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import CurrencyConverter

class CurrencyConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")
        master.geometry("400x300") # Set initial window size

        self.converter = CurrencyConverter()
        self.currencies = self.converter.get_available_currencies()

        if not self.currencies:
            messagebox.showerror("Error", "No currencies available. Please check exchange rates.")
            master.destroy()
            return

        # --- Widgets ---
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack(pady=5)

        self.source_label = tk.Label(master, text="Source Currency:")
        self.source_label.pack(pady=5)
        self.source_currency = ttk.Combobox(master, values=self.currencies, state="readonly")
        self.source_currency.pack(pady=5)
        self.source_currency.set(self.currencies[0] if self.currencies else "") # Set default

        self.target_label = tk.Label(master, text="Target Currency:")
        self.target_label.pack(pady=5)
        self.target_currency = ttk.Combobox(master, values=self.currencies, state="readonly")
        self.target_currency.pack(pady=5)
        self.target_currency.set(self.currencies[1] if len(self.currencies) > 1 else "") # Set default

        self.convert_button = tk.Button(master, text="Convert", command=self.perform_conversion)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(master, text="Converted Amount: ")
        self.result_label.pack(pady=5)

    def perform_conversion(self):
        try:
            amount = float(self.amount_entry.get())
            if amount < 0:
                messagebox.showerror("Input Error", "Amount cannot be negative.")
                return

            source = self.source_currency.get()
            target = self.target_currency.get()

            if not source or not target:
                messagebox.showerror("Selection Error", "Please select both source and target currencies.")
                return

            converted_amount = self.converter.convert(amount, source, target)

            if converted_amount is not None:
                self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} {target}")
            else:
                self.result_label.config(text="Conversion failed.")
                messagebox.showerror("Conversion Error", "Could not perform conversion. Check currencies and rates.")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the amount.")
        except Exception as e:
            messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterGUI(root)
    root.mainloop()