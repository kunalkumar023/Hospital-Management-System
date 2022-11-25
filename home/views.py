from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import doctor,patient,appoint


# Create your views here.

def home(request):
    return render(request,"home.html")

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        ad = authenticate(request,username=username,password=password)

        if ad is not None:
            login(request,ad) 
            return render(request,"other.html")

        else:
            # message.error("Credentials are wrong!")
            return redirect("login")

    return render(request,"login.html")
# def home2(request):

#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         ad = authenticate(request,username=username,password=password)

#         if ad is not None:
#             login(request,ad)
#             return render(request,"other.html")

#         else:
#             return render(request,'login.html')

def other(request):
    return render(request,'other.html')

def doc(request):

    if request.method == "POST":
        docname = request.POST['docname']
        specialization = request.POST['specialization']
        docid = request.POST['docid']
        docadd = request.POST['docadd']
        docnumber = request.POST['docnumber']

        newdoc = doctor(docname=docname,specialization=specialization,docid=docid,docadd=docadd,docnumber=docnumber)

        newdoc.save()
        return HttpResponse("Doctor is created:")
    return render(request,'doc.html')

def about(request):
    return render(request,'about.html')

def patient1(request):

    if request.method == "POST":
        patientname = request.POST['patname']
        disease = request.POST['disease']
        patid = request.POST['patid']
        patadd = request.POST['patadd']
        patnumber = request.POST['patnumber']

        newpat = patient(patientname=patientname,disease=disease,patid=patid,patadd=patadd,patnumber=patnumber)

        newpat.save()
        return HttpResponse("patient is added:")
    return render(request,"patient.html")

def contact(request):
    return render(request,"contact.html")

def appoint(request):
    if request.method == 'POST':
        doc = request.POST['doctorname']
        pat = request.POST['patientname']

        newapp = appoint(doc=doc,pat=pat)
        newapp.save()
        return HttpResponse("Appointment Added successfully:")
    return render(request,"appoint.html")

def bills(request):
    return render(request,"bills.html")