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
class job(models.Model):
    action_choices = (
      (  "","New"),
      (  "applied","Applied"),
        ("not_interested","Not Interested"),
        
    )
    employment_type_choices = (
      (  "","--"),
        ("part_time","Part-time"),
        ("contract","Contract"),
        ("remote","Remote"),
        ("internship","Internship"),
        ("full_time","Full-time"),

    )
    title = models.CharField(max_length= 100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_posted = models.DateField(null=True)
    employment_type = models.CharField(max_length=100,choices=employment_type_choices)
    experience_level = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    deadline = models.DateField()
    category = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    action = models.CharField(max_length=100, choices=action_choices, )
    
    
    class Meta:
        abstract = True
        

class Local(job):
    pass
class International(job):
    pass

    