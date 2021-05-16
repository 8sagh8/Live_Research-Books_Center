from YaMehdiData.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
import json, io, sys
import requests
   


##########################################################
# ~~~~~ Fetch LIst Typed Data from APIs ~~~~~~~~~ #
##########################################################
#  Fetch data from 'Authorized Person API' File 
def get_authPerson_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/authPerson_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'topicsJSON.json' File 
def get_topics_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/topics_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'categoriesJSON.json' File 
def get_categories_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/categories_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'statusJSON.json' File 
def get_status_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/statuss_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'religionJSON.json' File 
def get_religion_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/religions_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'personJSON.json' File 
def get_person_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/persons_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'needJSON.json' File 
def get_need_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/needs_list/?format=json'
    ).json()

    
    return _data

#  Fetch data from 'languageJSON.json' File 
def get_language_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/languages_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'bookJSON.json' File 
def get_book_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/books_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'referenceJSON.json' File 
def get_reference_json():
    _data = requests.get(
        'https://live-search-restful-api.herokuapp.com/rest_api/references_list/?format=json'
    ).json()

    return _data
################################################
# ~~~~~ General Functions ~~~~~~~~~ #
################################################
# Authorized Person ## auth_person = auth_Person_Function(str(request.user))
def auth_Person_Function(current_user_name):
    data_list = get_authPerson_json()

    for p in data_list:
        for auth_per in p.values():
            if (current_user_name == auth_per):
                return "Authorized Person"
    return False

# Topics
def topic():
    all_topics = get_topics_json()
    list_size = 0
    if len(all_topics) != 0:
        list_size = len(all_topics)

    return (all_topics, list_size )

# Determine if in Production or Development (localhost)
def isServerLocalFunction():
    isServerLocal = False
    if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
        isServerLocal = True
    return isServerLocal

# standard function for get JSON Data and count Books
def getData_countBooks(jsonData, all_books, _field):
    isServerLocal = isServerLocalFunction()
    dict_jsonData = {}
    total_books = 0
    
    for jsonData_dict in jsonData:
        for jsonData in jsonData_dict.values():
            print("==jsonData==>", jsonData, flush=True)
            counter = 0
            for book in all_books:
                if (jsonData == str(book[_field])):
                    counter += 1
                    if len(dict_jsonData) == 0:
                        dict_jsonData = {jsonData: [jsonData_dict['id'], counter]}
                    elif jsonData in dict_jsonData.keys():
                        dict_jsonData[jsonData] = [jsonData_dict['id'], counter]
                    else:
                        dict_jsonData[jsonData] = [jsonData_dict['id'], counter]
                else:
                    
                    if jsonData in dict_jsonData.keys():
                        pass
                    elif jsonData == jsonData_dict['_need']:
                        print("==jsonData in else==>", jsonData, "|",jsonData_dict['_need'] , flush=True)
                        if len(dict_jsonData) == 0:
                            dict_jsonData = {jsonData: [jsonData_dict['id'], 0]}
                        else:
                            dict_jsonData[jsonData] = [jsonData_dict['id'], 0]
            total_books += counter
    return [dict_jsonData, total_books, isServerLocal]

#standard function to get Books by Demand
def books_by_demand(request, demanded_name, _field):
    auth_person = auth_Person_Function(str(request.user))
    all_books = get_book_json()
    isServerLocal = isServerLocalFunction()
    new_books_list = []

    # for books_list in all_books.values():
    for book in all_books:
        if str(demanded_name) == book[_field]:
            new_books_list.append(book)
    new_books_list.reverse()

    return [auth_person, demanded_name, new_books_list, isServerLocal]

