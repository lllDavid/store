# Store

- This project simulates an e-commerce platform where users can explore products, access detailed product information, manage their shopping cart, and perform account registration and authentication.

## Features
- Products displayed in a grid layout
- Individual product detail view
- Product search functionality
- User registration workflow
- User authentication (login/logout)
- Password reset capability
- Add products to cart with customizable quantity
- Cart overview interface
- Checkout process (Payment and Shipping Steps Not Included)

![Home](images/home.png)
![Products](images/products-grid.png)
![Product Details](images/product-details.png)
![Responsive](images/responsive.png)
![Cart](images/cart.png)
![Checkout](images/checkout.png)
![Register](images/register.png)
![Login](images/login.png)
![About](images/about.png)
![Contact](images/contact.png)

## Prerequisites:
- Python 3.13+
- PostgreSQL
- `pip`

## Setting up Environment Variables
Set your DB Configuration in a `.env` file in root dir

```env
DB_NAME=store_db
DB_USER=""
DB_PASSWORD=""
DB_HOST=localhost
DB_PORT=5432

POSTGRES_PASSWORD=""
POSTGRES_DB=store_db
```
## Installation
You can set up the **Store** in two ways: using **Git** or **Docker**.

## How to Use with Git

### 1. Clone the Repository
```bash
git clone https://github.com/lllDavid/store
```

### 2. Install dependencies
**Navigate to the directory:**
```bash
cd store
```

**Create a virtual environment:**
```bash
python -m venv venv
```


**Activate the virtual environment:**
```bash
.\venv\Scripts\activate
```


**Install requirements:**
```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL
**Download and install PostgreSQL from their official site:** [PostgreSQL](https://www.postgresql.org/download/)

Add PostgreSQL to **PATH** environment variable

### 4. Connect to Database

**Login to PostgreSQL Session**
```bash
psql -U postgres
```
### 5. Create Database 
```text
CREATE DATABASE store_db;
```

### 6. Apply Database migrations
```bash
python manage.py migrate
```
### 7. Run the Application
```bash
python manage.py runserver

```
### This will start the App at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## How to Use with Docker

#### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### 1. Clone the Repository

```bash
git clone https://github.com/lllDavid/store
```
### 2. **Navigate to the directory:**
```bash
cd store
```
### 3. Build and run the Container

```bash
docker-compose up 
```
### This will start the App at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

# Products
- The Products database is empty at the start.

### 1. Create a Superuser Account
You can create a superuser account to add your own products manually:
```bash
python manage.py createsuperuser # regular environment
```
```bash
docker exec -it store-app-1 python manage.py createsuperuser # Docker environment
```
### 2. Generate Random Products
Alternatively, generate a specified number of random products:
```bash
python manage.py create_products <n> # regular environment
```
```bash
docker exec -it store-app-1 python manage.py create_products <n> # Docker environment
```