# prompt: use tkinter to make an UI taking the users inputs and showing the results
import tkinter as tk
import requests

def get_exchange_rate(from_currency, to_currency):
  """Fetches the exchange rate between two currencies using the ExchangeRate-API."""
  your_api_key="9decbe2aaa-9b4dff2ae4-sk8pln"

  url=f"https://api.fastforex.io/fetch-one?from={from_currency}&to={to_currency}&api_key={your_api_key}"
  headers = {"accept": "application/json"}
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()

    if "result" in data:
      if isinstance(data["result"], dict):
          for currency, rate in data["result"].items():
              return rate
    elif "error" in data:
      print(f"Error: {data['error']}")
      return None
    else:
      print("Error fetching exchange rate: API returned an error.")
      return None
  except requests.exceptions.RequestException as e:
    print(f"Error connecting to the API: {e}")
    return None
  except KeyError:
    print("Error: Invalid currency code provided.")
    return None

def convert_currency():
  try:
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()

    exchange_rate = get_exchange_rate(from_currency, to_currency)

    if exchange_rate:
      converted_amount = amount * exchange_rate
      result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
      result_label.config(text="Error fetching exchange rate.")
  except ValueError:
    result_label.config(text="Please enter a valid amount.")

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Create and place labels and entry widgets
amount_label = tk.Label(window, text="Enter Amount:")
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1)

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.grid(row=1, column=0)
from_currency_entry = tk.Entry(window)
from_currency_entry.grid(row=1, column=1)

to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.grid(row=2, column=0)
to_currency_entry = tk.Entry(window)
to_currency_entry.grid(row=2, column=1)

# Create and place the convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the tkinter event loop
window.mainloop()