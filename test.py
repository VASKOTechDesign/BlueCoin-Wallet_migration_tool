def mouse_move(pyautogui, time, waiting_time,possition: tuple) -> None:
    time.sleep(waiting_time)
    pyautogui.moveTo(possition[0], possition[1])

def mouse_move_one_line(pyautogui, time, waiting_time) -> None:
    time.sleep(waiting_time)
    possition = pyautogui.position()
    pyautogui.moveTo(possition[0], possition[1] + 35)

def mouse_clic(pyautogui, time, waiting_time) -> None:
    time.sleep(waiting_time)
    pyautogui.click()

def mouse_scroll(pyautogui, time, waiting_time, line) -> None:
    time.sleep(waiting_time)
    pyautogui.scroll(line)

def press_one_key(pyautogui, time, waiting_time, key) -> None:
    time.sleep(waiting_time)
    pyautogui.press(key)

def press_two_keys(pyautogui, time, waiting_time, key1, key2) -> None:
    time.sleep(waiting_time)
    with pyautogui.hold(key1):
        pyautogui.press([key2])

def write_text(pyautogui, time, waiting_time, text) -> None:
    time.sleep(waiting_time)
    pyautogui.write(text)

import pyautogui
import time
from datetime import datetime
import pandas
pandas.options.mode.chained_assignment = None

# Accout
Account_list = ["AED", "CZK", "CZK - Společný", "EUR", "GBP", "HRK", "HUF", "SEK", "Trezor", "Stravenky", "AirBank - Společný", "AirBank - Spořící", "AirBank - VASKO TechDesign", "KB - Personal - účet", "Airbank - Svatební půjčka", "KB - Hypotéka", "KB - Americká Hypotéka", "KB - Stavební spoření - úvěr 2", "KB - Stavební spoření - úvěr 1", "KB - VASKOTechDesign - PMG", "Benzina - Karta", "Hornbach Karta", "IKEA - Karta", "Stravenková Karta", "Fortuna", "Chance", "Sazka", "SynotTip", "Tipsport", "Allianz - Penzijní pripojištění", "AXA", "Conseq"]
Account_Type_list = ["Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Bank", "Bank", "Bank", "Bank", "Loans", "Loans","Loans", "Loans", "Loans", "Loans", "Bonus", "Bonus", "Bonus", "Bonus", "Virtual", "Virtual", "Virtual", "Virtual", "Virtual", "Investments", "Investments", "Investments"]
Account_Currency_list = ["AED", "CZK", "CZK", "EUR", "GBP", "HRK", "HUF", "SEK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK"]
Account_possition_list = [26, 0, 1, 4, 27, 28, 29, 30, 2, 3, 10, 11, 12, 5, 13, 9, 7, 6, 8, 22, 23, 24, 25, 15, 14, 16, 17, 18, 19, 20, 21, 1]         #! Opravit je to špatně kvůli Americké hypotéce (udělat kompletně od začátku)
Account_possition_TO_list = [27, 1, 2, 5, 28, 29, 30, 31, 3, 4, 11, 12, 13, 6, 14, 10, 8, 7, 9, 23, 24, 25, 26, 16, 15, 17, 18, 19, 20, 21, 22, 1]     #! Opravit je to špatně kvůli Americké hypotéce (udělat kompletně od začátku)
Accounts_dict = {
    "Account": Account_list,
    "Account_Type": Account_Type_list,
    "Account_Currency": Account_Currency_list,
    "Account_Possition": Account_possition_list,
    "Account_possition_TO_list": Account_possition_TO_list}
Accounts_df = pandas.DataFrame(data=Accounts_dict, columns=Accounts_dict.keys())

# Currency
Currency_list = ["CZK", "CZK", "AED", "EUR", "GBP", "HRK", "HUF", "SEK"]
Currency_possition_list = [1, 2, 3, 4, 5, 6, 7, 8]
Currency_dict = {
    "Currency": Currency_list,
    "Currency_Posstion": Currency_possition_list}
Currency_df = pandas.DataFrame(data=Currency_dict, columns=Currency_dict.keys())


Account = "EUR"
Currency = "EUR"
Account_possition = (750, 430)   

Currency_index = Currency_df[Currency_df["Currency"] == Currency].index
Currency_pos = int(Currency_df.iloc[Currency_index]["Currency_Posstion"].values[0])

Account_index = Accounts_df[Accounts_df["Account"] == Account].index
Account_Type = str(Accounts_df.iloc[Account_index]["Account_Type"].values[0])
Account_pos = int(Accounts_df.iloc[Account_index]["Account_Possition"].values[0])
print(Account_Type)
print(Account_pos)
