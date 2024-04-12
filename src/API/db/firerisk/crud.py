import psycopg2
from API.db.conDeconDb import Database

def print_data(db, table):
    try:
        db.cursor.execute(f'SELECT * FROM {table}')
        for row in db.cursor.fetchall():
            print(row)

    except Exception as e:
        print(f'Data not printed. Error: {e}')

def insert_location_and_get_id(latitude, longitude):
    db = Database("firerisk")
    location_id = None
    try:
        db.cursor.execute(
            "INSERT INTO locations (latitude, longitude) VALUES (%s, %s) RETURNING id",
            (latitude, longitude)
        )
        location_id = db.cursor.fetchone()[0]  # Fetch the ID of the inserted location
        db.conn.commit()
        print("Location inserted successfully, ID:", location_id)
    except psycopg2.Error as e:
        print(f'Error inserting location: {e}')
    finally:
        db.close()
   
    return location_id

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
def insert_fire_risk_prediction(location_id, timestamp, fire_risk_score):
    db = Database("firerisk")
    if location_id is None:
        print("No location ID provided for fire risk prediction.")
    try:
        db.cursor.execute(
            "INSERT INTO fire_risk_predictions (location_id, timestamp, fire_risk_score) VALUES (%s, %s, %s)",
            (location_id, timestamp, fire_risk_score)
        )
        db.conn.commit()
        print("Fire risk prediction inserted successfully")
    except psycopg2.Error as e:
        print(f'Error inserting fire risk prediction: {e}')
    finally:
        db.close()

def delete_data(db, Lokasjon):
    try:
        db.cursor.execute("""DELETE FROM frcm
                        WHERE lokasjon = %s""", (Lokasjon,))
        db.mydb.commit()
        print("Data deleted successfully")
    
    except Exception as e:
        print(f'Data not deleted. Error: {e}')
