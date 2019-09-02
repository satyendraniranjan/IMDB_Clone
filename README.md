# Build a Movie Website with Python & Django

This is the supplementary cheat sheet document:

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Git](#git)
- [Virtual Environments](#virtual-environments)
- [Django Management Commands](#django-management-commands)

<!-- /TOC -->

## Git

Use the below Git commands in the Windows Command Prompt or macOS Terminal.

**Configure default email and name**

*Note: This only needs to be done the first time you use Git on your machine*

```
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
```

**Initialise a new Git repository**

```
git init
```

**Commit changes to Git**

```
git add .
git commit -am "Commit message"
```

**Set Git remote**

*Note: This only needs to be done once, the details are provided by GitHub after creating a new project*

```
git remote add origin <URL TO PROJECT>
git push -u origin master
```

**Push changes to GitHub**

```
git push origin
```

## SSH Key Management

The below commands are used to manage SSH keys on your local development machine.

**Checking for existing SSH key**

```
ls ~/.ssh/
```

**Print contents of public key**

```
cat ~/.ssh/id_rsa.pub
```

**Generate new SSH key on your local machine**

```
ssh-keygen -t rsa -b 4096 -C "EMAIL ADDRESS"
```


## Virtual Environments

The below commands are used for managing Virtual Environments using Python3-env. Use these commands when connected to your Vagrant server.

**Create new environment**

```
python -m venv ~/env
```

**Activate virtual environment**

```
source ~/env/bin/activate
```

**De-activate virtual environment**

```
deactivate
```

**Install requirements from requirements.txt**

*Note: Virtual environment must be activated*

```
pip install -r requirements.txt
```

## Django Management Commands

**Create new Django project**

```
django-admin.py startproject profiles_project  .
```

**Create new Django app**

```
python manage.py startapp profiles_api
```

**Start Django development server**

```
python manage.py runserver 0.0.0.0:8000
```

**Create database migrations file**

```
python manage.py makemigrations
```

**Run migrations**

```
python manage.py migrate
```

**Create new superuser**

```
python manage.py createsuperuser
```

**check install requirements**

```
pip freeze
```

