from module import *
from module.creating_applications import Creating_Applications
from module.infocloud_login import Login


def test_login(page:Page):
    login = Login(page)
    login.infocloud_login_click("119509","XJL_info","@Aa1234567")
    login.infocloud_login_中间页()

def test_Goto_应用中心(page:Page):
    creat = Creating_Applications(page)
    creat.goto_应用中心()
    creat.空白创建()