print('hr file')
import json
import textwrap


def printall():
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        for person in data:
            print('personal_summary:')
            print("     ID:" + person['personal_summary']['id'])
            print("     Name:" + person['personal_summary']['name'])
            print("     Email:" + person['personal_summary']['email'])
            print("     Gender:" + person['personal_summary']['gender'])
            print("     Pic:" + person['personal_summary']['pic'])
            print('\nAcademic history:')
            print('\n'.join(textwrap.wrap(person['academic_history'], 64)))
            print('\nExperience:')
            print('\n'.join(textwrap.wrap(person['experience'], 64)))
            print('\nSkills:')
            print('\n'.join(textwrap.wrap(person['skills'], 64)))
            print('\nCareer history:')
            print('\n'.join(textwrap.wrap(person['career_history'], 64)))
            print('\nReferences:')
            print('\n'.join(textwrap.wrap(person['references'], 64)))
            print('\nHR:')
            print("     Status:" + str(person['HR']['status']))
            print("     Notes:" + person['HR']['notes'])
        f.close()
        return True


def printid(id):
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        for person in data:
            if person['personal_summary']['id'] == str(id):
                print('personal_summary:')
                print("     ID:" + person['personal_summary']['id'])
                print("     Name:" + person['personal_summary']['name'])
                print("     Email:" + person['personal_summary']['email'])
                print("     Gender:" + person['personal_summary']['gender'])
                print("     Pic:" + person['personal_summary']['pic'])
                print('\nAcademic history:')
                print('\n'.join(textwrap.wrap(person['academic_history'], 64)))
                print('\nExperience:')
                print('\n'.join(textwrap.wrap(person['experience'], 64)))
                print('\nSkills:')
                print('\n'.join(textwrap.wrap(person['skills'], 64)))
                print('\nCareer history:')
                print('\n'.join(textwrap.wrap(person['career_history'], 64)))
                print('\nReferences:')
                print('\n'.join(textwrap.wrap(person['references'], 64)))
                print('\nHR:')
                print("     Status:" + str(person['HR']['status']))
                print("     Notes:" + person['HR']['notes'])
                # idmenu(person)
                f.close()
                return True
        f.close()
        print("this id is not in our data")
        return False


def editstatus(id, select):
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        for person in data:
            if person['personal_summary']['id'] == str(id):
                person['HR']['status'] = str(select)
                print("candidate status was cahnge to" + select)
                # json.dumps(data, f)
                f.close()
                try:
                    f = open('DATA.json', 'w')
                except Exception as e:
                    print(e)
                else:
                    json.dump(data, f)
                    f.close()
                    return True
        f.close()
        return False


def editnotes(id, select):
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        for person in data:
            if person['personal_summary']['id'] == str(id):
                person['HR']['notes'] = select
                print("candidate notes was cahnge !")
                f.close()
                try:
                    f = open('DATA.json', 'w')
                except Exception as e:
                    print(e)
                else:
                    json.dump(data, f)
                    f.close()
                    return True
        f.close()
        return False


def searchpro(pro):
    try:
        with open('DATA.json') as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    else:
        print("the id's with this professional are:\n")
        flag = 0
        for person in data:
            if pro in person['career_history']:
                flag = 1
                print("     ID:" + person['personal_summary']['id'])
        if flag == 1:
            return True
        else:
            print("None,there is no such professional in this data")
            return False
