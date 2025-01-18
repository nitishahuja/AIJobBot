import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
from bs4 import BeautifulSoup


class JobScraper:
    def __init__(self, driver_path, user_data_dir=None, profile_dir="Default", cookies_file="cookies.pkl"):
        """
        Initialize the scraper with the provided driver path and Chrome profile.
        """
        options = uc.ChromeOptions()  # Use undetected-chromedriver

        if user_data_dir:
            # Correctly pass the user-data-dir and profile-directory as Chrome options
            options.add_argument(f"user-data-dir={user_data_dir}")  # Path to Chrome user data
            options.add_argument(f"profile-directory={profile_dir}")  # Specific profile directory

        # Start undetected ChromeDriver with the correct options
        self.driver = uc.Chrome(service=Service(driver_path), options=options)
        self.wait = WebDriverWait(self.driver, 20)  # Default wait timeout set to 20 seconds
        
        # Try loading cookies
        self._load_cookies(cookies_file)

    def login_with_google(self, job_portal_url):
        """
        Navigate to a job portal using an already logged-in Google session.
        """
        self.driver.get(job_portal_url)
        time.sleep(3)  # Wait for the page to load
        print("Navigated to job portal with your logged-in session.")

    def _load_cookies(self, cookies_file):
        """Load cookies from the file to bypass login."""
        try:
            self.driver.get("https://www.google.com")  # Navigate to a website
            with open(cookies_file, "rb") as cookies:
                cookies_data = pickle.load(cookies)
                for cookie in cookies_data:
                    self.driver.add_cookie(cookie)
            print("Cookies loaded successfully.")
        except Exception as e:
            print(f"Error loading cookies: {e}")

    def fetch_jobs(self, website, search_query, location):
        """
        Dynamically fetch jobs from the specified website.
        """
        if website == "google":
            return self._scrape_google_jobs(search_query, location)
        elif website == "linkedin":
            return self._scrape_linkedin_jobs(search_query, location)
        else:
            raise ValueError(f"Unsupported website: {website}")

    def _scrape_google_jobs(self, search_query, location):
        """
        Scrape job postings from Google Jobs.
        """
        self.driver.get(f"https://www.google.com/search?q={search_query}+jobs+in+{location}")
        time.sleep(3)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        jobs = []
        for job_card in soup.select(".BjJfJf"):
            title = job_card.select_one(".BjJfJf span").text.strip()
            company = job_card.select_one(".vNEEBe").text.strip()
            link = job_card.select_one("a")["href"]
            jobs.append({"title": title, "company": company, "link": link})
        return jobs

    def _scrape_linkedin_jobs(self, search_query, location):
        """
        Scrape job postings from LinkedIn.
        """
        self.driver.get(f"https://www.linkedin.com/jobs/search?keywords={search_query}&location={location}")
        time.sleep(3)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        jobs = []
        for job_card in soup.select(".base-card"):
            title = job_card.select_one(".base-card__full-link").text.strip()
            company = job_card.select_one(".base-search-card__subtitle").text.strip()
            link = job_card.select_one(".base-card__full-link")["href"]
            jobs.append({"title": title, "company": company, "link": link})
        return jobs

    def apply_to_job(self, job_link, resume_path, answers=None):
        """
        Navigate to a job application page and apply.
        """
        self.driver.get(job_link)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply Now')]"))).click()

        # Upload resume
        resume_upload = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        resume_upload.send_keys(resume_path)

        # Answer additional questions
        if answers:
            for question, answer in answers.items():
                question_field = self.driver.find_element(By.XPATH, f"//label[contains(text(), '{question}')]/following-sibling::input")
                question_field.send_keys(answer)

        # Submit the application
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))).click()

    def close(self):
        """
        Close the WebDriver.
        """
        self.driver.quit()
