# vega
# ---------------------------
# user_dao
# ---------------------------
# Administrator 2021/2/22 23:09 
# ---------------------------
from db.mysql_db import pool

class UserDao:
    # 验证用户登录
    def login(self,username,password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select count(*) from t_user where username=%s and aes_decrypt(unhex(password),"123")=%s'
            cursor.execute(sql,(username,password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 验证用户名
    def search_username(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select username from t_user'
            cursor.execute(sql)
            username = cursor.fetchall()
            return username
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 验证用户角色
    def search_user_role(self,username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select r.role from t_user u inner join t_role r on u.role_id = r.id where u.username = %s;'
            cursor.execute(sql,[username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接
    # 添加用户
    def insert_user(self,username,password,email,role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'insert into t_user(username,password,email,role_id) values(%s,HEX(AES_ENCRYPT(%s' \
                  ',"123")),%s,%s)'
            cursor.execute(sql,(username,password,email,role_id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 查看用户表的总页数
    def search_user_page_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/5) from t_user;'
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 分页查询用户
    def search_user(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select u.username,u.email,r.role from t_user u inner join t_role r on u.role_id = r.id limit %s,%s;'
            cursor.execute(sql,((page-1)*5,5))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 修改用户信息
    def update_user_by_username(self,username,password,email,role_id,old_username):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'update t_user set username=%s,password=HEX(AES_ENCRYPT(%s,"123")),email=%s,role_id=%s ' \
                  'where username =%s; '
            cursor.execute(sql,(username,password,email,role_id,old_username))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接


