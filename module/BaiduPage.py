from module import *
from module.basepage import PageObiect

class Baidu(PageObiect):
    def __init__(self, page):
        super().__init__(page)
        self.url ="https://www.baidu.com"
        self.search_input = self.page.locator('//input[@name="wd"]')
    def baidu_search(self,search_keyword,search_resoult):
        self.navigate()
        self.search_input.fill(search_keyword)
        self.click_button("百度一下")
        expect(self.page.get_by_text(search_resoult).last).to_be_visible()