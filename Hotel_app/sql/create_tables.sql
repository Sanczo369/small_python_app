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
