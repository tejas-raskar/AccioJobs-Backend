import os
import json
import psycopg2

connection_string = os.getenv('DATABASE_URL')
# Load jobs
with open('jobs.json', 'r') as f:
    jobs = json.load(f)

# Connect to database
conn = psycopg2.connect(connection_string)
cur = conn.cursor()

# Get existing job IDs
cur.execute("SELECT position, company FROM jobs")
existing_jobs = {f"{row[0]}_{row[1]}" for row in cur.fetchall()}

# Insert new jobs and track them
new_jobs = []
for job in jobs[:115]:
    job_key = f"{job['position']}_{job['company']}"
    if job_key not in existing_jobs:
        cur.execute("INSERT INTO jobs (posted_on, company, company_logo, position, category, tags, salary, location, apply_url, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;", (job['postedOn'], job['company'], job['company_logo'], job['position'], job['category'], job['tags'], job['salary'], job['location'], job['apply_url'], job['description']))
        job_id = cur.fetchone()[0]
        new_jobs.append({**job, 'id': job_id})

# Process relevant jobs for users
if new_jobs:
    cur.execute("SELECT u.id, u.intrested_categories FROM users u")
    users = cur.fetchall()
    
    for user_id, categories in users:
        user_categories = set(categories)
        relevant_jobs_for_user = []
        
        for job in new_jobs:
            job_category = job['category']
            if job_category in user_categories:
                cur.execute("""
                    INSERT INTO relevant_jobs (user_id, job_id, resume)
                    VALUES (%s, %s, %s)
                    RETURNING id
                """, (user_id, job['id'], None))  # Setting resume as NULL initially
                
                relevant_jobs_for_user.append({
                    'job_id': job['id'],
                    'position': job['position'],
                    'company': job['company']
                })

        # You might want to store this information for notifications
        if relevant_jobs_for_user:
            print(f"Found {len(relevant_jobs_for_user)} relevant jobs for user {user_id}")

conn.commit()
cur.close()
conn.close()

# Save new jobs for notification
with open('new_jobs.json', 'w') as f:
    json.dump(new_jobs, f)