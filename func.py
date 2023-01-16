import requests
import json
import argparse
from configparser import ConfigParser

def in_pages(listartif):
    page_size = 10
    choice = "n"
    m =1
    while choice != 'e':
        if choice == "n":
            for i in listartif[m:m+page_size]:
                print(i)
            choice = input()
        m +=page_size

def artifact_list(repo,host_jfrog,username_jfrog,password_jfrog):
    artiflist = requests.get(f'{host_jfrog}/api/storage/{repo}', auth = (username_jfrog, password_jfrog))
    try:
        datastr = artiflist.text
        data = json.loads(datastr)
        datapars = data['children']
        artifacts=[]
        for x in datapars:
            artifacts.append(x['uri'])
        return artifacts
    except: 
        print("List-failed.")





def print_artif_list_pages(listartif,repo):
    print ("Next page-n")
    print ("Exit-e\n")
    print(f'Artifacts({repo}):')
    in_pages(listartif)


def print_artif_list(listartif,repo):
    print(f'Artifacts({repo}):')
    for i in listartif:
            print(i)


def add_artifact(repo,host_jfrog,username_jfrog,password_jfrog, file_name, file_f):
    try:
        files = {'file': open(file_f, 'rb')}
        artifput = requests.put(f'{host_jfrog}/{repo}/{file_name}', auth = (username_jfrog, password_jfrog), files = files)
        print(f'\nThe file ({file_f}) is added. {host_jfrog}/{repo}/{file_name}')
        print('.....................')
    except:
        print("Add-failed. Enter the file name for Artifactory(-n) and valid file name to open(-f).")


def delete_artifact(repo,host_jfrog,username_jfrog,password_jfrog,file_name):
    try:
        artifdelete = requests.delete(f'{host_jfrog}/{repo}/{file_name}', auth = (username_jfrog, password_jfrog))
        print(f'\nThe file ({file_name}) is deleted.')
        print('.....................')
    except:
        print("Delete-failed. Enter the file name for Artifactory(-n).")