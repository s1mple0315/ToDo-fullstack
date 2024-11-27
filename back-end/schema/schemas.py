def individual_serial(todo) -> dict:
    return {
        "id" : str(todo["_id"]),
        "name" : todo["name"],
        "description" : todo["description"],
        "complete" : todo["complete"]
    }
    
def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]

def user_serial(user) -> dict:
    return {
        "id" : str(user["_id"]),
        "username" : user["username"],
        "email" : user["email"]
    }