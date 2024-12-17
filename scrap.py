import requests
from bs4 import BeautifulSoup
import time

# Задаємо URL сторінки
url = "https://iq.vntu.edu.ua/b04213/teach_journ/stud_journ.php"

# Попередньо отриманий вміст таблиці
previous_rows = []

def check_for_new_rows():
    global previous_rows
    
    # Отримуємо вміст сторінки
    response = requests.get(url)
    response.raise_for_status()  # Перевірка на помилки запиту
    
    # Парсимо HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Знаходимо таблицю та всі рядки в ній
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        
        # Якщо є нові рядки
        if len(rows) > len(previous_rows):
            print("УРААА! З'явився новий рядок.")
            previous_rows = rows  # Оновлюємо попередні рядки
        else:
            print("Немає нових рядків.")
    else:
        print("Таблиця не знайдена на сторінці.")

# Перевіряємо кожні 10 хвилин
while True:
    check_for_new_rows()
    time.sleep(600)  # Чекаємо 10 хвилин (600 секунд)
