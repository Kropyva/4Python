import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

try:
    df = pd.read_csv('employees.csv', sep=';', encoding='utf-8-sig')
except FileNotFoundError:
    print("Warning about absent or issues with openning the CSV file.")
    exit()

try:
    wb = Workbook()
    all_sheet = wb.active
    all_sheet.title = "all"
    all_sheet.append(df.columns.tolist())
    for row in dataframe_to_rows(df, index=False, header=False):
        all_sheet.append(row)

    age_categories = {
        "younger-18": (0, 18),
        "18-45": (18, 45),
        "45-70": (45, 70),
        "older-70": (70, 120)
    }

    for sheet_name, (min_age, max_age) in age_categories.items():
        ws = wb.create_sheet(title=sheet_name)
        ws.append(["№", "Прізвище", "Ім'я", "По батькові", "Дата народження", "Вік"])
        for index, row in df.iterrows():
            birthdate = datetime.strptime(row['Дата народження'], '%Y-%m-%d')
            age = calculate_age(birthdate)
            if min_age <= age < max_age:
                ws.append([index + 1, row['Прізвище'], row["Ім'я"], row['По-батькові'], row['Дата народження'], age])

    wb.save('employees.xlsx')
    print("Ok, everything is done.")
except Exception as e:
    print("Impossible to create XLSX file:", str(e))