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
