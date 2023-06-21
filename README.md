# api_final
api final
Получение публикаций

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
QUERY PARAMETERS

limit	
integer
Количество публикаций на страницу
offset	
integer
Номер страницы после которой начинать выдачу
Responses

200 Удачное выполнение запроса без пагинации

GET
/api/v1/posts/
Response samples

200
Content type
application/json

Copy
Expand all Collapse all
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
