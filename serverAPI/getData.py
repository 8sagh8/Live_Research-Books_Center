
##########################################################
# ~~~~~ Fetch Dictionary Typed Data from Files ~~~~~~~~~ #
##########################################################

import json
#  Fetch data from 'authorizedPersonJSON.json' File 
def get_authPerson_json():
    file_obj = open('staticfiles/authorizedPersonJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    
    return data_dict

#  Fetch data from 'topicsJSON.json' File 
def get_topics_json():
    file_obj = open('staticfiles/topicsJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    
    return data_dict

#  Fetch data from 'categoriesJSON.json' File 
def get_categories_json():
    file_obj = open('staticfiles/categoriesJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'statusJSON.json' File 
def get_status_json():
    file_obj = open('staticfiles/statusJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'religionJSON.json' File 
def get_religion_json():
    file_obj = open('staticfiles/religionJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'personJSON.json' File 
def get_person_json():
    file_obj = open('staticfiles/personJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'needJSON.json' File 
def get_need_json():
    file_obj = open('staticfiles/needJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'languageJSON.json' File 
def get_language_json():
    file_obj = open('staticfiles/languageJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'bookJSON.json' File 
def get_book_json():
    file_obj = open('staticfiles/bookJSON.json')
    data_dict = json.load(file_obj)
    file_obj.close()
    return data_dict

#  Fetch data from 'referenceJSON.json' File 
def get_reference_json():
    file_obj = open('staticfiles/referenceJSON.json', encoding='utf-16')
    data_dict = json.load(file_obj)
    file_obj.close()

    return data_dict