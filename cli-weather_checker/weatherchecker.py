import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=1.349500&longitude=103.868139&daily=sunset,sunrise&hourly=temperature_2m,rain,showers&current=is_day,showers,precipitation,rain&timezone=Asia%2FSingapore&forecast_days=1"

response = requests.get(url)

data = response.json()

print("Current Time",data["current"]["time"])

if (data["current"]["rain"]) == 0.0:
  print("No rain")
elif (data["current"]["rain"]) > 0.0 and (data["current"]["rain"]) <= 0.5:
  print("Drizzling")
elif (data["current"]["rain"]) >= 0.6 and (data["current"]["rain"]) <= 2.5:
  print("Light rain")
elif (data["current"]["rain"]) >= 2.6 and (data["current"]["rain"]) <= 10:
  print("Moderate rain")
elif (data["current"]["rain"]) > 10:
  print("Heavy rain")

current_hour = int(data["current"]["time"][11:13])

print("Current Tempertaure",data["hourly"]["temperature_2m"][current_hour], "°C")
