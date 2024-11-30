import feedparser
from bs4 import BeautifulSoup

# clean the rss response to get the required fields
def clean_jobs(job, key_mappings):
    cleaned_jobs = {}
    for key, api_key in key_mappings.items():
        value = job.get(api_key)
        if value is None:
            cleaned_jobs[key] = None
            continue
        
        if key == "description":
            parsed_description = BeautifulSoup(value, 'html.parser')
            cleaned_jobs[key] = parsed_description.get_text()
        elif key == "company":
            cleaned_jobs[key] = value.split(': ')[0] if value else None
        elif key == "position":
            cleaned_jobs[key] = value.split(': ')[1] if value else None
        elif key == "company_logo":
            cleaned_jobs[key] = value[0]['url'] if value and isinstance(value, list) and len(value) > 0 else None
        else:
            cleaned_jobs[key] = value
    return cleaned_jobs

# key_mappings - maps the key used by the rss to a single common key to use across the projct
rss_key_mapping = {
    "postedOn": "published",
    "company": "title",
    "company_logo": "media_content",
    "position": "title",
    "category": "category",
    "tags": "tags",
    "salary": "salary",
    "location": "region",
    "apply_url": "link",
    "description": "description"
}

rss_feed = feedparser.parse("https://weworkremotely.com/remote-jobs.rss")
rss_jobs = rss_feed.entries
cleaned_rss_jobs = [clean_jobs(job, rss_key_mapping) for job in rss_jobs]