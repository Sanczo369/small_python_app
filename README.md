# Small Python App
Small Python App in Tkinter


## Kółko i krzyżyk
Jest to program gry "Kółko i krzyżyk" (Tic Tac Toe) w interfejsie graficznym za pomocą biblioteki tkinter w języku Python. Oto opis aplikacji:
### Oto rozkład kodu:
- Importowanie potrzebnych modułów
- Tworzenie zmiennych globalnych
- Funkcje
- Plansza gry
- Inicjalizacja głównego okna root 
- Konfiguracja okna, ikony, tytułu i rozmiaru.
- Tworzenie elementów interfejsu: etykiety, przycisk
### Opis działania
Aplikacja skupia się na grze "Kółko i krzyżyk", umożliwiając rozpoczęcie rozgrywki, wyświetlenie informacji o autorze i zamknięcie programu. Plansza gry jest obsługiwana przez funkcje make_move, check_winner i announce_winner. Gdy gra zostanie zakończona, pojawi się okno z informacją o zwycięzcy. Po zakończeniu gry użytkownik może wrócić do głównego menu.
### requirements
- PIL
- tkinter

  
## Prosty Kalkulator
Jest to program w języku Python wykorzystujący bibliotekę Tkinter do stworzenia prostej aplikacji kalkulatora z graficznym interfejsem użytkownika (GUI).
### Oto rozkład kodu:
- Importowanie Tkintera
- Tworzenie okna GUI
- Definiowanie funkcji kalkulatora
- Tworzenie elementów GUI
- Pozycjonowanie elementów GUI
- Główna pętla zdarzeń
### Operacje matematyczne:
- Dodawanie (+)
- Odejmowanie (-)
- Mnożenie (x)
- Dzielenie (÷)
- Procent liczby (%)
### requirements
- PIL
- tkinter
### Opis działania
Ten kod tworzy podstawową aplikację kalkulatora z prostym interfejsem użytkownika. Użytkownicy mogą wykonywać podstawowe operacje arytmetyczne, klikając przyciski, a wynik jest wyświetlany w polu wejściowym.


## Generowania kodów QR
Aplikacją do generowania kodów QR z interfejsem graficznym przy użyciu biblioteki qrcode, tkinter, i PIL. 
### Bibliotekę qrcode
Upewnij się, że masz bibliotekę qrcode zainstalowaną na swoim systemie, aby ten program działał poprawnie. Jeśli nie jest zainstalowana, możesz ją zainstalować za pomocą narzędzia pip, wykonując polecenie:
pip install qrcode
### requirements
- PIL
- tkinter
- qrcode


  
## Stoper
 Aplikacja Stoper napisana w Pythonie przy użyciu modułu Tkinter do tworzenia interfejsu graficznego. Aplikacja umożliwia użytkownikowi uruchamianie, zatrzymywanie i resetowanie stopera.
### Oto rozkład kodu:
- Importowanie modułów
- Inicjalizacja zmiennych
- Funkcje
- Tworzenie głównego okna Tkinter
- Styl przycisków
- Tworzenie interfejsu użytkownika
- Układ elementów
- Uruchomienie głównej pętli Tkinter:
### Funkcje
- start(): Rozpoczyna działanie stopera, wywołując funkcję update().
- pause(): Zatrzymuje stoper poprzez anulowanie aktualizacji czasu.
- reset(): Resetuje stoper do stanu początkowego, zerując zmienne czasu i ustawiając etykietę z czasem na "00:00:00".
- update(): Aktualizuje czas na stoperze, inkrementując sekundy, minuty i godziny, a następnie formatuje czas i aktualizuje etykietę co sekundę za pomocą after().
### requirements
- PIL
- tkinter


  
## To Do List
Aplikacja "To-Do List" (lista zadań) jest narzędziem, które pomaga użytkownikom organizować swoje obowiązki, zadania i plany w sposób bardziej efektywny.
Aplikacja zapisuje liste zadań do plku txt co pozwala przy ponownym uruchomieniu aplikacji widok zadań które były wpisane wcześniej i nie zostały usunięty podczas poprzedniego używania aplikacji
### Oto rozkład kodu:
- Importowanie Tkinter
- Inicjalizacja głównego okna
- Ustawienie tytułu, rozmiaru i tła
- Zmienna "value"
- Funkcja "add"
- Główna pętla programu
### requirements
- tkinter



## Time and data
Aplikacja Time and data napisana w Pythonie przy użyciu modułu Tkinter do tworzenia interfejsu graficznego. Aplikacja umożliwia użytkownikowi wyświetlenie aktualnej godziny oraz daty.
### Oto rozkład kodu:
- Importowanie niezbędnych bibliotek
- Tworzenie głównego okna aplikacji
- Definiowanie funkcji update
- Tworzenie elementów GUI
### requirements
- datetime
- tkinter
- time



