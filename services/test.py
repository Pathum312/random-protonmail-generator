from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from proton_register_automated import Registration_Process

def main() -> None:
    # FireFox instance opens the provided URL
    driver.get(url=url)
    
    try:
        # Initialize the registration process by passing the webdriver to the class
        registration_process: Registration_Process = Registration_Process(driver=driver)
        
        # Automating the registration process for protonmail takes several steps:
        # Firstly, fill the proton registration form and submit the form
        registration_process.fill_register_form()
        
        # Secondly, select the free plan
        registration_process.select_free_plan()
        
        # Since, automating the captcha verification is againt TOS, so do it manually :(
        
        # Thirdly, set the display name
        registration_process.set_display_name()
        
        # Finally, skip the recovery method
        registration_process.skip_recovery_method()
        
        # Print the account details
        registration_process.get_account_details()
    finally:
        # Closes the FireFox instance
        driver.close()

if __name__ == '__main__':
    # Website URL
    url: str = 'https://account.proton.me/mail/signup'
    
    # Opens a FireFox browser instance
    driver: WebDriver = webdriver.Firefox()
    
    # Open the website in the browser and finish signing up
    main()

    