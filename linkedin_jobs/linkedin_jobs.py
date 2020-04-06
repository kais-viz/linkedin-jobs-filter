# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:11:51 2020

@author: Ice
"""

import json
import sys
import re
import os
from urllib.parse import urlencode
from datetime import datetime
import urllib

def get_company_ids(data):
    company_name = {}
    for job in data['included']:
        if ("logo" in job and "name" in job):
            company_id = int(re.search(r'\d+', job['entityUrn']).group())
            company_name[company_id] = job['name']
    return company_name

def order_jobs(jobs, order):
    if (order == "newest"):
        return sorted(jobs, key = lambda i: i['listedAt'],reverse=True)
    else:
        return sorted(jobs, key = lambda i: i['listedAt'])

def get_company_name(job, comp_ids):
    if (job['companyDetails'].get("company")):
        company_id = int(re.search(r'\d+', job['companyDetails'].get("company")).group())
        return comp_ids.get(company_id)
    else:
        return job['companyDetails']['companyName']

def get_apply_method(job):
    if (job['applyMethod'].get('companyApplyUrl')):
        return job['applyMethod']['companyApplyUrl']
    elif(job['applyMethod'].get('easyApplyUrl')):
        return job['applyMethod']['easyApplyUrl']
    else:
        job_id = int(re.search(r'\d+', job['entityUrn']).group())
        return f"https://www.linkedin.com/jobs/view/{job_id}"
    
def get_jobs_list(jobs, order = "newest"):
    comp_ids = get_company_ids(jobs)
    clean_jobs = {}
    clean_jobs['keywords'] = jobs['data']['metadata']['keywords']
    clean_jobs['location'] = jobs['data']['metadata']['locationInfo']['location']
    clean_jobs['geoUrn'] = jobs['data']['metadata']['locationInfo']['geoUrn']
    clean_jobs['paging'] = jobs['data']['paging']
    
    retrieved_jobs = []
    for job in jobs['included']:
        if "applyMethod" in job:
            temp = {}
            temp['title'] = job['title']
            temp['location'] = job['formattedLocation']
            temp['entityUrn'] = job['entityUrn']
            temp['listedDate'] = datetime.utcfromtimestamp(job['listedAt']//1000).strftime('%Y-%m-%d %H:%M:%S')
            temp['listedAt'] = job['listedAt']
            temp['expireAt'] = job['expireAt']
            temp['companyName'] = get_company_name(job, comp_ids)
            temp['applyMethod'] = get_apply_method(job)
            retrieved_jobs.append(temp)
    
    retrieved_jobs = order_jobs(retrieved_jobs, order)
    clean_jobs['jobs'] = retrieved_jobs
#     print(json.dumps(temp, indent=1))
    return clean_jobs


