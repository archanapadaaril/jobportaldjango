from django.shortcuts import render,redirect
from .forms import SignupForm,SigninForm
from .models import Category,Job,JobDetails,apply,Jobpost,Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect("/")
            messages.success(request,"User saved")
            
        else:
            messages.error(request,"Error in form")

    else:
        form=SignupForm()
    context={"form":form}
    return render(request,'signup.html',context)

def signin(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        
        username=form["username"].value()
        password=form["password"].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect("jobpost.html")
        else:
            messages.error(request,"Invalid Username or Password")
    else:
        form=SigninForm()
    context={"form":form}
    return render(request,'signin.html',context)


def about(request):
    return render(request,'about.html')

def category(request):
    category=Category.objects.filter(is_active=True)
    return render(request,'category.html',{'category':category})

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Contact(name=name,email=email,subject=subject,message=message).save()
    return render(request,'contact.html')

def jobdetail(request):
    jobdet=JobDetails.objects.all()   
    return render(request,'job-detail.html',{'jobdet':jobdet})


def joblist(request):
    joblist=Job.objects.filter(is_active=True)
    return render(request,'job-list.html',{'joblist':joblist})

@login_required
def jobpostpage(request):
    if request.method=='POST':
        title=request.POST.get('title')
        company_logo=request.POST.get('company_logo')
        location=request.POST.get('location')
        salary=request.POST.get('salary')
        job_nature=request.POST.get('job_nature')
        Date_line=request.POST.get('Date_line')
        Jobpost(title=title,company_logo=company_logo,salary=salary,Date_line=Date_line,job_nature=job_nature,location=location).save()       
    return render(request,'jobpost.html')

def jobpostlist(request):
    post=Jobpost.objects.all()
    return render(request,'jobpostlist.html',{'post':post})

def testimonial(request):
    return render(request,'testimonial.html')

@login_required
def applypage(request):
    if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       contact=request.POST.get('contact')
       state=request.POST.get('state')
       city=request.POST.get('city')
       address=request.POST.get('address')
       resume=request.POST.get('resume')
       apply(name=name,email=email,contact=contact,state=state,city=city,address=address,resume=resume).save()
    return render(request,'apply.html')


def logoutpage(request):
    logout(request)
    return redirect("/")