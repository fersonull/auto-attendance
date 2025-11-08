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
from app.services.DiscordWebhook import DiscordWebhook

class AttendanceBot:
    BASE_URL = "https://pmftci.com/college"

    def __init__(self, email, password):

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        self.email = email
        self.password = password

        options = Options()

        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--enable-javascript")
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)

        self.hook = DiscordWebhook()

    def login(self):
        self.tag(f"Logging in with your email: {self.email}")
        self.hook.send(f"Logging in with your email: {self.email}")
        self.driver.get(f"{self.BASE_URL}/login-app")

        try:
            self.find_elem(By.ID, "email").send_keys(self.email)
            self.find_elem(By.ID, "password").send_keys(self.password)
            login_btn = self.find_elem(By.ID, "login-btn")

            self.safe_click(login_btn)

            hasError = self.wait_to_load_elem(By.CLASS_NAME, "alert_danger", 10)

            if (hasError):
                return False
            
            self.tag("You are now logged in!", "success")
            self.hook.send("You are now logged in!")
            return True

        except AttributeError:
            return False

    def start(self, subject):
        sub_link_loaded = self.wait_to_load_elem(By.XPATH, f"//a[@href='{self.BASE_URL}/my-subjects']")

        if not sub_link_loaded: 
            self.tag("Failed to load subjects link.", "error")
            self.hook.send("Failed to load subjects link.")
            return

        self.tag("Fetching subjects...")
        self.hook.send("Fetching subjects...")
        go_to_subject_btn = self.find_elem(By.XPATH, f"//a[@href='{self.BASE_URL}/my-subjects']")
        
        self.safe_click(go_to_subject_btn)

        subjects = self.find_elems(By.XPATH, f"//a[contains(@href, '{self.BASE_URL}/view-subject-lessons/')]")

        links = [href_link.get_attribute("href") for href_link in subjects]

        if len(links) < 1:
            self.tag("No subjects found", "error")
            self.hook.send("No subjects found", "error")
            return

        self.tag(f"{len(links)} subjects found!", "success")
        self.hook.send(f"{len(links)} subjects found!")

        # print(links)

        subject_ids = [int(link.rstrip('/').split('/')[-1]) for link in links]

        for id in subject_ids:
            if id == subject["subject_id"]:
                self.tag(f"found subject: {subject["name"]}")
                self.hook.send(f"found subject: {subject["name"]}")

                scheduled_subject = self.find_elem(By.XPATH, f"//a[@href='{self.BASE_URL}/view-subject-lessons/{subject["subject_id"]}']")

                self.safe_click(scheduled_subject)

                self.tag(f"Subject {subject["name"]} loaded!", "success")
                self.hook.send(f"Subject {subject["name"]} loaded!")
                self.driver.quit()
                return
        
        self.tag(f"Subject ID: {subject["name"]} not found", "error")
        return

        # print(subject_ids)


    def find_elems(self, by, selector):
        try:
            elements = self.driver.find_elements(by, selector)
            return elements
        except (NoSuchElementException or TimeoutException):
            self.tag(f"Element '{selector}' not found.", "error")
            return None

    def find_elem(self, by, selector):
        try:
            element = self.driver.find_element(by, selector)
            return element
        except (NoSuchElementException or TimeoutException):
            self.tag(f"Element '{selector}' not found.", "error")
            return None

    def safe_click(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)


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

    