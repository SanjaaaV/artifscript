import requests
import json
import argparse
from configparser import ConfigParser
import func

parser = argparse.ArgumentParser(description="JFrog Artifactory")
parser.add_argument("-a", "--action", metavar="", choices=['add', 'delete', 'list', 'plist'], required = True)
parser.add_argument(
    "-f", "--file_f", metavar="", help="Enter the file name to open.")
parser.add_argument(
    "-n", "--file_name", metavar="", help="Enter the file name for Artifactory.")
parser.add_argument(
    "-r", "--repo", metavar="", help="Enter the repository key in Artifactory.", required = True)
args = parser.parse_args()


config = ConfigParser()
config.read("parametersjfrog.ini")
config_data = config["JFROG"]
host_jfrog = config_data["hostjfrog"]
username_jfrog = config_data["usernamejfrog"]
password_jfrog = config_data["passwordjfrog"]



if __name__ == "__main__":
    action = args.action
    repo = args.repo
    
       
    if  action == 'add':
        file_name = args.file_name
        file_f = args.file_f
        func.add_artifact(repo,host_jfrog,username_jfrog,password_jfrog,file_name, file_f)
        

    elif action == 'list':
        print('.....................')
        listartif = func.artifact_list(repo,host_jfrog,username_jfrog,password_jfrog)
        func.print_artif_list(listartif,repo)

    elif action == 'plist':
        print('.....................')
        listartif = func.artifact_list(repo,host_jfrog,username_jfrog,password_jfrog)
        func.print_artif_list_pages(listartif,repo)

    elif action == 'delete':
        file_name = args.file_name
        func.delete_artifact(repo,host_jfrog,username_jfrog,password_jfrog,file_name)
        
    


   