import mysql.connector
import CredS
from mysql.connector import Error
from ConCreate import create_connection
from ConCreate import execute_query
from ConCreate import execute_read_query

#creating connection to mysql database
myCreds = CredS.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

# create a new entry and add it to the table
query = "INSERT INTO snowboard (Boardtype, Brand, msrp, size) VALUES ('RibStick','Vans','68','30')"
execute_query(conn, query)  

# select all boards READ
select_boards = "SELECT * FROM snowboard"
boards = execute_read_query(conn, select_boards)

for board in boards:
    print(board["Boardtype"] + " has the brand: " + board["Brand"])

# add a table for invoices
create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices(
id INT AUTO_INCREMENT,
amount INT,
description VARCHAR(255) NOT NULL,
user_id INTEGER UNSIGNED NOT NULL,
FOREIGN KEY fk_user_id(user_id) REFERENCES users(id),
PRIMARY KEY (id)
)"""

execute_query(conn, create_invoice_table)

# add invoice record to invoice table
invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_from_user)

execute_query(conn, query)            

# updating invoice record
new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1 """ % (new_amount)

execute_query(conn, update_invoice_query)

# delete invoice record from invoice table
invoice_id_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (invoice_id_to_delete)
execute_query(conn, delete_statement)

# delete invoices table
delete_table_statement = "DROP TABLE invoices"
execute_query(conn, delete_table_statement)

## CONCLUDES CRUD OPERATIONS ##
    