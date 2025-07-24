-- Users
INSERT INTO users (name, email, hashed_password, state) VALUES ('Alice', 'alice@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'CA');
INSERT INTO users (name, email, hashed_password, state) VALUES ('Bob', 'bob@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'NY');
INSERT INTO users (name, email, hashed_password, state) VALUES ('Carol', 'carol@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'TX');
INSERT INTO users (name, email, hashed_password, state) VALUES ('Dave', 'dave@example.com', '$2b$12$abcdefghijklmnopqrstuv', 'FL');

-- Transactions (income and capital gains)
INSERT INTO transactions (user_id, type, amount, date) VALUES (1, 'income', 40000, '2024-01-15');
INSERT INTO transactions (user_id, type, amount, date) VALUES (1, 'income', 15000, '2024-03-10');
INSERT INTO transactions (user_id, type, amount, date) VALUES (2, 'income', 60000, '2024-02-20');
INSERT INTO transactions (user_id, type, amount, date) VALUES (3, 'income', 80000, '2024-01-25');
INSERT INTO transactions (user_id, type, amount, date) VALUES (4, 'income', 20000, '2024-03-01');
INSERT INTO transactions (user_id, type, amount, date) VALUES (1, 'capital_gain', 5000, '2024-02-10');
INSERT INTO transactions (user_id, type, amount, date) VALUES (2, 'capital_gain', 12000, '2024-03-15');
INSERT INTO transactions (user_id, type, amount, date) VALUES (3, 'capital_gain', 3000, '2024-02-28');
INSERT INTO transactions (user_id, type, amount, date) VALUES (4, 'capital_gain', 7000, '2024-01-30');

-- Tax Liabilities
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (1, 'Q1', 5000, 2000);
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (2, 'Q1', 9000, 3000);
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (3, 'Q1', 15000, 0);
INSERT INTO tax_liabilities (user_id, quarter, federal_tax, state_tax) VALUES (4, 'Q1', 2500, 0);

-- Scenarios
INSERT INTO scenarios (user_id, scenario_json, result_json) VALUES (1, '{"type": "stock_sale", "amount": 10000}', '{"estimated_tax_impact": 1500}');
INSERT INTO scenarios (user_id, scenario_json, result_json) VALUES (2, '{"type": "freelance_gig", "amount": 20000}', '{"estimated_tax_impact": 4000}');
INSERT INTO scenarios (user_id, scenario_json, result_json) VALUES (3, '{"type": "business_expense", "amount": 5000}', '{"estimated_tax_impact": -1000}'); 