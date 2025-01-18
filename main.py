from app.scraper import JobScraper

def main():
    # Path to your Chrome user data directory
    user_data_dir = "/Users/nitishahuja/Library/Application Support/Google/Chrome"
    driver_path = "./chromedriver"  # Path to your chromedriver

    # Specify a new profile directory to avoid conflicts, use "Default" or any other profile
    profile_directory = "Default"  # This can be "Profile 1", "Profile 2", or "Default"

    # Initialize the scraper with your Chrome profile
    scraper = JobScraper(driver_path=driver_path, user_data_dir=user_data_dir, profile_dir=profile_directory)

    # Login to a job portal (no manual login needed)
    job_portal_url = "https://www.linkedin.com/"
    scraper.login_with_google(job_portal_url)

    # Fetch jobs from LinkedIn
    linkedin_jobs = scraper.fetch_jobs(website="linkedin", search_query="Frontend Developer", location="San Francisco")
    print("LinkedIn Jobs:", linkedin_jobs)

    # Apply to a job
    if linkedin_jobs:
        job_to_apply = linkedin_jobs[0]  # Apply to the first job
        scraper.apply_to_job(job_to_apply["link"], resume_path="/path/to/your/resume.pdf")

    # Close the scraper
    scraper.close()

if __name__ == "__main__":
    main()
