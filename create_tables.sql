CREATE TABLE employees(
	first_name varchar(100) not NULL,
	last_name varchar(100) not NULL,
	title varchar(100) not NULL,
	birth_date date,
	notes text,
	employee_id int unique not NULL
);
CREATE TABLE customers(
    customer_id varchar(100) unique not NULL,
	company_name varchar(100) not NULL ,
	contact_name varchar(100) not NULL
);

CREATE TABLE orders(
	order_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id) ,
	employee_id int not NULL REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(100) not NULL
);

select * from employees