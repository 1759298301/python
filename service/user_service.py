# vega
# ---------------------------
# user_service
# ---------------------------
# Administrator 2021/2/23 10:56 
# ---------------------------

from db.user_dao import UserDao

class UserService:
    __user_dao = UserDao()

    # 验证用户登录
    def login(self,username,password):
        result = self.__user_dao.login(username,password)
        return result

    # 验证用户身份
    def sear_user_role(self,username):
        role = self.__user_dao.search_user_role(username)
        return role
    # 添加用户
    def insert_user(self,username,password,email,role_id):
        self.__user_dao.insert_user(username,password,email,role_id)
    # 验证用户名
    def search_username(self):
        username = self.__user_dao.search_username()
        return username
    # 查看用户表的总页数
    def search_user_page_count(self):
        page_count = self.__user_dao.search_user_page_count()
        return page_count
    # 分页查询用户
    def search_user(self,page):
        result = self.__user_dao.search_user(page)
        return result
    # 修改用户信息
    def update_user_by_username(self,username,password,email,role_id,old_username):
        self.__user_dao.update_user_by_username(username,password,email,role_id,old_username)

