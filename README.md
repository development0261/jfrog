# Working on CLI in Python or Bash to manage an Artifactory SaaS instance via its API.

# Project Setup

Follow the given steps to setup the project

create a python virtual environment in src/python/backend

```
python3 -m venv .venv
```

activate the virtual environment

```
.venv\Scripts\activate
```

install the dependencies

```
pip install -r requirements.txt
```

run following commands project 

```
python main.py sdist upload -r local
OR
python main.py bdist_wheel upload -r local
```