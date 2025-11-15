-- Mahsulot 5070 (sidena chixol) ning stock tarixini ko'rish
-- Do'kon stock
SELECT 
    'Do\'kon Stock' as type,
    s.name as location_name,
    ss.quantity as current_stock,
    p.name as product_name
FROM store_stocks ss
JOIN stores s ON s.id = ss.store_id
JOIN products p ON p.id = ss.product_id
WHERE ss.product_id = 5070;

-- Ombor stock
SELECT 
    'Ombor Stock' as type,
    w.name as location_name,
    ws.quantity as current_stock,
    p.name as product_name
FROM warehouse_stocks ws
JOIN warehouses w ON w.id = ws.warehouse_id
JOIN products p ON p.id = ws.product_id
WHERE ws.product_id = 5070;
