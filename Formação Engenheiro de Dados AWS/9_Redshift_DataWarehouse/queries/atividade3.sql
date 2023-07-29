select p.product_name nome, p.unit_price preco from products p
    order by p.unit_price desc
    limit 10