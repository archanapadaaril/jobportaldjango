from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category,Job,JobDetails,apply,Jobpost,Contact


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','is_active','is_featured')
    list_editable=('is_active','is_featured')
    list_filter=('is_active','is_featured')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category,CategoryAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display=('title','slug','company_logo','location','job_nature','salary','category','Date_line','is_active','is_featured')
    list_editable=('company_logo','salary','category','is_active','is_featured')
    list_filter=('is_active','is_featured')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Job,JobAdmin)

class JobDetailsAdmin(admin.ModelAdmin):
    list_display=('job','company_logo','location','job_nature','salary','job_description','responsibilities','qualifications','companywebsite','companyemail','contact','experience','published_on','Date_line')
    list_editable=('company_logo','location','job_nature','salary','qualifications','companywebsite','contact','experience',)
    list_filter=('published_on','Date_line')
admin.site.register(JobDetails,JobDetailsAdmin)

class applyAdmin(admin.ModelAdmin):
    list_display=('name','email','address','contact','state','city','resume')
    list_editable=('email','address','contact','state','city','resume')
admin.site.register(apply,applyAdmin)

class JobpostAdmin(admin.ModelAdmin):
    list_dispaly=('title','company_logo','location','job_nature','salary','Date_line','job_nature')   
admin.site.register(Jobpost,JobpostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
admin.site.register(Contact,ContactAdmin)