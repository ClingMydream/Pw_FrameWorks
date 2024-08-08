from module import *
from module.infocloud_login import Login


def test_login(page:Page):
    login = Login(page)
    login.infocloud_login_click("119509","XJL_info","@Aa1234567")
    login.infocloud_login_中间页()
