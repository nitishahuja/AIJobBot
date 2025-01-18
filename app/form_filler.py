from selenium import webdriver

class FormFiller:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def fill_form(self, job_link, user_data):
        self.driver.get(job_link)
        self.driver.find_element_by_name('name').send_keys(user_data['name'])
        self.driver.find_element_by_name('email').send_keys(user_data['email'])
        self.driver.find_element_by_name('resume').send_keys(user_data['resume_path'])
        self.driver.find_element_by_name('submit').click()

if __name__ == "__main__":
    filler = FormFiller("/path/to/chromedriver")
    sample_user = {"name": "John Doe", "email": "john@example.com", "resume_path": "/path/to/resume.pdf"}
    filler.fill_form("https://example-job-apply.com", sample_user)
