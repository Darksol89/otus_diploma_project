import time


def test_get_url(browser_driver, get_url, login_to_youtrack):
    assert browser_driver.title == 'YouTrack Dashboard'
