#Group 5/11 - We add a product (p100, cd, 5) in Product and (p100, d2, 50) in stock
#Fahad Mulla and Likith Kothapally

import psycopg2

hostname = "localhost"
database="postgres"
username="postgres"
pwd="F*************"
port_id = "5432"
conn = None
cur = None

try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
    )

    cur = conn.cursor()
    #QUERY
    cur.execute("INSERT INTO product (prod, pname, price) VALUES ('p100', 'cd', 5); INSERT INTO stock (prod, dep, quantity) VALUES ('p100', 'd2', 50);")
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close
    if conn is not None:
        conn.close