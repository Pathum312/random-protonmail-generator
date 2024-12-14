from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .account_details import Account_Details
from .web_scraper import Web_Scraper


class Registration_Process:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.account_details = Account_Details()
        self.full_name: str = self.account_details.get_full_name()
        self.username: str = self.account_details.get_username()
        self.password: str = self.account_details.get_password()
        self.web_scraper: Web_Scraper = Web_Scraper(driver=self.driver)

    def fill_register_form(self) -> None:
        # To set the email value, certain steps are needed:
        # First, find the iframe
        username_iframe: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.CSS_SELECTOR, value='iframe[title="Email address"]'
        )

        # Second, switch the driver focus to that iframe
        self.driver.switch_to.frame(frame_reference=username_iframe)

        # Third, find and set the value for the email as with the other input elements
        email: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.ID, value="email"
        )
        email.send_keys(self.username)

        # Finally, switch back to the default document
        self.driver.switch_to.default_content()

        # Set a password value
        password: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.ID, value="password"
        )
        password.send_keys(self.password)

        # Set a repeat-password value
        repeat_password: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.ID, value="repeat-password"
        )
        repeat_password.send_keys(self.password)

        # Click the sumbit button
        submit_button: WebElement = self.web_scraper.getClickableElement(
            timeout=10, by=By.CSS_SELECTOR, value='button[type="submit"]'
        )
        submit_button.click()

    def select_free_plan(self) -> None:
        # Click the Continue with Free button
        free_plan_button: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.XPATH, value="//button[text()='Continue with Free']"
        )
        free_plan_button.click()

        # Click the No, thanks button
        no_thanks_button: WebElement = self.web_scraper.getElement(
            timeout=10, by=By.XPATH, value="//button[text()='No, thanks']"
        )
        no_thanks_button.click()

    def set_display_name(self) -> None:
        # Set a display name value
        display_name: WebElement = self.web_scraper.getElement(
            timeout=30, by=By.ID, value="displayName"
        )
        # The display name is set by default to the username, so clear it
        display_name.clear()
        # Then set the full name as the display name
        display_name.send_keys(self.full_name)

        # Click the Continue button
        continue_button: WebElement = self.web_scraper.getElement(
            timeout=30, by=By.XPATH, value="//button[text()='Continue']"
        )
        continue_button.click()

    def skip_recovery_method(self) -> None:
        # Click the Maybe later button
        maybe_later_button: WebElement = self.web_scraper.getElement(
            timeout=50, by=By.XPATH, value="//button[text()='Maybe later']"
        )
        maybe_later_button.click()

        # Click the Confirm button
        confirm_button: WebElement = self.web_scraper.getElement(
            timeout=50, by=By.XPATH, value="//button[text()='Confirm']"
        )
        confirm_button.click()

    def get_account_details(self) -> dict[str, str]:
        return {
            "name": self.full_name,
            "username": self.username,
            "password": self.password,
        }
