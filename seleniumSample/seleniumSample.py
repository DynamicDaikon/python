# coding: UTF-8

from curses import KEY_ENTER
from selenium import webdriver
from selenium.webdriver.common.by import By

import csv

# ドライバー、URL登録
# TODO 暫定バージョンチェックしない。一律最新版ダウンロード。
driver = webdriver.Chrome()
driver.get("https://www5.tenseidatanet.co.jp/cb2/office.cgi?")

# 入力要素取得
id = driver.find_element(By.NAME, "_ID")
password = driver.find_element(By.NAME, "_Password")
loginBtn = driver.find_element(By.NAME, "_Submit")

# 入力実行
# TODO パスワード外部ファイル参照させたい。
id.send_keys("上山拓馬")
password.send_keys("tensei035@")

loginBtn.click()

# 予定表の画面に遷移
schedule = driver.find_element(By.LINK_TEXT, "スケジュール")
schedule.click()
# csv ファイル読み込み
csv_file = open(
    "/Users/dynamic_daikon/git/projects/python/seleniumSample/schedule.csv",
    "r",
    encoding="UTF-8",
    errors="",
    newline="",
)
# リスト形式で読み込み
f = csv.reader(
    csv_file,
    delimiter=",",
    doublequote=True,
    lineterminator="\r\n",
    quotechar='"',
    skipinitialspace=True,
)
header = next(f)
for row in f:
    # rowはList
    # row[0]で必要な項目を取得することができる
    # form要素取得
    form = driver.find_element(By.XPATH,
        "/html/body/form/table[2]/tbody/tr[2]/td[2]/a[2]"
    )

    form.click()

    setStrtMonth = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[1]"
    )
    setStrtMonth.send_keys(row[0])

    setStrtDay = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[2]"
    )
    setStrtDay.send_keys(row[1])

    setStrtHour = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[3]"
    )
    setStrtHour.send_keys(row[2])

    setStrtMinute = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[4]"
    )
    setStrtMinute.send_keys(row[3])

    setEndMonth = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[5]"
    )
    setEndMonth.send_keys(row[0])

    setEndDay = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[6]"
    )
    setEndDay.send_keys(row[1])

    setEndHour = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[7]"
    )
    setEndHour.send_keys(row[4])

    setEndMinute = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[1]/td[2]/select[8]"
    )
    setEndMinute.send_keys(row[5])

    setStatus = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[2]/td[2]/select"
    )
    setStatus.send_keys("【□予定】")

    setTask = driver.find_element(By.XPATH,
        "/html/body/form/table/tbody/tr[2]/td[2]/input"
    )
    setTask.send_keys(row[6])
    # setTask.send_keys(KEY_ENTER)

    submit = driver.find_element(By.XPATH, "/html/body/form/input[7]")
    submit.click()
