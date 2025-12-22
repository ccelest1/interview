CREATE user_table(
    user_id INT primary key AUTOINCREMENT,
    username varchar(50) not null unique,
    email varchar(100) not null unique,
    password_hash varchar(255) not null,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE products_table(
    product_id INT primary key AUTOINCREMENT,
    name varchar(50) not null,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantitiy INT NOT NULL DEFAULT 0,
    INDEX idx_name (name)
);


CREATE transaction_table(
    transaction_id primary key AUTOINCREMENT,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'shipped', 'delivered', 'cancelled'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) references users(user_id)
);

CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY AUTOINCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INTO NOT NULL,
    price_at_purchase DECIMAL(10,2) NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
