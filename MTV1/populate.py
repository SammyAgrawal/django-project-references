import os
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTV1.settings')
django.setup()

from posts.models import Topic, Reply
from faker import Faker

fake = Faker()

topics = ["Capitalism", "Income Inequality", "Minimum Wage", "Death", "Can we find universe?"]
def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=10):
    for i in range(n):
        t = add_topic()
        rep = Reply(topic=t, reply=fake.text())
        rep.save()


print("populating...")
populate()
print("Done")
