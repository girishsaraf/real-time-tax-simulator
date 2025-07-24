-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    state VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Accounts table
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    type VARCHAR(50),
    provider VARCHAR(100)
);

-- Transactions table
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    type VARCHAR(50),
    amount NUMERIC(12,2),
    date DATE
);

-- Tax liabilities table
CREATE TABLE tax_liabilities (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    quarter VARCHAR(10),
    federal_tax NUMERIC(12,2),
    state_tax NUMERIC(12,2)
);

-- Scenarios table
CREATE TABLE scenarios (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    scenario_json JSONB,
    result_json JSONB
); 