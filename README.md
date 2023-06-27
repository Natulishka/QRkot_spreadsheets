# QRKot приложение для Благотворительного фонда поддержки котиков

## Описание

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.   
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.   
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект. 

## Стек технологий:

```
Python 3.7  
FastAPI 0.78.0
Pydantic 1.9.1
Alembic 1.7.7
Uvicorn 0.17.6
```

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Natulishka/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv

source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Создать и заполнить файл .env со следующими переменными:

```
APP_TITLE=Название приложения
DESCRIPTION=Описание приложения
VERSION=Версия приложения
DATABASE_URL=sqlite+aiosqlite:///./название_БД.db
SECRET=Секретное слово
FIRST_SUPERUSER_EMAIL=Почта
FIRST_SUPERUSER_PASSWORD=Пароль
Данные сервисного акаунта Google API
EMAIL=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
```

Применить миграции:

```
alembic upgrade head
```

Запустить сервис:
```
uvicorn app.main:app --reload
```
## Документация:
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
