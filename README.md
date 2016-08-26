# News
Apis to get and put news data in json format.
# Requirements
1. djangorestframework==3.3.3
2. django 1.9
3. Sqlite
# Usage
1. Clone the repo and run  using python manage.py runserver
2. Then hit the url 127.0.0.1:8000/apis/news/ to fetch the latest news from the database.You may pass language and count as     parameters otherwise default parameters are language="eng" and count as 10.
3. To enter new data, hit 127.0.0.1:8000/apis/new/ and params are title,language and body.
4. News are fetched according to insert_time in descending order.
