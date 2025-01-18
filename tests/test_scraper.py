import pytest
from app.scraper import JobScraper

@pytest.fixture
def scraper():
    # Pass the correct chromedriver path
    return JobScraper(driver_path="./chromedriver")

def test_fetch_jobs(scraper):
    """Test if the scraper fetches jobs."""
    jobs = scraper.fetch_jobs(
        search_query="Software Engineer",
        location="United States",
        job_board_url="https://www.indeed.com"
    )
    assert len(jobs) > 0, "No jobs were fetched."
    assert "title" in jobs[0], "Job title is missing."
    scraper.close()
