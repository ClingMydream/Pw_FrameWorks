from playwright.sync_api import sync_playwright,expect

def pw1_baidu():
    with sync_playwright() as pw:
        # pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.baidu.com')
        page.locator('//input[@name="wd"]').fill("palywright")
        page.get_by_text("百度一下").click()
        expect(page.get_by_text("http://github.com/microsoft/palywright"))
        pw.stop()

def pw2_baidu():
        # pw层 最底层启动层
        pw = sync_playwright().start()
        # 浏览器层,定义启用什么浏览器
        browser = pw.chromium.launch(headless=False)
        # 上下文层,对应需要测试的上下文
        context = browser.new_context()
        # 页面层,根据上下文对页面的操作
        page = context.new_page()
        page.goto('https://www.baidu.com')
        page.locator('//input[@name="wd"]').fill("palywright")
        page.get_by_text("百度一下").click()
        expect(page.get_by_text("http://github.com/microsoft/palywright"))
        pw.stop()

pw1_baidu()
pw2_baidu()