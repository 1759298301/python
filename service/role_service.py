# vega
# ---------------------------
# role_service
# ---------------------------
# Administrator 2021/2/23 19:56 
# ---------------------------
from db.role_dao import RoleDao

class RoleService:
    __role_dao = RoleDao()
    # 查询所有权限
    def search_role(self):
        result = self.__role_dao.search_role()
        return result

