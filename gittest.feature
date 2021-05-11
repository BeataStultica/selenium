Feature: search on github 'webdriver python' and login
  Scenario: search selenium python github
    Given The Github page is displayed
    When I have entered "webdriver python" in github search
    Then tags contains "python", "webdriver" and "selenium"
  Scenario: login
    Given click the star
    When title is "Sign in to GitHub"
    And I enter the "username" and "password"
    Then error contain "There have been several failed attempts to sign in from this account or IP address. Please wait a while and try again later."