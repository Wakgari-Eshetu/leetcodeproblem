SELECT product_id, product_name, description
FROM products
WHERE description REGEXP '(^|[^0-9A-Za-z])[S][N][0-9]{4}-[0-9]{4}($|[^0-9])'
ORDER BY product_id;
