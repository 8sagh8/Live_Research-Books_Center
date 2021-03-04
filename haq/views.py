from YaMehdiData.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
import json

# Topics
def topic():
    all_topics = Topic.objects.all()
    list_size = 0
    if len(all_topics) != 0:
        list_size = len(all_topics)

    return (all_topics, list_size )


# About page
def AboutView(request):
    list_Authorized_People = Authorized_Person.objects.all()
    topics = Topic.objects.all()
    references = Reference.objects.all()
    books = Book.objects.all()
    categories= Category.objects.all()

    list_about = []

    list_about.append(('Topics', topics.count()))
    list_about.append(('References', references.count()))
    list_about.append(('Books', books.count()))
    list_about.append(('Categories', categories.count()))

    return render(request, 'haq/about.html', {
        "auth_persons": list_Authorized_People,
        "all_details": list_about,
    })



# to search a Topic in database
def TopicSearchView(request):
    temp = topic()
    _searchWord = None
    list_Authorized_People = Authorized_Person.objects.all()
    all_topic = Topic.objects.all()
    found_list = []  #will be sent to html page
    _length_found = 0 #length of the list found

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        _len_search = len(_searchWord)

        if _len_search < 3:
            return render(request, 'haq/topicSearch.html', {
                "auth_persons": list_Authorized_People,
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
            "auth_persons": list_Authorized_People,
            "length_found": length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })
       
    else:
        new_topic_list = []
        
        for t in all_topic:
            new_topic_list.append(t)

        new_topic_list.reverse()

        return render(request, 'haq/topicSearch.html', {
            "auth_persons": list_Authorized_People,
            "all_topics": new_topic_list,       
        })

# to Get references of a Topic in database
def GetTopicView(request, topic_id):
    topic_name = get_object_or_404(Topic, pk=topic_id)
    all_refer = Reference.objects.all()
    list_Authorized_People = Authorized_Person.objects.all()
    new_refer_list = [] 

    for reference in all_refer:
        if (topic_name == reference.subject):
            new_refer_list.append(reference)

    return render(request, 'haq/referencesByTopic.html', {
        "auth_persons": list_Authorized_People,
        'topic': topic_name,
        'refer': new_refer_list
        })

# main Index Page
def IndexView(request):
    list_Authorized_People = Authorized_Person.objects.all()
    temp = Topic.objects.all()
    reference = Reference.objects.all()
    reference = reversed(list(reference))
    return render(request, 'haq/index.html', {
        "auth_persons": list_Authorized_People,
        "all_topics": temp[0], 
        "list_size": temp[1],
        "reference": reference
    })



# Searching for References
def SearchRefView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
                "auth_persons": list_Authorized_People,
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
            "auth_persons": list_Authorized_People,
            "length_found" : length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })


# Books page
def BookView(request):
    temp = topic()
    list_Authorized_People = Authorized_Person.objects.all()
    all_books = Book.objects.all()
    new_list = []
    new_set = set()
    final_list = []

    for book in all_books:
        new_set.add(book.name)
        new_list.append(book)

    for _set in new_set:
        for i, _list in enumerate(new_list):
            if _list.name == _set:
                final_list.append(_list)
                new_list.pop(i)
                break
            
    return render(request, 'haq/books.html', {
        "auth_persons": list_Authorized_People,
        'final_list': final_list,
        "all_topics": temp[0],
        "list_size": temp[1]
       })


# Searching for Books
def BookSearchView(request):
    temp = topic()
    _searchWord = None
    list_Authorized_People = Authorized_Person.objects.all()
    all_book = Book.objects.all()
    found_list = []  #will be sent to html page
    _length_found = 0 #length of the list found

    if request.method == "POST":
        _searchWord = request.POST['searchWord']
        _len_search = len(_searchWord)

        if _len_search < 3:
            return render(request, 'haq/searchRef.html', {
                "auth_persons": list_Authorized_People,
                "size": _len_search,
                "all_topics": temp[0],
                "list_size": temp[1]
            })

        else:
            for book in all_book: # getting single reference from all list of references
                _flag = False
                book_list = []

                book_list.append(str(book.name))

                for _word in book_list:
                    _len_word = len(_word)
                    _start_point = 0
                    _end_point = _len_search

                    if _len_word >= _len_search:
                        while (_end_point <= _len_word):
                            if _word[_start_point : _end_point].lower() == _searchWord.lower():
                                found_list.append(book)
                                _flag = True
                                break;
                            else:
                                _start_point += 1
                                _end_point += 1
                    
                    if _flag == True:
                        break;

            length_found = len(found_list)

    
        return render(request, 'haq/bookSearch.html', {
            "auth_persons": list_Authorized_People,
            "length_found": length_found,
            "found_list" : found_list,
            "all_topics": temp[0],
            "list_size": temp[1]
        })
    else:
        return render(request, 'haq/bookSearch.html', {
            "auth_persons": list_Authorized_People,
            "all_topics": temp[0],
            "list_size": temp[1]
        })


# Category(ies) page
def CategoryView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_cat': dict_cat,
       })


# Language page
def LanguageView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_lang': dict_lang,
       })

# Needs page
def NeedView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_need': dict_need,
       })

# Personalities page
def PersonalityView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_person': dict_person,
       })

# Religions page
def ReligionView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_religion': dict_religion,
       })

# Status page
def StatusView(request):
    list_Authorized_People = Authorized_Person.objects.all()
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

    return render(request, 'haq/status.html', {
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_status': dict_status,
       })

###########################################
###########################################
###########################################


# BookSectView -- Display Books List Sect-Wise
def BookSectOptionView(request):
    temp = topic()
    all_sects = Religion.objects.all()
    _size = len(all_sects)
    print(_size)
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
        print("==> bNeed: ", bNeed)
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
    print("   ==> haqAPI", flush=True)
    # return redirect("intoJSON/")

    list_Authorized_People = Authorized_Person.objects.all()
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

    return render(request, 'haq/status.html', {
        "auth_persons": list_Authorized_People,
        'total_books': total_books,
        'dict_status': dict_status,
       })


# TopicJSONView -- TRIAL!!! getting Topic from JSON files
def TopicJSONView(request):

    file_obj = open('haq/static/haq/json_files/topics.json')
    data_dict = json.load(file_obj)

    for d in data_dict['topics']:
        print(d, flush=True)
    
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