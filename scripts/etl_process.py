import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import random

# Настройка подключения к базе данных
db_engine = create_engine('postgresql+psycopg2://postgres:0051@localhost:5432/bank_data')

# Пути к файлам данных
files = {
    "customers": r"C:\Users\vladi\OneDrive\Рабочий стол\csv\Customers.csv",
    "credit_agreements": r"C:\Users\vladi\OneDrive\Рабочий стол\csv\CreditAgreements.csv",
    "credit_products": r"C:\Users\vladi\OneDrive\Рабочий стол\csv\CreditProducts.csv",
    "credit_transactions": r"C:\Users\vladi\OneDrive\Рабочий стол\csv\CreditTransactions.csv",
    "transaction_types": r"C:\Users\vladi\OneDrive\Рабочий стол\csv\TransactionTypes.csv"
}

# Функция для генерации случайной даты
def generate_random_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + pd.Timedelta(days=random_days)).strftime('%Y-%m-%d')

# Функция очистки данных
def clean_data(df, table_name):
    # Удаляем дубликаты
    df.drop_duplicates(inplace=True)
    
    # Очистка данных для таблицы Customers
    if table_name == "customers":
        # Заполнение пустых дат случайными значениями
        if 'DateOfBirth' in df.columns:
            df['DateOfBirth'] = df['DateOfBirth'].apply(
                lambda x: generate_random_date(1950, 2000) if pd.isna(x) else x
            )
        if 'RegistrationDate' in df.columns:
            df['RegistrationDate'] = df['RegistrationDate'].apply(
                lambda x: generate_random_date(2010, 2023) if pd.isna(x) else x
            )
        # Заполнение пустых имен клиентов
        if 'Name' in df.columns:
            df['Name'] = df['Name'].fillna('Неизвестный клиент')
    
    # Очистка других таблиц
    if table_name == "credit_transactions" and 'TransactionDate' in df.columns:
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
        df.dropna(subset=['TransactionDate'], inplace=True)
    
    # Удаляем пустые строки, если важные поля остались не заполнены
    if 'CustomerID' in df.columns:
        df.dropna(subset=['CustomerID'], inplace=True)

    return df

# ETL-процесс
for table_name, file_path in files.items():
    print(f"Загрузка данных из {file_path}")
    df = pd.read_csv(file_path, encoding='utf-8')
    
    print(f"Очистка данных для {table_name}")
    df = clean_data(df, table_name)
    
    print(f"Загрузка данных в таблицу {table_name}")
    df.to_sql(table_name, db_engine, if_exists='replace', index=False)

print("ETL-процесс завершен!")