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

    def get_client_name(self, client_id):
        query = "SELECT first_name, last_name FROM clients WHERE client_id = ?"
        self.cursor.execute(query, (client_id,))
        result = self.cursor.fetchone()
        if not result:
            raise ClientNotFoundException(f"Client with ID {client_id} not found.")
        return f"{result[0]} {result[1]}"
