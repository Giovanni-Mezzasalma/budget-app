-- ============================================
-- BUDGET APP - Database Schema Creation
-- PostgreSQL 16+
-- ============================================
-- 
-- Questo script crea lo schema completo del database:
-- - 6 tabelle principali
-- - ENUM types
-- - Indexes per performance
-- - Triggers per auto-update
-- 
-- Eseguire in pgAdmin su database: budget_app_dev
-- 
-- Author: Giovanni Mezzasalma
-- Date: November 2025
-- Version: 1.0

-- ============================================
-- CLEANUP (solo per re-esecuzione script)
-- ============================================
-- ATTENZIONE: Decommenta solo se vuoi ricreare tutto da zero!
-- DROP TABLE IF EXISTS custom_charts CASCADE;
-- DROP TABLE IF EXISTS transfers CASCADE;
-- DROP TABLE IF EXISTS transactions CASCADE;
-- DROP TABLE IF EXISTS categories CASCADE;
-- DROP TABLE IF EXISTS accounts CASCADE;
-- DROP TABLE IF EXISTS users CASCADE;
-- DROP TYPE IF EXISTS account_type_enum;
-- DROP TYPE IF EXISTS transaction_type_enum;
-- DROP TYPE IF EXISTS chart_type_enum;

-- ============================================
-- EXTENSIONS
-- ============================================

-- UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- ENUM TYPES
-- ============================================

-- Account types
CREATE TYPE account_type_enum AS ENUM (
    'checking',     -- Conto corrente
    'savings',      -- Risparmio
    'credit',       -- Carta di credito
    'cash',         -- Contanti
    'investment'    -- Investimenti
);

-- Transaction types
CREATE TYPE transaction_type_enum AS ENUM (
    'income',       -- Entrata
    'expense'       -- Uscita
);

-- Chart types
CREATE TYPE chart_type_enum AS ENUM (
    'line',         -- Grafico a linee
    'bar',          -- Grafico a barre
    'pie',          -- Grafico a torta
    'area'          -- Grafico ad area
);

-- ============================================
-- TABLE: users
-- ============================================

