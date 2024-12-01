CREATE TABLE DataMart_TransactionsSummary AS
SELECT
    c."Name" AS CustomerName,
    cp."ProductName" AS CreditProduct,
    SUM(ct."TransactionAmount") AS TotalTransactionAmount,
    COUNT(ct."TransactionID") AS TotalTransactionCount,
    tt."TransactionTypeName" AS TransactionType,
    ca."AgreementDate" AS AgreementDate
FROM "customers" c
JOIN "credit_agreements" ca ON c."CustomerID" = ca."CustomerID"  -- Используем правильное имя столбца с кавычками
JOIN "credit_products" cp ON ca."CreditProductID" = cp."CreditProductID"
JOIN "credit_transactions" ct ON ca."CreditAgreementID" = ct."CreditAgreementID"
JOIN "transaction_types" tt ON ct."TransactionTypeID" = tt."TransactionTypeID"
GROUP BY c."Name", cp."ProductName", tt."TransactionTypeName", ca."AgreementDate";