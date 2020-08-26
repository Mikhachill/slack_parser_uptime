from selenium.webdriver.common.by import By


class SlackPageLocators():
    WORK_ZONE_INSERT = (By.CSS_SELECTOR, "input#domain")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    SIGN_WITH_GOOGLE_BUTTON = (By.CSS_SELECTOR, "#index_google_sign_in_with_google")

    INSERT_MAIL = (By.CSS_SELECTOR, "input[type='email']")
    DALEE = (By.CSS_SELECTOR, "div.VfPpkd-RLmnJb")

    INSERT_PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    DALEE2 = (By.CSS_SELECTOR, "div.qhFLie>div")

    INFRA_GROUP = (By.CSS_SELECTOR, "span[data-qa='channel_sidebar_name_infra-notifications']")
    # span[data-qa="channel_sidebar_name_infra-notifications"]
    TO_DAY = (By.CSS_SELECTOR, "button.c-button-unstyled.c-message_list__day_divider__label__pill")

    SPECIFIC_DATE = (By.CSS_SELECTOR, "button.c-button-unstyled.c-menu_item__button.c-menu_item__button--with_submenu")

    BUTTON_2020 = (By.CSS_SELECTOR, "button.c-button-unstyled.c-button-unstyled.c-calendar_view_header__title_btn")

    JANUARY = (By.CSS_SELECTOR,
               "button.c-button-unstyled.c-button-unstyled.c-mini_calendar__month_button.c-mini_calendar__month_1")

    FIRST = (By.CSS_SELECTOR, "button[aria-label='1, January 2020, Wednesday']")

    SCROLL_BAR = (By.CSS_SELECTOR, "div.c-scrollbar__bar")

    MAIN_SCROLL_BAR = (By.CSS_SELECTOR, "div[role='list']>div.c-scrollbar__hider+div>div.c-scrollbar__bar")

    DATA_FOR_PARS = (By.CSS_SELECTOR, "div[aria-expanded='false'].c-virtual_list__item")

    DATA_XPATH = (By.XPATH,
                  "//div[@class='c-virtual_list c-virtual_list--scrollbar c-message_list c-scrollbar c-scrollbar--fade']/div/div/div[@data-qa='slack_kit_list']/div[4]")

    # DAY=div.c-virtual_list__item+div.c-virtual_list__sticky_container+div.c-virtual_list__item
