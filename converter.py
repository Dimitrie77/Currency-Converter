import tkinter as tk
from tkinter import ttk, messagebox
import requests

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        
        url = f"https://openexchangerates.org/api/latest.json?app_id=1adf188095a546c894518bac1dab1450"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            rates = data['rates']
            from_rate = rates[from_currency]
            to_rate = rates[to_currency]
            converted_amount = (amount / from_rate) * to_rate
            result_textbox.config(state=tk.NORMAL)
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            result_textbox.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Eroare", f"Nu am putut obține rata de schimb: {data['description']}")
    except ValueError:
        messagebox.showerror("Eroare", "Vă rugăm să introduceți o sumă validă.")
    except KeyError:
        messagebox.showerror("Eroare", "Codul monedei introdus nu este valid.")
    except Exception as e:
        messagebox.showerror("Eroare", str(e))

def switch_currencies():
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    from_currency_combobox.set(to_currency)
    to_currency_combobox.set(from_currency)

app = tk.Tk()
app.title("Convertor Valutar")
app.geometry("800x400")

style = ttk.Style(app)
style.theme_use('clam')
style.configure('TButton', font=('Arial', 12), background='light green')
style.configure('TLabel', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=10)
style.configure('TCombobox', font=('Arial', 12), padding=10)

main_frame = ttk.Frame(app, padding="10")
main_frame.grid(sticky=(tk.E + tk.W + tk.N + tk.S))
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

header_label = ttk.Label(main_frame, text="Convertor Valutar", font=('Arial', 16))
header_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')


tk.Label(main_frame, text="Suma:").grid(row=1, column=0, sticky='e')
amount_entry = ttk.Entry(main_frame)
amount_entry.grid(row=1, column=1, sticky='ew')

tk.Label(main_frame, text="Selectați moneda sursă:").grid(row=2, column=0, sticky='e')
from_currency_combobox = ttk.Combobox(main_frame, values=["USD", "EUR", "GBP", "JPY", "RON"], state="readonly")
from_currency_combobox.grid(row=2, column=1, sticky='ew')
from_currency_combobox.current(0)

tk.Label(main_frame, text="Selectați moneda țintă:").grid(row=3, column=0, sticky='e')
to_currency_combobox = ttk.Combobox(main_frame, values=["USD", "EUR", "GBP", "JPY", "RON"], state="readonly")
to_currency_combobox.grid(row=3, column=1, sticky='ew')
to_currency_combobox.current(1)

convert_button = ttk.Button(main_frame, text="Convertește", command=convert_currency)
convert_button.grid(row=4, column=0, columnspan=2, sticky='ew', pady=10)

switch_button = ttk.Button(main_frame, text="Inverseaza Valutele", command=switch_currencies)
switch_button.grid(row=5, column=0, columnspan=2, sticky='ew', pady=10)

result_label = ttk.Label(main_frame, text="Rezultatul:")
result_label.grid(row=6, column=0, sticky='e')

result_textbox = tk.Text(main_frame, height=2, width=30)
result_textbox.grid(row=6, column=1, sticky='ew')
result_textbox.config(state=tk.DISABLED)

for i in range(2):
    main_frame.columnconfigure(i, weight=1)
for i in range(7):
    main_frame.rowconfigure(i, weight=1)

app.mainloop()