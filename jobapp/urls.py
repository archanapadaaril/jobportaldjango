from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('about',views.about,name='about'),
    path('category',views.category,name='category'),
    path('contact',views.contact,name='contact'),
    path('job-detail',views.jobdetail,name='jobdetail'),
    path('job-list',views.joblist,name='joblist'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('jobpost',views.jobpostpage,name='jobpost'),
    path('apply',views.applypage,name='apply'),
    path('jobpostlist',views.jobpostlist,name='jobpostlist')


    ]