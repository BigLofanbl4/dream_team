-- Таблица Customers
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    CustomerTypeID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    DateOfBirth DATE,
    RegistrationDate DATE,
    TIN VARCHAR(20) NOT NULL,
    ContactInfo VARCHAR(100)
);

-- Таблица CreditProducts
CREATE TABLE CreditProducts (
    CreditProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    InterestRate DECIMAL(5, 2),
    MaxLoanAmount DECIMAL(15, 2),
    MinRepaymentTerm INT,
    CollateralRequired BOOLEAN
);

-- Таблица CreditAgreements
CREATE TABLE CreditAgreements (
    CreditAgreementID SERIAL PRIMARY KEY,
    CustomerID INT REFERENCES Customers(CustomerID),
    CreditProductID INT REFERENCES CreditProducts(CreditProductID),
    AgreementDate DATE NOT NULL,
    LoanAmount DECIMAL(15, 2) NOT NULL,
    LoanTerm INT NOT NULL,
    InterestRate DECIMAL(5, 2)
);

-- Таблица TransactionTypes
CREATE TABLE TransactionTypes (
    TransactionTypeID SERIAL PRIMARY KEY,
    TransactionTypeName VARCHAR(255) NOT NULL
);

-- Таблица CreditTransactions
CREATE TABLE CreditTransactions (
    TransactionID SERIAL PRIMARY KEY,
    CustomerID INT REFERENCES Customers(CustomerID),
    CreditAgreementID INT REFERENCES CreditAgreements(CreditAgreementID),
    TransactionDate DATE NOT NULL,
    TransactionAmount DECIMAL(15, 2) NOT NULL,
    TransactionTypeID INT REFERENCES TransactionTypes(TransactionTypeID)
);