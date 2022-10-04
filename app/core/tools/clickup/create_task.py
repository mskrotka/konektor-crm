from core.tools.post_api import post_api


def create_task_clickup(url, data, token):
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": token
    }
    task_id = post_api(url, data, headers).json()
    return task_id["id"]