## Quiz
Aplikacja Quiz napisana w Pythonie przy użyciu modułu Tkinter do tworzenia interfejsu graficznego. Aplikacja jest rodzaj zabawy, rozrywki intelektualnej, polegającej na odpowiedz na losowe pytania z 4 wariantami odpowiedzi.
### Pliki
- quiz_ui.py
- quiz_data.py
- quiz_brain.py
- main.py
- question_model.py
- logo.ico
### requirements
- tkinter
- question_model
- quiz_data
- quiz_brain
- quiz_ui
- random
- html
### Opis działania
Aplikacjawyświetla pytanie oraz 4 warianty odpowiedzi po udzieleniu odpowiedzi gracz otrzymuje informacje o prawidłowej odpowiedzi. Po odpowiedzi na 10 pytań program wyświetla rezulta z informacją o procentowej skutecznośći oraz liczbie prawidłowych oraz błędnych odpowiedzi. Pytania pobierane są ze strony opentdb.com



## BMI CALCULATOR
Aplikacja pozwala na szybkie i precyzyjne obliczenie Twojego BMI na podstawie podanych danych takich jak masa ciała i wzrost. Dzięki temu dowiesz się, czy Twoja waga jest w normie, czy może wymaga pewnych zmian.
### Oto rozkład kodu:
- Importowanie Tkinter
- Inicjalizacja głównego okna
- Ustawienie tytułu, rozmiaru i tła
- Funkcja BMI()
- Tworzenie interfejsu użytkownika
- Główna pętla programu
### requirements
- tkinter


  
## Data Entry
Aplikacja umożliwia wprowadzanie danych osobowych do arkusza kalkulacyjnego i zapisywanie ich w pliku "Backened_Data.xlsx".
### Oto rozkład kodu:
- Importowanie potrzebnych modułów:(openpyxl, xlrd,tkinter)
- Inicjalizacja głównego okna aplikacji:
- Sprawdzanie istnienia pliku "Backened_Data.xlsx" i jego tworzenie, jeśli nie istnieje.
- Funkcje clear() i submit():
clear(): Czyści wprowadzone dane w polach tekstowych i komboboxie.
submit(): Pobiera dane z pól wprowadzania, zapisuje je do arkusza kalkulacyjnego "Backened_Data.xlsx", wyświetla komunikat o sukcesie i czyści pola wprowadzania.
- Tworzenie etykiet, pól tekstowych, komboboxa i przycisków w oknie głównym aplikacji.
- Uruchamianie root.mainloop()
  
## White_board
Proste narzędzie do rysowania i malowania z graficznym interfejsem użytkownika (GUI) wykorzystującym bibliotekę Tkinter w Pythonie.
### Oto rozkład kodu:
- Interfejs użytkownika
- Rysunek na płótnie
- Paleta kolorów
- Suwak grubości linii
- Przycisk Gumki 
- Funkcjonalność rysowania
- Wybór koloru
- Regulacja grubości linii
- Wyczyść płótno

## Translate
Aplikacja "Translator" stworzona w Pythonie przy użyciu biblioteki Tkinter do tworzenia interfejsu graficznego użytkownika (GUI). Aplikacja przy pomocy modułu googletrans tłumaczy tekstu przy użyciu Google Translate.
### Oto rozkład kodu:
- Importowanie niezbędnych modułów i bibliotek
- Definiowanie dwóch głównych funkcji:label_change() i translate_now()
- Tworzenie elementów interfejsu graficznego
- Inicjalizacja aplikacji

## Excel_Viewer
Aplikacja to przeglądarkę arkuszy danych programu Excel za pomocą Pythona. jest to całkowicie projekt GUI Tkinter
### requirements
- numpy
- pandas
## Student Registration System
Aplikacja "Student Registration System" to system rejestracji studentów z bazą danych Excel przy użyciu Pythona. jest to całkowicie projekt GUI Tkinter
### requirements
- pathlib
- openpyxl
- xlrd
- pillow
- tkinter
- xlsxwriter
- PIL
- datetime
- os
## Bill Mangement
Aplikacja "Bill Mangement" to system wyliczający wartość rachunku na podstawie ceny oraz ilośći zamowionych dań przy użyciu Pythona. jest to całkowicie projekt GUI Tkinter
### Oto rozkład aplikacji:
- Belka z nazwą aplikacji
- Aktualne Menu z cenami
- formularz do wprowadzenia ilości zamówionych dań
- Przycisk do resetu
- Przycisk do podliczenia 
- wyświetlenie sumy za zamówienie

## Speed Test
Aplikacja "Speed Test" to system wyliczający wartość PING, DOWNLOAD oraz UPLOAD
### requirements
- speedtest
- tkinter

## PDF Protector Tool
Program do szyfrowania pliku formacie PDF. Jest to projekt całkowicie gui tkinter.
### requirements
- PyPDF2
- tkinter
