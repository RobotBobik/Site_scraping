import requests
from bs4 import BeautifulSoup

def check_for_new_row():
    url = "https://iq.vntu.edu.ua/b04213/teach_journ/stud_journ.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Перевіряємо, чи є таблиця
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        return len(rows)
    else:
        print("Таблиця не знайдена.")
        return 0

# Перевіряємо наявність нового рядка
previous_row_count = check_for_new_row()
new_row_count = check_for_new_row()

if new_row_count > previous_row_count:
    print("УРАА! З'явився новий рядок!")
