import requests
from bs4 import BeautifulSoup

# cleans the api response to better structure the db 
def clean_jobs(job, key_mappings):
    cleaned_jobs = {}
    for key, api_key in key_mappings.items():
        if key == "description":
            parsed_description = BeautifulSoup(job.get(api_key), 'html.parser')
            cleaned_jobs[key] = parsed_description.get_text()
        else:
            cleaned_jobs[key] = job.get(api_key)
    return cleaned_jobs

# key_mappings - maps the key used by the api to a single common key to use across the projct
remotive_key_mapping = {
    "postedOn": "publication_date",
    "company": "company_name",
    "company_logo": "company_logo",
    "position": "title",
    "category": "category",
    "tags": "tags",
    "salary": "salary",
    "location": "candidate_required_location",
    "apply_url": "url",
    "description": "description"
}

remotive_response = requests.get("https://remotive.com/api/remote-jobs")
remotive_jobs = remotive_response.json().get("jobs")
remotive_jobs = remotive_jobs[2:]
cleaned_remotive_jobs = [clean_jobs(job, remotive_key_mapping) for job in remotive_jobs]
