import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="11111",
    database="OpenWeatherMap",
    port="5433"
)
print("Database opened successfully")

cur = connection.cursor()
cur.execute('''CREATE TABLE OWM  
     (coord_lat real,
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
