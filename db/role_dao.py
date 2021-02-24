# vega
# ---------------------------
# role_dao
# ---------------------------
# Administrator 2021/2/23 19:53 
# ---------------------------
from db.mysql_db import pool

class RoleDao:
    # 查询所有权限
    def search_role(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select * from t_role order by id asc;'
            cursor.execute(sql)
            role = cursor.fetchall()
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接


