import psycopg2
import csv

con = psycopg2.connect(host='localhost', database='north', user='postgres', password='1991')
count = 1
try:
    with con:
        with con.cursor() as cur:
            with open('customers_data.csv') as customers:
                file = csv.DictReader(customers)
                for row in file:
                    cur.execute('Insert into customers values (%s, %s, %s)',
                                (row["customer_id"], row["company_name"], row["contact_name"]))
            with open('employees_data.csv') as employeer:
                file = csv.DictReader(employeer)
                for row in file:
                    cur.execute('INSERT into employees values(%s, %s, %s, %s, %s, %s)', (
                    row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"], count))
                    count += 1
            with open('orders_data.csv') as order:
                file = csv.DictReader(order)
                for row in file:
                    cur.execute('INSERT into orders values(%s, %s, %s, %s, %s)', (
                    row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))


finally:
    con.close()
