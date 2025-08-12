from pyexpat import model
from turtle import mode, title
from django.db import models
"""
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field() #e.g., Addis Ababa, Remote
    date_posted = scrapy.Field()
    employment_type = scrapy.Field() #e.g., Full-time, Part-time, Contract
    experience_level = scrapy.Field() #e.g., Junior, Mid-level, Senior  
    salary = scrapy.Field()
    deadline = scrapy.Field()
    category = scrapy.Field() #the category of the job
    source = scrapy.Field() #the source of the job posting
    url = scrapy.Field()s
    
    
     {
        "title": "Software Developer - Python",
        "company": "INSPYR Solutions",
        "location": "Austin, TX",
        "url": "https://www.linkedin.com/jobs/view/software-developer-python-at-inspyr-solutions-4277219739?position=11&pageNum=0&refId=BHknxtGq3sgdjs6vk7ncjw%3D%3D&trackingId=Ese6nvH3x1Pn8NWS3EpT5w%3D%3D"
    },
"""
class job(models):
    title = models.CharField(max_length= 100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_posted = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    
    class Meta:
        abstract = True
        

class Local(job):
    

    