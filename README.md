# Bakery Website

1. Check for Docker presence
```
  docker -v
```

2. Clone the repository
```
  git clone <link>
```

3. Launch the container
```
  docker-compose up -d --build
```

4. Start docker-compose from the root directory
```
  docker-compose up -d
```

5. Create a superuser
```
  docker-compose exec web python manage.py createsuperuser
```
