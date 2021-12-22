# Social Network API
This project is an API written with Python for social network that allows to register users, create posts and like them.

## Built with
* [Django REST](https://www.django-rest-framework.org/)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [PostgreSQL](https://www.postgresql.org/)


## About Project
### Project Structure
This project encludes folders whish are separate functional parts of project:

* `social_network/` encludes main settings;
* `users/` encludes users model `User` with it's views, serializers and urls;
* `post/` encludes posts model `Post` with post's likes model `PostLike` with their views, serializers and urls;

### Endpoints
In this project exists API resources:

#### Main resources:
* `api/token/` - for logining and creating JWT token
* `api/token/refresh/` - refresh access token

#### User resources, start with `api/user/`:
* `activity/` - last user login and last activity
* `register/` - create new user
* `logout/` - logout

#### Post resources, start with `api/post/`
* blank request return all posts
* `<int:user_id>/` - return post detail
* `like/` - set like for post
* `analitics/` - analytics about how many likes was made in date range agregated by date. Example url
`api/post/analitics/?date_from=2020-02-02&date_to=2020-02-15`

## Getting Started
### Environment Setup

For running this API locally you shold have installed Python.

After creating Python virtual environment with `python -m venv /venv`, running it and copied this project install all requirements:
```bash
pip install -r requirements.txt
```
Go to `server/` folder and run API after applying migrations and creating superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
``` 

### Database setup
For cteating Postgres database you need to write change `DATABASES` config in social_network/settings.py
