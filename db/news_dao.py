# vega
# ---------------------------
# news_dao
# ---------------------------
# Administrator 2021/2/23 13:44 
# ---------------------------

from db.mysql_db import pool

class NewsDao:
    # 查询待审批的新闻
    def search_unreview_news(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select n.id,n.title,u.username,t.type ' \
                  'from t_news n inner join t_user u on n.editor_id = u.id ' \
                  'inner join t_type t on n.type_id = t.id ' \
                  'where n.state = "待审批" order by n.create_time desc limit %s,%s;'
            cursor.execute(sql,((page-1)*5,5))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 查询待审批新闻总页数
    def search_unreview_news_page_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/5) from t_news where state="待审批";'
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 更新待审批新闻为已审批
    def update_unreview_news(self,id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            con.start_transaction()
            sql = 'update t_news set state="已审批" where id=%s;'
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 查看新闻的总页数
    def search_news_page_count(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select ceil(count(*)/5) from t_news;'
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 分页查询新闻
    def search_news(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'select n.id,n.title,u.username,t.type ' \
                  'from t_news n inner join t_user u on n.editor_id = u.id ' \
                  'inner join t_type t on n.type_id = t.id ' \
                  'order by n.create_time desc limit %s,%s;'
            cursor.execute(sql,((page-1)*5,5))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

    # 删除指定的新闻
    def delete_news_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'delete from t_news where id=%s;'
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()  # 归还连接

# a = NewsDao()
# print(a.search_unreview_news(1))
# print(a.search_unreview_news(2))
