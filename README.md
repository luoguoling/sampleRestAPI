This is sample rest API using django(https://docs.djangoproject.com/) and django-piston (https://bitbucket.org/jespern/django-piston/).


* Install python 2.7+
* Install pip first : http://jpython.blogspot.com/search/label/pip
* pip install django
* pip install django-piston



#### Running the project:
+ python manage.py syncdb
+ python manage.py runserver


Some API call example:

#### Book API:

+ http://127.0.0.1:8000/myapi/getbook/1/
+ http://127.0.0.1:8000/myapi/getbook/1/xml/

+ http://127.0.0.1:8000/myapi/allbook/
+ http://127.0.0.1:8000/myapi/allbook/xml/

+ http://127.0.0.1:8000/myapi/category/1/
+ http://127.0.0.1:8000/myapi/category/1/xml/

## Book API(Extended):

+ http://127.0.0.1:8000/myapi/extend/allbook/
+ http://127.0.0.1:8000/myapi/extend/allbook/xml/
+ http://127.0.0.1:8000/myapi/extend/category/1/ # books of category 1
+ http://127.0.0.1:8000/myapi/extend/category_name/child/ # books of category name child


Resources:
+ http://www.djangobook.com/en/2.0/index.html
+ jpython.blogspot.com