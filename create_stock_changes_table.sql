-- StockChange jadvali yaratish
CREATE TABLE IF NOT EXISTS stock_changes (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    action VARCHAR(20) NOT NULL CHECK (action IN ('add', 'deduct', 'transfer', 'sale')),
    quantity DECIMAL(15, 3) NOT NULL,
    location_type VARCHAR(20) NOT NULL CHECK (location_type IN ('warehouse', 'store')),
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE SET NULL,
    store_id INTEGER REFERENCES stores(id) ON DELETE SET NULL,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    change_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexlar yaratish
CREATE INDEX idx_stock_changes_product_id ON stock_changes(product_id);
CREATE INDEX idx_stock_changes_action ON stock_changes(action);
CREATE INDEX idx_stock_changes_change_date ON stock_changes(change_date DESC);
CREATE INDEX idx_stock_changes_warehouse_id ON stock_changes(warehouse_id);
CREATE INDEX idx_stock_changes_store_id ON stock_changes(store_id);
CREATE INDEX idx_stock_changes_user_id ON stock_changes(user_id);

-- Izoh qo'shish
COMMENT ON TABLE stock_changes IS 'Stock o''zgarishlari tarixi - har bir qo''shish, ayirish, ko''chirish operatsiyasi';
COMMENT ON COLUMN stock_changes.action IS 'add: qo''shish, deduct: ayirish, transfer: ko''chirish, sale: sotish';
COMMENT ON COLUMN stock_changes.quantity IS 'O''zgargan miqdor';
COMMENT ON COLUMN stock_changes.location_type IS 'warehouse: ombor, store: do''kon';
