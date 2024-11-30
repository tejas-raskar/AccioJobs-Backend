import json
from scripts.fetch_jobs_api import cleaned_remotive_jobs as api_jobs
from scripts.fetch_jobs_rss import cleaned_rss_jobs as rss_jobs

combined_jobs = api_jobs + rss_jobs

unique_jobs = {}
for job in combined_jobs:
    key = f"{job['position']}_{job['company']}"
    if key not in unique_jobs:
        unique_jobs[key] = job

final_jobs = list(unique_jobs.values())

# Save to output
with open('jobs.json', 'w') as f:
    json.dump(final_jobs, f)