# standard function for get JSON Data and count References
def getData_countReferences(request, jsonData, _field):
    auth_person = auth_Person_Function(str(request.user))
    all_references = get_reference_json()
    dict_jsonData = {}
    total_references = 0
    isServerLocal = isServerLocalFunction()

    for jsonData_dict in jsonData:
        for jsonData in jsonData_dict.values():
            counter = 0
            for references in all_references:
                if (jsonData == str(references[_field])):
                    counter += 1
                    if len(dict_jsonData) == 0:
                        dict_jsonData = {jsonData: [jsonData_dict['id'], counter]}
                    elif jsonData in dict_jsonData.keys():
                        dict_jsonData[jsonData] = [jsonData_dict['id'], counter]
                    else:
                        dict_jsonData[jsonData] = [jsonData_dict['id'], counter]
            total_references += counter
    # below is to get Dictionary in Reverse ORDER...
    new_dict_jsonData = {}
    for key, value in reversed(dict_jsonData.items()):
        if len(new_dict_jsonData) == 0:
            new_dict_jsonData = {key : value}
        else:
            new_dict_jsonData[key] = value

    return [auth_person, total_references, new_dict_jsonData, isServerLocal]

#standard function to get References by Demand
def references_by_demand(request, demanded_name, _field):
    auth_person = auth_Person_Function(str(request.user))
    all_references = get_reference_json()
    isServerLocal = isServerLocalFunction()
    new_references_list = []

    if demanded_name == None:
        for references_list in all_references.values():
            for references in references_list:
                    new_references_list.append(references)
    else:
        for references in all_references:
            if str(demanded_name) == references[_field]:
                new_references_list.append(references)
    new_references_list.reverse()

    return [auth_person, demanded_name, new_references_list, isServerLocal]

def getData(request, all_json_data):
    auth_person = auth_Person_Function(str(request.user))
    isServerLocal = isServerLocalFunction()
    final_list = []
    
    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        for json_data in all_json_data.values():
            for data in json_data:      
                for d in data.values():
                    if _searchWord.lower() in str(d).lower():
                        final_list.append(data)
    else:
        # for json_data in all_json_data.values():
        for json in all_json_data:
            final_list.append(json)
    final_list.reverse()

    return [auth_person, final_list, isServerLocal]

################################################
# ~~~~~ General VIEWS ~~~~~~~~~ #
################################################

# About page
def get_count(_list):
    count = 0
    for value in _list:
        count += 1
    return count

# About and Instruction Page
def AboutView(request):
    auth_person = auth_Person_Function(str(request.user))
    isServerLocal = isServerLocalFunction()

    return render(request, 'haq/about.html', {
        "auth_person": auth_person,
        'isServerLocal' : isServerLocal,
    })

# main Index Page
def IndexView(request):
    auth_person = auth_Person_Function(str(request.user))
    isServerLocal = isServerLocalFunction()

    topics = get_topics_json()
    topics = get_count(topics)
    categories = get_categories_json()
    categories = get_count(categories)
    status = get_status_json()
    status = get_count(status)
    religion = get_religion_json()
    religion = get_count(religion)
    person = get_person_json()
    person = get_count(person)
    need = get_need_json()
    need = get_count(need)
    language = get_language_json()
    language = get_count(language)
    books = get_book_json()
    books = get_count(books)
    references = get_reference_json()
    references = get_count(references)    

    list_about = []                         
                                
    list_about.append(('Topics', topics))
    list_about.append(('Categories', categories))
    list_about.append(('Status', status))
    list_about.append(('Religion', religion))
    list_about.append(('Person', person))
    list_about.append(('Need', need))
    list_about.append(('Language', language))
    list_about.append(('Books', books))
    list_about.append(('References', references))
    
    return render(request, 'haq/pages/index.html', {
        "auth_person": auth_person,
        "all_details": list_about,
        "isServerLocal" : isServerLocal,
    })

# Status page
def StatusView(request):
    auth_person = auth_Person_Function(str(request.user))
    status = get_status_json()
    all_books = get_book_json()

    # 3rd parameter, is field name in BOOK MODULE
    returning_value = getData_countBooks(status, all_books, 'status')

    return render(request, 'haq/pages/status.html', {
        "auth_person": auth_person,
        'total_books': returning_value [1],
        'dict_status': returning_value [0],
        'isServerLocal' : returning_value [2]
    })

