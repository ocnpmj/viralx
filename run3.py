import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import string


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


# Fungsi membaca CSV dengan rentang baris tertentu
def read_csv_range(filename, start, end):
    with open(filename, newline='', encoding='utf-8') as f:
        rows = [row[0] for i, row in enumerate(csv.reader(f)) if start <= i < end]
    return rows

# Rentang data yang diproses (misal dari baris 1 sampai 50)
start_row =0  # Baris pertama (0-based index)
end_row = 32  # Baris terakhir yang ingin diproses

# Deklarasi akun tunggal
email = "tigermanohasa"
password = "@@Eskepal123"

# Baca judul video sesuai rentang yang diinginkan
titles = read_csv_range("data.csv", start_row, end_row)

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.get("https://old.bitchute.com/channel/")
time.sleep(3)

# Login
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(email)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
time.sleep(5)

# Proses upload
for title in titles:
    try:
        modif_kata = title.replace(' ', '_')
        kw = f'[VIRAL] {title}  MMS Video ({random_string(5)})'

        konten = f'''
        29 minutes ago - Access {title} Leaked viral New Updaload FIles 2025

        LINK ⏩⏩ https://viralclupsx.web.app?title={modif_kata}

        {title} viral new
        '''

        video_path = os.path.abspath("video/video.mp4")
        
        driver.get("https://old.bitchute.com/channel/")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-upload.fa-2x").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input[name='videoInput']").send_keys(video_path)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "input[type='title']").send_keys(kw)
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, "button[id='thumbnailButton']").click()
        time.sleep(15)
        driver.find_element(By.CSS_SELECTOR, "textarea[id='description']").send_keys(konten)
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(7)
        print("Berhasil Upload : "+title)

    except:
        print("TERJADI ERROR")
        
driver.quit()
