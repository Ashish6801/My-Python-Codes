from bs4 import BeautifulSoup # For parsing HTML and XML documents
import requests # For making HTTP requests
import time # For time related operations

urls = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
def findJobs():
	count = 0 # Initialize job count to zero
	html_text = requests.get(urls).text # Get the HTML content of the page
	soup = BeautifulSoup(html_text, 'lxml') # Parse the HTML content using BeautifulSoup
	
	# Find all the job listings in the HTML content
	jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

	with open(f'posts/saved.txt','w') as f:  # Open the file to save job listings
    		# Loop through each job listing and extract relevant information
    		for index, job in enumerate(jobs):
        		location = job.find('ul', class_="top-jd-dtl clearfix").span.text
        		skills = job.find('ul', class_="list-job-dtl clearfix").span.text
        		company = job.find('h3', class_="joblist-comp-name").text
        		link = job.find('header', class_="clearfix").h2.a['href']

        		if True:
            			count += 1  # Increment job count
            			# Write job information to file
            			f.write(f"Company: {company.strip().replace('(More Jobs)','')}\n")
            			f.write(f"Location: {location.strip()}\n")
            			f.write(f"Skills: {skills.strip()}\n")
            			f.write(f"Link: {link}\n\n")

	return count

print(f'Fetching Data from\n{urls}\n.')
x = findJobs()
print(f'{x} new jobs updated.')
