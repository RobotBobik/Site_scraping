import time
import requests
from bs4 import BeautifulSoup

def check_for_new_rows():
    url = "https://iq.vntu.edu.ua/b04213/teach_journ/stud_journ.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        print(row.get_text())

while True:
    check_for_new_rows()
    time.sleep(1200)
