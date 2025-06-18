# Store

- This project replicates an online store experience, allowing users to browse products, view product details, manage cart contents, and handle account login and registration.

## Features
- Product Grid View
- Product Details View
- Product Search Functionality
- Register User
- Login/Logout User
- Forgot Password Functionality
- Add Products to Cart (Custom Quantity)
- Cart Overview
- Checkout Functionality (Missing Actual Payment/Shipping Process)

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

## Installation
You can set up the **Store** using **Git**.

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
```bash
CREATE DATABASE store_db;
```
- Exact **DB Config** is located in: store/settings.py

### 6. Apply Database migrations
```bash
python manage.py migrate
```
### 7. Run the Application
```bash
python manage.py runserver

```
### This will start the App at: [http://127.0.0.1:5000](http://127.0.0.1:5000)