# get Books by Status
def GetStatusBooksView(request, status_id):
    status_name = get_object_or_404(Status, pk=status_id)
    
    # 3rd parameter, is field name in BOOK MODULE
    demanded = books_by_demand(request, status_name, 'status')
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": demanded[0],
        'status': demanded[1],
        'books': demanded[2],
        'isServerLocal' : demanded[3],
    })

    
# Religions page
def ReligionView(request):
    auth_person = auth_Person_Function(str(request.user))

    religion = get_religion_json()
    all_books = get_book_json()

    # 3rd parameter, is field name in BOOK MODULE
    returning_value = getData_countBooks(religion, all_books, 'sect')

    return render(request, 'haq/pages/religions.html', {
        "auth_person": auth_person,
        'total_books': returning_value [1],
        'dict_religion': returning_value [0],
        'isServerLocal': returning_value [2],
       })

# get Books by Religious / Sects
def GetReligiousBooksView(request, sect_id):
    religion_name = get_object_or_404(Religion, pk=sect_id)
    
    # 3rd parameter, is field name in BOOK MODULE
    demanded = books_by_demand(request, religion_name, 'sect')
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": demanded[0],
        'status': demanded[1],
        'books': demanded[2],
        'isServerLocal': demanded[3],
    })


# Needs page
def NeedView(request):
    auth_person = auth_Person_Function(str(request.user))
    all_books = get_book_json()
    is_added = False # to know if new item added
    newItem = None

    if request.method == 'POST':
        newItem = (request.POST['add_item']).title()
        curr_user = str(request.user)
        _url = None
        
        isServerLocal = isServerLocalFunction()
        if isServerLocal == True:
            _url = 'http://127.0.0.1:8080/rest_api/needs_list/'
        else:
            _url = 'https://live-search-restful-api.herokuapp.com/rest_api/needs_list/'

        
        response = requests.post(_url, data={
            'curr_user' : curr_user,
            'newItem' : newItem
        })

        if (response.status_code == 200):
            is_added = True

    need = get_need_json()
    # 3rd parameter, is field name in BOOK MODULE
    returning_value = getData_countBooks(need, all_books, 'need')

    return render(request, 'haq/pages/need.html', {
        "auth_person": auth_person,
        'total_books': returning_value [1],
        'dict_need': returning_value [0],
        'isServerLocal': returning_value [2],
        'is_added' : is_added,
        'newItem': newItem,
    });


# get Books by Need
def GetNeedBooksView(request, need_id):
    need_name = get_object_or_404(Need, pk=need_id)
    
    # 3rd parameter, is field name in BOOK MODULE
    demanded = books_by_demand(request, need_name, 'need')
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": demanded[0],
        'status': demanded[1],
        'books': demanded[2],
        'isServerLocal': demanded[3],
    })

# Languages page
def LanguagesView(request):
    auth_person = auth_Person_Function(str(request.user))
    # languages = get_language_json()
    # all_books = get_book_json()
    languages = get_language_json()
    all_books = get_book_json()

    # 3rd parameter, is field name in BOOK MODULE
    returning_value = getData_countBooks(languages, all_books, 'lang')

    return render(request, 'haq/pages/languages.html', {
        "auth_person": auth_person,
        'total_books': returning_value [1],
        'dict_languages': returning_value [0],
        'isServerLocal': returning_value [2],
    })


# get Books by Languages
def GetLanguagesBooksView(request, language_id):
    languages_name = get_object_or_404(Language, pk=language_id)

    # 3rd parameter, is field name in BOOK MODULE
    demanded = books_by_demand(request, languages_name, 'lang')
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": demanded[0],
        'status': demanded[1],
        'books': demanded[2],
        'isServerLocal': demanded[3],
    })


# categories page
def CategoriesView(request):
    auth_person = auth_Person_Function(str(request.user))
    categories = get_categories_json()
    all_books = get_book_json()
    

    # 3rd parameter, is field name in BOOK MODULE
    final_list = getData_countBooks(categories, all_books, 'cat')
    
    if request.method == 'POST':
        _searchWord = request.POST['searchWord']
        temp = final_list[0] 
        final_list[0] = None

        for key, value in temp.items():
            if _searchWord.lower() in key.lower():
                if final_list[0] == None:
                    final_list[0] = {key: value}
                else:
                    final_list[0][key] = value

    return render(request, 'haq/pages/categories.html', {
        "auth_person": auth_person,
        'total_books': final_list [1],
        'dict_categories': final_list [0],
        'isServerLocal': final_list[2],
    })


