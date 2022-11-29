# DF preparatoin
def Replace_signs_in_file(From_File_Name, To_File_Name) -> None:
    with open(file=f"./Data/{From_File_Name}.csv", mode="tr", encoding="utf-8-sig") as f:
        lines = f.readlines()
    f.close()
    with open(file=f"./Data/{To_File_Name}.csv", mode="w", encoding="utf-8-sig") as f_result:
        for line in lines:
            line = line.rstrip("\n")
            line = line.replace('","',";")
            line = line[1:]
            line = line[:-1]
            line = line + "\n"
            f_result.write(line)
    f_result.close()

def BlueCoin_create_labels(text):
    Label_list = ["2017 - Budapešť", "2017 - Španělsko", "2018 - Amsterdam", "2018 - Francie", "2018 - Praha", "2018 - Slovinsko", "2019 - Beskydy", "2019 - Harrachov", "2019 - Itálie", "2019 - Kapverdy", "2019 - Mušov", "2019 - Slovensko", "2020 - Kanárské ost.", "2020 - Lukavice", "2020 - Velikonoce", "2020 - Wichterle", "2021 - Kréta", "2021 - Kutná Hora", "2021 - Pluskoveček", "2021 - Slovinsko", "2021 - Šumava", "2022 - Chorvatsko", "2022 - Rokytnice", "Byt - Rogoznica", "Byt - Provazníkova", "Byt - Těsná", "Dovolena: All", "KM-BBL: 2019-08", "KM-BBL: 2022-08", "KM-BBL: 2022-11","KM-BEU: 2018-06", "KM-BHR: 2018-01", "KM-BHR: 2018-06", "KM-BHR: 2018-08A", "KM-BHR: 2018-08B", "KM-BHR: 2018-10A", "KM-BHR: 2018-10B", "KM-BPL: 2019-10", "KM-BPL: 2019-12", "KM-BPL: 2020-07", "KM-BPL: 2020-08", "KM-BPL: 2021-11", "KM-BR: 2019-01", "KM-BRO: 2018-01", "KM-BSL: 2017-10", "KM-BSL: 2019-03", "KM-BSL: 2019-05", "KM-BSL: 2019-09", "KM-BSL: 2019-10", "KM-BSL: 2019-11", "KM-BSL: 2020-01", "KM-BSL: 2020-02", "KM-Dubai: 2019-03", "KM-Služebka-All", "Renault Laguna", "Sebastien Vaško", "Schampy", "Svatba", "Vánoce", "VASKO TechDesign", "VASKO: Energy Sol.", "VASKO: IoT - PUR", "VASKO: SportBet", "Vklad - Andrea", "Vklad - Honza", "Výlety"]
    row_label = []
    if text == "nan":
        return "[]"
    else:
        for label in Label_list:
            if label in text:
                row_label.append(label)
        return row_label

def BlueCoin_delete_df_text(text):
    try:
        text = str(text)
        text = text.replace("[", "")
        text = text.replace("{", "")
        text = text.replace("}", "")
        text = text.replace("]", "")
        text = text.replace("NaN", "")
        text_len = len(text)
        if text_len == 3:
            text = text.replace("nan", "")
        else:
            pass
    except:
        pass
    return text

def Wallet_create_number(text):
    try:
        return text.replace(",", ".")
    except:
        return text

def Wallet_get_date(text):
    text = text.split(" ")
    return text[0]

def Wallet_Payment_Status(text) -> str:
    if text == "None":
        return "Uncleared"
    elif text == "Void":
        return "Uncleared"
    else:
        return text

def Wallet_Labels_List(text) -> list:
    text = str(text)
    text = text.replace(", ", ",")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace('"', "")
    text = text.replace("'", "")
    return text.split(sep=",")

# General Functions mouse and keyboard
def mouse_move(pyautogui, time, waiting_time, possition: tuple) -> None:
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

