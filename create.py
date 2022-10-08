import psycopg2
import json #библиотеки

with open('config.json', 'r', encoding='utf-8') as f:  # открываем конфигурационный файл json
    text = json.load(f)  # загнали все из файла в переменную

    for txt in text['postgres']: # создали цикл, который будет работать построчно
        host = (txt['host'])
        user = (txt['user'])
        password = (txt['password'])
        database = (txt['database'])
        port = (txt['port'])

connection = psycopg2.connect(
    host=host,
    user=(user),
    password=(password),
    database=(database),
    port=(port)
)
print("Database opened successfully")

cur = connection.cursor()
cur.execute('''CREATE TABLE owm_python_parser  
     (id serial PRIMARY KEY,
     coord_lat real,
     coord_lon real,
     unix_time INT,
     temp INT,
     temp_feels INT,
     pressure INT,
     pressure_sea INT,
     pressure_grnd INT,
     humidity INT,
     visibility INT,
     wind_seed real,
     wind_gust real,
     wind_deg INT,
     snow_1h real,
     rain_1h real,
     clouds INT,
     sunrise_unix INT,
     sunset_unix INT);''')

print("Table created successfully")
connection.commit()

connection.close()
