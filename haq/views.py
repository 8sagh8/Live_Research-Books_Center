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
        'https://live-research-books.herokuapp.com/rest_api/authPerson_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'topicsJSON.json' File 
def get_topics_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/topics_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'categoriesJSON.json' File 
def get_categories_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/categories_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'statusJSON.json' File 
def get_status_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/statuss_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'religionJSON.json' File 
def get_religion_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/religions_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'personJSON.json' File 
def get_person_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/persons_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'needJSON.json' File 
def get_need_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/needs_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'languageJSON.json' File 
def get_language_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/languages_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'bookJSON.json' File 
def get_book_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/books_list/?format=json'
    ).json()

    return _data

#  Fetch data from 'referenceJSON.json' File 
def get_reference_json():
    _data = requests.get(
        'https://live-research-books.herokuapp.com/rest_api/references_list/?format=json'
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
    # need = get_need_json()
    # all_books = get_book_json()
    need = get_need_json()
    all_books = get_book_json()
    
    # 3rd parameter, is field name in BOOK MODULE
    returning_value = getData_countBooks(need, all_books, 'need')

    return render(request, 'haq/pages/need.html', {
        "auth_person": auth_person,
        'total_books': returning_value [1],
        'dict_need': returning_value [0],
        'isServerLocal': returning_value [2],
    })


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









# Category(ies) page
def CategoryView(request):
    auth_person = auth_Person_Function(str(request.user))
    categories= Category.objects.all()
    all_books = Book.objects.all()
    dict_cat = {}
    total_books = 0

    for cat in categories:
        counter = 0
        dict_cat[cat] = counter

        for book in all_books:
            if (cat == book.cat):
                counter += 1
                dict_cat[cat] = counter
        
        total_books += counter


            
    return render(request, 'haq/categories.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_cat': dict_cat,
       })


# Language page
def LanguageView(request):
    auth_person = auth_Person_Function(str(request.user))
    language= Language.objects.all()
    all_books = Book.objects.all()
    dict_lang = {}
    total_books = 0

    for lang in language:
        counter = 0
        dict_lang[lang] = counter

        for book in all_books:
            if (lang == book.lang):
                counter += 1
                dict_lang[lang] = counter
        
        total_books += counter


            
    return render(request, 'haq/languages.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_lang': dict_lang,
       })


###########################################
###########################################
###########################################


# BookSectView -- Display Books List Sect-Wise
def BookSectOptionView(request):
    temp = topic()
    all_sects = Religion.objects.all()
    _size = len(all_sects)

    return render(request, 'haq/bookSectOption.html', {
        "all_sects": all_sects,
        "size": _size,
        "all_topics": temp[0],
        "list_size": temp[1]
    })


# Add book option
def BookAddView(request):
    message = "Add A Book"
    submission_form = "no"
    p_list = [] #empty list to store persons name for html
    r_list = [] #empty list to store religions / sect name for html
    c_list = [] #empty list to store categories name for html
    s_list = [] #empty list to store status name for html
    n_list = [] #empty list to store need name for html
    l_list = [] #empty list to store languages name for html

    p_obj = Person.objects.all()
    r_obj = Religion.objects.all()
    c_obj = Category.objects.all()
    s_obj = Status.objects.all()
    n_obj = Need.objects.all()
    l_obj = Language.objects.all()

    for p in p_obj:
        p_list.append([p.id, p._p_name])
    for r in r_obj:
        r_list.append([r.id, r._sect])
    for c in c_obj:
        c_list.append([c.id, c._category])
    for s in s_obj:
        s_list.append([s.id, s._status])
    for n in n_obj:
        n_list.append([n.id, n._need])
    for l in l_obj:
        l_list.append([l.id, l._language])

    if request.method == "POST":
        
        bName = request.POST['bookName']
        bAuthor = request.POST['bookAuthor']

        bSect = request.POST['bookSect']
        bCat = request.POST['bookCat']
        bStatus = request.POST['bookStatus']
        bNeed = request.POST['bookNeed']
        bLang = request.POST['bookLang']
        
        data = None
        data = Book(name = bName, author = Person.objects.get(id = bAuthor), sect = Religion.objects.get(id = bSect), cat = Category.objects.get(id = bCat), status = Status.objects.get(id = bStatus), need = Need.objects.get(id = bNeed), lang = Language.objects.get(id = bLang))
        
        data.save() # persist in database
        
        message = bName + " Book is Added"
        submission_form = "yes"

    return render(request, 'haq/bookAdd.html', {
        "message": message,
        "submission_form": submission_form,
        "p_list": p_list,
        "r_list": r_list,
        "c_list": c_list,
        "s_list": s_list,
        "n_list": n_list,
        "l_list": l_list,
    })




###############################



### Log out View

def LogOutView(request):
    auth.logout(request)
    return redirect("/")

### API routes' Views
def IntoJsonView(request):
    # return redirect("intoJSON/")

    auth_person = auth_Person_Function(str(request.user))
    status = Status.objects.all()
    all_books = Book.objects.all()
    dict_status = {}
    total_books = 0

    for status in status:
        counter = 0
        dict_status[status] = counter

        for book in all_books:
            if (status == book.status):
                counter += 1
                dict_status[status] = counter
        
        total_books += counter

    return render(request, 'haq/pages/status.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_status': dict_status,
       })

