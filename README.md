# Social Network API
This project is an API written with Python for the social network that allows to register users, create posts, and like them.

## Built with
* [Django REST](https://www.django-rest-framework.org/)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [PostgreSQL](https://www.postgresql.org/)


## About Project
### Project Structure
This project includes consists of folders which are separate functional parts of the project, that includes:

* `social_network/` - main settings;
* `users/` - users model `User` with its views, serializers, and urls;
* `post/` - posts model `Post` with posts, likes model `PostLike` with their views, serializers, and urls.

### Endpoints
This project contains the following API resources:

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

For running this API locally you should have installed Python.

After creating Python virtual environment with `python -m venv /venv`, running it, and copying this project install all requirements:
```bash
pip install -r requirements.txt
```
Go to the `server/` folder and run API after applying migrations and creating superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
``` 

### Database setup
For creating a Postgres database you need to create a database locally and change the `DATABASES` config in `social_network/settings.py`.
