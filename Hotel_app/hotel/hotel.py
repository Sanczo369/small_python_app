import sqlite3
from hotel.exceptions import (
    ClientNotFoundException,
    RoomNotFoundException,
    RoomReservedException,
)


class Hotel:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def add_client(self, first_name, last_name, age):
        query = "INSERT INTO clients (first_name, last_name, age) VALUES (?, ?, ?)"
        self.cursor.execute(query, (first_name, last_name, age))
        self.connection.commit()
        return self.cursor.lastrowid