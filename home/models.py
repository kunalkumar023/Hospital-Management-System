from django.db import models

# Create your models here.

class doctor(models.Model):
    docname= models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    docid = models.IntegerField()
    docadd = models.CharField(max_length=50)
    docnumber = models.IntegerField()

    def __str__(self):
        return self.docname

class patient(models.Model):
    patientname = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    patid = models.IntegerField()
    patadd = models.CharField(max_length=50)
    patnumber = models.IntegerField()

    def __str__(self):
        return self.patientname

class appoint(models.Model):
    doc = models.ForeignKey(doctor,on_delete=models.CASCADE)
    pat = models.ForeignKey(patient,on_delete=models.CASCADE)

class bills(models.Model):
    name = models.CharField(max_length=50)
    room = models.IntegerField()
    medicine = models.IntegerField()
    other = models.IntegerField()