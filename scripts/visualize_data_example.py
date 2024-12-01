import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Создание подключения к базе данных
db_engine = create_engine('postgresql+psycopg2://postgres:0051@localhost:5432/bank_data')

# Извлечение данных из витрины
query = """
SELECT customername, creditproduct, totaltransactionamount, totaltransactioncount, transactiontype, agreementdate
FROM DataMart_TransactionsSummary;
"""
df = pd.read_sql(query, db_engine)

# Простой график для отображения суммы транзакций по клиентам
df_grouped = df.groupby('customername')['totaltransactionamount'].sum().reset_index()
df_grouped.sort_values(by='totaltransactionamount', ascending=False, inplace=True)

plt.figure(figsize=(10, 6))
plt.bar(df_grouped['customername'], df_grouped['totaltransactionamount'])
plt.xticks(rotation=45)
plt.title('Сумма транзакций по клиентам')
plt.xlabel('Клиенты')
plt.ylabel('Сумма транзакций')
plt.tight_layout()
plt.show()