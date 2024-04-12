import psycopg2

def print_data(db, table):
    try:
        db.cursor.execute(f'SELECT * FROM {table}')
        for row in db.cursor.fetchall():
            print(row)
    except Exception as e:
        print(f'Data not printed. Error: {e}')

def insert_frcm_data(db, Lokasjon, Dato, Temperatur, Fuktighet, Vind, Regnfall, Firerisk):
    try:
        db.cursor.execute("""INSERT INTO frcm (
                    lokasjon, 
                    dato, 
                    temp, 
                    fuktighet, 
                    vind, 
                    regnfall, 
                    firerisk) 
                    VALUES 
                    (%s, %s, %s, %s, %s, %s, %s)""", 
                    (Lokasjon, Dato, Temperatur, Fuktighet, Vind, Regnfall, Firerisk))
        db.mydb.commit()
        print(f"{Lokasjon} inserted successfully")
    except psycopg2.Error as e:
        print(f'Data not inserted Error: {e}')

def delete_data(db, Lokasjon):
    try:
        db.cursor.execute("""DELETE FROM frcm
                        WHERE lokasjon = %s""", (Lokasjon,))
        db.mydb.commit()
        print("Data deleted successfully")
    except Exception as e:
        print(f'Data not deleted. Error: {e}')
