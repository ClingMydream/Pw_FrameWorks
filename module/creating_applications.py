from module import *
from module.basepage import PageObiect

class Creating_Applications(PageObiect):
    def __init__(self,page):
        super().__init__(page)
        self.url ="https://bizpc-uat.infocloud.cc/base-editor-component/#/platform/home/index"
    def goto_应用中心(self):
        self.goto_page()
        self.click_button("应用中心")
        expect(self.page.get_by_text("我的应用列表")).to_be_visible()

    def 空白创建(self):
        self.click_button("创建应用")
        expect(self.page.get_by_role("dialog")).to_be_visible()