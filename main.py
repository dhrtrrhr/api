import requests

valcode = input("введіть валюту")
date = input("введіть рік")

response = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")

print(response.status_code)
result = response.json()
print(result)
rate = result[0]["rate"]
asd = 100 / rate
print(result[0])
print(asd)