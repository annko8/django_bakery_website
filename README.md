# Bakery Website

install dependecies
```
  pip freeze > requirements. txt
```

database migartions
```
  // load data in DB
  python manage.py loaddata fixtures/products/categories.json 
  python manage.py loaddata fixtures/products/products.json

  python manage.py makemigrations
  python manage.py migrate  
```

local run
```
    python manage.py runserver
```
