# vega
# ---------------------------
# mysql_db
# ---------------------------
# Administrator 2021/2/22 22:33 
# ---------------------------
import mysql.connector.pooling

__config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'wanglei',
    'password' : '123456',
    'database' : 'vega'
}
# 创建数据库连接池
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)

