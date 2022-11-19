"""
Tool:
- je to migrační tool, který využívá selenium k vytváření záznamů v aplikaci Wallet
- po každém vypsání kliknout do levého vrchního rohu po odstanění pop-up formuláře (jako to má Labels)

Transaction type
    --> vybrat mezi Expense, Income, Transfer
Account:
    --> pozor, aby šlo zapsat musejí být všechny accounts viditelné !!!

Amount:
    --> oddělovač může být čárka i tečka

Curency
    --> Expense, Income 
    --> když v cizí měně (tak dát do poznámky info o tom kolik to bylo v původní měně)
    Example: 
        Note = "8 EUR"

Exchange Rate:
    --> u Transferu nejde změnit ve WEb aplikaci

Category:
    --> vybrat správnou podle mapování
        Způsob 1: 
            double click do fieldu --> nastartuje Search, zapsat co chci vyhledat a pak přesunout myš na první dostupnou hodnotu (pozor neumí mezery!!!)
            --> mezery by šlo nahradit spodním pottržítkem
        Způsob 2:
            po 
        
Labels:
    --> prně je potřeba vybrat všechny existující label z Bluecoin a vložit je do listu 
    --> pokud je zdrojové pole Datatrame prázdné tak vynechat,  
        for label in Lables:
            search
                Ano --> napsat a enter
                Ne --> vynechat
    --> kliknout a napsat label 

Date:
    --> Postup
        1) Označit vše a vymazat
        2) vepsat datum format "dd.mm.yyyy" + Enter

Time:
    --> postup
        1) kliknout do pole
        2) scrolovat až nahozu
        3) najít správný čas
        4) kliknout

Payee
    --> zkopírovat 

Note 
    --> zkopírovat

Payment type 
    CASH account = CASH
    BAnkovní = Debit CArd

Payment Status 
    vepsat fixní hodnotu "UnCleared"

Place --> budu doplňovat manuálně
"""

# DF preparatoin
def BlueCoin_create_labels(text):
    Label_list = ["2017 - Budapešť", "2017 - Španělsko", "2018 - Amsterdam", "2018 - Francie", "2018 - Praha", "2018 - Slovinsko", "2019 - Beskydy", "2019 - Harrachov", "2019 - Itálie", "2019 - Kapverdy", "2019 - Mušov", "2019 - Slovensko", "2020 - Kanárské ost.", "2020 - Lukavice", "2020 - Velikonoce", "2020 - Wichterle", "2021 - Kréta", "2021 - Kutná Hora", "2021 - Pluskoveček", "2021 - Slovinsko", "2021 - Šumava", "2022 - Chorvatsko", "2022 - Rokytnice", "Byt - Chorvatsko", "Byt - Provazníkova", "Byt - Těsná", "Dovolena: All", "KM-BBL: 2019-08", "KM-BBL: 2022-08", "KM-BEU: 2018-06", "KM-BHR: 2018-01", "KM-BHR: 2018-06", "KM-BHR: 2018-08A", "KM-BHR: 2018-08B", "KM-BHR: 2018-10A", "KM-BHR: 2018-10B", "KM-BPL: 2019-10", "KM-BPL: 2019-12", "KM-BPL: 2020-07", "KM-BPL: 2020-08", "KM-BPL: 2021-11", "KM-BR: 2019-01", "KM-BRO: 2018-01", "KM-BSL: 2017-10", "KM-BSL: 2019-03", "KM-BSL: 2019-05", "KM-BSL: 2019-09", "KM-BSL: 2019-10", "KM-BSL: 2019-11", "KM-BSL: 2020-01", "KM-BSL: 2020-02", "KM-Dubai: 2019-03", "KM-Služebka-All", "Renault Laguna", "Sebastien Vaško", "Schampy", "Svatba", "Vánoce", "VASKO TechDesign", "VASKO: Energy Sol.", "VASKO: IoT - PUR", "VASKO: SportBet", "Vklad - Andrea", "Vklad - Honza", "Výlety"]
    row_labe = []

    if text == "nan":
        return "[]"
    else:
        for label in Label_list:
            if label in text:
                row_labe.append(label)
        return row_labe

def BlueCoin_delete_df_text(text):
    try:
        text = str(text)
        text = text.replace("[", "")
        text = text.replace("{", "")
        text = text.replace("}", "")
        text = text.replace("]", "")
        text = text.replace("nan", "")
        text = text.replace("NaN", "")
    except:
        pass
    return text

