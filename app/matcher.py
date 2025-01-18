import yaml

class JobMatcher:
    def __init__(self, user_profile_path):
        with open(user_profile_path, 'r') as file:
            self.user_profile = yaml.safe_load(file)

    def match_jobs(self, jobs):
        keywords = self.user_profile['skills']
        matched_jobs = [
            job for job in jobs
            if any(keyword.lower() in job['title'].lower() for keyword in keywords)
        ]
        return matched_jobs

if __name__ == "__main__":
    matcher = JobMatcher("config/user_profile.yaml")
    sample_jobs = [
        {"title": "Python Developer", "company": "Tech Corp", "link": "example.com/job1"},
        {"title": "Java Engineer", "company": "Code Ltd", "link": "example.com/job2"}
    ]
    matched = matcher.match_jobs(sample_jobs)
    print(matched)
