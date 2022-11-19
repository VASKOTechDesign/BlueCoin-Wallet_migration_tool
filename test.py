import pandas


# Read csv.
Wallet_Income_Expense_df = pandas.read_csv(filepath_or_buffer="./Data/2022_11_19-all_transaction.csv", sep=";")
Category_mapping_df = pandas.read_csv(filepath_or_buffer="Category_Mapping.csv", sep=";")

for row in Wallet_Income_Expense_df.iterrows():
    try:
        row_df = pandas.Series(data=row[1])
        
        BlueCoin_Type = row_df["Type"]
        BlueCoin_Cateogry_Main = row_df["Category Group Name"]
        BlueCoin_Cateogry_Sub = row_df["Category"]

        Mask1 = Category_mapping_df["BlueCoin_Type"] == BlueCoin_Type
        Mask2 = Category_mapping_df["BlueCoin_Main"] == BlueCoin_Cateogry_Main
        Mask3 = Category_mapping_df["BlueCoin_Sub-Category"] == BlueCoin_Cateogry_Sub

        Category_mapping_Series = Category_mapping_df[Mask1 & Mask2 & Mask3]

        Wallet_Income_Expense_df.at[row[0],"Category_1"] = Category_mapping_Series.iloc[0]["Wallet_Main"]
        Wallet_Income_Expense_df.at[row[0],"Category_2"] = Category_mapping_Series.iloc[0]["Wallet_Sub-Category"]
        Wallet_Income_Expense_df.at[row[0],"Category_3"] = Category_mapping_Series.iloc[0]["Wallet_Sub2-Category"]
    except:
        if BlueCoin_Type != "Transfer":
            print(BlueCoin_Type, BlueCoin_Cateogry_Main, BlueCoin_Cateogry_Sub)
        else:
            pass
print(Wallet_Income_Expense_df[["Category_1", "Category_2", "Category_3"]])
Wallet_Income_Expense_df.to_excel(path_or_buf="./Data/2022_11_19-category_mapped.xlsx")