# Создание таблиц
create_employees_table = """
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT NOT NULL
);
"""

create_customers_table = """
CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);
"""

create_orders_table = """
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    employee_id BIGINT NOT NULL,
    order_date DATE,
    ship_city VARCHAR(255) NOT NULL,
    CONSTRAINT fk_employee FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
"""