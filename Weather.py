import requests
import json #библиотеки

with open('config.json', 'r', encoding='utf-8') as f:  # открываем конфигурационный файл json
    text = json.load(f)  # загнали все из файла в переменную

for txt in text['owm']:  # создали цикл, который будет работать построчно
    lat = (txt['lat'])  # вытаскиваем переменные из файла
    lon = (txt['lon'])
    appid = (txt['appid'])

print('\n Прогноз погоды сейчас\n')
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'lat': lat, 'lon':lon, 'units': 'metric', 'lang': 'eng', 'APPID': appid})
    data = res.json()
    #print(res.text)
#    d = data['dt']
    print('coord.lat', data['coord']['lat'])
    print('coord.lon', data['coord']['lon'])
    print('unix_time', data['dt'])
#    dt = datetime.fromtimestamp(int(d))
#    print('Время вычисления данных, UTC', dt.strftime("%d.%m.%y %H:%M:%S"))
#    print('UTC', '+', data['timezone'] / 60 / 60)
#    print("id:", data['weather'][0]['id'])
#    print("Погода:", data['weather'][0]['main'])
#    print("Погода:", data['weather'][0]['description'])
    print('Temp:',data['main']['temp'])
    print('Temp_feels:',data['main']['feels_like'])
    print('Pressure:', data['main']['pressure'], 'hPa')
    print('Humidity:', data['main']['humidity'], '%')
    print('Pressure_sea:', data['main']['sea_level'], 'hPa')
    print('Pressure_grnd:', data['main']['grnd_level'], 'hPa')
    print('visibility:', data['visibility'])
    print('wind_seed:', data['wind']['speed'], 'м/с')
    print('wind_deg:', data['wind']['deg'], '*')
    print('wind_gust:', data['wind']['gust'], 'м/с')
    print('clouds:', data['clouds']['all'], '%')
    print('sunrise_unix', data['sys']["sunrise"])
    print('sunset_unix', data['sys']["sunset"])


#    s = data['sys']['sunrise']
#    st = datetime.fromtimestamp(int(s))
#    print('Восход:', st.strftime("%d.%m.%y %H:%M:%S"))
#    z = data['sys']['sunset']
#    zt = datetime.fromtimestamp(int(z))
#    print('Закат:', zt.strftime("%d.%m.%y %H:%M:%S"))


except Exception as e:
    print("Exception (weather):", e)
    pass

try:
    print('snow_1h', data['snow']['1h'], 'мм')
except Exception as e:
    print("Exeption (weather):", e)
    snow_1h = 0
    pass

try:
    print('rain_1h', data['rain']['1h'], 'мм')
except Exception as e:
    print("Exeption (weather):", e)
    rain_1h = 0
    pass

'''
print('\n Прогноз погоды на 5 дней каждые 3 часа\n')

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
        print("Exception (forecast):", e)
        pass
'''
