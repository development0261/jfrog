from datetime import datetime
import json
import sys
import requests
from artifactory import ArtifactoryPath
from requests.auth import HTTPBasicAuth

API_KEY = "AKCp8nG6BdwkZjY8vYSF9tRhwtezJycKzfvkkEk6jjLACFCTBXEGsMtizve4eFVyCfYVBFBAg"
USERNAME = "development0261@gmail.com"
PASSWORD = "AP9dyuzGSRM51vy5GyS8idpMghW3"
PASS="Test@123"
URL = "https://development0261.jfrog.io/artifactory/"

path = ArtifactoryPath(
    URL, auth=(USERNAME, PASSWORD),
)


def system_health_ping():
    url = str(path)+"/api/system/ping"
    print(url)

    header = {
        "api_key": API_KEY,
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASS))
    print(response.text)


def system_info():
    url = str(path)+"/api/storageinfo"
    print(url)

    header = {
        "api_key": API_KEY,
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASS))
    print(response.text)


def get_storage_info():
    url = str(path)+"/api/system"
    print(url)
    header = {
        "api_key": API_KEY,
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASS))
    print(response.text)


def create_repo(new_repository):

    get = "api/repositories"
    url = "https://development0261.jfrog.io/artifactory/"+get+"/"

    header = {
        "key": new_repository,
        "projectKey": "projx",
        "environments": str(["DEV", "PROD"]),
        "rclass": "remote",
        "packageType": "pypi",
        "url": url,
        "username": USERNAME,
        "password": PASSWORD,
        "proxy": "proxy1",
        "description": "Remote repository",
        "notes": "Remote repositor",
        "includesPattern": "pypi",
        "repoLayoutRef": "maven-2-default",
        "remoteRepoChecksumPolicyType": "generate-if-absent",
        "localAddress": "127.0.0.1",
        "propertySets": str(["ps1", "ps2"]),
        "externalDependenciesPatterns": str(["**/*microsoft*/**", "**/*github*/**"]),
        "feedContextPath": "api/v2",
        "downloadContextPath": "api/v2/package",
        "v3FeedUrl": "https://api.nuget.org/v3/index.json",
    }

    try:
        response = requests.get(url, auth=HTTPBasicAuth("development0261@gmail.com", "AP9dyuzGSRM51vy5GyS8idpMghW"),
                                headers=header)
        if response.status_code == 200:
            print("Repository Created Successfully")
            print('-'*50)
            print(response.text)

        elif response.status_code == 400:
            print("Repository Already Exists...")
        else:
            print("Something Went Wrong...")
            print("Repository not Created")
    except Exception as e:
        print(e)
        print("Something Went Wrong...")


def update_repo(repository):
    get = "api/repositories"
    url = "https://development0261.jfrog.io/artifactory/" + \
        get+" -H Content-Type: application/json"
    print(url)
    print("To Update the Repository Enter the Following Details:")
    print('='*50)
    project_key = input("Project Key (Default value is projx): ")
    environments = input("Environments in form of list: ")
    if type(environments) != list:
        environments = input("Please Add Enviroments in form of list: ")
    package_type = input("Package type (default is pypi): ")
    proxy = input("Proxy Value (Default is proxy1): ")
    description = input("Description: ")
    notes = input("Notes: ")
    localAddress = input("Local Address (Default is 127.0.0.1): ")
    print('='*50)
    header = {
        "key": repository,
        "projectKey": project_key if project_key != "" else "projex",
        "environments": str(environments) if environments != "" else "['DEV', 'PROD']",
        "rclass": "remote",
        "packageType": package_type if package_type != "" else "pypi",
        "url": url,
        "username": USERNAME,
        "password": PASSWORD,
        "proxy": proxy if proxy != "" else "proxy1",
        "description": description if description != "" else "",
        "notes": notes if notes != "" else "",
        "includesPattern": "pypi",
        "repoLayoutRef": "maven-2-default",
        "remoteRepoChecksumPolicyType": "generate-if-absent",
        "localAddress": localAddress if localAddress != "" else "127.0.0.1",
        "propertySets": str(["ps1", "ps2"]),
        "externalDependenciesPatterns": str(["**/*microsoft*/**", "**/*github*/**"]),
        "feedContextPath": "api/v2",
        "downloadContextPath": "api/v2/package",
        "v3FeedUrl": "https://api.nuget.org/v3/index.json",
    }

    try:

        response = requests.post(url, auth=HTTPBasicAuth("development0261@gmail.com", "AP9dyuzGSRM51vy5GyS8idpMghW"),
                                 headers=header)
        print(response.text)
        if response.status_code == 200:
            print("Repository Updated Successfully")
            print('-'*50)
            print(response.text)
        else:
            print("Something Went Wrong...")
            print("Repository not Created")
    except Exception as e:
        print(e)
        print("Something Went Wrong...")


def list_all_repo():

    header = {
         "api_key": API_KEY,
        "username": USERNAME,
        "password": PASSWORD,
    }
    try:
        url = str(path)+"/api/repositories"
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, "Pass"))
        print(response.content)

    except Exception as e:
        print(e)
        print("Something Went Wrong...")


def create_user(username, email, password):
    get = "api/security/users/"+username
    url = "https://development0261.jfrog.io/artifactory/"
    path=url+get
    _date = datetime.now().isoformat()
    
    header = {
        "name": username,
        "email" : email,
        "password": password,
        "disableUIAccess" : "true",
        "lastLoggedIn": _date,
        "realm": "ldap",
        "groups" :str([ "deployers", "users" ]),
        }
    try:

        response = requests.put(path, auth=(USERNAME, PASSWORD))

        if response == 200:
            print("User Created Successfully")
            print('-'*50)
            print(response.content)
        else:
            print(response.text)
    except Exception as e:
        print(e)
        print("Something Went Wrong...")


def delete_user(userName):
    url = "https://development0261.jfrog.io/api/security/users/"
    path=url+userName
    try:
        response = requests.delete(path, auth=(
            USERNAME, "AP9dyuzGSRM51vy5GyS8idpMghW"))
        if response.status_code == 200:
            print("User Record Deleted")
        else:
            print("User Record does not Deleted")
    except Exception as e:
        print("Something Went Wrong...")
        print(e)


def selection(args):
    if args == 1:
        system_info()
    elif args == 2:
        print("1.Create User\n 2.Delete User")
        args_val = int(input("Please enter: "))

        if args_val == 1:
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            create_user(username, email, password)
        elif args_val == 2:
            username = input("Username: ")
            delete_user(username)

    elif args == 3:
        print("1.Create Repository\n 2.Update Repository\n 3.List All Repository")
        args_val = int(input("Please enter: "))
        if args_val == 1:
            repository = input("Repository: ")
            create_repo(repository)
        elif args_val == 2:
            repository = input("Repository: ")
            update_repo(repository)
        elif args_val == 3:
            list_all_repo()

    elif args == 4:
        get_storage_info()
    elif args==5:
        system_health_ping()
    else:
        sys.exit()


print(" 1.Get System Info \n 2.User Details \n 3.Repo Details\n 4.Get Storage Information\n 5.System Health Ping Info.\n6.Quit")
args = int(input("Please enter: "))
selection(args)


