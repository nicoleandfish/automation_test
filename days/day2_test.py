from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.bing.com")

        # 等页面稳定
        page.wait_for_load_state("domcontentloaded")

        # ✅ 用 placeholder 定位（最稳）
        search_box = page.get_by_placeholder("搜索网页")
        search_box.fill("自动化测试")

        page.keyboard.press("Enter")

        page.wait_for_timeout(2000)
        page.screenshot(path="biying_result.png")

        assert "自动化" in page.title()

        browser.close()

if __name__ == "__main__":
    run_test()