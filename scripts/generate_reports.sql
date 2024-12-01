SELECT CustomerName, SUM(TotalTransactionAmount) AS TotalAmount
FROM DataMart_TransactionsSummary
GROUP BY CustomerName
ORDER BY TotalAmount DESC
LIMIT 10;

SELECT TransactionType, SUM(TotalTransactionAmount) AS TotalAmount
FROM DataMart_TransactionsSummary
GROUP BY TransactionType
ORDER BY TotalAmount DESC;