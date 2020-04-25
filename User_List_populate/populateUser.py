import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CourseLevel2.settings')

import django
django.setup()

import random
from Users.models import User
from faker import Faker

fake = Faker()

def add_user(n=5):
    for i in range(n):
        fname = fake.first_name()
        lname = fake.last_name()
        email = fake.email()
        user = User(f_name=fname, lname=lname, email=email)
        user.save()

if __name__ == '__main__': # if run directly
    print("populating")
    add_user(25)
    print("done populating")