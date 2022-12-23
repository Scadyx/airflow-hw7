INSERT INTO order_status_stats(dt, order_status_name, orders_count)
        SELECT sale.date_sale::date AS dt,
        status_name.status_name AS order_status_name,
        count(1) AS orders_count
        FROM sale
        LEFT JOIN order_status
            ON sale.sale_id = order_status.sale_id
        LEFT JOIN status_name
            ON status_name.status_name_id = order_status.status_name_id
        GROUP BY dt, order_status_name;