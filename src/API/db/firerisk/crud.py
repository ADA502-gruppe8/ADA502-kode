import psycopg2

def print_data(table):
    conn = psycopg2.connect("dbname=firerisk user=postgres password=123456aa host=host.docker.internal port=5555")    
    cursor = conn.cursor()
    try:
        cursor.execute(f'SELECT * FROM {table}')
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(f'Data not printed. Error: {e}')

def insert_location(latitude, longitude):
    conn = psycopg2.connect("dbname=firerisk user=postgres password=123456aa host=host.docker.internal port=5555")    
    cursor = conn.cursor()
    try:
        cursor.execute(
            ("INSERT INTO locations (latitude, longitude) VALUES (%s, %s)"),
            (latitude, longitude)
        )
        conn.commit()
        print("Location inserted successfully")
    
    except psycopg2.Error as e:
        print(f'Error inserting location: {e}')

# Insert into the weather_observations table
def insert_weather_observation(db, location_id, timestamp, temperature, humidity, wind_speed):
    try:
        cursor.execute(
            ("INSERT INTO weather_observations (location_id, timestamp, temperature, humidity, wind_speed) VALUES (%s, %s, %s, %s, %s)"),
            (location_id, timestamp, temperature, humidity, wind_speed)
        )
        conn.commit()
        print("Weather observation inserted successfully")
    
    except psycopg2.Error as e:
        print(f'Error inserting weather observation: {e}')

# Insert into the weather_forecasts table
def insert_weather_forecast(db, location_id, timestamp, temperature, humidity, wind_speed):
    try:
        db.cursor.execute(
            ("INSERT INTO weather_forecasts (location_id, timestamp, temperature, humidity, wind_speed) VALUES (%s, %s, %s, %s, %s)"),
            (location_id, timestamp, temperature, humidity, wind_speed)
        )
        db.mydb.commit()
        print("Weather forecast inserted successfully")
    
    except psycopg2.Error as e:
        print(f'Error inserting weather forecast: {e}')

# Insert into the fire_risk_predictions table
def insert_fire_risk_prediction(location_id, timestamp, fire_risk_score):
    conn = psycopg2.connect("dbname=firerisk user=postgres password=123456aa host=host.docker.internal port=5555")    
    cursor = conn.cursor()
    try:
        cursor.execute(
            ("INSERT INTO fire_risk_predictions (location_id, timestamp, fire_risk_score) VALUES (%s, %s, %s)"),
            (location_id, timestamp, fire_risk_score)
        )
        conn.commit()
        print("Fire risk prediction inserted successfully")
    
    except psycopg2.Error as e:
        print(f'Error inserting fire risk prediction: {e}')

def delete_data(db, Lokasjon):
    try:
        db.cursor.execute("""DELETE FROM frcm
                        WHERE lokasjon = %s""", (Lokasjon,))
        db.mydb.commit()
        print("Data deleted successfully")
    
    except Exception as e:
        print(f'Data not deleted. Error: {e}')
