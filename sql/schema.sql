CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

CREATE TABLE IF NOT EXISTS ecommerce_events (
    event_time TIMESTAMP,
    event_type VARCHAR(20),
    product_id INT,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255),
    price FLOAT,
    user_id INT,
    user_session VARCHAR(255),
    event_type_numeric INT,
    year INT,
    month INT,
    day_of_week INT,
    hour INT,
    session_start TIMESTAMP,
    session_end TIMESTAMP,
    session_duration BIGINT,
    session_event_count INT,
    viewed INT,
    added_to_cart INT,
    purchased INT
);

CREATE TABLE IF NOT EXISTS user_engagement (
    user_id INT PRIMARY KEY,
    total_views INT,
    total_add_to_cart INT,
    total_purchases INT,
    view_to_cart_rate FLOAT,
    cart_to_purchase_rate FLOAT
);

CREATE TABLE IF NOT EXISTS session_revenue (
    user_session VARCHAR(255) PRIMARY KEY,
    total_revenue FLOAT
);