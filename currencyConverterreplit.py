import json
def get_exchange_rate(source_currency, destination_currency, exchange_rates):
  """Gets the exchange rate between two currencies."""
  if source_currency == destination_currency:
    return 1.0
  else:
    return exchange_rates.get(source_currency, {}).get(destination_currency, None)
def convert_currency(amount, source_currency, destination_currency, exchange_rates):
  """Converts an amount from one currency to another."""
  rate = get_exchange_rate(source_currency, destination_currency, exchange_rates)
  if rate is None:
    return "Invalid currency code."
  else:
    return amount * rate
# Define exchange rates (you can replace this with an API call or a JSON file)
exchange_rates = {
  "USD": {"EUR": 0.90, "JPY": 130.00},
  "EUR": {"USD": 1.11, "JPY": 144.00},
  "JPY": {"USD": 0.0077, "EUR": 0.0069}
}
# Get user input
amount = float(input("Enter the amount: "))
source_currency = input("Enter the source currency: ").upper()
destination_currency = input("Enter the destination currency: ").upper()
# Perform the conversion
converted_amount = convert_currency(amount, source_currency, destination_currency, exchange_rates)
# Display the result
print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {destination_currency}")