# Yatube API
## _API для соцнальной сети yatube_
API для Yatub представляет собой социальную сеть, в которой реализованы следующие возможности: публиковать записи и прикреплять к нней фотографию, комментировать записи, а так же подписываться или отписываться от авторов.

### Tecnologies
- Python 3.7
- Django 4.2
- DRF
- JWT, Djoser

### Run project in dev
- Install and activate virtual environment
```
python3 -m venv venv
```
```
source venv/bin/activate
```
- In 'api_final_yatube' create ".env" file and place there SECRET_KEY, DEBUG, ALLOWED_HOSTS

- Install dependencies from the file requirements.txt
```
pip install -r requirements.txt
``` 
- Make migrations
```
python3 manage.py migrate
``` 
- Run progect
```
python3 manage.py runserver
``` 


## Примеры запросов API
GET api/v1/posts/ - получить список всех публикаций.
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id

POST api/v1/posts/ -> передаем:
{
"text": "string",
"image": "string",
"group": 0
}

  
### Author
*Maria Svetlichnaya*
[telegram](https://t.me/msvetlichnaya)
