from turtle import up
from django.shortcuts import redirect, render
from .forms import notesForm, signupForm, contactForm
from .models import signup_master,notes
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import random
import requests
import json

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get("signup")=="signup":
            userSignup=signupForm(request.POST)
            if userSignup.is_valid():
                userSignup.save()
                print("Signup Successfully!")

                # Send MAIL
                otp=random.randint(11111,99999)
                subject="Woohoo! Welcome"
                msg=f"Hello User\nWelcome to TOPS Technologies Pvt.Ltd - Rajkot(Gujarat).\nYour account has been created with us!\nYour One Time Password:{otp}\nEnjoy our services.\n\nThanks & Regards!\nSanket Chauhan - Technical Trainer\n+91 9724799469 | sanket.chauhan@tops-int.com"
                #from_id='batchprojecttops@gmail.com'
                from_id=settings.EMAIL_HOST_USER
                #to_id=['vishveks2000@gmail.com','hardikkateliya2@gmail.com','batchprojecttops@gmail.com']
                to_id=[request.POST['username']]

                send_mail(subject,msg,from_id,to_id)

                return redirect('/')
            else:
                print(userSignup.errors)
        elif request.POST.get("login")=="login":
            unm=request.POST["username"]
            pas=request.POST["password"]

            userLogin=signup_master.objects.filter(username=unm,password=pas)
            userid=signup_master.objects.get(username=unm)
            print("USerID:",userid.id)
            #usermob=signup_master.objects.get(username=unm)
            mob=userid.zipcode
            print("Mobile:",mob)
           

            if userLogin:
                print("Login Success!")
                request.session['user']=unm
                request.session['userID']=userid.id
                request.session['usermobile']=userid.zipcode

                # Send SMS
                # mention url
                otp=random.randint(11111,99999)

                # Save OTP into Database
                

                url = "https://www.fast2sms.com/dev/bulk"
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS', 
                    
                    # Put your message here!
                    'message': f'Your One time password is {otp}', 
                    
                    'language': 'english',
                    'route': 'p',
                    
                    # You can send sms to multiple numbers
                    # separated by comma.
                    #'numbers': '8320275089,6354700138,9157139905'    
                    'numbers':f'{mob}'
                }
                
                # create a dictionary
                headers = {
                    'authorization': 'dZkciDBeMfbKa8FUgmJ3A4oHWRtI7zQ0nqTyxvjN5pGXOwY6r2WMVxL2DbpkRHwu7N8eqOcU1T5v9PmJ',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }
                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)
                
                # print the send message
                print(returned_msg['message'])
                return redirect("notes")
            else:
                print("Error..Login fail!")
    return render(request,'index.html')

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        contactfrm=contactForm(request.POST)
        if contactfrm.is_valid():
            contactfrm.save()
            print("Your feedback has been submitted!")
            return redirect('contact')
        else:
            print(contactfrm.errors)
    return render(request,'contact.html',{'user':user})

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        notesUpload=notesForm(request.POST,request.FILES)
        if notesUpload.is_valid():
            notesUpload.save()
            print("Your post has been uploaded!")
        else:
            print(notesUpload.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userID')
    stid=signup_master.objects.get(id=userid)
    if request.method=='POST':
        updateData=signupForm(request.POST)
        if updateData.is_valid():
            updateData=signupForm(request.POST,instance=stid)
            updateData.save()
            print("Your profile has been updated!")
            return redirect('profile')
        else:
            print(updateData.errors)
    return render(request,'profile.html',{'user':user,'userid':userid,'userUpdate':signup_master.objects.get(id=userid)})

def userlogout(request):
    logout(request)
    return redirect("/")