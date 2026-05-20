from pom.google_home import GoogleHome
import time


def test_google_search(page):
    page.locator(GoogleHome.text_search_box).click()
    page.locator(GoogleHome.text_search_box).fill("hello")
    # page.locator("textarea[name='q']").click()
    # page.locator("textarea[name='q']").fill("hello")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    time.sleep(5)
    assert "hello" in page.title().lower()

def test_iframe(page):
    page.locator('//a[.="JavaScript Dialogs"]//following::span[@title="Debugging software licenses"]').click()
    page.wait_for_load_state("networkidle")
    page.frame_locator('iframe[name="aswift_0"]').locator('//a[.="cyara.com"]').click()
    page.wait_for_load_state("networkidle")
    time.sleep(20)