def Wallet_create_number(text):
    return text.replace(",", ".")

def Waller_get_date(text):
    text = text.split(" ")
    return text[0]

# General Functions mouse and keyboard
def mouse_move(pyautogui, time, possition: tuple) -> None:
    time.sleep(0.25)
    pyautogui.moveTo(possition[0], possition[1])

def mouse_move_one_line(pyautogui, time) -> None:
    time.sleep(0.25)
    possition = pyautogui.position()
    pyautogui.moveTo(possition[0], possition[1] + 35)

def mouse_clic(pyautogui, time) -> None:
    time.sleep(0.25)
    pyautogui.click()

def mouse_scroll(pyautogui, time, line) -> None:
    time.sleep(0.25)
    pyautogui.scroll(line)

def press_one_key(pyautogui, time, key) -> None:
    time.sleep(0.25)
    pyautogui.press(key)

def press_two_keys(pyautogui, time, key1, key2) -> None:
    time.sleep(0.25)
    with pyautogui.hold(key1):
        pyautogui.press([key2])

def write_text(pyautogui, time, text) -> None:
    time.sleep(0.25)
    pyautogui.write(text)

# Each Fields fill in WEB app
def Date_Month_Difference(Transaction_date, datetime) -> int:
    Transaction_date = datetime.strptime(Transaction_date,"%d.%m.%Y")
    Today = datetime.now()
    Current_Month = Today.month
    Current_Year = Today.year

    Transaction_Day = Transaction_date.day
    Transaction_Month = Transaction_date.month
    Transaction_Year = Transaction_date.year
    Transaction_date = datetime(Transaction_Year, Transaction_Month, Transaction_Day) 

    difference = Current_Month - Transaction_Month + 12*(Current_Year - Transaction_Year)
    return difference

def Callendar_Colum_index(Transaction_date, datetime) -> int:
    # to find correct weekday to which the date belongs to Callendar_matrix_possition --> correctly grab possition
    Transaction_date = datetime.strptime(Transaction_date, "%d.%m.%Y")
    week_day = Transaction_date.weekday() 
    #! Because calendar starts on Sunday
    if week_day == 6:
        colum_index = 0
    else:
        colum_index = week_day + 1
    return colum_index

def Callendar_Line_index(Transaction_date, datetime) -> int:
    # to find correct week to which the date belongs to Callendar_matrix_possition --> correctly grab possition
    Transaction_date = datetime.strptime(Transaction_date,"%d.%m.%Y")
    Transaction_date_day = Transaction_date.day
    Transaction_date_month = Transaction_date.month
    Transaction_date_year = Transaction_date.year

    First_day_of_Month_week = f"01.{Transaction_date_month}.{Transaction_date_year}"
    First_day_Colum_index = Callendar_Colum_index(First_day_of_Month_week, datetime)
    Calculated_day = 6 - First_day_Colum_index + 1
    Line_index = 0
    
    while True:
        if (Calculated_day + 7) <= Transaction_date_day:
            Line_index += 1 
            Calculated_day += 7
        elif (Transaction_date_day - Calculated_day) > 0:
            Line_index += 1 
            Calculated_day += 7
        else:
            break
            
    return Line_index

