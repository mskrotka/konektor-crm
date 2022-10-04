import requests

def get_api_clickup_response(list_id, token):
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/field"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": token
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return data


def get_custom_fields(name_source, list, token, field):
    try:
        data = get_api_clickup_response(list, token)
        get_data = data.get("fields", {})
        get_data = [item for item in get_data if item["name"] == field]
        get_data = [item for item in get_data[0]["type_config"]["options"]]
        get_source = [item["id"] for item in get_data if item["name"] == name_source]
        source_id = get_source[0]
    except IndexError:
        source_id = False

    return source_id

def check_exist(list, token, field):
    try:
        data = get_api_clickup_response(list, token)
        get_data = data.get("fields", {})
        search_data = [item for item in get_data if item["name"] == field]
        search_data[0]
        exist = True
    except IndexError:
        exist = False

    return exist
