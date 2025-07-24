-- Users
INSERT INTO users (name, email, hashed_password, state) VALUES ('Alice', 'alice@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'CA');
INSERT INTO users (name, email, hashed_password, state) VALUES ('Bob', 'bob@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'NY');

-- Transactions (income)
INSERT INTO transactions (user_id, type, amount, date) VALUES (1, 'income', 40000, '2024-01-15');
INSERT INTO transactions (user_id, type, amount, date) VALUES (1, 'income', 15000, '2024-03-10');
INSERT INTO transactions (user_id, type, amount, date) VALUES (2, 'income', 60000, '2024-02-20');

-- Tax Liabilities
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (1, 'Q1', 5000, 2000);
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (2, 'Q1', 9000, 3000); 