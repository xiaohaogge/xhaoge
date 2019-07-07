


def login(browser):
    browser.get("https://allblue.gloryholiday.com/#/login")
    username1 = 'root'
    password1 = '123456'
    # 登录页面；
    browser.maximize_window()
    browser.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys(username1)
    browser.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(password1)
    browser.find_element_by_xpath('//span[contains(text(),"Login")]').click()