CREATE TABLE users (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Authentication
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    
    -- Profile
    full_name VARCHAR(255),
    
    -- Status
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Comments
COMMENT ON TABLE users IS 'Utenti dell''applicazione';
COMMENT ON COLUMN users.email IS 'Email univoca per login';
COMMENT ON COLUMN users.password_hash IS 'Password hashata con bcrypt';
COMMENT ON COLUMN users.is_active IS 'FALSE per soft delete';

-- ============================================
-- TABLE: accounts
-- ============================================

CREATE TABLE accounts (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Foreign Key
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Account Details
    name VARCHAR(100) NOT NULL,
    account_type account_type_enum NOT NULL DEFAULT 'checking',
    balance NUMERIC(12, 2) DEFAULT 0.00 NOT NULL,
    currency VARCHAR(3) DEFAULT 'EUR' NOT NULL,
    
    -- Customization
    color VARCHAR(7),  -- HEX color: #RRGGBB
    icon VARCHAR(50),  -- Emoji or icon name
    
    -- Status
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraints
    CONSTRAINT chk_account_balance_positive CHECK (balance >= 0),
    CONSTRAINT chk_account_color_format CHECK (color ~ '^#[0-9A-Fa-f]{6}$' OR color IS NULL),
    CONSTRAINT chk_account_currency_iso CHECK (length(currency) = 3)
);

-- Comments
COMMENT ON TABLE accounts IS 'Conti bancari e portafogli utente';
COMMENT ON COLUMN accounts.balance IS 'Aggiornato automaticamente da transactions/transfers';
COMMENT ON COLUMN accounts.color IS 'Colore HEX per UI (#3B82F6)';

-- ============================================
-- TABLE: categories
-- ============================================

CREATE TABLE categories (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Foreign Keys
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    parent_category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    
    -- Category Details
    name VARCHAR(100) NOT NULL,
    type transaction_type_enum NOT NULL,
    
    -- Customization
    color VARCHAR(7),  -- HEX color
    icon VARCHAR(50),  -- Emoji or icon name
    
    -- System Flag
    is_system BOOLEAN DEFAULT FALSE NOT NULL,
    
    -- Timestamp
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    -- Constraints
    CONSTRAINT chk_category_color_format CHECK (color ~ '^#[0-9A-Fa-f]{6}$' OR color IS NULL)
);

-- Comments
COMMENT ON TABLE categories IS 'Categorie per classificare transazioni';
COMMENT ON COLUMN categories.parent_category_id IS 'Per sottocategorie (self-referential)';
COMMENT ON COLUMN categories.is_system IS 'TRUE = categoria predefinita non eliminabile';

-- ============================================
-- TABLE: transactions
-- ============================================

CREATE TABLE transactions (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Foreign Keys
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE RESTRICT,
    
    -- Transaction Details
    amount NUMERIC(12, 2) NOT NULL,
    type transaction_type_enum NOT NULL,
    date DATE NOT NULL,
    description VARCHAR(255),
    notes TEXT,
    
    -- Tags (PostgreSQL array)
    tags TEXT[],
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Constraints
    CONSTRAINT chk_transaction_amount_positive CHECK (amount > 0),
    CONSTRAINT chk_transaction_date_not_future CHECK (date <= CURRENT_DATE)
);

-- Comments
COMMENT ON TABLE transactions IS 'Movimenti finanziari (entrate e uscite)';
COMMENT ON COLUMN transactions.date IS 'Data transazione (può essere passata)';
COMMENT ON COLUMN transactions.created_at IS 'Data inserimento nel sistema';
COMMENT ON COLUMN transactions.tags IS 'Array di tag per ricerca/filtro';

-- ============================================
-- TABLE: transfers
-- ============================================

CREATE TABLE transfers (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Foreign Keys
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    from_account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    to_account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    
    -- Transfer Details
    amount NUMERIC(12, 2) NOT NULL,
    date DATE NOT NULL,
    description VARCHAR(255),
    
    -- Timestamp
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    -- Constraints
    CONSTRAINT chk_transfer_amount_positive CHECK (amount > 0),
    CONSTRAINT chk_transfer_different_accounts CHECK (from_account_id != to_account_id),
    CONSTRAINT chk_transfer_date_not_future CHECK (date <= CURRENT_DATE)
);

-- Comments
COMMENT ON TABLE transfers IS 'Trasferimenti tra account dello stesso utente';
COMMENT ON COLUMN transfers.amount IS 'Importo trasferito';

-- ============================================
-- TABLE: custom_charts
-- ============================================

CREATE TABLE custom_charts (
    -- Primary Key
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Foreign Key
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Chart Details
    name VARCHAR(100) NOT NULL,
    chart_type chart_type_enum NOT NULL,
    
    -- Configuration (JSONB for flexibility)
    config JSONB NOT NULL,
    filters JSONB,
    
    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Comments
COMMENT ON TABLE custom_charts IS 'Grafici personalizzati salvati dall''utente';
COMMENT ON COLUMN custom_charts.config IS 'Configurazione completa grafico (JSONB)';
COMMENT ON COLUMN custom_charts.filters IS 'Filtri applicati (date, accounts, categories)';

-- ============================================
-- INDEXES FOR PERFORMANCE
-- ============================================

-- Users
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_is_active ON users(is_active) WHERE is_active = TRUE;

-- Accounts
CREATE INDEX idx_accounts_user_id ON accounts(user_id);
CREATE INDEX idx_accounts_user_active ON accounts(user_id, is_active) WHERE is_active = TRUE;

-- Categories
CREATE INDEX idx_categories_user_id ON categories(user_id);
CREATE INDEX idx_categories_type ON categories(type);
CREATE INDEX idx_categories_user_type ON categories(user_id, type);

-- Transactions (most queried table)
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_account_id ON transactions(account_id);
CREATE INDEX idx_transactions_category_id ON transactions(category_id);
CREATE INDEX idx_transactions_date ON transactions(date DESC);
CREATE INDEX idx_transactions_user_date ON transactions(user_id, date DESC);
CREATE INDEX idx_transactions_type ON transactions(type);

-- Transfers
CREATE INDEX idx_transfers_user_id ON transfers(user_id);
CREATE INDEX idx_transfers_date ON transfers(date DESC);
CREATE INDEX idx_transfers_from_account ON transfers(from_account_id);
CREATE INDEX idx_transfers_to_account ON transfers(to_account_id);

-- Custom Charts
CREATE INDEX idx_custom_charts_user_id ON custom_charts(user_id);

-- ============================================
-- TRIGGERS FOR AUTO-UPDATE
-- ============================================

-- Function: Update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to tables with updated_at
CREATE TRIGGER trigger_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trigger_accounts_updated_at
    BEFORE UPDATE ON accounts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trigger_transactions_updated_at
    BEFORE UPDATE ON transactions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trigger_custom_charts_updated_at
    BEFORE UPDATE ON custom_charts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- SEED DATA - Default Categories Function
-- ============================================

-- Function to seed default categories for new user
CREATE OR REPLACE FUNCTION seed_default_categories(p_user_id UUID)
RETURNS VOID AS $$
BEGIN
    -- Income Categories
    INSERT INTO categories (user_id, name, type, color, icon, is_system) VALUES
    (p_user_id, 'Stipendio', 'income', '#10B981', '💰', TRUE),
    (p_user_id, 'Freelance', 'income', '#3B82F6', '💼', TRUE),
    (p_user_id, 'Investimenti', 'income', '#8B5CF6', '📈', TRUE),
    (p_user_id, 'Bonus', 'income', '#F59E0B', '🎁', TRUE),
    (p_user_id, 'Altro reddito', 'income', '#6B7280', '💵', TRUE);
    
    -- Expense Categories
    INSERT INTO categories (user_id, name, type, color, icon, is_system) VALUES
    (p_user_id, 'Casa', 'expense', '#EF4444', '🏠', TRUE),
    (p_user_id, 'Affitto', 'expense', '#DC2626', '🔑', TRUE),
    (p_user_id, 'Bollette', 'expense', '#F97316', '💡', TRUE),
    (p_user_id, 'Alimentari', 'expense', '#F59E0B', '🛒', TRUE),
    (p_user_id, 'Ristoranti', 'expense', '#EAB308', '🍽️', TRUE),
    (p_user_id, 'Trasporti', 'expense', '#14B8A6', '🚗', TRUE),
    (p_user_id, 'Benzina', 'expense', '#06B6D4', '⛽', TRUE),
    (p_user_id, 'Salute', 'expense', '#EC4899', '🏥', TRUE),
    (p_user_id, 'Farmacia', 'expense', '#F472B6', '💊', TRUE),
    (p_user_id, 'Svago', 'expense', '#8B5CF6', '🎭', TRUE),
    (p_user_id, 'Abbigliamento', 'expense', '#06B6D4', '👕', TRUE),
    (p_user_id, 'Educazione', 'expense', '#3B82F6', '📚', TRUE),
    (p_user_id, 'Tecnologia', 'expense', '#6366F1', '💻', TRUE),
    (p_user_id, 'Viaggi', 'expense', '#10B981', '✈️', TRUE),
    (p_user_id, 'Sport', 'expense', '#84CC16', '🏋️', TRUE),
    (p_user_id, 'Altro', 'expense', '#6B7280', '📦', TRUE);
END;
$$ LANGUAGE plpgsql;

-- Comments
COMMENT ON FUNCTION seed_default_categories(UUID) IS 'Crea categorie predefinite per nuovo utente';

-- ============================================
-- VERIFICATION QUERIES
-- ============================================

-- Run these queries to verify schema creation:

-- 1. Check all tables exist
-- SELECT table_name FROM information_schema.tables 
-- WHERE table_schema = 'public' 
-- ORDER BY table_name;

-- 2. Check all ENUM types
-- SELECT typname FROM pg_type 
-- WHERE typtype = 'e' 
-- ORDER BY typname;

-- 3. Check all indexes
-- SELECT indexname FROM pg_indexes 
-- WHERE schemaname = 'public' 
-- ORDER BY indexname;

-- 4. Check all triggers
-- SELECT trigger_name, event_object_table 
-- FROM information_schema.triggers 
-- WHERE trigger_schema = 'public';

-- ============================================
-- EXAMPLE USAGE
-- ============================================

-- Create test user and seed categories:
-- INSERT INTO users (email, password_hash, full_name) 
-- VALUES ('test@example.com', 'hash', 'Test User') 
-- RETURNING id;

-- Then call (replace UUID):
-- SELECT seed_default_categories('your-user-uuid-here');

-- ============================================
-- SCHEMA VERSION
-- ============================================

-- Store schema version (optional, for migrations tracking)
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    description TEXT,
    applied_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO schema_version (version, description) 
VALUES (1, 'Initial schema creation with 6 tables');

-- ============================================
-- END OF SCRIPT
-- ============================================

-- Schema created successfully! ✅
-- Next steps:
-- 1. Verify tables in pgAdmin (Databases → budget_app_dev → Schemas → Tables)
-- 2. Create SQLAlchemy models in Python
-- 3. Setup Alembic migrations
