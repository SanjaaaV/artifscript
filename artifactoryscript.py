import requests
import json
import argparse
from configparser import ConfigParser

parser = argparse.ArgumentParser(description="Jenkins server")
parser.add_argument("-a", "--action", metavar="", help="add, delete, list")
parser.add_argument(
    "-f", "--file_name", metavar="", help="Enter the file name."
)
parser.add_argument(
    "-r", "--repo", metavar="", help="Enter the repository key in artifactory."
)
#parser.add_argument("-r", "--repo_to_list", metavar="", help="Enter repo_key to list the artifacts.")
args = parser.parse_args()


config = ConfigParser()
config.read("parametersjfrog.ini")

config_data = config["JFROG"]
host_jfrog = config_data["hostjfrog"]
username_jfrog = config_data["usernamejfrog"]
password_jfrog = config_data["passwordjfrog"]
url_projects = config_data["url_projects"]





#authentication-JFROG
artifserver = requests.get(host_jfrog, auth = (username_jfrog, password_jfrog))
print(f'Status(auth): {artifserver.status_code}')
#print(artifserver.text)
print('.....................\n')


def create_list(repo,host_jfrog,username_jfrog,password_jfrog):
    artiflist = requests.get(f'{host_jfrog}api/storage/{repo}', auth = (username_jfrog, password_jfrog))
    print(f'Status(list): {artiflist.status_code}\n')
    datastr = artiflist.text
    data = json.loads(datastr)
    datapars = data['children']
    print(f'Artifacts({repo}):')
    for x in datapars:
    	print(x['uri'])



action = args.action
repo = args.repo
if action == 'add':
    file_name = args.file_name
    files = {'file': open('artiffile', 'rb')}
    artifpost = requests.put(f'{host_jfrog}{repo}/{file_name}', auth = (username_jfrog, password_jfrog), files = files)
    print(f'{host_jfrog}{repo}/{file_name}')
    print(f'Status(add): {artifpost.status_code}\n')
    print('.....................\n')

elif action == 'list':
    create_list(repo,host_jfrog,username_jfrog,password_jfrog)
    print('.....................\n')

elif action == 'delete':
    file_name = args.file_name
    artifdelete = requests.delete(f'{host_jfrog}{repo}/{file_name}', auth = (username_jfrog, password_jfrog))
    print(f'Status(delete): {artifdelete.status_code}\n')
    create_list(repo,host_jfrog,username_jfrog,password_jfrog)
    print('.....................\n')

   