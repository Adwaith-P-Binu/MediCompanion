from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from datetime import date, timedelta
from  django.core.files.storage import FileSystemStorage
from .models import *
import pycurl
from urllib.parse import urlencode
from django.shortcuts import get_object_or_404


def sends_mail(mail,msg):

	crl = pycurl.Curl()
	crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
	data = {'email': mail,'msg':msg}
	pf = urlencode(data)

	# Sets request method to POST,
	# Content-Type header to application/x-www-form-urlencoded
	# and data to send in request body.
	crl.setopt(crl.POSTFIELDS, pf)
	crl.perform()
	crl.close()
def first(request):
    sel=drug.objects.all()
    return render(request,'index.html',{'result':sel})
    

def index(request):
    sel=drug.objects.all()

    return render(request,'index.html',{'result':sel})
    



def readmin(request):
    return render(request,'readmin.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def productt(request):
    sel = drug.objects.all()
    today = date.today()
    expiry_range = today + timedelta(days=10)  # Set the expiry range (e.g., next 10 days)
    
    drugs = drug.objects.filter(expdate__lte=expiry_range)

    # Filter drugs with quantity less than 5
    low_stock_drugs = drug.objects.filter(qty__lt=5)

    return render(request, 'productt.html', {'result': sel, 'drugs': drugs, 'low_stock_drugs': low_stock_drugs})

# def drug_expiry_alert(request):
#     today = date.today()
#     expiry_range = today + timedelta(days=10)  # Set the expiry range (e.g., next 30 days)
    
#     drugs = drug.objects.filter(expdate=expiry_range)
    
#     return render(request, 'productt.html', {'drugs': drugs})

def drugupdt(request,id):
    upd=drug.objects.get(id=id)
    return render(request,'updtdrug.html',{'result':upd})

def updtdrug(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        genericname=request.POST.get('genericname')
        dosage=request.POST.get('dosage')
        form=request.POST.get('form')
        manufature=request.POST.get('manufature')
        expdate=request.POST.get('expdate')
        price=request.POST.get('price')
        qty=request.POST.get('qty')
        myfile=request.FILES['image']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        
        donor=drug(name=name,genericname=genericname,dosage=dosage,form=form,manufature=manufature,expdate=expdate,price=price,qty=qty,image=myfile,id=id)
        donor.save()
        return redirect(productt)

def drugdelete(request,id):
    sel=drug.objects.get(id=id)
    sel.delete()
    return redirect(productt)



def adddoctor(request):
    return render(request,'adddoctor.html')

from django.db.models import Q

def viewuserproduct(request):
    query = request.GET.get('q')
    if query:
        sel = drug.objects.filter(
            Q(name__icontains=query)
        )
    else:
        sel = drug.objects.all()
    return render(request, 'viewuserproduct.html', {'result': sel, 'query': query})



# def viewuserproduct(request):
#     sel=drug.objects.all()
#     return render(request,'viewuserproduct.html',{'result':sel})
def viewdoctorproduct(request):
    sel=drug.objects.all()
    return render(request,'viewdoctorproduct.html',{'result':sel})
  
# def viewuserdoctor(request):
#     sel=doctor.objects.all()
#     return render(request,'viewuserdoctor.html',{'result':sel})


from django.db.models import Q

def viewuserdoctor(request):
    query = request.GET.get('q')
    if query:
        sel = doctor.objects.filter(
            Q(specialization__icontains=query)
        )
    else:
        sel = doctor.objects.all()
    return render(request, 'viewuserdoctor.html', {'result': sel, 'query': query})



def viewuserpaid(request):
    sel=payment.objects.filter(uid=request.session['uid'])
    sel1=drug.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.pid)==str(j.id):
                i.pid=j.name
    return render(request,'viewpaidd.html',{'result':sel})
    
def userprescribe(request):
    sel=consult.objects.filter(uid=request.session['uid'],status='consult')
    sel1=doctor.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.did)==str(j.id):
                i.did=j.name
    return render(request,'userprescribe.html',{'result':sel})
    

