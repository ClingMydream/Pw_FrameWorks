from module import *
from module.basepage import PageObiect

class Login(PageObiect):
    def __init__(self, page):
        super().__init__(page)
        self.url ="https://dpp-uat.infocloud.cc/#/login"
        self.infocloud_number   = self.page.get_by_placeholder("请输入企业编号")
        self.infocloud_user     = self.page.get_by_placeholder("请输入登录名/手机号")
        self.infocloud_password = self.page.get_by_placeholder("请输入登录密码")

    def infocloud_login_click(self,number_input,user_input,password_input):
        self.goto_page()
        self.infocloud_number.fill(number_input)
        self.infocloud_user.fill(user_input)
        self.infocloud_password.fill(password_input)
        self.click_button("登录")
        expect(self.page.get_by_text("暂不处理").last).to_be_visible()

    def infocloud_login_中间页(self):
        self.page.get_by_text("暂不处理").click()
        self.page.get_by_text("数字化生产平台").wait_for(state="visible")
        expect(self.page.get_by_text("数字化生产平台")).to_be_visible()
