
import pandas as pd
import pymysql


dbInfo = {
    'host': 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'roottest',
    'db' : 'testdb'
}
conn = pymysql.connect(
    host = dbInfo['host'],
    port = dbInfo['port'],
    user = dbInfo['user'],
    password = dbInfo['password'],
    db = dbInfo['db'],
    charset = 'utf8'
)
df = pd.read_sql('SELECT * FROM data', conn)


# 1. SELECT * FROM data

df = pd.read_sql('SELECT * FROM data', conn)
print(df)



# 2. SELECT * FROM data LIMIT(10)

df.head(10)


# 3. SELECT id FROM data

df['id']

# 4. SELECT COUNT(id) FROM data

df['id'].count()


# 5. SELECT * FROM data WHERE id<1000 AND age>30

df[ df['id'] < 1000] & [ df['age'] > 30 ]


# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id

df.groupby('id')
df.groupby('order_id').sum()


# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id

pd.merge(table1, table2, on='id')


# 8. SELECT * FROM table1 UNION SELECT * FROM table2

pd.concat(table1, table2)


# 9. DELETE FROM table1 WHERE id=10

df[ df['id'] != 10 ]

# 10. ALTER TABLE table1 DROP COLUMN column_name

df.drop( 'column_name' ,axis = 1)