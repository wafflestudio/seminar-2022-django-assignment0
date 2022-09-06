# Assignment 0 | Problem 2 : Django Tutorial 

설문 조사 앱 만들기.

## Common


To run local server, 

```shell
$ python manage.py runserver {Port Number: 8000}
```
local url : http://127.0.0.1:8000  
#
  

## Part 1
- Django 설치 및 프로젝트 빌드
- 새로운 App 추가

To create new app
```shell
$ python manage.py startapp {App Name: polls}
```

#

## Part 2
- settings.py 기초적 이해
- model 정의 및 활성화
- django manage.py 가 제공하는 기초 기능들

Basic Commands
```shell
# make migrations for changed model
$ python manage.py makemigrations {App Name: polls}

# apply migrations
$ python manage.py migrate

# if you want to check executed sql query
$ python manage.py sqlmigrate {App Name: polls} {migration number : 0001}

# if you want to check project without changing DB
$ python manage.py check

# if you run python shell on django project environment
$ python manage.py shell

# if you want to create admin user
$ python manage.py createsuperuser
```

## Part 3

## Part 4

## Part 5

## Part 6

## Part 7