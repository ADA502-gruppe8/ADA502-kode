import psycopg2
# import asyncpg

class Database:
    def __init__(self, dsn):
        self.conn = None
        self.dsn = dsn

    async def connect(self):
        try:
            self.conn = await psycopg2.connect(self.dsn)
            print("Database connection was successful")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")

    async def close(self):
        if self.conn:
            await self.conn.close()
            print("Database connection closed")