INSERT INTO clients (first_name, last_name, age) VALUES
('John', 'Doe', 25),
('Jane', 'Smith', 17),
('Alice', 'Johnson', 30);

INSERT INTO rooms (floor, bed_type, area) VALUES
(1, 'queen', 20.5),
(2, 'king', 25.0),
(1, 'single', 15.0);

INSERT INTO reservations (client_id, room_id, date) VALUES
(1, 1, '2024-12-20'),
(2, 2, '2024-12-21');