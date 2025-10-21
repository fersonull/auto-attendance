from time import sleep
from rich import print
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class AttendanceBot:
    BASE_URL = "https://pmftci.com/college"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        options = Options()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.tag("Logging in...")
        self.driver.get(f"{self.BASE_URL}/login-app")

        try:
            self.find_elem(By.ID, "email").send_keys(self.email)
            self.find_elem(By.ID, "password").send_keys(self.password)
            self.find_elem(By.ID, "login-btn").click()

            hasError = self.wait_to_load_elem(By.CLASS_NAME, "alert_danger", 10)

            if (hasError):
                return False

        except AttributeError:
            return False
        
        return True

    def start(self):
        sub_link_loaded = self.wait_to_load_elem(By.XPATH, f"//a[@href='{self.BASE_URL}/my-subjects']")

        if not sub_link_loaded: 
            self.tag("Failed to load subjects link.", "error")
            return

        self.tag("Fetching subjects...")
        subject_link = self.find_elem(By.XPATH, f"//a[@href='{self.BASE_URL}/my-subjects']")
        
        subject_link.click()
        self.tag("Subjects found","success")

        sleep(5)


    def find_elem(self, by, selector):
        try:
            element = self.driver.find_element(by, selector)
            return element
        except NoSuchElementException:
            self.tag(f"Element '{selector}' not found.", "error")
            return None

    def wait_to_load_elem(self, by, selector, seconds=10):
        try:
            WebDriverWait(self.driver, seconds).until(
                EC.presence_of_element_located((by, selector))
            )
            return True
        except TimeoutException:
            return False

    def curr_time(self):
        return datetime.now().strftime("%H:%M:%S")
    
    def tag(self, text="", type="default"):
        match type:
            case "success":
                print(f"[green][{self.curr_time()}][/green]: {text}")
            case "error":
                print(f"[red][{self.curr_time()}][/red]: {text}")
            case _:
                print(f"[blue][{self.curr_time()}][/blue]: {text}")

    