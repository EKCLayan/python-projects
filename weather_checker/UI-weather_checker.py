import requests
import tkinter 

window = tkinter.Tk()
window.configure(bg="#1a1a1a")
window.iconbitmap("Weather_icon.ico")
window.title("Weather_Checker")



def cli_weatherchecker():
  url = "https://api.open-meteo.com/v1/forecast?latitude=1.349500&longitude=103.868139&daily=sunset,sunrise&hourly=temperature_2m,rain,showers&current=is_day,showers,precipitation,rain&timezone=Asia%2FSingapore&forecast_days=1"

  response = requests.get(url)

  data = response.json()

  Time = data["current"]["time"]
  label_time.config(text = f"Current Time: {Time}")
 

  if (data["current"]["rain"]) == 0.0:
     raincheck = "No rain"
  elif (data["current"]["rain"]) > 0.0 and (data["current"]["rain"]) <= 0.5:
     raincheck = "Drizzling"
  elif (data["current"]["rain"]) >= 0.6 and (data["current"]["rain"]) <= 2.5:
     raincheck ="Light rain"
  elif (data["current"]["rain"]) >= 2.6 and (data["current"]["rain"]) <= 10:
     raincheck = "Moderate rain"
  elif (data["current"]["rain"]) > 10:
     raincheck = "Heavy rain"

  label_raincheck.config(text = f"Current condition: {raincheck}")

  current_hour = int(data["current"]["time"][11:13])

  Temp = data["hourly"]["temperature_2m"][current_hour]
  
  label_Temp.config(text = f"Current Temperature:{Temp}°C")
  

label_time = tkinter.Label(window, text = f"Current Time: --",bg="#1a1a1a",fg="#ffffff")
label_time.pack()

label_raincheck = tkinter.Label(window, text = f"Current condition: --",bg="#1a1a1a",fg="#ffffff")
label_raincheck.pack()  
  
label_Temp = tkinter.Label(window, text = f"Current Temperature: --°C",bg="#1a1a1a",fg="#ffffff")
label_Temp.pack()


button =  tkinter.Button(window, text = "Check Weather",command=cli_weatherchecker,bg="#1a1a1a",fg="#ffffff")

button.pack()
                         
window.mainloop()
