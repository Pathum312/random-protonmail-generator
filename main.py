import sys
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, 
    QLabel, 
    QPushButton, 
    QWidget, 
    QVBoxLayout, 
    QLineEdit, 
    QGridLayout,
)
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from services.proton_register_automated import Registration_Process

class Generator(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super(Generator, self).__init__(parent=parent)
        self.setWindowTitle('Proton Mail Generator')
        
        # Status text widget
        self.status_text: QLabel = QLabel(text='Welcome :)')
        
        # Generate button used to trigger the automation script
        self.generate_button: QPushButton = QPushButton(text='Generate')
        
        self.generate_button.clicked.connect(self.generate_proton_mail)
        
        # Account detail label widgets
        self.name_label: QLabel = QLabel(text='Name:')
        self.username_label: QLabel = QLabel(text='Username:')
        self.password_label: QLabel = QLabel(text='Password:')
        
        # Account detail text edit widgets
        self.name_edit: QLineEdit = QLineEdit('Name will appear here...')
        self.username_edit: QLineEdit = QLineEdit('Username will appear here...')
        self.password_edit: QLineEdit = QLineEdit('Password will appear here...')
        
        # Grid widget to showcase the account details
        account_details_layout: QGridLayout = QGridLayout()
        # Name Label and Line Edit
        account_details_layout.addWidget(self.name_label, 0, 0)
        account_details_layout.addWidget(self.name_edit, 0, 1)
        # Username Label and Line Edit
        account_details_layout.addWidget(self.username_label, 1, 0)
        account_details_layout.addWidget(self.username_edit, 1, 1)
        # Password Label and Line Edit
        account_details_layout.addWidget(self.password_label, 2, 0)
        account_details_layout.addWidget(self.password_edit, 2, 1)
        
        # Create App Layout
        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.generate_button)
        layout.addWidget(self.status_text)
        layout.addLayout(account_details_layout)
        
        # Set the App Layout
        self.setLayout(layout)
    
    @Slot()
    def generate_proton_mail(self) -> None:
        # Website URL
        url: str = 'https://account.proton.me/mail/signup'
        
        # Opens a FireFox browser instance
        driver: WebDriver = webdriver.Firefox()
        
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
            account_details: dict[str, str] = registration_process.get_account_details()
            name: str | None = account_details.get('name')
            username: str | None = account_details.get('username')
            password: str | None = account_details.get('password')
            
            # Set name in the line edit widget
            self.name_edit.clear()
            self.name_edit.setText(name) # type: ignore
            
            # Set username in the line edit widget
            self.username_edit.clear()
            self.username_edit.setText(username) # type: ignore
            
            # Set password in the line edit widget
            self.password_edit.clear()
            self.password_edit.setText(password) # type: ignore
        finally:
            # Closes the FireFox instance
            driver.close()

if __name__ == '__main__':
    # Create the QT Application
    app: QApplication = QApplication(sys.argv)
    
    # Set applications logo
    app_logo: QIcon = QIcon('./img/logo.ico')
    app.setWindowIcon(app_logo)
    
    # Create and show the generator
    generator: Generator = Generator()
    generator.resize(500, 20)
    generator.show()
    
    # Add styling for the QT Application
    with open(file='./styles/style.qss', mode='r') as f:
        _style: str = f.read()
        app.setStyleSheet(_style)
    
    # Run the main QT Loop
    sys.exit(app.exec())
    