def Replace_diacritic(text):
    try:
        text = text.replace("á", "a")
        text = text.replace("é", "e")
        text = text.replace("ě", "e")
        text = text.replace("í", "i")
        text = text.replace("ó", "o")
        text = text.replace("ú", "u")
        text = text.replace("ů", "u")
        text = text.replace("ý", "y")
        text = text.replace("č", "c")
        text = text.replace("ď", "d")
        text = text.replace("ň", "n")
        text = text.replace("ř", "r")
        text = text.replace("š", "s")
        text = text.replace("ť", "t")
        text = text.replace("ž", "z")
        text = text.replace("Á", "A")
        text = text.replace("É", "E")
        text = text.replace("Ě", "E")
        text = text.replace("Í", "I")
        text = text.replace("Ó", "O")
        text = text.replace("Ú", "U")
        text = text.replace("Ý", "Y")
        text = text.replace("Č", "C")
        text = text.replace("Ď", "D")
        text = text.replace("Ň", "N")
        text = text.replace("Ř", "R")
        text = text.replace("Š", "S")
        text = text.replace("Ť", "T")
        text = text.replace("Ž", "Z")
    except:
        pass
    return  text

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

def Calendar_direct_write(pyautogui, Transaction_date, datetime, time) -> None:
    press_two_keys(pyautogui, time, 0.1, "ctrl", "a")
    press_one_key(pyautogui, time, 0.1, "delete")
    # Define correct format of Date
    Transaction_date = datetime.strptime(Transaction_date,"%Y-%m-%d")
    Months = ["empty_index","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    Transaction_Day = Transaction_date.day
    Transaction_Month = Transaction_date.month
    Transaction_Month = Months[Transaction_Month]
    Transaction_Year = Transaction_date.year
    date_formated = f"{Transaction_Month} {Transaction_Day}, {Transaction_Year}"
    write_text(pyautogui, time, 0.1, date_formated)
       
def Time_Scroll_up(pyautogui, time, first_line) -> None:
    mouse_move(pyautogui, time, 0.25, first_line)
    mouse_scroll(pyautogui, time, 0.5, 30000)

def Time_Set_correct(pyautogui, Transaction_Time, time, waiting_time,Time_First_line) -> None:
    Time_Scroll_up(pyautogui, time, Time_First_line)
    One_line_height = 83
    Transaction_Time_split = Transaction_Time.split(":")
    Transaction_Hour = int(Transaction_Time_split[0])
    Transaction_Minute = int(Transaction_Time_split[1])

    No_scrolls = (Transaction_Hour * 4) + (Transaction_Minute // 15)
    Scroll_click = No_scrolls * One_line_height * (-1)

    # Scroll down to correct time
    if No_scrolls >= 90:
        mouse_scroll(pyautogui, time, 0.5, -7470)
        No_scrolls = No_scrolls - 89
        possition_X = Time_First_line[0]
        possition_Y = Time_First_line[1]
        One_line_height = 30
        possition_Y +=  No_scrolls * One_line_height
        possition = (possition_X, possition_Y)
        mouse_move(pyautogui, time, 0.25, possition)
        time.sleep(waiting_time)
        mouse_clic(pyautogui, time, 0.1)
    else:
        mouse_scroll(pyautogui, time, 0.5, Scroll_click)
        time.sleep(waiting_time)
        mouse_clic(pyautogui, time, 0.1)
        
import pyautogui
import time
from datetime import datetime
import pandas
import pyperclip
pandas.options.mode.chained_assignment = None

# --------------------------------- Defaults ---------------------------------#
# Currency and amount Method
Expense_Income_Method = "CZK" # Values: "CZK", "Original"
Transfer_Method = "CZK" # Values: "CZK", "Original"

# X/Y coordinates on notebook screen - Absolute
New_record_button_possition = (1460,70)     # New record
Expense_button_possition = (660, 350)       # Expense button
Income_button_possition = (780, 350)        # Income button
Transfer_button_possition = (900, 350)      # Transfer Button
Account_possition = (750, 430)              # Acount
Amount_possition = (760, 500)               # Amount
Currency_possition = (850, 500)             # Currency
Currency_First_line = (850, 540)            # Currency
Currency_line_height = 35                   # Currency line height
Trasnfer_From_Account = (600, 440)          # Transfer From Account
Trasnfer_To_Account = (860, 440)            # Transfer To Account
Transfer_From_Amount = (600, 510)           # Transfer From Amount
Transfer_To_Amount = (900, 510)             # Transfer To Amount
Transfer_From_Currency = (700, 510)         # Transfer From Currency
Transfer_To_Currency = (980, 510)           # Transfer To Currency
Category_Search_possition = (600, 610)      # Category
Category_First_line = (600, 645)            # Category
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
Cancel_cross = (1400, 270)                  # Add record and create new

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
Account_list = ["AED", "CZK", "CZK - Společný", "EUR", "GBP", "HRK", "HUF", "SEK", "Trezor", "Stravenky", "AirBank - Společný", "AirBank - Spořící", "AirBank - VASKO TechDesign", "KB - Personal - účet", "Airbank - Svatební půjčka", "KB - Hypotéka", "KB - Americká Hypotéka", "KB - Stavební spoření - úvěr 1", "KB - Stavební spoření - úvěr 2", "KB - VASKOTechDesign - PMG", "Benzina - Karta", "Hornbach Karta", "IKEA - Karta", "Stravenková Karta", "Chance", "Fortuna", "Sazka", "SynotTip", "Tipsport", "Allianz - Penzijní pripojištění", "AXA", "Conseq"]
Account_Type_list = ["Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Cash", "Bank", "Bank", "Bank", "Bank", "Loans", "Loans", "Loans", "Loans", "Loans", "Loans", "Bonus", "Bonus", "Bonus", "Bonus", "Virtual", "Virtual", "Virtual", "Virtual", "Virtual", "Investments", "Investments", "Investments"]
Account_Currency_list = ["AED", "CZK", "CZK", "EUR", "GBP", "HRK", "HUF", "SEK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK", "CZK"]
Account_possition_list = [27, 0, 1, 4, 28, 29, 30, 31, 2, 2, 11, 12, 13, 5, 14, 9, 10, 6, 7, 8, 23, 24, 25, 26, 15, 16, 17, 18, 19, 20, 21, 22]
Account_possition_FROM_list = [27, 0, 1, 4, 28, 29, 30, 31, 2, 2, 11, 12, 13, 5, 14, 9, 10, 6, 7, 8, 23, 24, 25, 26, 15, 16, 17, 18, 19, 20, 21, 22]
Account_possition_TO_list = [28, 1, 2, 5, 29, 30, 31, 32, 3, 3, 12, 13, 14, 6, 15, 10, 11, 7, 8, 9, 24, 25, 26, 27, 16, 17, 18, 19, 20, 21, 22, 23]
Accounts_dict = {
    "Account": Account_list,
    "Account_Type": Account_Type_list,
    "Account_Currency": Account_Currency_list,
    "Account_Possition": Account_possition_list,
    "Account_possition_From_list": Account_possition_FROM_list,
    "Account_possition_TO_list": Account_possition_TO_list}
Accounts_df = pandas.DataFrame(data=Accounts_dict, columns=Accounts_dict.keys())

# Currency
Currency_list = ["CZK", "AED", "EUR", "GBP", "HRK", "HUF", "SEK", "USD", "CZK"]
Currency_possition_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
Currency_dict = {
    "Currency": Currency_list,
    "Currency_Posstion": Currency_possition_list}
Currency_df = pandas.DataFrame(data=Currency_dict, columns=Currency_dict.keys())

# Categorry Mapping
Category_df = pandas.read_csv(filepath_or_buffer="Category_Mapping.csv", sep=";")
Category_df["Wallet_Main"] = Category_df["Wallet_Main"].apply(BlueCoin_delete_df_text)
Category_df["Wallet_Sub_Category"] = Category_df["Wallet_Sub_Category"].apply(BlueCoin_delete_df_text)
Category_df["Wallet_Sub2_Category"] = Category_df["Wallet_Sub2_Category"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Type"] = Category_df["BlueCoin_Type"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Main"] = Category_df["BlueCoin_Main"].apply(BlueCoin_delete_df_text)
Category_df["BlueCoin_Sub_Category"] = Category_df["BlueCoin_Sub_Category"].apply(BlueCoin_delete_df_text)
Category_df["Note"] = Category_df["Note"].apply(BlueCoin_delete_df_text)

# --------------------------------- Main ---------------------------------#
Year_to_Process = 2016
From_File_Name = f"{Year_to_Process}_transactions_list"
From_File_Name = f"test"
To_File_Name = f"{Year_to_Process}transactions_list_process"
To_File_Name = "test_test"
Replace_signs_in_file(From_File_Name, To_File_Name)
BlueCoins_df = pandas.read_csv(filepath_or_buffer=f"./Data/{To_File_Name}.csv", sep=";", header=0)
BlueCoins_df["Notes"] = BlueCoins_df["Notes"].apply(BlueCoin_delete_df_text)
BlueCoins_df["Labels"] = BlueCoins_df["Labels"].apply(BlueCoin_delete_df_text)
BlueCoins_df["Title"] = BlueCoins_df["Title"].apply(BlueCoin_delete_df_text)

# ----------------- BlueCoin-----------------#
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
Pujcky_df.to_csv(path_or_buf=f"{Year_to_Process}_Wallet_Pujcky_df.csv", sep=";", index=False)

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
Wallet_Income_Expense_df["Category_1"] = ""
Wallet_Income_Expense_df["Category_2"] = ""
Wallet_Income_Expense_df["Category_3"] = ""
for row in Wallet_Income_Expense_df.iterrows():
    row_df = pandas.Series(data=row[1])

    Mask1 = Category_df["BlueCoin_Type"] == row_df["Type"]
    Mask2 = Category_df["BlueCoin_Main"] == row_df["Category Group Name"]
    Mask3 = Category_df["BlueCoin_Sub_Category"] == row_df["Category"]

    Category_mapping_Series = Category_df[Mask1 & Mask2 & Mask3]

    Wallet_Income_Expense_df.at[row[0],"Category_1"] = Category_mapping_Series.iloc[0]["Wallet_Main"]
    Wallet_Income_Expense_df.at[row[0],"Category_2"] = Category_mapping_Series.iloc[0]["Wallet_Sub_Category"]
    Wallet_Income_Expense_df.at[row[0],"Category_3"] = Category_mapping_Series.iloc[0]["Wallet_Sub2_Category"]

Wallet_Income_Expense_df["Date"] = Wallet_Income_Expense_df["Date"].apply(Wallet_get_date)
Wallet_Income_Expense_df["Time"] = Wallet_Income_Expense_df["Set Time"] 

Wallet_Income_Expense_df["Payee"] = Wallet_Income_Expense_df["Title"] 

# Payment Type - mapping
Wallet_Income_Expense_df["Payment_type"] = ""
for row in Wallet_Income_Expense_df.iterrows():
    row_df = pandas.Series(data=row[1])

    Mask1 = Accounts_df["Account"] == str(row_df["Account"])
    Account_mapping_Series = Accounts_df[Mask1]

    if row_df["Type"] == "Expense":
        if Account_mapping_Series.iloc[0]["Account_Type"] == "Cash":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Cash"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Bank":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Debit card"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Loans":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Transfer"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Virtual":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Debit card"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Bonus":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Debit card"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Investments":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Transfer"
        else:
            pass
    elif row_df["Type"] == "Income":
        if Account_mapping_Series.iloc[0]["Account_Type"] == "Cash":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Cash"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Bank":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Web payment"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Loans":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Transfer"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Virtual":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Transfer"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Bonus":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Web payment"
        elif  Account_mapping_Series.iloc[0]["Account_Type"] == "Investments":
            Wallet_Income_Expense_df.at[row[0],"Payment_type"] = "Transfer"
        else:
            pass
    else:
        pass

Wallet_Income_Expense_df["Payment_Status"] = Wallet_Income_Expense_df["Status"].apply(Wallet_Payment_Status)
Wallet_Income_Expense_df["Place"] = ""
Wallet_Income_Expense_df.drop(labels=["Set Time", "Title", "Category Group Name", "Category", "Status"], inplace=True, axis=1)
Wallet_Income_Expense_df.to_csv(path_or_buf=f"{Year_to_Process}_Wallet_Income_Expense_df.csv", sep=";", index=False, columns=["Type","Date","Time","Account","Amount","Amount_LCY","Currency","Category_1","Category_2","Category_3","Payee","Payment_type","Payment_Status","Labels","Notes"])

# DF - Transferes
Wallet_Transfers_df = Transfers_df 

Wallet_Transfers_df["Amount"] = Wallet_Transfers_df["Amount"].apply(Wallet_create_number)
Wallet_Transfers_df["Amount"] = Wallet_Transfers_df["Amount"].apply(float)

Wallet_Transfers_df["Exchange Rate"] = Wallet_Transfers_df["Exchange Rate"].apply(Wallet_create_number)
Wallet_Transfers_df["Exchange Rate"] = Wallet_Transfers_df["Exchange Rate"].apply(float)

Wallet_Transfers_df["From_Account"] = ""
Wallet_Transfers_df["From_Amount"] = ""
Wallet_Transfers_df["From_Amount_LCY"] = ""
Wallet_Transfers_df["From_Currency"] = ""
Wallet_Transfers_df["From_Exchange_Rate"] = ""
Wallet_Transfers_df["To_Account"] = ""
Wallet_Transfers_df["To_Amount"] = ""
Wallet_Transfers_df["To_Amount_LCY"] = ""
Wallet_Transfers_df["To_Currency"] = ""
Wallet_Transfers_df["To_Exchange_Rate"] = ""

for row in Wallet_Transfers_df.iterrows():
    row_df = pandas.Series(data=row[1])

    if row_df["Amount"] < 0:
        Wallet_Transfers_df.at[row[0],"From_Account"] = row_df["Account"]
        Wallet_Transfers_df.at[row[0],"From_Amount"] = row_df["Amount"]
        Wallet_Transfers_df.at[row[0],"From_Amount_LCY"] = round(row_df["Amount"] / row_df["Exchange Rate"], 2)
        Wallet_Transfers_df.at[row[0],"From_Currency"] = row_df["Currency"]
        Wallet_Transfers_df.at[row[0],"From_Exchange_Rate"] = row_df["Exchange Rate"]
    elif row_df["Amount"] > 0:
        Wallet_Transfers_df.at[row[0]-1,"To_Account"] = row_df["Account"]
        Wallet_Transfers_df.at[row[0]-1,"To_Amount"] = row_df["Amount"]
        Wallet_Transfers_df.at[row[0]-1,"To_Amount_LCY"] = round(row_df["Amount"] / row_df["Exchange Rate"], 2)
        Wallet_Transfers_df.at[row[0]-1,"To_Currency"] = row_df["Currency"]
        Wallet_Transfers_df.at[row[0]-1,"To_Exchange_Rate"] = row_df["Exchange Rate"]
    else:
        print("Issue")

Wallet_Transfers_df2 = Wallet_Transfers_df[Wallet_Transfers_df['From_Account'] != ""].reset_index()
Wallet_Transfers_df2.drop(labels=["index"], inplace=True, axis=1)
del Wallet_Transfers_df
Wallet_Transfers_df = Wallet_Transfers_df2
del Wallet_Transfers_df2

Wallet_Transfers_df["From_Amount"] = Wallet_Transfers_df["From_Amount"].apply(abs)
Wallet_Transfers_df["From_Amount_LCY"] = Wallet_Transfers_df["From_Amount_LCY"].apply(abs)
Wallet_Transfers_df["To_Amount"] = Wallet_Transfers_df["To_Amount"].apply(abs)
Wallet_Transfers_df["To_Amount_LCY"] = Wallet_Transfers_df["To_Amount_LCY"].apply(abs)

Wallet_Transfers_df["Date"] = Wallet_Transfers_df["Date"].apply(Wallet_get_date)
Wallet_Transfers_df["Time"] = Wallet_Transfers_df["Set Time"]

Wallet_Transfers_df["Payment_type"] = "Transfer"
Wallet_Transfers_df["Payment_Status"] = Wallet_Transfers_df["Status"].apply(Wallet_Payment_Status)
Wallet_Transfers_df["Place"] = ""

Wallet_Transfers_df.drop(labels=["Amount", "Currency", "Category Group Name", "Category", "Status", "Exchange Rate", "Title", "Account", "Set Time"], inplace=True, axis=1)
Wallet_Transfers_df.to_csv(path_or_buf=f"{Year_to_Process}_Wallet_Transfers_df.csv", sep=";", index=False, columns=["Type","Date","Time","From_Account","To_Account","From_Amount","From_Amount_LCY","To_Amount","To_Amount_LCY","From_Currency","To_Currency","Payment_type","Payment_Status","Labels","Notes"])

# Web App
time.sleep(5)
for row in Wallet_Income_Expense_df.iterrows():
    row_df = pandas.Series(data=row[1])

    # New Record
    mouse_move(pyautogui, time, 0.25, New_record_button_possition)
    mouse_clic(pyautogui, time, 0.1)

    # Type:
    if row_df["Type"] == "Expense":
        mouse_move(pyautogui, time, 0.25, Expense_button_possition)
        mouse_clic(pyautogui, time, 0.1)
    elif row_df["Type"] == "Income":
        mouse_move(pyautogui, time, 0.25, Income_button_possition)
        mouse_clic(pyautogui, time, 0.1)
    else:
        pass
        #! Register issue into LOG
    
    # Account
    Account_index = Accounts_df[Accounts_df["Account"] == row_df["Account"]].index
    Account_pos = int(Accounts_df.iloc[Account_index]["Account_Possition"].values[0])
    mouse_move(pyautogui, time, 0.25, Account_possition)
    mouse_clic(pyautogui, time, 0.1)
    for i in range(Account_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")
    press_one_key(pyautogui, time, 0.1, "tab")

    # Amount
    Account_Type = str(Accounts_df.iloc[Account_index]["Account_Type"].values[0])
    if Account_Type == "Bank":
        if Expense_Income_Method == "CZK":
            if  row_df["Currency"] != "CZK":
                write_text(pyautogui, time, 0.1, str(row_df["Amount_LCY"]))
            else:
                write_text(pyautogui, time, 0.1, str(row_df["Amount"]))
        elif Expense_Income_Method == "Original":
            write_text(pyautogui, time, 0.1, str(row_df["Amount"]))
        else:
            pass
            #! write issue to Log   
    else:
        write_text(pyautogui, time, 0.1, str(row_df["Amount"]))

    # Currency   
    if Account_Type == "Bank":
        mouse_move(pyautogui, time, 0.25, Currency_possition)
        mouse_clic(pyautogui, time, 0.1)
        if Expense_Income_Method == "CZK":
            Currency_index = Currency_df[Currency_df["Currency"] == "CZK"].index
            Currency_pos = int(Currency_df.iloc[Currency_index]["Currency_Posstion"].values[0])
            Currency_possition2 = 540 + Currency_line_height * Currency_pos
        elif Expense_Income_Method == "Original":
            Currency_index = Currency_df[Currency_df["Currency"] == row_df["Currency"]].index
            Currency_pos = int(Currency_df.iloc[Currency_index]["Currency_Posstion"].values[0])
            Currency_possition2 = 540 + Currency_line_height * Currency_pos
        else:
            pass
            #! write issue to Log
        mouse_move(pyautogui, time, 0.25, (850, Currency_possition2))
        mouse_clic(pyautogui, time, 0.1)
    else:
        pass
        
    # Category
    mouse_move(pyautogui, time, 0.25, Category_Search_possition)
    mouse_clic(pyautogui, time, 0.1)
    mouse_clic(pyautogui, time, 0.1)
    if str(row_df["Category_3"]) != "":
        write_text(pyautogui, time, 0.1, Replace_diacritic(str(row_df["Category_3"])))
    elif str(row_df["Category_2"]) != "":
        write_text(pyautogui, time, 0.1, Replace_diacritic(str(row_df["Category_2"])))
    elif str(row_df["Category_1"]) != "":
        write_text(pyautogui, time, 0.1, Replace_diacritic(str(row_df["Category_1"])))
    else:
        pyautogui.alert(text='Record with empty Category', title='Allert - stop running', button='OK')
    mouse_move(pyautogui, time, 0.25, Category_First_line)
    mouse_clic(pyautogui, time, 0.1)
    press_one_key(pyautogui, time, 0.1, "tab")
    press_one_key(pyautogui, time, 0.1, "tab")

    # Date
    Calendar_direct_write(pyautogui, row_df["Date"], datetime, time)
    press_one_key(pyautogui, time, 0.1, "tab")

    # Time
    Time_Set_correct(pyautogui, row_df["Time"], time, 0.5, Time_First_line)

    # Payee
    mouse_move(pyautogui, time, 0.25, Payee_possition)
    mouse_clic(pyautogui, time, 0.1)
    pyperclip.copy(str(row_df["Payee"]))
    pyautogui.hotkey("ctrl", "v")
    press_one_key(pyautogui, time, 0.1, "tab")

    # Note
    if row_df["Currency"] != "CZK":
        if Account_Type == "Bank":
            if Expense_Income_Method == "CZK":
                write_text(pyautogui, time, 0.1, str(f"""{row_df["Currency"]}: {row_df["Amount"]},"""))
            elif Expense_Income_Method == "Original":
                write_text(pyautogui, time, 0.1, str(f"""CZK: {row_df["Amount_LCY"]},"""))
            else:
                pass
                #! write issue to Log
            press_one_key(pyautogui, time, 0.25, "enter")
        else:
            write_text(pyautogui, time, 0.1, str(f"""CZK: {row_df["Amount_LCY"]},"""))
            press_one_key(pyautogui, time, 0.25, "enter")
    else:
        pass
    if str(row_df["Notes"]) != "":
        pyperclip.copy(str(row_df["Notes"]))
        pyautogui.hotkey("ctrl", "v")
    else:
        pass
    press_one_key(pyautogui, time, 0.1, "tab")

    # Payment Type
    Payment_Type_index = Payment_Type_df[Payment_Type_df["Payment_Type"] == str(row_df["Payment_type"])].index
    Payment_Type_pos = int(Payment_Type_df.iloc[Payment_Type_index]["Payment_Type_Possition"].values[0])
    for i in range(Payment_Type_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")
    press_one_key(pyautogui, time, 0.1, "tab")
    
    # Payment Status
    Payment_Status_index = Payment_Status_df[Payment_Status_df["Payment_Status"] == str(row_df["Payment_Status"])].index
    Payment_Status_pos = int(Payment_Status_df.iloc[Payment_Status_index]["Payment_Status_Possition"].values[0])
    for i in range(Payment_Status_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")

    # Labels
    if str(row_df["Labels"]) != "[]":
        # Return to Labels --> beucase if there is a lot of them then it change measurements of page
        mouse_move(pyautogui, time, 0.25, Labels_Search_possition)
        mouse_clic(pyautogui, time, 0.1)

        # Write Labels
        labels_text = Replace_diacritic(str(row_df["Labels"]))
        labels = Wallet_Labels_List(labels_text)
        for label in labels:
            write_text(pyautogui, time, 0.1, label)
            press_one_key(pyautogui, time, 0.25, "enter")

        # Record Transaction
        for i in range(3):
            press_one_key(pyautogui, time, 0.1, "tab")
        press_one_key(pyautogui, time, 0.25, "enter")
    else:
        # Record Transaction
        mouse_move(pyautogui, time, 0.25, Add_record)
        mouse_clic(pyautogui, time, 0.1)


for row in Wallet_Transfers_df.iterrows():
    row_df = pandas.Series(data=row[1])

    # New Record
    mouse_move(pyautogui, time, 0.25, New_record_button_possition)
    mouse_clic(pyautogui, time, 0.1)

    if row_df["Type"] == "Transfer":
        mouse_move(pyautogui, time, 0.25, Transfer_button_possition)
        mouse_clic(pyautogui, time, 0.1)
    else:
        pass
        #! Zapsat chybu do logu

    # From
    # From Account
    From_Account_index = Accounts_df[Accounts_df["Account"] == row_df["From_Account"]].index
    From_Account_pos = int(Accounts_df.iloc[From_Account_index]["Account_possition_From_list"].values[0])
    mouse_move(pyautogui, time, 0.25, Trasnfer_From_Account)
    mouse_clic(pyautogui, time, 0.1)
    for i in range(From_Account_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")
    press_one_key(pyautogui, time, 0.1, "tab")

    # From Amount
    From_Account_Type = str(Accounts_df.iloc[From_Account_index]["Account_Type"].values[0])
    if From_Account_Type == "Bank":
        if Transfer_Method == "CZK":
            if  row_df["From_Currency"] != "CZK":
                write_text(pyautogui, time, 0.1, str(row_df["From_Amount_LCY"]))
            else:
                write_text(pyautogui, time, 0.1, str(row_df["From_Amount"]))
        elif Transfer_Method == "Original":
            write_text(pyautogui, time, 0.1, str(row_df["From_Amount"]))
        else:
            pass
            #! Zapsat chybu do logu
    else:
        write_text(pyautogui, time, 0.1, str(row_df["From_Amount"]))

    # From_Currency   
    if From_Account_Type == "Bank":
        mouse_move(pyautogui, time, 0.25, Transfer_From_Currency)
        mouse_clic(pyautogui, time, 0.1)
        if Transfer_Method == "CZK":
            From_Currency_index = Currency_df[Currency_df["Currency"] == "CZK"].index
            From_Currency_pos = int(Currency_df.iloc[From_Currency_index]["Currency_Posstion"].values[0])
            From_Currency_possition2 = 540 + Currency_line_height * From_Currency_pos
        elif Transfer_Method == "Original":
            From_Currency_index = Currency_df[Currency_df["Currency"] == row_df["From_Currency"]].index
            From_Currency_pos = int(Currency_df.iloc[From_Currency_index]["Currency_Posstion"].values[0])
            From_Currency_possition2 = 540 + Currency_line_height * From_Currency_pos
        else:
            pass
            #! Zapsat chybu do logu
        mouse_move(pyautogui, time, 0.25, (700, From_Currency_possition2))
        mouse_clic(pyautogui, time, 0.1)
    else:
        pass

    # To
    # To Account
    To_Account_index = Accounts_df[Accounts_df["Account"] == row_df["To_Account"]].index
    To_Account_pos = int(Accounts_df.iloc[To_Account_index]["Account_possition_TO_list"].values[0])
    mouse_move(pyautogui, time, 0.25, Trasnfer_To_Account)
    mouse_clic(pyautogui, time, 0.1)
    for i in range(To_Account_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")

    # To Currency
    To_Account_Type = str(Accounts_df.iloc[To_Account_index]["Account_Type"].values[0])
    if To_Account_Type == "Bank":
        mouse_move(pyautogui, time, 0.25, Transfer_To_Currency)
        mouse_clic(pyautogui, time, 0.1)
        if Transfer_Method == "CZK":
            To_Currency_index = Currency_df[Currency_df["Currency"] == "CZK"].index
            To_Currency_pos = int(Currency_df.iloc[To_Currency_index]["Currency_Posstion"].values[0])
            To_Currency_possition2 = 540 + Currency_line_height * To_Currency_pos
        elif Transfer_Method == "Original":
            To_Currency_index = Currency_df[Currency_df["Currency"] ==  row_df["To_Currency"]].index
            To_Currency_pos = int(Currency_df.iloc[To_Currency_index]["Currency_Posstion"].values[0])
            To_Currency_possition2 = 540 + Currency_line_height * To_Currency_pos
        else:
            pass
            #! Zapsat chybu do logu
        mouse_move(pyautogui, time, 0.25, (980, To_Currency_possition2))
        mouse_clic(pyautogui, time, 0.1)
    else:
        pass

    # Date
    mouse_move(pyautogui, time, 0.25, Callendar_date)
    mouse_clic(pyautogui, time, 0.1)
    Calendar_direct_write(pyautogui, row_df["Date"], datetime, time)
    press_one_key(pyautogui, time, 0.1, "tab")

    # Time
    Time_Set_correct(pyautogui, row_df["Time"], time, 0.5, Time_First_line)
    
    # Notes
    mouse_move(pyautogui, time, 0.25, Note_possition)
    mouse_clic(pyautogui, time, 0.1)
    if (row_df["From_Currency"] != "CZK") or (row_df["To_Currency"] != "CZK"):
        write_text(pyautogui, time, 0.1, str(f"""{row_df["From_Currency"]}: {row_df["From_Amount"]} = CZK: {row_df["From_Amount_LCY"]}, """))
        press_one_key(pyautogui, time, 0.25, "enter")

        write_text(pyautogui, time, 0.1, str(f"""{row_df["To_Currency"]}: {row_df["To_Amount"]} = CZK: {row_df["To_Amount_LCY"]}, """))
        press_one_key(pyautogui, time, 0.25, "enter")
    else:
        pass
    if str(row_df["Notes"]) != "":
        pyperclip.copy(str(row_df["Notes"]))
        pyautogui.hotkey("ctrl", "v")
    else:
        pass
    press_one_key(pyautogui, time, 0.1, "tab")

    # Payment Type -> Always Transfer
    Payment_Type_index = Payment_Type_df[Payment_Type_df["Payment_Type"] == "Transfer"].index
    Payment_Type_pos = int(Payment_Type_df.iloc[Payment_Type_index]["Payment_Type_Possition"].values[0])
    for i in range(Payment_Type_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")
    press_one_key(pyautogui, time, 0.1, "tab")

    # Payment Status
    Payment_Status_index = Payment_Status_df[Payment_Status_df["Payment_Status"] == str(row_df["Payment_Status"])].index
    Payment_Status_pos = int(Payment_Status_df.iloc[Payment_Status_index]["Payment_Status_Possition"].values[0])
    for i in range(Payment_Status_pos):
        press_one_key(pyautogui, time, 0.1, "down")
    press_one_key(pyautogui, time, 0.25, "enter")

    # Labels
    if str(row_df["Labels"]) != "[]":
        # Return to Labels --> beucase if there is a lot of them then it change measurements of page
        mouse_move(pyautogui, time, 0.25, Labels_Search_possition)
        mouse_clic(pyautogui, time, 0.1)

        # Write Labels
        labels_text = Replace_diacritic(str(row_df["Labels"]))
        labels = Wallet_Labels_List(labels_text)
        for label in labels:
            write_text(pyautogui, time, 0.1, label)
            press_one_key(pyautogui, time, 0.25, "enter")

        # Record Transaction
        for i in range(3):
            press_one_key(pyautogui, time, 0.1, "tab")
        press_one_key(pyautogui, time, 0.25, "enter")
    else:
        # Record Transaction
        mouse_move(pyautogui, time, 0.25, Add_record)
        mouse_clic(pyautogui, time, 0.1)

print("Finished")