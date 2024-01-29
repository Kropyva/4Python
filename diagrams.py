import pandas as pd
import matplotlib.pyplot as plot

try:
    df = pd.read_csv('employees.csv', sep=';', encoding='utf-8-sig')
except FileNotFoundError:
    print("Warning about absent or issues with openning the CSV file.")
    exit()

print("Ok")

def calculate_age(birthdate):
    today = pd.to_datetime('today')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

gender_counts = df['Стать'].value_counts()
print("Count of employees by gender:")
print(gender_counts)

plot.figure(figsize=(6, 6))
plot.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plot.title("Distribution of employees by gender")
plot.show()

def categorize_age(age):
    if age < 18:
        return "younger-18"
    elif 18 <= age < 45:
        return "18-45"
    elif 45 <= age < 70:
        return "45-70"
    else:
        return "older-70"

df['Вік'] = df['Дата народження'].apply(lambda x: calculate_age(pd.to_datetime(x)))
age_category_counts = df['Вік'].apply(lambda x: categorize_age(x)).value_counts()
print("\nCount of employees by age:")
print(age_category_counts)

plot.figure(figsize=(8, 6))
age_category_counts.plot(kind='bar')
plot.xlabel("Age category")
plot.ylabel("Count of employees")
plot.title("Distribution of employees by age")
plot.show()

gender_age_counts = df.groupby(['Стать', df['Вік'].apply(categorize_age)]).size().unstack(fill_value=0)
print("\nCount of employees by gender and age:")
print(gender_age_counts)

gender_age_counts.plot(kind='bar', stacked=True)
plot.xlabel("Age category")
plot.ylabel("Count of employees")
plot.title("Count of employees by gender and age")
plot.show()