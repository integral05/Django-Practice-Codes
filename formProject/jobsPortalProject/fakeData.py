import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsPortalProject.settings')
import django
django.setup()

from testApp.models import *
from faker import Faker
from random import *

fake = Faker()

def phoneNumberGen():
    d1 = randint(7,9)
    num = ''+str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Developer','Intern','Tester'))
        feligibility = fake.random_element(elements=('B.Tech','B.E.','M.Tech','M.E.','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phoneNumberGen()
        
        punejobs_record = PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phoneNumber=fphonenumber)

populate(25)


