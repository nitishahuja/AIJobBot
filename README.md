# Job Application Agent

The **Job Application Agent** is an automated tool designed to help job seekers streamline their job application process by automatically scraping job listings from popular platforms like **Google Jobs** and **LinkedIn**, filling out application forms, uploading resumes, and submitting job applications.

It uses **Selenium**, **undetected-chromedriver**, and **Python** to interact with the job portals, simulate user interactions, and apply for jobs using pre-stored information like resumes and login credentials.

## Features

- Scrapes job listings from **Google Jobs** and **LinkedIn**.
- Automatically applies to jobs by filling out application forms.
- Uploads resumes from a predefined location.
- Supports using an existing **Google login session** for authentication (using stored cookies).
- Customizable to add support for more job portals.
- Can use a **specific Chrome user profile** to persist session and avoid manual logins.

## Requirements

- **Python 3.8+**: Ensure you have Python 3.8 or higher installed.
- **Chrome browser**: Make sure Google Chrome is installed on your machine.
- **ChromeDriver**: The matching version of ChromeDriver must be installed (this is used by Selenium).
- **undetected-chromedriver**: A special version of the ChromeDriver used to bypass detection by some websites.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/job-application-agent.git
cd job-application-agent
```

### 2. Set up a Python virtual environment (Optional but recommended)

```bash
python3 -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### 3. Install required dependencies

Make sure you're in the project directory and have activated your virtual environment. Then, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

This will install the following dependencies:

- **undetected-chromedriver**: To avoid detection on job portals.
- **selenium**: To interact with the web browser.
- **beautifulsoup4**: For web scraping the job listings.
- **pickle**: To load cookies (for reusing Google login session).
- **webdriver-manager**: Manages ChromeDriver binaries.
- **requests**: Used for network requests.
- **python-dotenv**: To load environment variables (if needed).

### 4. Download and set up ChromeDriver

1. **Check your Chrome version**:

   - Open Google Chrome and go to **chrome://settings/help** to find your version.

2. **Download the appropriate ChromeDriver**:

   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/) and download the matching version.

3. **Place `chromedriver` in your project directory**:

   - After downloading **ChromeDriver**, place the `chromedriver` binary inside the project directory and ensure it's executable.

   For macOS/Linux, make sure to set permissions:

   ```bash
   chmod +x chromedriver
   ```

### 5. Update your Google Profile Path

1. **Find your Chrome user data directory**:
   On macOS, the default Chrome user data directory is:

   ```bash
   /Users/<your-username>/Library/Application Support/Google/Chrome
   ```

2. **Specify the path** to the **user data directory** and **profile directory** (e.g., `Default`, `Profile 1`) in the script.

---

## Configuration

You can configure the script by modifying the **profile directory** and **ChromeDriver** paths in the `main.py` file.

```python
# Example path configuration
user_data_dir = "/Users/your-username/Library/Application Support/Google/Chrome"
driver_path = "./chromedriver"  # Ensure chromedriver is in the project folder
profile_directory = "Default"  # Use the default profile or create a new profile
```

### 1. **`user-data-dir`**: The path to your **Chrome User Data** directory.

- This directory stores all your Chrome profiles and browser data.

### 2. **`profile-directory`**: The specific Chrome **profile** to use.

- **`Default`**: The default profile.
- **`Profile 1`, `Profile 2`, etc.**: Other profiles created in Chrome.

---

## Running the Script

To run the script, simply execute the following:

```bash
python main.py
```

### Steps executed by the script:

1. **Login**: The script will use your saved cookies to log in to Google via the **`user-data-dir`** and **`profile-directory`** you provided.
2. **Fetch Jobs**: It will scrape job listings from the specified website (`LinkedIn` or `Google Jobs`).
3. **Apply to Jobs**: It will navigate to the job applications and fill out the required fields, uploading your resume if necessary.
4. **Close the Browser**: Once done, the script will gracefully close the browser.

---

## Customization

### Adding More Job Portals

Currently, the scraper supports **LinkedIn** and **Google Jobs**, but you can extend it to include other job portals by following these steps:

1. Create a new scraping method for the website (e.g., **\_scrape_monster_jobs**).
2. Modify the **fetch_jobs()** method to call the new scraping function for the added website.

Example:

```python
def _scrape_monster_jobs(self, search_query, location):
    """
    Scrape job postings from Monster Jobs.
    """
    self.driver.get(f"https://www.monster.com/jobs/search?q={search_query}&where={location}")
    time.sleep(3)

    soup = BeautifulSoup(self.driver.page_source, "html.parser")
    jobs = []
    for job_card in soup.select(".job-card"):
        title = job_card.select_one(".job-title").text.strip()
        company = job_card.select_one(".company-name").text.strip()
        link = job_card.select_one("a")["href"]
        jobs.append({"title": title, "company": company, "link": link})
    return jobs
```

### Modifying the `apply_to_job` function

If the job application form has extra fields or specific formats, you can modify the **`apply_to_job()`** method to include new elements to be filled out.

---

## Troubleshooting

1. **Chrome version mismatch**: Ensure your **ChromeDriver** version matches the installed **Chrome** version. If they don’t match, download the correct version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
2. **Cookies not loading properly**: Make sure you have valid cookies saved in a `cookies.pkl` file. You can use your Chrome session to manually log in to Google and then export the cookies using browser extensions like **EditThisCookie**.

3. **Permissions**: Ensure the `chromedriver` binary has execution permissions:

   ```bash
   chmod +x chromedriver
   ```

4. **Profile directory already in use**: If you encounter errors related to the profile already being in use, try using a different profile or make sure Chrome is not running while the script is executing.

---

## Future Enhancements

- **Integration with Email/Notifications**: Send notifications when a job application is successfully submitted.
- **Job Matching Algorithm**: Automatically select jobs based on your preferences (e.g., job title, company).
- **Error Handling**: Add better error handling for cases when the web pages or forms are not found.
- **Headless Mode**: Run the browser in **headless mode** to speed up the process.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
