# Store
![Status](https://img.shields.io/badge/status-Early_Development-orange)

E-Commerce store built with Django, very basic atm, missing most functions. 

![Home](images/home.png)

![Products](images/products.png)

![Responsive](images/responsive.png)

# Installation

## Prerequisites:
- Python 3.13.1+
- PostgreSQL 17.2+
- pip

### Clone
```bash
git clone https://github.com/lllDavid/store
```

### Change Directory
```bash
cd store
```

### Setup venv

### Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
### Windows 
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

# Setup PostgreSQL

## Linux
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

## Windows
- Download and install PostgreSQL: https://www.postgresql.org/download/

## Create User

### Linux
#### Use postgres user
```bash
sudo -i -u postgres
```

```bash
psql -U postgres
```

```bash
ALTER USER postgres PASSWORD 'root';
```
#### Create new user
```bash
CREATE USER username WITH PASSWORD 'password';
```
(Remember to adjust config below)


## Create Database 
```bash
CREATE DATABASE store_db;
```
- This is my db config in Django:
- 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store_db',  
        'USER': 'postgres',  
        'PASSWORD': 'root',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    }
}

# Apply Database migrations
```bash
python manage.py migrate
```

# Run
```bash
python manage.py runserver
```

- To access admin panel:
```bash
python manage.py createsuperuser
```

- Access panel at (Might need to set admin account):
http://127.0.0.1:8000/admin/

