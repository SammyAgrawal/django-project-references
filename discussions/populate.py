import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discussions.settings')

import django
django.setup()

import random
from topics.models import Topic,Discussion
from faker import Faker

fake = Faker()