from hotel.hotel import Hotel

DB_PATH = "hotel.db"

def main():
    hotel = Hotel(DB_PATH)

    # Dodaj klienta
    client_id = hotel.add_client("Mark", "Lee", 35)
    print(f"Dodano klienta o ID: {client_id}")

    # Pobierz imię i nazwisko klienta
    name = hotel.get_client_name(client_id)
    print(f"Imię i nazwisko klienta: {name}")