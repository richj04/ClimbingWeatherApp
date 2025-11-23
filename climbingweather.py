#a temeprature app for the crag

import requests
from datetime import datetime
import pytz

API_KEY = "4f8c6cec0b07527a37d7b7fe92dad5fa"

def get_weather(lat, lon):
    url = (f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial')
    response = requests.get(url)
    return response.json()

crags = {
    "SLC": (40.7606, -111.8910),
    "Little Cottonwood": (40.5710, -111.7070),
    "Big Cottonwood": (40.6249, -111.7997),
    "American Fork Canyon": (40.435, -111.676),
    "Joes Valley": (39.8504, -111.3394),
    "Moes Valley": (37.06533, -113.63443),
    "Logan Canyon": (41.8633, -111.7962),
    "Hueco Tanks": (31.9460, -106.0375),
    "Bishop": (37.3611,-118.3996),
    "Rocky Mountain": (40.3428, -105.6836),
    "Red Rock Canyon": (36.1351, -115.4270),
    "Font": (48.4030, 2.7020),
    "Rocklands": (-32.1587, 19.1572),
    "Magic Wood": (46.8620, 9.1160),
    
    "North Antartica": (-82.8628, 135.0000)

}

print("What crag we climbing at brotato? Your options are: ")
for crag in crags.keys():
    print(crag)

choice = input('Enter the crag name exactly pls: ')

if choice in crags:
    lat, lon = crags[choice]
    print(f'wow you actually can spell! Here is available climbing windows for {choice}:')
else:
    print('nice try brotato, try spelling correctly next time... ')
    print('Just so my code doesnt crash lets give you the conditions for climbing in North Antartica:')
    lat, lon = crags["North Antartica"]

print('---------------------------------------------')
#-----------------------------------#
weather_data = get_weather(lat, lon)

def utc_to_mst(utc_string):
    utc_time = datetime.strptime(utc_string, '%Y-%m-%d %H:%M:%S')
    mst_time = utc_time.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('US/Mountain'))
    return mst_time.strftime('%m/%d %I:%M %p') 

foundGoodWeather = False

def checkConditions(index):

    global foundGoodWeather
    tempMin = 40.0
    tempMax = 65.0
    humidityMax = 70.0
    badWeather = ('Rain','Snow')

    dt_txt = weather_data['list'][index]['dt_txt']
    local_time = utc_to_mst(dt_txt)  

    temp = weather_data['list'][index]['main']['temp']
    humidity = weather_data['list'][index]['main']['humidity']
    weatherType = weather_data['list'][index]['weather'][0]['main']
    
  

    if (temp >= tempMin and temp <= tempMax and humidity <= humidityMax and weatherType not in badWeather):
        print(f'valid 3 hour climbing window starting at: {local_time}')
        print(f'full weather details for this window -> temp: {temp} humidity: {humidity} weatherType: {weatherType}')
        print('')

        foundGoodWeather = True

        return
    else:
        return 

for x in range(40):
    checkConditions(x)

if foundGoodWeather == False:
    print('no good conditions lol, try again next week')