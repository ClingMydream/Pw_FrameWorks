import pytest
from playwright.sync_api import Page, expect


def test_pw_action(page: Page):
    page.goto("/demo/button")
    page.wait_for_timeout(2_000)
    page.get_by_text("点击我试试1").dblclick()
    expect(page.get_by_text("点击成功1")).to_be_visible()

@pytest.mark.only
# 仅让此用例执行 命令行:pytest -m only pw_pytest_fixtrue.py
def test_pw_notification__message(page: Page):
    # 代表所有网络请求在500毫秒之内没有新的请求才推出goto这个操作
    page.goto("/demo/button",wait_until="networkidle")
    # page.wait_for_timeout(3_000)
    page.get_by_text("点击我试试2").click()
    expect(page.get_by_text("点击成功2!")).to_be_visible()



def test_pw2_action(page: Page):
    page.goto("/demo/button")
    page.wait_for_timeout(2_000)
    page.get_by_text("点击我试试1").dblclick()
    expect(page.get_by_text("点击成功1")).to_be_visible()


