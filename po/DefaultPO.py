class DefaultPO:
    def __init__(self, driver):
        self.driver = driver

    def get_page_source(self):
        return self.driver.page_source
