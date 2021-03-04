from django.shortcuts import get_object_or_404, render,redirect
from YaMehdiData.settings import AUTH_PASSWORD_VALIDATORS
from django.http import HttpResponse
from haq.models import *
from django.contrib.auth.models import User, auth
import json 

# Create your views here.

# get data from DATABASE 'sqlite3' and store into JSON files
def IntoJSONView(request):
    print("   ==> serverAPI", flush=True)
    topics = Topic.objects.all()
    topics_list = [] # will store all topics and then go inside json_topic

    for t in topics:
        topics_list.append({"id": t.id, "_topic": t._topic})

    # will store topics json in here
    json_topic = { "topics" : topics_list }
    # convert into json data
    my_json = json.dumps(json_topic, indent=1)

    with open('serverAPI/static/json/topics.json', mode='w+') as myFile:
        myFile.write(my_json)

    return render(request, 'serverAPI/filecreated.html')


