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

    def count_minors(self):
        query = "SELECT COUNT(*) FROM clients WHERE age < 18"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def add_room(self, floor, bed_type, area):
        query = "INSERT INTO rooms (floor, bed_type, area) VALUES (?, ?, ?)"
        self.cursor.execute(query, (floor, bed_type, area))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_room_area(self, room_id):
        query = "SELECT area FROM rooms WHERE room_id = ?"
        self.cursor.execute(query, (room_id,))
        result = self.cursor.fetchone()
        if not result:
            raise RoomNotFoundException(f"Room with ID {room_id} not found.")
        return result[0]