def phpres(request):
    sel=consult.objects.all()
    sel1=doctor.objects.all()
    sel2=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.did)==str(j.id):
                i.did=j.name
    for i in sel:
        for j in sel2:
            if str(i.uid)==str(j.id):
                i.uid=j.name            
    return render(request,'phpres.html',{'result':sel})
    


def viewuserconsult(request):
    sel=consult.objects.filter(did=request.session['did'],status='pending')
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.uid)==str(j.id):
                i.uid=j.name
    return render(request,'vieww.html',{'result':sel})
    
def buy(request,id):
    sel=drug.objects.get(id=id)
    return render(request,'buy.html',{'result':sel})
    
def dtt(request,id):
    sel=consult.objects.get(id=id)
    return render(request,'dc.html',{'result':sel})
    
def consult1(request,id):
    sel=doctor.objects.get(id=id)
    return render(request,'consult.html',{'result':sel})
def addpro(request,id):
    sel=drug_req.objects.get(id=id)
    return render(request,'drugg.html',{'result':sel})
def viewdoctorreq(request):
    sel=drug_req.objects.filter(status='pending')
    sel1=doctor.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.did)==str(j.id):
                i.did=j.name
        
    return render(request,'viewdreq.html',{'result':sel})
def viewadminpayment(request):
    sel=payment.objects.all()
    sel1=user.objects.all()
    sel2=drug.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.uid)==str(j.id):
                i.uid=j.name
        for k in sel2:
            if str(i.pid)==str(k.id):
                i.pid=k.name
    return render(request,'viewadminpayment.html',{'result':sel})

def adddrug(request):
    if request.method=="POST":
        name=request.POST.get('name')
        genericname=request.POST.get('genericname')
        dosage=request.POST.get('dosage')
        form=request.POST.get('form')
        manufature=request.POST.get('manufature')
        expdate=request.POST.get('expdate')
        price=request.POST.get('price')
        qty=request.POST.get('qty')
        myfile=request.FILES['image']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        
        donor=drug(name=name,genericname=genericname,dosage=dosage,form=form,manufature=manufature,expdate=expdate,price=price,qty=qty,image=myfile)
        donor.save()
        return redirect(productt)
   
def finall(request):
    if request.method=="POST":
        idd=request.POST.get('idd')
        name=request.POST.get('name')
        genericname=request.POST.get('genericname')
        dosage=request.POST.get('dosage')
        form=request.POST.get('form')
        manufature=request.POST.get('manufature')
        expdate=request.POST.get('expdate')
        price=request.POST.get('price')
        qty=request.POST.get('qty')
        myfile=request.FILES['image']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        sel=drug_req.objects.get(id=idd)
        name1=sel.name
        genericname1=sel.genericname	
        dosage1=sel.dosage
        form1=sel.form
        manufature1=sel.manufature
        did1=sel.did
        idd1=sel.id
        donor1=drug_req(name=name1,genericname=genericname1,dosage=dosage1,form=form1,manufature=manufature1,did=did1,status='approve',id=idd1)
        donor1.save()
        donor=drug(name=name,genericname=genericname,dosage=dosage,form=form,manufature=manufature,expdate=expdate,price=price,qty=qty,image=myfile)
        donor.save()
        return redirect(viewdoctorreq)
    