################################################
# ~~~~~ JSON FILES Functions & VIEWS ~~~~~~~~~ #
################################################
# create 'authorizedPersonJSON.json' file
def _createAuthPersonJSON(request):
    auth_person = Authorized_Person.objects.all()
    authPerson_list = [] # will store all auth.per in here 

    for person in auth_person:
        authPerson_list.append({
            "name": person.auth_name,
            "data_status" : person.data_status,
            "data_user" : '',
        })
        
    json_person = {"authPerson": authPerson_list}
    my_json = json.dumps(json_person, indent=1)

    with open('staticfiles/authorizedPersonJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "AuthPerson"

# create 'topicsJSON.json' file
def _createTopicsJSON():
    topics = Topic.objects.all()
    topics_list = [] # will store all topics and then go inside json_topic

    for t in topics:
        topics_list.append({
            "id": t.id, "_topic": t._topic,
            "data_status" : t.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "topics" : topics_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/topicsJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Topics"

# create 'categoriesJSON.json' file
def _createCategoriesJSON():
    categories = Category.objects.all()
    categories_list = [] # will store all categories and then go inside json file

    for c in categories:
        categories_list.append({
            "id": c.id,
            "_category": c._category,
            "data_status" : c.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "categories" : categories_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/categoriesJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Categories"


    # create 'statusJSON.json' file
def _createStatusJSON():
    status = Status.objects.all()
    status_list = [] # will store all status and then go inside json file

    for s in status:
        status_list.append({
            "id": s.id, 
            "_status": s._status,
            "data_status" : s.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "status" : status_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/statusJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Status"

    # create 'religionJSON.json' file
def _createReligionJSON():
    religion = Religion.objects.all()
    religion_list = [] # will store all religion and then go inside json file

    for r in religion:
        religion_list.append({
            "id": r.id, 
            "_sect": r._sect,
            "data_status" : r.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "religion" : religion_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/religionJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Religion"


    # create 'personJSON.json' file
def _createPersonJSON():
    person = Person.objects.all()
    person_list = [] # will store all person and then go inside json file

    for p in person:
        person_list.append({
            "id": p.id, 
            "_p_name": p._p_name,
            "_birth_year": p._birth_year, 
            "_death_year": p._death_year,
            "data_status" : p.data_status,
            "data_user" : '',
        })

    # will store topics json in here
    json_data = { "person" : person_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/personJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Persons"

    # create 'needJSON.json' file
def _createNeedJSON():
    need = Need.objects.all()
    need_list = [] # will store all need and then go inside json file

    for n in need:
        need_list.append({
            "id": n.id, 
            "_need": n._need,
            "data_status" : n.data_status,
            "data_user" : '',
        })

    # will store need json in here
    json_data = { "need" : need_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/needJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Need"

    # create 'languageJSON.json' file
def _createLanguageJSON():
    language = Language.objects.all()
    language_list = [] # will store all language and then go inside json file

    for l in language:
        language_list.append({
            "id": l.id, 
            "_language": l._language,
            "data_status" : l.data_status,
            "data_user" : '',
        })

    # will store language json in here
    json_data = { "language" : language_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('staticfiles/languageJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Language"

    # create 'bookJSON.json' file
def _createBookJSON():
    book = Book.objects.all()
    book_list = [] # will store all book and then go inside json file

    for b in book:
        book_list.append({
            "id": b.id,
            "name": b.name, 
            "author": str(b.author),
            "sect": str(b.sect),
            "cat": str(b.cat), 
            "status": str(b.status), 
            "need": str(b.need), 
            "lang": str(b.lang),
            "data_status" : b.data_status,
            "data_user" : '',
        })
    
    # will store language json in here
    json_data = { "book" : book_list }
    
    # convert into json data
    my_json = json.dumps(json_data, indent=1)
    
    with open('staticfiles/bookJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Book"


    # create 'referenceJSON.json' file
def _createReferenceJSON():
    reference = Reference.objects.all()
    reference_list = [] # will store all reference and then go inside json file
    
    for r in reference:
        reference_list.append({
            "id": r.id,
            "subject": str(r.subject),
            "speaker" : str(r.speaker),
            "personFor" : str(r.personFor),
            "book" : str(r.book),
            "vol_para" : r.vol_para,
            "page_chapter" : r.page_chapter,
            "hadees_verse" : r.hadees_verse,
            "description" : r.description,
            "data_status" : r.data_status,
            "data_user" : '',
        })

    # will store reference json in here
    json_data = { "reference" : reference_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=2)

    with io.open('staticfiles/referenceJSON.json', mode='w+', encoding="utf-16") as myFile:
        myFile.write(my_json)
    
    return "Reference"

def CreateJSONView(request):
    auth_person = auth_Person_Function(str(request.user))

    msg = []
    if request.method == "POST":
        # create Authorized Person File
        create_authPerson = _createAuthPersonJSON(request)
        msg.append(create_authPerson)
        # create Topics File
        created_file = _createTopicsJSON()
        msg.append(created_file)
        # create Categories File
        created_file = _createCategoriesJSON()
        msg.append(created_file)
        # create Status File
        created_file = _createStatusJSON()
        msg.append(created_file)
        # create Religion File
        created_file = _createReligionJSON()
        msg.append(created_file)
        # create Person File
        created_file = _createPersonJSON()
        msg.append(created_file)
        # create Need File
        created_file = _createNeedJSON()
        msg.append(created_file)
        # create Language File
        created_file = _createLanguageJSON()
        msg.append(created_file)
        # create Books File
        created_file = _createBookJSON()
        msg.append(created_file)
        # create References File
        created_file = _createReferenceJSON()
        msg.append(created_file)


    return render(request, 'haq/jsonFiles/createJson.html', {
        "auth_person": auth_person,
        "msg" : msg,
    })