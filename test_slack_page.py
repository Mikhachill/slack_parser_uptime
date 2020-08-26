from .pages.slack_page import SlackPage

import pytest
import time


def test_guest_cant_see_success_message(browser):
    link = "https://app.slack.com/client/__"
    page = SlackPage(browser, link)
    page.open()
    time.sleep(15)

    page.registration('work-zone', 'mail', 'password')
    page.data_for_pars()

    time.sleep(6)
