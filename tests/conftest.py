import pytest
from selene import browser
from saucedemo_tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
def settings_browser():
    browser.config.base_url = 'https://Saucedemo.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