def Calendar_direct_write(pyautogui, Transaction_date, datetime, possition, time) -> None:
    mouse_move(pyautogui, time, possition)
    mouse_clic(pyautogui, time)
    press_two_keys(pyautogui, time, "ctrl", "a")
    press_one_key(pyautogui, time, "delete")

    # Define correct format of Date
    Transaction_date = datetime.strptime(Transaction_date,"%d.%m.%Y")
    Months = ["empty_index","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    Transaction_Day = Transaction_date.day
    Transaction_Month = Transaction_date.month
    Transaction_Month = Months[Transaction_Month]
    Transaction_Year = Transaction_date.year
    date_formated = f"{Transaction_Month} {Transaction_Day}, {Transaction_Year}"
    write_text(pyautogui, time, date_formated)
    press_one_key(pyautogui, time, "tab")
       
def Time_Scroll_up(pyautogui, time, first_line) -> None:
    mouse_move(pyautogui, time, first_line)
    pyautogui.scroll(clicks=30000)

def Time_Set_correct(pyautogui, Transaction_Time, time, Time_First_line, Time_possition) -> None:
    mouse_move(pyautogui, time, Time_possition)
    mouse_clic(pyautogui, time)
    Time_Scroll_up(pyautogui, time, Time_First_line)
    One_line_height = 83
    Transaction_Time_split = Transaction_Time.split(":")
    Transaction_Hour = int(Transaction_Time_split[0])
    Transaction_Minute = int(Transaction_Time_split[1])

    No_scrolls = (Transaction_Hour * 4) + (Transaction_Minute // 15)
    Scroll_click = No_scrolls * One_line_height * (-1)

    # Scroll down to correct time
    if No_scrolls >= 90:
        mouse_scroll(pyautogui, -7470)
        No_scrolls = No_scrolls - 89
        possition_X = Time_First_line[0]
        possition_Y = Time_First_line[1]
        One_line_height = 30
        possition_Y +=  No_scrolls * One_line_height
        possition = (possition_X, possition_Y)
        mouse_move(pyautogui, time, possition)
        time.sleep(0.25)
        mouse_clic(pyautogui, time)
    else:
        mouse_scroll(pyautogui, Scroll_click)
        time.sleep(0.25)
        mouse_clic(pyautogui, time)
    press_one_key(pyautogui, time, "tab")
        
import pyautogui
import time
from datetime import datetime
import pandas

# --------------------------------- Defaults ---------------------------------#
# X/Y coordinates on notebook screen - Absolute
New_record_button_possition = (1460,70)     # New record
Expense_button_possition = (660, 350)       # Expense button
Income_button_possition = (780, 350)        # Income button
Transfer_button_possition = (900, 350)      # Transfer Button
Account_possition = (750, 430)              # Acount
Amount_possition = (760, 500)               # Amount
Currency_possition = (850, 500)             # Currency
Trasnfer_From_Account = (600, 440)          # Transfer From Account
Trasnfer_To_Account = (860, 440)            # Transfer To Account
Transfer_From_Amount = (600, 510)           # Transfer From Amount
Transfer_To_Amount = (900, 510)             # Transfer To Amount
Transfer_From_Currency = (700, 510)         # Transfer From Currency
Transfer_To_Currency = (980, 510)           # Transfer To Currency
Category_Search_possition = (600, 610)      # Category
Category_Choose_possition = (750, 610)      # Category
Labels_Search_possition = (900, 610)        # Labels
Date_possition = (630, 680)                 # Date

# Caledar starts at Sunday - so [0][0] = (547,795) --> Sunday
Callendar_date = (640, 690)
Callendar_matrix_possition = [
    [(547,795),(580,795),(613,795),(646,795),(679,795),(712,795),(745,795)],
    [(547,828),(580,828),(613,828),(646,828),(679,828),(712,828),(745,828)],
    [(547,861),(580,861),(613,861),(646,861),(679,861),(712,861),(745,861)],
    [(547,894),(580,894),(613,894),(646,894),(679,894),(712,894),(745,894)],
    [(547,927),(580,927),(613,927),(646,927),(679,927),(712,927),(745,927)],
    [(547,960),(580,960),(613,960),(646,960),(679,960),(712,960),(745,960)]]
Callendar_previous_month = (550, 733)
Callendar_next_month = (745, 733)

# Time
Time_possition = (900, 680)                 # Time
Time_First_line = (900, 770)                # Time - firs line with any time

Payee_possition = (1200, 385)               # Payee
Note_possition = (1200, 480)                # Note
Payment_type_possition = (1200, 570)        # Payment type 
Payment_Status_possition = (1200, 650)      # Payment Status 
Add_record = (770, 750)                     # Add record
Add_record_new = (770, 795)                 # Add record and create new

# Payment Type
Payment_Type_list = ["Cash", "Debit card", "Credit card", "Transfer", "Voucher", "Mobile payment", "Web payment"]
Payment_Type_pos_list = []
Payment_Type_len = len(Payment_Type_list)
for pos in range(Payment_Type_len):
    Payment_Type_pos_list.append(pos)
Payment_Type_dict = {
    "Payment_Type": Payment_Type_list,
    "Payment_Type_Possition":Payment_Type_pos_list}
Payment_Type_df = pandas.DataFrame(data=Payment_Type_dict, columns=Payment_Type_dict.keys())

# Payment Status
Payment_Status_list = ["Uncleared", "Cleared", "Reconciled"]
Payment_Status_possition_list = [1, 0, 2] # Pozor default je "Cleared" --> "Uncleared" --> "REconciled"
Payment_Status_dict = {
    "Payment_Status": Payment_Status_list,
    "Payment_Status_Possition": Payment_Status_possition_list}
Payment_Status_df = pandas.DataFrame(data=Payment_Status_dict, columns=Payment_Status_dict.keys())

# Accout
Account_list = ["AED", "CZK", "CZK - Společný", "EUR", "GBP", "HRK", "HUF", "SEK", "Trezor", "Stravenky", "AirBank - Společný", "AirBank - Spořící", "AirBank - VASKO TechDesign", "KB - Personal - účet", "Airbank - Svatební půjčka", "KB - Hypotéka", "KB - Stavebíi spoření - úvěr 2", "KB - Stavební spoření - úvěr 1", "KB - VASKOTechDesign - PMG", "Benzina - Karta", "Hornbach Karta", "IKEA - Karta", "Stravenková Karta", "Fortuna", "Chance", "Sazka", "SynotTip", "Tipsport", "Allianz - Penzijní pripojištění", "AXA", "Conseq"]
Account_Type_list = ["Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Bank", "Bank", "Bank", "Bank", "Loans", "Loans", "Loans", "Loans", "Loans", "Bonus", "Bonus", "Bonus", "Bonus", "Virtual", "Virtual", "Virtual", "Virtual", "Virtual", "Investments", "Investments", "Investments"]
Account_Currency_list = ["AED", "CZK", "CZK", "EUR", "GBP", "HRK", "HUF", "SEK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK"]
Account_possition_list = [26, 0, 1, 4, 27, 28, 29, 30, 2, 3, 10, 11, 12, 5, 13, 9, 7, 6, 8, 22, 23, 24, 25, 15, 14, 16, 17, 18, 19, 20, 21]
Account_possition_TO_list = [27, 1, 2, 5, 28, 29, 30, 31, 3, 4, 11, 12, 13, 6, 14, 10, 8, 7, 9, 23, 24, 25, 26, 16, 15, 17, 18, 19, 20, 21, 22]
Accounts_dict = {
    "Account": Account_list,
    "Account_Type": Account_Type_list,
    "Account_Currency": Account_Currency_list,
    "Account_Possition": Account_possition_list,
    "Account_possition_TO_list": Account_possition_TO_list}
Accounts_df = pandas.DataFrame(data=Accounts_dict, columns=Accounts_dict.keys())

# Categorry Mapping
Category_df = pandas.read_csv(filepath_or_buffer="Category_Mapping.csv", sep=";")
Category_df["Wallet_Main"] = Category_df["Wallet_Main"].apply(BlueCoin_delete_df_text)
Category_df["Wallet_Sub-Category"] = Category_df["Wallet_Sub-Category"].apply(BlueCoin_delete_df_text)
Category_df["Wallet_Sub2-Category"] = Category_df["Wallet_Sub2-Category"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Type"] = Category_df["BlueCoin_Type"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Main"] = Category_df["BlueCoin_Main"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Sub-Category"] = Category_df["BlueCoin_Sub-Category"].apply(BlueCoin_delete_df_text)
Category_df["Note"] = Category_df["Note"].apply(BlueCoin_delete_df_text)

# --------------------------------- Main ---------------------------------#
# Read csv.
BlueCoins_df = pandas.read_csv(filepath_or_buffer="./Data/2022_11_12-transactions_list.csv", sep=";")
BlueCoins_df["Notes"] = BlueCoins_df["Notes"].apply(BlueCoin_delete_df_text)
BlueCoins_df["Labels"] = BlueCoins_df["Labels"].apply(BlueCoin_delete_df_text)
BlueCoins_df["Title"] = BlueCoins_df["Title"].apply(BlueCoin_delete_df_text)

# ----------------- BlueCoin-----------------#
# ----- Delete -----#
# Delete starting balance
New_Balance_row = BlueCoins_df[BlueCoins_df["Type"] == "New Account"].index
BlueCoins_df = BlueCoins_df.drop(New_Balance_row, axis=0)

# Create DFs
Transfers_mask = BlueCoins_df["Type"] == "Transfer"
Transfers_df = BlueCoins_df[Transfers_mask]
Transfers_df["Labels"] = Transfers_df["Labels"].apply(str)
del Transfers_mask

Income_Expense_mask = BlueCoins_df["Type"] != "Transfer"
Income_Expense_df = BlueCoins_df[Income_Expense_mask]
Income_Expense_df["Labels"] = Income_Expense_df["Labels"].apply(str)
del Income_Expense_mask

Pujcky_mask_1 = BlueCoins_df["Category"] == "Pujcky - pujceni"
Pujcky_mask_2 = BlueCoins_df["Category"] == "Pujcky - vraceni"
Pujcky_df = BlueCoins_df[Pujcky_mask_1 | Pujcky_mask_2]
Pujcky_df["Labels"] = Pujcky_df["Labels"].apply(str)
del Pujcky_mask_1, Pujcky_mask_2

# Labels assignment to transaction --> Column for each label ("Pujcky" - není součástí - bude jako nová entita)
Income_Expense_df["Labels"] = Income_Expense_df["Labels"].apply(BlueCoin_create_labels)
Transfers_df["Labels"] = Transfers_df["Labels"].apply(BlueCoin_create_labels)
Pujcky_df["Labels"] = Pujcky_df["Labels"].apply(BlueCoin_create_labels)

# ----------------- Wallet -----------------#
# DF - Income / Expense
Wallet_Income_Expense_df = Income_Expense_df

Wallet_Income_Expense_df["Amount"] = Wallet_Income_Expense_df["Amount"].apply(Wallet_create_number)
Wallet_Income_Expense_df["Amount"] = Wallet_Income_Expense_df["Amount"].apply(float)
Wallet_Income_Expense_df["Amount"] = Wallet_Income_Expense_df["Amount"].apply(abs)

Wallet_Income_Expense_df["Exchange Rate"] = Wallet_Income_Expense_df["Exchange Rate"].apply(Wallet_create_number)
Wallet_Income_Expense_df["Exchange Rate"] = Wallet_Income_Expense_df["Exchange Rate"].apply(float)

Wallet_Income_Expense_df["Amount_LCY"] = round(Wallet_Income_Expense_df["Amount"] / Wallet_Income_Expense_df["Exchange Rate"], 2)

# Category - mapping
for row in Wallet_Income_Expense_df.iterrows():
    row_df = pandas.Series(data=row[1])
    
    BlueCoin_Type = row_df["Type"]
    BlueCoin_Cateogry_Main = row_df["Category Group Name"]
    BlueCoin_Cateogry_Sub = row_df["Category"]

    Mask1 = Category_df["BlueCoin_Type"] == BlueCoin_Type
    Mask2 = Category_df["BlueCoin_Main"] == BlueCoin_Cateogry_Main
    Mask3 = Category_df["BlueCoin_Sub-Category"] == BlueCoin_Cateogry_Sub

    Category_mapping_Series = Category_df[Mask1 & Mask2 & Mask3]
    print(Category_mapping_Series)

    Wallet_Income_Expense_df.at[row[0],"Category_1"] = Category_mapping_Series.iloc[0]["Wallet_Main"]
    Wallet_Income_Expense_df.at[row[0],"Category_2"] = Category_mapping_Series.iloc[0]["Wallet_Sub-Category"]
    Wallet_Income_Expense_df.at[row[0],"Category_3"] = Category_mapping_Series.iloc[0]["Wallet_Sub2-Category"]

Wallet_Income_Expense_df["Date"] = Wallet_Income_Expense_df["Date"].apply(Waller_get_date)
Wallet_Income_Expense_df["Time"] = Wallet_Income_Expense_df["Set Time"] 

Wallet_Income_Expense_df["Payee"] = Wallet_Income_Expense_df["Title"] 
Wallet_Income_Expense_df["Original_Value"] = ""
Wallet_Income_Expense_df["Original_Value"].loc[Wallet_Income_Expense_df["Currency"] != "CZK"] = Wallet_Income_Expense_df["Amount"]

# Payment Type - mapping
Wallet_Income_Expense_df["Payment type"] = 

Wallet_Income_Expense_df["Payment status"] = Wallet_Income_Expense_df["Status"] 
Wallet_Income_Expense_df["Place"] = ""
Wallet_Income_Expense_df.drop(labels=["Set Time", "Title", "Category Group Name", "Category", "Status"], inplace=True)
print(Wallet_Income_Expense_df)
# DF - Transferes



# Web App --> issues

print("Finished")