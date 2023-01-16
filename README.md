## ARTIFSCRIPT PROJECT

## Description
This project is the Python script for interaction with the FJrog Artifactory.
It allows you to add, delete, or list the repository's artifacts in pages (10 artifacts per page) or all of them on one page. 
The JFrog REST API and the Python requests library were used. 

## Pull  files
- Pull this Git repository with the following command:
```
cd existing_repo
git remote add origin http://192.168.10.200:8083/svukelic/artifscript.git
git branch -M main
git pull origin main
```

## To run the script at the command prompt, enter the following commands:
```
py artifactoryscript.py -a <action> -repo <repository_in_artifactory> 
```
## Options are:
  -h, --help         show this help message and exit
  -a , --action      Enter the action to execute. (add, delete, list, plist)
  -r , --repo        Enter the repository key in Artifactory.
  -f , --file_f      Enter the file name to open. (It is required if you choose to add an artifact.)
  -n , --file_name   Enter the file name for Artifactory.(It is required if you choose to add or delete an artifact.)
  
    *** add- to add an artifact
    delete - to delete an artifact 
    list- to list all artifacts of repository
    plist- to list artifact of repository in pages (10 artifacts per page)***