def requu(request):
    if request.method=="POST":
        name=request.POST.get('name')
        genericname=request.POST.get('genericname')
        dosage=request.POST.get('dosage')
        form=request.POST.get('form')
        manufature=request.POST.get('manufature')
        did=request.session['did']

        donor=drug_req(name=name,genericname=genericname,dosage=dosage,form=form,manufature=manufature,did=did,status='pending')
        donor.save()
        return render(request,'readmin.html',{'status':' Successfully Added'})
        
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)
def adduser(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        age=request.POST.get('age')

        donor=user(name=name,email=email,phone=phone,address=address,password=password,age=age)
        donor.save()
        return render(request,'register.html',{'status':'Register Successfully'})
    
def addconsult(request):
    if request.method=="POST":
        des=request.POST.get('des')
        date=request.POST.get('date')
        did=request.POST.get('did')
        medicine=request.POST.get('medicine')
        fee=request.POST.get('fee')
        uid=request.session['uid']
        file = request.FILES['file']
        fs = FileSystemStorage()
        file = fs.save(file.name,file)
        

        donor=consult(did=did,uid=uid,date=date,des=des,file=file,medicine=medicine,fee=fee,status='pending')
        donor.save()
        return redirect(viewuserdoctor)

def paydoc(request,id):
    sel=user.objects.all()
    sel1=doctor.objects.get(id=id)
    return render(request,'paydoc.html',{'res':sel,'result':sel1})


def addpaydoc(request):
    if request.method=="POST":
        pid=request.POST.get('pid')
        fee=request.POST.get('fee')
        cardname=request.POST.get('cardname')
        cardnumber=request.POST.get('cardnumber')
        cvv=request.POST.get('cvv')
        
        ins=doc_payment(pid=pid,fee=fee,cardname=cardname,cardnumber=cardnumber,cvv=cvv,status="paid",user_id=request.session['uid'])
        ins.save()
    return redirect(viewuserdoctor)    



def addd(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        age=request.POST.get('age')
        specialization=request.POST.get('specialization')
        experience=request.POST.get('experience')
        fee=request.POST.get('fee')

        donor=doctor(specialization=specialization,experience=experience,name=name,email=email,phone=phone,address=address,password=password,age=age,fee=fee)
        donor.save()
        return render(request,'adddoctor.html',{'status':' Successfully Added'})

def paid(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        cardname = request.POST.get('cardname')
        cardnumber = request.POST.get('cardnumber')
        qty1 = int(request.POST.get('qty'))
        cvv = request.POST.get('cvv')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        uid = request.session['uid'] 

        # Get drug details
        a = drug.objects.get(id=pid)

        qty = a.qty
        price = int(a.price)
        total = qty1 * price


        # Update drug quantity
        remaining_qty = int(qty) - int(qty1)
        a.qty = remaining_qty
        a.save()

        # Save payment details
        donor = payment.objects.create(pid=pid, uid=uid, cardname=cardname, cardnumber=cardnumber, qty=qty1, price=total, cvv=cvv, phone=phone,address=address)

        return redirect(viewuserproduct)

        
        
        
def dconsult(request):
    if request.method == "POST":
        cid = request.POST.get('cid')
        prescription = request.POST.get('prescription')
        a = consult.objects.get(id=cid)
        did = a.did
        uid = a.uid
        des = a.des
        date = a.date
        file = a.file
        medicine = a.medicine
        fee = a.fee

        # Split the medicine and prescription fields into lists of individual items
        consult_medicines = [m.strip() for m in medicine.split(',')]
        consult_prescriptions = [p.strip() for p in prescription.split(',')]

        for consult_med in consult_medicines:
            for consult_pres in consult_prescriptions:
                # Check if the consult medicine matches any medicine in drug_interaction table
                interaction_exists = drug_interaction.objects.filter(medicine=consult_med).exists()

                if interaction_exists:
                    # Check if the nonmedicine in drug_interaction is the same as the prescription in consult table
                    matching_interaction = drug_interaction.objects.filter(medicine=consult_med, nonmedicine=consult_pres).exists()

                    if matching_interaction:
                        # Display an alert or take any action for the alert 
                        sel = consult.objects.filter(did=request.session['did'], status='pending')
                        sel1 = user.objects.all()
                        for i in sel:
                            for j in sel1:
                                if str(i.uid) == str(j.id):
                                    i.uid = j.name
                        return render(request, 'vieww.html', {'msg': 'The prescribed medicine has a potential drug interaction with the medicine used by the patient.', 'result': sel})

        idd = a.id

        donor1 = consult(did=did, file=file, uid=uid, des=des, date=date, medicine=medicine, prescription=prescription, status='consult',fee=fee, id=idd)
        donor1.save()
    return redirect(viewuserconsult)



    
def nonmed(request):
    return render(request,'nonusemed.html')

def addnonmed(request):
    if request.method=="POST":
        medicine=request.POST.get('medicine')
        nonmedicine=request.POST.get('nonmedicine') 
        donor=drug_interaction(nonmedicine=nonmedicine,medicine=medicine)
        donor.save()
        return render(request,'nonusemed.html',{'status':' Successfully Added'})




def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'index.html')


    else:
        return render(request, 'login.html', {'status': 'Invalid Email or Password'})

# def addlogin(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     if email == 'admin@gmail.com' and password =='admin':
#         request.session['logintdetail'] = email
#         request.session['admin'] = 'admin'
#         return render(request,'index.html')

#     elif user.objects.filter(email=email,password=password).exists():
#         userdetails=user.objects.get(email=request.POST['email'], password=password)
#         if userdetails.password == request.POST['password']:
#             request.session['uaddress']=userdetails.address
#             request.session['uid'] = userdetails.id
#             request.session['uname'] = userdetails.name

#             request.session['uemail'] = email

#             request.session['user'] = 'user'


#             return render(request,'index.html')


#     elif doctor.objects.filter(email=email,password=password).exists():
#         userdetails=doctor.objects.get(email=request.POST['email'], password=password)
#         if userdetails.password == request.POST['password']:
#             request.session['did'] = userdetails.id
#             request.session['tname'] = userdetails.name

#             request.session['temail'] = email

#             request.session['doctor'] = 'doctor'


#             return render(request,'index.html')
        
#     elif pharmacy_tbl.objects.filter(email=email,password=password).exists():
#             userdetails=pharmacy_tbl.objects.get(email=email ,password=password)
#             request.session['phid'] = userdetails.id
#             request.session['phname'] = userdetails.name

#             request.session['phemail'] = email

#             request.session['pharmacy'] = 'doctor'


#             return render(request,'index.html')
    
#     else:
#         return render(request, 'login.html', {'status': 'Invalid Email or Password'})
        
        
def login1doc(request):
    return render(request,'login1doc.html')      

def addlogindoc(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if doctor.objects.filter(email=email,password=password).exists():
        userdetails=doctor.objects.get(email=request.POST['email'], password=password)
        request.session['did'] = userdetails.id
        request.session['tname'] = userdetails.name

        request.session['temail'] = email

        request.session['doctor'] = 'doctor'


        return render(request,'index.html')
        
    
    
    else:
        return render(request, 'login1doc.html', {'status': 'Invalid Email or Password'})



def login2ph(request):
    return render(request,'login2ph.html')      

def addlogin2ph(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if pharmacy_tbl.objects.filter(email=email,password=password).exists():
        userdetails=pharmacy_tbl.objects.get(email=request.POST['email'], password=password)
        request.session['phid'] = userdetails.id
        request.session['phname'] = userdetails.name

        request.session['phemail'] = email

        request.session['pharmacy'] = 'doctor'



        return render(request,'index.html')
        
    
    
    else:
        return render(request, 'login2ph.html', {'status': 'Invalid Email or Password'})


def login3user(request):
    return render(request,'login3user.html')      

def addlogin3user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if user.objects.filter(email=email,password=password).exists():
        userdetails=user.objects.get(email=request.POST['email'], password=password)
        request.session['uaddress']=userdetails.address
        request.session['uid'] = userdetails.id
        request.session['uname'] = userdetails.name

        request.session['uemail'] = email

        request.session['user'] = 'user'



        return render(request,'index.html')
        
    
    
    else:
        return render(request, 'login3user.html', {'status': 'Invalid Email or Password'})
        
             
              
def docpayssview(request):
    sel=doc_payment.objects.filter(pid=request.session['did'])
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.user_id)==str(j.id):
                i.user_id=j.name
    return render(request,'docpayssview.html',{'result':sel})



def viewuser(request):
    sel=user.objects.all()  
    return render(request,'viewuser.html',{'result':sel})    

def viewdoc(request):
    sel=doctor.objects.all()  
    return render(request,'viewdoc.html',{'result':sel})    


def deletedoctor(request,id):
    sel=doctor.objects.get(id=id)
    sel.delete()
    return redirect(viewdoc)


def updatedoctor(request,id):
    sel=doctor.objects.get(id=id)
    return render(request,'updatedoctor.html',{'result':sel})

def addupdatedoctor(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        age=request.POST.get('age')
        specialization=request.POST.get('specialization')
        experience=request.POST.get('experience')

        donor=doctor(specialization=specialization,experience=experience,name=name,email=email,phone=phone,address=address,password=password,age=age,id=id)
        donor.save()
    return redirect(viewdoc)

def viewph(request):
    sel=pharmacy_tbl.objects.all()  
    return render(request,'viewph.html',{'result':sel})    


def updatepharmacy(request,id):
    sel=pharmacy_tbl.objects.get(id=id)
    return render(request,'updatepharmacy.html',{'result':sel})

def deletepharmacy(request,id):
    sel=pharmacy_tbl.objects.get(id=id)
    sel.delete()
    return redirect(viewph)


def addupdatepharmacy(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
       
        donor=pharmacy_tbl(name=name,email=email,phone=phone,address=address,password=password,id=id)
        donor.save()
    return redirect(viewph)


def phr(request):
    return render(request,'addph.html')

def addpharmacy(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
       
        donor=pharmacy_tbl(name=name,email=email,phone=phone,address=address,password=password)
        donor.save()
    return render(request,'index.html',{'status':' Successfully Added'})



def dosss(request):
    sel=user.objects.all()
    return render(request,'adddosee.html',{'result':sel})

def adddosss(request):
    if request.method=="POST":
        date=request.POST.get('date')
        medicine_name=request.POST.get('medicine_name')
        no_of_days=request.POST.get('no_of_days')
        
        time=request.POST.get('time')
        dosage=request.POST.get('dosage')
        notes=request.POST.get('notes')
        patient_id=request.POST.get('patient_id')
       
        donor=dosage_tbl(date=date,medicine_name=medicine_name,no_of_days=no_of_days,time=time,dosage=dosage,notes=notes,patient_id=patient_id,doctor_id=request.session['did'],status="pending")
        donor.save()
    return render(request,'index.html',{'status':' Successfully Added'})


def chatss(request,id):
    sel=user.objects.all()
    sel1=doctor.objects.get(id=id)
    return render(request,'chat.html',{'res':sel,'result':sel1})


def addchatss(request):
    if request.method=="POST":
        doctor_id=request.POST.get('doctor_id')
        message=request.POST.get('message')
        
        ins=chat_tbl(doctor_id=doctor_id,message=message,patient_id=request.session['uid'])
        ins.save()
    return render(request,'chat.html')    






def viewchatsall(request):
    sel=chat_tbl.objects.filter(doctor_id=request.session['did'])
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.patient_id)==str(j.id):
                i.patient_id=j.name
    return render(request,'viewwchatall.html',{'result':sel})


def viewchats(request):
    sel=chat_tbl.objects.all()
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.patient_id)==str(j.id):
                i.patient_id=j.name
    return render(request,'viewwchat.html',{'result':sel})



def replyss(request,id):
    #sel=user.objects.all()
    sel1=chat_tbl.objects.get(id=id)
    return render(request,'reply.html',{'result':sel1})


def addreply(request,id):
    if request.method=="POST":
        patient_id=request.POST.get('patient_id')
        doctor_id=request.POST.get('doctor_id')
        message=request.POST.get('message')
        reply=request.POST.get('reply')
        
        ins=chat_tbl(doctor_id=doctor_id,message=message,reply=reply,patient_id=patient_id,id=id)
        ins.save()
    return render(request,'index.html')    






def viewchatsuser(request):
    sel=chat_tbl.objects.filter(patient_id=request.session['uid'])
    sel1=doctor.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.doctor_id)==str(j.id):
                i.doctor_id=j.name
           
    
    return render(request,'viewchatuser.html',{'result':sel})


from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
"""
def viewnoti(request):
    # Fetch the dosage schedule for the logged-in user
    sel = dosage_tbl.objects.filter(patient_id=request.session['uid'])

    # Get the current date and time
    current_datetime = timezone.now()

    # List to hold alert messages
    alerts = []

    # Check each dosage entry
    for entry in sel:
        # Combine the entry date and time to create a naive datetime object
        naive_medication_datetime = datetime.combine(entry.date, entry.time)

        # Convert the naive datetime object to an aware datetime object
        medication_datetime = timezone.make_aware(naive_medication_datetime, timezone.get_current_timezone())

        # Calculate the difference between current time and medication time
        time_difference = medication_datetime - current_datetime

        # If the medication time is within the next hour
        if timedelta(0) <= time_difference <= timedelta(hours=1):
            alert_message = f"Reminder: You have to take {entry.medicine_name} at {entry.time.strftime('%H:%M')} on {entry.date}."
            alerts.append(alert_message)

    # Render the template with the results and alerts
    return render(request, 'viewnoti.html', {'result': sel, 'alerts': alerts})"""

def viewnoti(request):
    sel = dosage_tbl.objects.filter(patient_id=request.session['uid'])
    return render(request,'viewnoti.html',{'result': sel})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import dosage_tbl

def update_dosage(request, id):
    dosage = get_object_or_404(dosage_tbl, id=id)
    if request.method == "POST":

        date=request.POST.get('date')
        medicine_name=request.POST.get('medicine_name')
        no_of_days=request.POST.get('no_of_days')
        
        time=request.POST.get('time')
        dosage=request.POST.get('dosage')
        notes=request.POST.get('notes')
        doctor_id=request.POST.get('doctor_id')
        description = request.POST.get('description')

        donor=dosage_tbl(date=date,medicine_name=medicine_name,no_of_days=no_of_days,time=time,dosage=dosage,notes=notes,doctor_id=doctor_id,description=description,patient_id=request.session['uid'],status="pending",id=id)
        donor.save()
        
        msg = "Dosage updated successfully"
         # Replace 'your_view_name' with your view name

    return render(request, 'viewnoti.html', {'dosage': dosage,'msg':msg})  # Adjust as needed




'''def viewnoti(request):
    sel=dosage_tbl.objects.filter(patient_id=request.session['uid'])
    return render(request,'viewnoti.html',{'result':sel})'''





def useraccept(request,id):
    s=dosage_tbl.objects.get(pk=id)
    s.status='Completed'
    s.save()
    return redirect(viewnoti)
    
    
def userreject(request,id):
    s=dosage_tbl.objects.get(pk=id)
    s.status='NotCompleted'
    s.save()
    return redirect(viewnoti)




def viewnotiii(request):
    sel=dosage_tbl.objects.filter(doctor_id=request.session['did'])
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.patient_id)==str(j.id):
                i.patient_id=j.name
    return render(request,'viewnotiii.html',{"result":sel})


from django.db.models import Q

def viewnonusable(request):
    query = request.GET.get('q')
    if query:
        sel = drug_interaction.objects.filter(
            Q(medicine__icontains=query) | Q(nonmedicine__icontains=query)
        )
    else:
        sel = drug_interaction.objects.all()
    return render(request, 'viewnon.html', {'res': sel, 'query': query})


# def viewnonusable(request):
#     sel=drug_interaction.objects.all()
#     return render(request,'viewnon.html',{'res':sel})




def forget(request):
    return render (request,'forgetpass.html')

def forgetpassword(request):
    if request.method == "POST":
        entered_email = request.POST.get('email')

        # Check if the entered email exists in the User model
        try:
            user_instance = user.objects.get(email=entered_email)  # Use a different variable name
            password = user_instance.password  # Retrieve the password from the User model

            # Send the password to the user's email using the sends_mail function
            message = f'Your password For user login is: {password}'
         
            sends_mail(entered_email, message)

            return render(request, 'login3user.html', {'msg': 'Your password has been sent to the registered email.'})

        except user.DoesNotExist:
            return render(request, 'login3user.html', {'msg': 'Entered email does not exist in the database.'})

    return render(request, 'login3user.html', {'msg': 'Enter your registered email to recover your password.'})



def feed(request):
    return render(request,'feed.html')

def addfeed(request):
    if request.method=="POST":
        feedbacks=request.POST.get('feedbacks')
        ins=feedback_tbl(feedbacks=feedbacks,user_id=request.session['uid'])
        ins.save()
    return render(request,'index.html',{'status':"Successfully Added"})    



def viewfeed(request):
    sel=feedback_tbl.objects.all()
    sel1=user.objects.all()
    for i in sel:
        for j in sel1:
            if str(i.user_id)==str(j.id):
                i.user_id=j.name
    return render(request,'viewfeed.html',{"result":sel})

def gello(request):
    return render(request,'index.html')   
