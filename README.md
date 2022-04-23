# <center>[Vaccinations](https://vaccination-q3.herokuapp.com/api/vaccinations)</center>

## Endpoints

- ### [/vaccinations](https://vaccination-q3.herokuapp.com/api/vaccinations)</center>
## **<center>POST</center>**

#### `POST /api/vaccinations - REQUEST FORMAT`</br>
Todos os campos a sequir são obrigatórios na requisição.

```json
{
    "cpf": "02323292963",
    "name": "Jose",
    "vaccine_name": "Pfizer", 
    "health_unit_name": "Santa Rita"
}
```

Caso todos os campos sejam passados como esperado.
#### `RESPONSE - 201 CREATED`

```json
{
    "cpf": "02323292963",
    "name": "Jose",
    "first_shot_date": "Fri, 22 Apr 2022 23:53:38 GMT",
    "second_shot_date": "Thu, 21 Jul 2022 23:53:38 GMT", 
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
}
```
Caso ocorra algum erro de chave ou tipo, será retornado um erro adequado.
## **<center>GET</center>**

#### `GET /api/vaccinations - REQUEST FORMAT`</br>
Retorno sera uma lista de "vaccinations" cadastradas.

#### `RESPONSE - 200 OK`

```json
[
	{
		"cpf": "02323292963",
		"name": "Joaquin",
		"first_shot_date": "Fri, 22 Apr 2022 19:16:51 GMT",
		"second_shot_date": "Thu, 21 Jul 2022 19:16:51 GMT",
		"vaccine_name": "Pfizer",
		"health_unit_name": "Santa Rita"
	},
	{
		"cpf": "12345678910",
		"name": "Chrystian",
		"first_shot_date": "Sat, 09 Apr 2022 15:31:07 GMT",
		"second_shot_date": "Fri, 08 Jul 2022 15:31:07 GMT",
		"vaccine_name": "Pfizer",
		"health_unit_name": "Santa Rita"
	},
	{
		"cpf": "22345678910",
		"name": "Jose",
		"first_shot_date": "Sat, 09 Apr 2022 15:31:07 GMT",
		"second_shot_date": "Fri, 08 Jul 2022 15:31:07 GMT",
		"vaccine_name": "Coronavac",
		"health_unit_name": "Santa Cecilia"
	},
	{
		"cpf": "32345678910",
		"name": "Joao",
		"first_shot_date": "Sat, 09 Apr 2022 15:31:07 GMT",
		"second_shot_date": "Fri, 08 Jul 2022 15:31:07 GMT",
		"vaccine_name": "Coronavac",
		"health_unit_name": "Santa Matilde"
	},
]
```
</br>

## <center>Para rodar a aplicação localmente</center>
- E necessario ter o Python 3.9.6 instalado. 
- No arquivo .env e necessário conectar as variaveis a um banco postgresql.
</br>

~~~bash
$ git clone git@github.com:Kenzie-Academy-Brasil-Developers/q3-sprint5-vacinacao-RobsonMT.git
~~~
~~~bash
$ cd q3-sprint5-vacinacao-RobsonMT
~~~
~~~bash
$ python -m ven venv
~~~
~~~bash
$ source venv/bin/activate
~~~
~~~bash
$ cp .env.example .env
~~~
~~~bash
$ pip install -U pip
~~~
~~~bash
$ pip install -r requirements.txt
~~~
~~~bash
$ rm -rf migrations
~~~
~~~bash
$ flask db init
~~~
~~~bash
$ flask db migrate -m "create database"
~~~
~~~bash
$ flask db upgrade
~~~
~~~bash
$ flask run
~~~