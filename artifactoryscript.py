import requests
import json
import argparse
from configparser import ConfigParser

parser = argparse.ArgumentParser(description="JFrog Artifactory")
parser.add_argument("-a", "--action", metavar="", help="add, delete, list")
parser.add_argument(
    "-f", "--file_f", metavar="", help="Enter the file name to open.")
parser.add_argument(
    "-n", "--file_name", metavar="", help="Enter the file name for Artifactory.")
parser.add_argument(
    "-r", "--repo", metavar="", help="Enter the repository key in Artifactory.")
args = parser.parse_args()


config = ConfigParser()
config.read("parametersjfrog.ini")
config_data = config["JFROG"]
host_jfrog = config_data["hostjfrog"]
username_jfrog = config_data["usernamejfrog"]
password_jfrog = config_data["passwordjfrog"]


#auth-JFROG
artifserver = requests.get(host_jfrog, auth = (username_jfrog, password_jfrog))
print(f'Status(auth): {artifserver.status_code}')
print('.....................\n')




#function - list repo
def create_list(repo,host_jfrog,username_jfrog,password_jfrog):
    artiflist = requests.get(f'{host_jfrog}api/storage/{repo}', auth = (username_jfrog, password_jfrog))
    statuslist = artiflist.status_code
    if statuslist == 200:
        datastr = artiflist.text
        data = json.loads(datastr)
        datapars = data['children']
        print(f'Artifacts({repo}):')
        for x in datapars:
            print(x['uri'])
    else: 
        print("List-failed.")



#main part
action = args.action
repo = args.repo
if action and repo and  action == 'add':
    file_name = args.file_name
    file_f = args.file_f
    if file_name and file_f:
        files = {'file': open(file_f, 'rb')}
        artifput = requests.put(f'{host_jfrog}{repo}/{file_name}', auth = (username_jfrog, password_jfrog), files = files)
        statusput = artifput.status_code
        if statusput == 201:
            print(f'The file ({file_f}) is added. {host_jfrog}{repo}/{file_name}')
            create_list(repo,host_jfrog,username_jfrog,password_jfrog)
            print('.....................\n')
        else: 
            print("Add-failed.")
    else:
        print("Enter the file name for Artifactory(-n) and the file name to open(-f).")



elif action and repo and action == 'list':
    create_list(repo,host_jfrog,username_jfrog,password_jfrog)
    print('.....................\n')


elif action and repo and action == 'delete':
    file_name = args.file_name
    if file_name:
        artifdelete = requests.delete(f'{host_jfrog}{repo}/{file_name}', auth = (username_jfrog, password_jfrog))
        statusdelete = artifdelete.status_code
        if statusdelete == 405 or statusdelete == 204:
            print(f'The file ({file_name}) is deleted.')
            create_list(repo,host_jfrog,username_jfrog,password_jfrog)
            print('.....................\n')
        else: 
            print("Delete-failed.")
    else:
        print("Enter the file name for Artifactory(-n).")


else:
    print ("Enter the action: (-a) add, delete, list. Enter the repository key in Artifactory (-r). ")
    print ("Argument '--help' for options.")

   