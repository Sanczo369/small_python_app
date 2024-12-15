CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
);

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    floor INTEGER NOT NULL,
    bed_type TEXT NOT NULL,
    area REAL NOT NULL
);

CREATE TABLE reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    confirmed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY(client_id) REFERENCES clients(client_id),
    FOREIGN KEY(room_id) REFERENCES rooms(room_id),
    UNIQUE(room_id, date)
);