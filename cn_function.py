import json

import cloudinary

cloudinary.config(
    cloud_name='akaton6',
    api_key='932415597598148',
    api_secret='_mEs3TgwRoZoJblmRCbJq03ZkXU'
)


def open_file():
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        f.close()
        return data


def delete_photo(id):
    cloudinary.uploader.destroy(id)


def login(username, password):
    data = open_file()
    for i in data:
        if "cn" + i['personal_summary']['id'] == username:
            if i['personal_summary']['password'] == password:
                return True
    print("The username or password are incorrect")
    return False


def register(json_cv):
    try:
        with open(json_cv)as f:
            cv = json.load(f)
    except Exception as e:
        print(e)
    else:
        f.close()
        data = open_file()
        data.append(cv)
        f = open('DATA.json', 'w')
        json.dump(data, f)
        f.close()
        # upload_photo(cv)
        return True


def delete_cv(id):
    data = open_file()
    flag = 0
    for i in data:
        if i['personal_summary']['id'] == id:
            if i['HR']['status'] == 2:
                flag = 1
                data.remove(i)
                delete_photo(id)
            break
    try:
        f = open('DATA.json', 'w')
    except Exception as e:
        print(e)
    else:
        json.dump(data, f)
        f.close()
        if flag:
            return True
        else:
            print("this id doesnt exist or status!=2")
            return False

# akaton 3
def change_time(id, new_time):
    flag = 0
    data = open_file()
    for i in data:
        if i['personal_summary']['id'] == id:
            flag = 1
            i['personal_summary']['time_to_reach'] = new_time
            break
    try:
        f = open('DATA.json', 'w')
    except Exception as e:
        print(e)
    else:
        json.dump(data, f)
        f.close()
        if flag:
            return True
        return False
def change_mobile(id, new_mobile):
    flag = 0
    data = open_file()
    for i in data:
        if i['personal_summary']['id'] == id:
            flag = 1
            i['personal_summary']['mobile'] = new_mobile
            break
    try:
        f = open('DATA.json', 'w')
    except Exception as e:
        print(e)
    else:
        json.dump(data, f)
        f.close()
        if flag:
            return True
        return False


def change_mail(id, new_mail):
    flag = 0
    data = open_file()
    for i in data:
        if i['personal_summary']['id'] == id:
            flag = 1
            i['personal_summary']['email'] = new_mail
            break
    try:
        f = open('DATA.json', 'w')
    except Exception as e:
        print(e)
    else:
        json.dump(data, f)
        f.close()
        if flag:
            return True
        return False
