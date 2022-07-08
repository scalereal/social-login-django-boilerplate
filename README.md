# Social Login Django BoilerPlate
This repository contains minimal backend code required to get Social Authentication configured for your backend

## 💻 Development

### Requirements:

- Python >= 3.8 🐍
- Postgres 🐘

### 🗄️ Database Setup: 

Create Database named `social_login_db` from Postgres console. 

Refer [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04) article for more information on how to create database.

### 👨‍💻 Project Setup: 

- Clone this repository
- `$ cd social-login-django-boilerplate`
- `$ pip install pipenv` [(What is pipenv?)](https://realpython.com/pipenv-guide/)
- Enter the shell by typing `$ pipenv shell`
- Install dependencies by typing `$ pipenv install`
- Complete the steps mentioned in **Environment variables** section
- Run migrations `$ python manage.py migrate`
- Run local server `$ python manage.py runserver`

### 🔐 Environment variables: 

- Create file `.env` inside `social-login-django-boilerplate` directory
- Copy contents from `.env.example` file and paste it in the `.env` file you just created.
- After copying the contents, edit the `SECRET_KEY`, `DATABASE_USER` and `DATABASE_PASSWORD` with your respective key, user and password.
- In `DATABASE_URL`,  replace `your_database_user` and `your_database_password` with your respective Database User and Password.

