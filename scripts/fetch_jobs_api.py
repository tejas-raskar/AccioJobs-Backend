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
remoteok_key_mapping = {
    "postedOn": "date",
    "company": "company",
    "company_logo": "company_logo",
    "position": "position",
    "tags": "tags",
    "salary": "salary_min",
    "location": "location",
    "apply_url": "apply_url",
    "description": "description"
}

remotive_key_mapping = {
    "postedOn": "publication_date",
    "company": "company_name",
    "company_logo": "company_logo",
    "position": "title",
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

remoteok_response = requests.get("https://remoteok.com/api")
remoteok_jobs = remoteok_response.json()
remoteok_jobs = remoteok_jobs[1:]
cleaned_remoteok_jobs = [clean_jobs(job, remoteok_key_mapping) for job in remoteok_jobs]

# commbines jobs from both the sources into a single objects
all_jobs = cleaned_remotive_jobs + cleaned_remoteok_jobs