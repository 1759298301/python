# vega
# ---------------------------
# new_service
# ---------------------------
# Administrator 2021/2/23 13:59 
# ---------------------------

from db.news_dao import NewsDao

class NewsService:
    __news_dao = NewsDao()

    # 查询待审批的新闻
    def search_unreview_news(self,page):
        result = self.__news_dao.search_unreview_news(page)
        return result
    # 查询待审批新闻总页数
    def search_unreview_news_page_count(self):
        count = self.__news_dao.search_unreview_news_page_count()
        return count
    # 更新待审批新闻为已审批
    def update_unreview_news(self,id):
        self.__news_dao.update_unreview_news(id)
    # 查看新闻的页数
    def search_news_page_count(self):
        count = self.__news_dao.search_news_page_count()
        return count
    # 分页查询新闻
    def search_news(self, page):
        result = self.__news_dao.search_news(page)
        return result
    # 删除指定的新闻
    def delete_news_by_id(self,id):
        self.__news_dao.delete_news_by_id(id)

