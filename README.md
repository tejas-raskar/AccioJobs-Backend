# 🌟 What is AccioJobs?
AccioJobs is an open source, AI powered job board that not only curates jobs from various sources and RSS feeds, but also creates customizable personalized resumes, and facilitates a one-click option to apply on the respective websites.  

**Key Features:**
- **Access Thousands of Remote Jobs Daily**: Our AI-powered platform continuously scans and aggregates remote positions from top companies worldwide, ensuring you never miss your perfect opportunity.
- **AI-Powered Resume Optimization**: Stand out from the crowd with tailored resumes. Our AI analyzes each job posting and customizes your resume to highlight relevant skills and experience, maximizing your chances of success.
- **Optimized Resume Customizability**: Our AI-powered platform not only creates an optimized resume but also allows user to modify the resume with a nice UI and without downloading a single file! 
- **Apply with One Click**: Say goodbye to repetitive applications. Our intelligent automation handles the entire process, from form filling to submission, saving you countless hours.

The rest of the project repos can be found here
- AccioJobs-Frontend - https://github.com/tejas-raskar/AccioJobs-Frontendv2/tree/master
- AccioJobs-ResumeBuilder - https://github.com/ayushjrathod/Acciojobs-Frontend2
- AccioJobs-ML - https://github.com/parth10-1/AccioJobs-ML

- Check demo video here: https://drive.google.com/file/d/1CHs9q_ushwRIRxTPRLpcSCy5jtRjqu60/view?usp=drive_link

---

### 🚀 AccioJobs-Backend
AccioJobs-Backend is the backend service for the AccioJobs project. Its main objective is to fetch job listings from various APIs like Remotive and RemoteOK, as well as from various RSS feeds. The collected data is then combined and pushed to the database.

The `kestra.yaml` file contains the workflow that clones the scripts on a docker container, runs them and generates a `jobs.json` containing the newly fetched jobs. We iterate through the `jobs.json` and the DB to filter out 'new' jobs that are not already present in the database. This are stored in a `new_jobs.json`. 

We iterate through this `new_jobs.json` and check if any users prefered category matches with these jobs. If yes, we post the relevant jobs to the database from where the ML flow is triggered to create a personalised resume.

if any of these tasks fails, a slack message is posted to notify the developers.

### Features
- Fetch jobs from Remotive API
- Fetch jobs from RemoteOK API
- Fetch jobs from various RSS feeds
- Combine and store job data in the databas
- Slack notifications for errors/alerts/success.

### License
This project is licensed under the GPL-3.0 License.
