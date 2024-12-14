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

    # Liczba niepełnoletnich
    minors = hotel.count_minors()
    print(f"Liczba niepełnoletnich klientów: {minors}")

    # Dodaj pokój
    room_id = hotel.add_room(2, "queen", 22.0)
    print(f"Dodano pokój o ID: {room_id}")

    # Powierzchnia pokoju
    area = hotel.get_room_area(room_id)
    print(f"Powierzchnia pokoju: {area} m2")

    # Pokoje z dużym łóżkiem na piętrze
    large_beds = hotel.count_large_bed_rooms_on_floor(2)
    print(f"Liczba pokoi z dużym łóżkiem na piętrze 2: {large_beds}")


if __name__ == "__main__":
    main()