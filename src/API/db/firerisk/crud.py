import psycopg2

def print_data(db, table):
    try:
        db.cursor.execute(f'SELECT * FROM {table}')
        for row in db.cursor.fetchall():
            print(row)

    except Exception as e:
        print(f'Data not printed. Error: {e}')

def insert_location(db, latitude, longitude):
    try:
        db.cursor.execute(
            ("INSERT INTO locations (latitude, longitude) VALUES (%s, %s)"),
            (latitude, longitude)
        )
        db.mydb.commit()
        print("Location inserted successfully")
    
    except psycopg2.Error as e:
        print(f'Error inserting location: {e}')

# Insert into the weather_observations table
def insert_weather_observation(db, location_id, timestamp, temperature, humidity, wind_speed):
    try:
        db.cursor.execute(
            ("INSERT INTO weather_observations (location_id, timestamp, temperature, humidity, wind_speed) VALUES (%s, %s, %s, %s, %s)"),
            (location_id, timestamp, temperature, humidity, wind_speed)
        )
        db.mydb.commit()
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
def insert_fire_risk_prediction(db, location_id, timestamp, fire_risk_score):
    try:
        db.cursor.execute(
            ("INSERT INTO fire_risk_predictions (location_id, timestamp, fire_risk_score) VALUES (%s, %s, %s)"),
            (location_id, timestamp, fire_risk_score)
        )
        db.mydb.commit()
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