# get Books by Categories
def GetCategoriesBooksView(request, category_id):
    categories_name = get_object_or_404(Category, pk=category_id)
    # 3rd parameter, is field name in BOOK MODULE
    demanded = books_by_demand(request, categories_name, 'cat')
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": demanded[0],
        'status': demanded[1],
        'books': demanded[2],
        'isServerLocal': demanded[3],
    })



# Books page
def BookView(request):
    all_books = get_book_json()
    final_list = getData(request, all_books)
    
    return render(request, 'haq/pages/books.html', {
        "auth_person": final_list[0],
        'status' : False, # the status is used by search by status, see 'GetStatusBooksView' 
        'books': final_list[1],
        'isServerLocal': final_list[2],
    })

# Topic page
def TopicsView(request):
    final_list = None
    topics = get_topics_json()
    
    # 3rd parameter, is field name in BOOK MODULE
    final_list = getData_countReferences(request, topics, 'subject')

    if request.method == 'POST':
        _searchWord = request.POST['searchWord']
        temp = final_list[2] 
        final_list[2] = None

        for key, value in temp.items():
            if _searchWord.lower() in key.lower():
                if final_list[2] == None:
                    final_list[2] = {key: value}
                else:
                    final_list[2][key] = value

    return render(request, 'haq/pages/topics.html', {
        "auth_person": final_list[0],
        'total_references': final_list[1],
        'dict_topics': final_list[2],
        'isServerLocal' : final_list[3],
    })

# to Get references of a Topic
def GetTopicView(request, topic_id):
    topic_name = get_object_or_404(Topic, pk=topic_id)
    returning_value = references_by_demand(request, topic_name, 'subject')
    
    return render(request, 'haq/pages/referencesByTopic.html', {
        "auth_person": returning_value[0],
        'topic': returning_value[1],
        'refer': returning_value[2],
        'isServerLocal' : returning_value[3],
    })

# to Get References
def ReferenceView(request):
    topic_name = None 
    all_references = get_reference_json()
    
    final_list = getData(request, all_references)
    
    return render(request, 'haq/pages/referencesByTopic.html', {
        "auth_person": final_list[0],
        'topic': topic_name,
        'refer': final_list[1],
        'isServerLocal' : final_list[2],
    })

# Personalities page
def PersonalityView(request):
    auth_person = auth_Person_Function(str(request.user))
    all_personalities = get_person_json()
    new_personalities_list = []
    isServerLocal = isServerLocalFunction()

    for personalities in all_personalities:
        temp = []
        for p in personalities.values():
            temp.append(p)
        new_personalities_list.append(temp)
    new_personalities_list.reverse()

    if request.method == 'POST':
        _searchWord = request.POST['searchWord']
        temp = new_personalities_list
        new_personalities_list = []

        for person in temp:
            if _searchWord.lower() in person[1].lower():
                new_personalities_list.append(person)


    return render(request, 'haq/pages/personalities.html', {
        'auth_person' : auth_person,
        'total_personalities': new_personalities_list,
        'isServerLocal' : isServerLocal
    })

# get References by Person
def GetPersonRefView(request, person_id):
    person_name = get_object_or_404(Person, pk=person_id)

    # 3rd parameter, is field name in Reference MODULE
    returning_value = references_by_demand(request, person_name, 'personFor')
    
    return render(request, 'haq/pages/referencesByTopic.html', {
        "auth_person": returning_value[0],
        'topic': returning_value[1],
        'refer': returning_value[2],
        'isServerLocal': returning_value[3],
    })

################################################
# ~~~~~ END -- General VIEWS ~~~~~~~~~ #
################################################





###########################################
###########################################
###########################################


### Log out View

def LogOutView(request):
    auth.logout(request)
    return redirect("/")