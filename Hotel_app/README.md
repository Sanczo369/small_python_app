# Aplikacja do obsługi rezerwacji hotelowych

## Wymagania

- Python 3.8+
- SQLite3

## Uruchomienie

1. Utwórz bazę danych:
   ```bash
   sqlite3 hotel.db < sql/create_tables.sql
   sqlite3 hotel.db < sql/insert_data.sql