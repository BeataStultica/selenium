import po.DefaultPO as DefPo
from selenium.webdriver.common.keys import Keys


class GithubPO(DefPo.DefaultPO):
    def get_github(self):
        self.driver.get("https://github.com/")

    def search(self, value):
        search = self.driver.find_element_by_name('q')
        search.send_keys(value) # "selenium python"
        search.send_keys(Keys.RETURN)

    def tags(self):
        tag = self.driver.find_elements_by_class_name("topic-tag")
        return [i.text for i in tag]

    def star_click(self):
        self.driver.find_element_by_css_selector(".starring-container > a").click()

    def get_title(self):
        return self.driver.find_element_by_css_selector('h1').text

    def sign_in(self, login, password):
        username = self.driver.find_element_by_name('login')
        username.send_keys(login)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def get_after_login_error(self):
        return self.driver.find_element_by_xpath('//*[@id="login"]/p').text
