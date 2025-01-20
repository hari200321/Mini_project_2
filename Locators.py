"""
Locators.py
which contains all locators needed for the program to automate
"""

class TestLocators:
    username_locator = "username"
    password_locator = "password"
    submit_locator = "//button[@type='submit']"
    logout_locator = "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p"
    logout_locator2 = "//a[text()='Logout']"
    admin_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text() = 'Admin']"
    pim_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']"
    leave_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Leave']"
    time_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Time']"
    recruitment_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Recruitment']"
    my_info_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='My Info']"
    performance_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Performance']"
    dashboard_locator = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='Dashboard']"

    select_admin_locator = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    add_locator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    user_role = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i"
    ess_locator = "//span[text()='ESS']"
    status_locator = "//div[@class='oxd-select-text-input' and text()='-- Select --']"
    enable_locator = "//span[text()='Enabled']"
    enter_password_locator = "(//input[@class='oxd-input oxd-input--active' and @type = 'password'])[1]"
    employee_name_locator  =  "//input[@placeholder = 'Type for hints...']"
    username2_locator = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    employee_name_selector_locator = "//span[text()='sampleAA testBB userCC']"
    enter_confirm_password_locator = "(//input[@class='oxd-input oxd-input--active' and @type = 'password'])[2]"
    save_locator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"


