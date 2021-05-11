from behave import fixture, use_fixture
from selenium import webdriver
from po import GithubPO
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def selenium_browser_chrome(context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    context.github_po = GithubPO.GithubPO(driver)
    yield context
    driver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
