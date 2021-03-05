from YaMehdiData.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
import json
import io

##########################################################
# ~~~~~ Fetch Dictionary Typed Data from Files ~~~~~~~~~ #
##########################################################

#  Fetch data from 'topicsJSON.json' File 
def get_topics_json():
    file_obj = open('haq/static/haq/json_files/topicsJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'categoriesJSON.json' File 
def get_categories_json():
    file_obj = open('haq/static/haq/json_files/categoriesJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'statusJSON.json' File 
def get_status_json():
    file_obj = open('haq/static/haq/json_files/statusJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'religionJSON.json' File 
def get_religion_json():
    file_obj = open('haq/static/haq/json_files/religionJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'personJSON.json' File 
def get_person_json():
    file_obj = open('haq/static/haq/json_files/personJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'needJSON.json' File 
def get_need_json():
    file_obj = open('haq/static/haq/json_files/needJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'languageJSON.json' File 
def get_language_json():
    file_obj = open('haq/static/haq/json_files/languageJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'bookJSON.json' File 
def get_book_json():
    file_obj = open('haq/static/haq/json_files/bookJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'referenceJSON.json' File 
def get_reference_json():
    file_obj = open('haq/static/haq/json_files/referenceJSON.json', encoding='utf-16')
    data_dict = json.load(file_obj)
    file_obj.close()

    return data_dict
################################################
# ~~~~~ General Functions ~~~~~~~~~ #
################################################
# Authorized Person ## auth_person = auth_Person_Function(str(request.user))
def auth_Person_Function(current_user_name):
    #  Fetch data from 'authorizedPersonJSON.json' File 
    file_obj = open('haq/static/haq/json_files/authorizedPersonJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()

    for person in data_dict.values():
        for p in person:
            for auth_per in p.values():
                if (current_user_name == auth_per):
                    return "Authorized Person"
    return False

# Topics
def topic():
    all_topics = Topic.objects.all()
    list_size = 0
    if len(all_topics) != 0:
        list_size = len(all_topics)

    return (all_topics, list_size )

################################################
# ~~~~~ General VIEWS ~~~~~~~~~ #
################################################

# About page
def get_count(_dict):
    count = 0
    for value_list in _dict.values():
        for value in value_list:
            count += 1
    return count

def AboutView(request):
    auth_person = auth_Person_Function(str(request.user))
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
    
    return render(request, 'haq/about.html', {
        "auth_person": auth_person,
        "all_details": list_about,
    })

# Status page
def StatusView(request):
    auth_person = auth_Person_Function(str(request.user))
    status = get_status_json()
    all_books = get_book_json()
    dict_status = {}
    total_books = 0
    
    for status_list in status.values():
        for status_dict in status_list:
            for status in status_dict.values():
                counter = 0

                for book_list in all_books.values():
                    for book in book_list:
                        if (status == str(book['status'])):
                            counter += 1
                            if len(dict_status) == 0:
                                dict_status= {status: [status_dict['id'], counter]}
                            elif status in dict_status.keys():
                                dict_status[status] = [status_dict['id'], counter]
                            else:
                                dict_status[status] = [status_dict['id'], counter]
                total_books += counter

    return render(request, 'haq/pages/status.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_status': dict_status,
       })

# get Books by Status
def GetStatusBooksView(request, status_id):
    auth_person = auth_Person_Function(str(request.user))
    status_name = get_object_or_404(Status, pk=status_id)
    all_books = get_book_json()
    new_books_list = [] 

    for books_list in all_books.values():
        for book in books_list:
            if str(status_name) == book['status']:
                new_books_list.append(book)

    new_books_list.reverse()

    return render(request, 'haq/pages/books.html', {
        "auth_person": auth_person,
        'status': status_name,
        'books': new_books_list
        })

    
# Books page
def BookView(request):
    auth_person = auth_Person_Function(str(request.user))
    all_books = get_book_json()
    final_list = []

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        for books in all_books.values():
            for book in books:      
                for v in book.values():
                    if _searchWord.lower() in str(v).lower():
                        final_list.append(book)
    else:
        for books in all_books.values():
            for book in books:
                final_list.append(book)
    final_list.reverse()
    return render(request, 'haq/pages/books.html', {
        "auth_person": auth_person,
        'status' : False, # the status is used by search by status, see 'GetStatusBooksView' 
        'books': final_list,
       })




################################################
# ~~~~~ END -- General VIEWS ~~~~~~~~~ #
################################################





# to search a Topic in database
def TopicSearchView(request):
    data_dict = get_topics_json() # get topics from json file

    
    auth_person = auth_Person_Function(str(request.user))

    temp = topic()
    _searchWord = None
    all_topic = Topic.objects.all()
    found_list = []  #will be sent to html page
    _length_found = 0 #length of the list found

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        _len_search = len(_searchWord)

        if _len_search < 3:
            return render(request, 'haq/topicSearch.html', {
                "auth_person": auth_person,
                "size": _len_search,
                "all_topics": temp[0],
                "list_size": temp[1]
            })

        else:
            for tp in all_topic: # getting single reference from all list of references
                _flag = False
                ttp = str(tp)
                _len_word = len(ttp)
                _start_point = 0
                _end_point = _len_search

                if _len_word >= _len_search:
                    while (_end_point <= _len_word):
                        if ttp[_start_point : _end_point].lower() == _searchWord.lower():
                            found_list.append({'tp_id': tp.id, 'tp_name': ttp})
                            _flag = True
                            break;
                        else:
                            _start_point += 1
                            _end_point += 1
            

            length_found = len(found_list)
            
        return render(request, 'haq/topicSearch.html', {
            "auth_person": auth_person,
            "length_found": length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })
       
    else:
        new_topic_list = []

        for d in data_dict.values():
            for v in d:
                new_topic_list.append({v['id'] : v['_topic']})

        new_topic_list.reverse()         

        return render(request, 'haq/topicSearch.html', {
            "auth_person": auth_person,
            # "all_topics": new_topic_list,  
            "all_topics": new_topic_list,      
        })

# to Get references of a Topic in database
def GetTopicView(request, topic_id):
    topic_name = get_object_or_404(Topic, pk=topic_id)
    all_refer = Reference.objects.all()
    auth_person = auth_Person_Function(str(request.user))
    new_refer_list = [] 

    for reference in all_refer:
        if (topic_name == reference.subject):
            new_refer_list.append(reference)

    return render(request, 'haq/referencesByTopic.html', {
        "auth_person": auth_person,
        'topic': topic_name,
        'refer': new_refer_list
        })

# main Index Page
def IndexView(request):
    auth_person = auth_Person_Function(str(request.user))
    temp = Topic.objects.all()
    reference = Reference.objects.all()
    reference = reversed(list(reference))
    return render(request, 'haq/index.html', {
        "auth_person": auth_person,
        "all_topics": temp[0], 
        "list_size": temp[1],
        "reference": reference
    })



# Searching for References
def SearchRefView(request):
    auth_person = auth_Person_Function(str(request.user))
    temp = topic()
    _searchWord = None
    all_ref = Reference.objects.all()
    found_list = []  #will be sent to html page
    length_found = 0 #length of found list

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        _len_search = len(_searchWord)


        if _len_search == 0 and _len_search < 3:
            return render(request, 'haq/searchRef.html', {
                "auth_person": auth_person,
                "size": _len_search
            })


        else:
            if _len_search > 2:
                for ref in all_ref: # getting single reference from all list of references
                    _flag = False
                    ref_list = []

                    ref_list.append(str(ref.subject))
                    ref_list.append(str(ref.speaker))
                    ref_list.append(str(ref.personFor))
                    ref_list.append(str(ref.book))
                    ref_list.append(str(ref.vol_para))
                    ref_list.append(str(ref.page_chapter))
                    ref_list.append(str(ref.hadees_verse))
                    ref_list.append(str(ref.description))

                    for _word in ref_list:
                        _len_word = len(_word)
                        _start_point = 0
                        _end_point = _len_search

                        if _len_word >= _len_search:
                            while (_end_point <= _len_word):
                                if _word[_start_point : _end_point].lower() == _searchWord.lower():
                                    found_list.append(ref)
                                    _flag = True
                                    break;
                                else:
                                    _start_point += 1
                                    _end_point += 1
                        
                        if _flag == True:
                            break;

                length_found = len(found_list) 

  
        return render(request, 'haq/searchRef.html', {
            "auth_person": auth_person,
            "length_found" : length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })






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

# Needs page
def NeedView(request):
    auth_person = auth_Person_Function(str(request.user))
    need = Need.objects.all()
    all_books = Book.objects.all()
    dict_need = {}
    total_books = 0

    for need in need:
        counter = 0
        dict_need[need] = counter

        for book in all_books:
            if (need == book.need):
                counter += 1
                dict_need[need] = counter
        
        total_books += counter


            
    return render(request, 'haq/needs.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_need': dict_need,
       })

# Personalities page
def PersonalityView(request):
    auth_person = auth_Person_Function(str(request.user))
    person = Person.objects.all()
    all_books = Book.objects.all()
    dict_person = {}
    total_books = 0

    for p in person:
        counter = 0
        dict_person[p] = counter

        for book in all_books:
            if (p == book.author):
                counter += 1
                dict_person[p] = counter
        
        total_books += counter


            
    return render(request, 'haq/personalities.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_person': dict_person,
       })

# Religions page
def ReligionView(request):
    auth_person = auth_Person_Function(str(request.user))
    religion = Religion.objects.all()
    all_books = Book.objects.all()
    dict_religion = {}
    total_books = 0

    for r in religion:
        counter = 0
        dict_religion[r] = counter

        for book in all_books:
            if (r == book.sect):
                counter += 1
                dict_religion[r] = counter
        
        total_books += counter

    return render(request, 'haq/religions.html', {
        "auth_person": auth_person,
        'total_books': total_books,
        'dict_religion': dict_religion,
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



# to search a PERSON in database
def PersonalitySearchView(request):
    temp = topic()
    _searchWord = None
    all_person = Person.objects.all()
    found_list = []  #will be sent to html page
    _length_found = 0 #length of the list found

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        _len_search = len(_searchWord)

        if _len_search < 3:
            return render(request, 'haq/personalitySearch.html', {
                "size": _len_search,
                "all_topics": temp[0],
                "list_size": temp[1]
            })

        else:
            for tp in all_person: # getting single reference from all list of references
                _flag = False
                tp = str(tp)
                _len_word = len(tp)
                _start_point = 0
                _end_point = _len_search

                if _len_word >= _len_search:
                    while (_end_point <= _len_word):
                        if tp[_start_point : _end_point].lower() == _searchWord.lower():
                            found_list.append(tp)
                            _flag = True
                            break;
                        else:
                            _start_point += 1
                            _end_point += 1
            

            length_found = len(found_list)

    
        return render(request, 'haq/personalitySearch.html', {
            "length_found": length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })
    else:
        return render(request, 'haq/personalitySearch.html', {
            "all_topics": temp[0],
            "list_size": temp[1]
        })


### Log out View

def LogOutView(request):
    auth.logout(request)
    return redirect("/")

def OSampleView(request):

    return render(request, 'haq/o_sample.html')

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


# TopicJSONView -- TRIAL!!! getting Topic from JSON files
def TopicJSONView(request):

    file_obj = open('haq/static/haq/json_files/topicsJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()

    return render(request, 'haq/topicJSON.html', {
        'data' : data_dict,
    })
    
# print("   ==> serverAPI", flush=True)
#     topics = Topic.objects.all()
#     topics_list = [] # will store all topics and then go inside json_topic

#     for t in topics:
#         topics_list.append({"id": t.id, "_topic": t._topic})

#     # will store topics json in here
#     json_topic = { "topics" : topics_list }
#     # convert into json data
#     my_json = json.dumps(json_topic, indent=1)

#     with open('serverAPI/static/json/topics.json', mode='w+') as myFile:
#         myFile.write(my_json)

#########################################
# ~~~~~ API Functions & VIEWS ~~~~~~~~~ #
#########################################

################################################
# ~~~~~ JSON FILES Functions & VIEWS ~~~~~~~~~ #
################################################
# create 'authorizedPersonJSON.json' file
def _createAuthPersonJSON():
    auth_person = auth_Person_Function(str(request.user))
    authPerson_list = [] # will store all auth.per in here 

    for person in list_Authorized_People:
        authPerson_list.append({"name": person.auth_name})

    json_person = {"authPerson": authPerson_list}
    my_json = json.dumps(json_person, indent=1)

    with open('haq/static/haq/json_files/authorizedPersonJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "AuthPerson"

# create 'topicsJSON.json' file
def _createTopicsJSON():
    topics = Topic.objects.all()
    topics_list = [] # will store all topics and then go inside json_topic

    for t in topics:
        topics_list.append({"id": t.id, "_topic": t._topic})

    # will store topics json in here
    json_data = { "topics" : topics_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/topicsJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Topics"

# create 'categoriesJSON.json' file
def _createCategoriesJSON():
    categories = Category.objects.all()
    categories_list = [] # will store all categories and then go inside json file

    for c in categories:
        categories_list.append({"id": c.id, "_category": c._category})

    # will store topics json in here
    json_data = { "categories" : categories_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/categoriesJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Categories"


    # create 'statusJSON.json' file
def _createStatusJSON():
    status = Status.objects.all()
    status_list = [] # will store all status and then go inside json file

    for s in status:
        status_list.append({"id": s.id, "_status": s._status})

    # will store topics json in here
    json_data = { "status" : status_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/statusJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Status"

    # create 'religionJSON.json' file
def _createReligionJSON():
    religion = Religion.objects.all()
    religion_list = [] # will store all religion and then go inside json file

    for r in religion:
        religion_list.append({"id": r.id, "_sect": r._sect})

    # will store topics json in here
    json_data = { "religion" : religion_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/religionJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Religion"


    # create 'personJSON.json' file
def _createPersonJSON():
    person = Person.objects.all()
    person_list = [] # will store all person and then go inside json file

    for p in person:
        person_list.append({"id": p.id, "_p_name": p._p_name,
        "_birth_year": p._birth_year, "_death_year": p._death_year})

    # will store topics json in here
    json_data = { "person" : person_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/personJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Persons"

    # create 'needJSON.json' file
def _createNeedJSON():
    need = Need.objects.all()
    need_list = [] # will store all need and then go inside json file

    for n in need:
        need_list.append({"id": n.id, "_need": n._need})

    # will store need json in here
    json_data = { "need" : need_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/needJSON.json', mode='w+') as myFile:
        myFile.write(my_json)
    
    return "Need"

    # create 'languageJSON.json' file
def _createLanguageJSON():
    language = Language.objects.all()
    language_list = [] # will store all language and then go inside json file

    for l in language:
        language_list.append({"id": l.id, "_language": l._language})

    # will store language json in here
    json_data = { "language" : language_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=1)

    with open('haq/static/haq/json_files/languageJSON.json', mode='w+') as myFile:
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
            "lang": str(b.lang)
        })
    
    # will store language json in here
    json_data = { "book" : book_list }
    
    # convert into json data
    my_json = json.dumps(json_data, indent=1)
    
    with open('haq/static/haq/json_files/bookJSON.json', mode='w+') as myFile:
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
            "description" : r.description
        })

    # will store reference json in here
    json_data = { "reference" : reference_list }
    # convert into json data
    my_json = json.dumps(json_data, indent=2)

    with io.open('haq/static/haq/json_files/referenceJSON.json', mode='w+', encoding="utf-16") as myFile:
        myFile.write(my_json)
    
    return "Reference"

def CreateJSONView(request):
    auth_person = auth_Person_Function(str(request.user))

    msg = []
    if request.method == "POST":
        # create Authorized Person File
        create_authPerson = _createAuthPersonJSON()
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