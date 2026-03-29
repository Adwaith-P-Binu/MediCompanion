from django.db import models

class doctor(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    age=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    specialization=models.CharField(max_length=150)
    experience=models.CharField(max_length=150)
    fee=models.CharField(max_length=150)


class pharmacy_tbl(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    


class user(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    password=models.CharField(max_length=150)  
    age=models.CharField(max_length=150)


class drug(models.Model):
    name=models.CharField(max_length=150)
    genericname=models.CharField(max_length=150)
    dosage=models.CharField(max_length=150)
    form=models.CharField(max_length=150)
    manufature=models.CharField(max_length=150)  
    expdate=models.CharField(max_length=150) 
    price=models.CharField(max_length=150)  
    image=models.CharField(max_length=150)
    qty = models.IntegerField()
    
class drug_req(models.Model):
    name=models.CharField(max_length=150)
    genericname=models.CharField(max_length=150)
    dosage=models.CharField(max_length=150)
    form=models.CharField(max_length=150)
    manufature=models.CharField(max_length=150)  
    did=models.CharField(max_length=150) 
    status=models.CharField(max_length=150) 

class consult(models.Model):
    did=models.CharField(max_length=150)
    uid=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    des=models.CharField(max_length=150)
    file=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    medicine=models.CharField(max_length=150)
    prescription=models.CharField(max_length=150)
    fee=models.CharField(max_length=150)
   
   
class payment(models.Model):
    uid=models.CharField(max_length=150)
    pid=models.CharField(max_length=150)
    price=models.CharField(max_length=150)
    qty=models.CharField(max_length=150)
    cardname=models.CharField(max_length=150)
    cardnumber=models.CharField(max_length=150)
    cvv=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
   
    
class drug_interaction(models.Model):
    medicine=models.CharField(max_length=150)
    nonmedicine=models.CharField(max_length=150)
   

class doc_payment(models.Model):
    user_id=models.CharField(max_length=150)
    pid=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    fee=models.CharField(max_length=150)
    pid=models.CharField(max_length=150)
    cardname=models.CharField(max_length=150)
    cardnumber=models.CharField(max_length=150)
    cvv=models.CharField(max_length=150)
   

    
class chat_tbl(models.Model):
    patient_id=models.CharField(max_length=150)
    doctor_id=models.CharField(max_length=150)
    message=models.CharField(max_length=150)
    reply=models.CharField(max_length=150)
   



class dosage_tbl(models.Model):
    date = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=150)
    notes = models.CharField(max_length=150)
    patient_id = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    doctor_id = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    no_of_days = models.CharField(max_length=150)
    

    def __str__(self):
        return f"{self.medication_name} - {self.date} "


class feedback_tbl(models.Model):
    user_id=models.CharField(max_length=150)
    feedbacks=models.CharField(max_length=150)
  