import json 

def get_json_from_script(data):
    begin_of_json_index = data.find('>')
    end_of_json_index = data.find('</')
    data = data[begin_of_json_index+1:end_of_json_index]
    data_json = json.loads(data)
    return data_json

def get_info_from_json(data, *sections):
    data_json = get_json_from_script(data)
    for section in sections:
        data_json = data_json[section]
    return data_json
    
