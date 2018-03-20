from chalice import Chalice
cors_config = True

app = Chalice(app_name='RestExample')
users = {'users': ['john', 'josh', 'nick', 'tyler']}


# DELETE deletes previous information
# delete a user
@app.route('/user', methods=['DELETE'], cors=cors_config)
def delete_user():
    json = app.current_request.json_body
    users['users'].remove(json['user'])
    return {'user_deleted': json['user']}

# POST adds new information
# adds new user
@app.route('/user', methods=['POST'], cors=cors_config)
def create_user():
    user_as_json = app.current_request.json_body
    users['users'].append(user_as_json['user'])
    return {'user_added': user_as_json['user']}


# PUT updates and replaces previous information
# update an old user info with a new user info
@app.route('/user', methods=['PUT'], cors=cors_config)
def replace_user():
    json = app.current_request.json_body
    users['users'].remove(json['user_old'])  # remove old user info
    users['users'].append(json['user_new'])  # add updated user info
    return {'user_updated': json['user_new']}

# GET returns information
# get all users currently saved
@app.route('/users', methods=['GET'], cors=cors_config)
def get_users():
    return users
