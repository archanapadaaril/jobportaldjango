from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=150,verbose_name="Category Title")
    slug=models.SlugField(max_length=55,verbose_name="Category Slug")
    vacancy=models.PositiveIntegerField()
    is_active=models.BooleanField(verbose_name="Is Active?")
    is_featured=models.BooleanField(verbose_name="Is Featured?")

    def __str__(self):
        return self.title
    

class Job(models.Model):
    title=models.CharField(max_length=150,verbose_name="job Title")   
    slug=models.SlugField(max_length=160,verbose_name="job slug")
    company_logo=models.ImageField(upload_to='Job',blank=True,null=True,verbose_name="company_logo") 
    location=models.CharField(max_length=200,null=True)
    job_nature=models.CharField(max_length=200,null=True)
    salary=models.IntegerField()    
    category=models.ForeignKey(Category,verbose_name="job_category",null=True,on_delete=models.CASCADE)
    Date_line=models.CharField(max_length=20)
    is_active=models.BooleanField(verbose_name="Is Active",null=True)
    is_featured=models.BooleanField(verbose_name="Is Featured",null=True)


    def __str__(self): 
        return self.title
    

    
class JobDetails(models.Model):
    job=models.ForeignKey(Job,null=True,verbose_name="job_title",on_delete=models.CASCADE)
    company_logo=models.ImageField(upload_to='JobDetails',blank=True,null=True,verbose_name="company_logo") 
    location=models.CharField(max_length=100,null=True)
    job_nature=models.CharField(max_length=100)
    salary=models.IntegerField()
    job_description=models.TextField(max_length=250)
    responsibilities=models.TextField(max_length=250)
    qualifications=models.CharField(max_length=250)
    companywebsite=models.CharField(max_length=200)
    companyemail=models.EmailField(max_length=200)
    contact=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    Date_line=models.CharField(max_length=30)
    published_on=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.location

class apply(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    resume=models.FileField()

    def __str__(self):
        return self.name

class Jobpost(models.Model):
    title=models.CharField(max_length=100,null=True)
    company_logo=models.ImageField(upload_to='Jobpost',blank=True,null=True,verbose_name="company_logo") 
    location=models.CharField(max_length=100,null=True)
    job_nature=models.CharField(max_length=100)
    salary=models.IntegerField()
    Date_line=models.CharField(max_length=30)
    job_nature=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
class Contact(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.TextField(max_length=200,null=True)
    message=models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name