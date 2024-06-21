# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:13:50 2024

@author: anilk
"""
import requests
response=requests.get("https://www.naukri.com/skilllabs-overview-3442166?tab=jobs&searchId=17112769340583111&src=orgCompanyListing")
print(response.content)

#find following values and store it in datafram using beautifulsoupt
#using same link write code for scrapy
#job title, company name, experience rquired, salary, location