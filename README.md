# fgis_parser_bot
Сервис для проверки результатов поверки СИ. (разработка)

#### Приложение быстрого получения информации персоналу о результатах поверок средств измерений из данных сайта Федерального агентства по техническому регулированию и метрологии.

#### Ключевые возможности сервиса:
- автоматический парсинг данных с сайта https://fgis.gost.ru/ (при отсутствии актуальной информации),
- возможность подключения API в свой проект,

## Используемые технологии
- python 3.12
- fastapi 0.110.0
- alembic 1.13.1
- uvicorn 0.29.0

## Настройка проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ZhdanovAM72/fgis_parser_bot.git
```
```
cd fgis_parser_bot
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
```
source venv/bin/activate
```
* Если у вас windows
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Заполнить файл с секретами:
``` 
# пример заполненного файла:
APP_TITLE=Заголовок
DESCRIPTION=Описание
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=admin@admin.com
FIRST_SUPERUSER_PASSWORD=admin
VERSION=0.1.1
``` 


### Запуск приложения:
Запустить сервер на локальном ПК можно используя следующую команду (из основной директории проекта):
```
uvicorn app.main:app --reload
```
либо из дирректории с файлом `main.py`
```
uvicorn main:app --reload
```

### Документация проекта

Примеры запросов к API, варианты ответов и ошибок приведены в документации по следующим ссылкам:
[Swagger](http://127.0.0.1:8000/api/swagger)
[ReDoc](http://127.0.0.1:8000/api/redoc)


## TODO:
- ~Парсер с возможностью выбора фильтров~
- API
- Aiogram bot


## Автор:
- [Александр Жданов ](https://github.com/ZhdanovAM72)