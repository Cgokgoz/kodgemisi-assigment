import requests

bitbucket_url = 'http://localhost:7990/Bitbucket/rest/api/1.0/projects'
jira_url = 'http://localhost:8080/JIRA/rest/api/2/project/'
headers = {'Content-Type': 'application/json'}
bitbucket_username = 'caglagokgoz'
bitbucket_password = 'password'
jira_username = 'caglagokgoz'
jira_password = 'password'


# options = {
#    'server': 'http://localhost:8080/JIRA'}
# jira = JIRA(options, basic_auth=(jira_username, jira_password))
# projects = jira.projects()


def get_jira_projects():
    r = requests.get(jira_url, auth=(jira_username, jira_password), headers=headers)
    status_code = r.status_code
    if 200 <= status_code < 300:

        if r.json() is not None:
            print(f'Jira returned {len(r.json())} projects.')
            return r.json()
    else:
        print(f'Cannot retrieve jira projects! Return code {status_code}')

    return []


def create_bitbucket_project(key, name):
    json = {
        "key": key,
        "name": name
    }

    r = requests.post(bitbucket_url, json=json, auth=(bitbucket_username, bitbucket_password), headers=headers)
    status_code = r.status_code
    if 200 <= status_code < 300:
        print(f'Created a bitbucket project key : {key} , name: {name}')
    else:
        print(f'Cannot create a bitbucket project key : {key} , name: {name}')


projects = get_jira_projects()

for project in projects:
    key = project.get('key')
    name = project.get('name')
    create_bitbucket_project(key, name)
