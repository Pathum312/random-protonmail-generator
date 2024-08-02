from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

class Web_Scraper:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def elementDetails(self, element: WebElement) -> None:
        # Finding the element's attributes and properties
        element_tag_name: str = element.tag_name
        element_id: str | None = element.get_attribute(name='id') # type: ignore
        element_for: str | None = element.get_attribute(name='for') # type: ignore
        element_class: str | None = element.get_attribute(name='class') # type: ignore
        element_value: str | None = element.get_attribute(name='value') # type: ignore
        element_text: str = element.text
    
        print('')
        print(f'Tag Name: <{element_tag_name}>')
        print(f'ID: {element_id}')
        print(f'For: {element_for}')
        print(f'Class: {element_class}')
        print(f'Value: {element_value}')
        print(f'Text: {element_text}')
        print('')

    def showElementDetails(self, timeout: float, value: str) -> None:
        # Finding the requested elements
        elements: list[WebElement] = WebDriverWait(driver=self.driver, timeout=timeout).until(
            method=EC.presence_of_all_elements_located(locator=(By.TAG_NAME, value))
        )
    
        for element in  elements:
            self.elementDetails(element=element)

    def getElement(self, timeout: float, by: str, value: str) -> WebElement:
        # Finding a visible element in the document
        element: WebElement = WebDriverWait(driver=self.driver, timeout=timeout).until(
            method=EC.visibility_of_element_located(locator=(by, value))
        )
    
        return element