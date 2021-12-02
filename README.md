Подготовка к собеседованию Python-разработчика

Репозиторий для сдачи домашнего задания.

Студент: Коробанов Георгий

* ###### Django MVC Model View Control (Template)
* Model -> Model
* View -> Controller
* Template -> Шаблон
* ###### Создание проекта
* `django-admin startproject djproject` - создать проект
* `python manage.py startapp djapp` - создать приложение
* `settings.py` - добавить приложение
* `models.py` - создаем модель
* `python manage.py makemigrations` - делаем миграции
* `python manage.py migrate` - применяем миграции
* Создание папки models, в ней __init__.py и перемещаем модель туда
* `python manage.py sqlmigrate djapp 0001` - применяем конкретной миграции
* ###### Кастомные миграции, позиция видео: ~0:55:00 минут
* В кастомной миграции можно сразу заливать объекты
* `python manage.py makemigrations djapp --empty` - создание кастомной миграции 0:58:20
* `admin.site.register(Product)` - регистрируем модель в админке
* `python manage.py createsuperuser` - создаем суперпользователя
* `def __str__` - добавить в модели для отображения в админке
* `python manage.py migrate djapp 0001` - unapplying миграции (если была накатана свежее)
* ###### Создаем контроллер
* Создание класса в `views.py`
* Создание папки templates
* Добавление пути к templates в settings.py `'DIRS': [ BASE_DIR / 'templates']`
* index.html - создание шаблона
* `path('', ProductView.as_view())` - добавляем в urlpatterns
* Создание urls.py в djapp
* ###### SQL
* 0:21 проблема n+1 `SomeOtherModel` для демонстрации запросов
* 0:32 `logger` sql запросов
* 0:36 запрос `select_related` для связи 2 таблиц с помощью JOIN
* 0:45 запрос `prefetch_related` для many-to-many
* 1:00 счетчик переходов
* 1:11 middleware hit_count (1:36 middleware)
* 2:00 @receiver сигналы
* ###### Settings
* 0:20 related_name related_query_name
* 0:36 Site model
* 0:50 CurrentSiteManager
* 1:15 CustomManager get_queryset
* 1:21 CustomQuerySet value_filter
* 1:30 local_settings DEBUG False для малых проектов
* 1:40 module base local (runserver --settings=djproject.settings.local)
* 1:45 добавить parent
* 1:49 SECRET_KEY = os.environ['SECRET_KEY'] в переменной окружения
* 1:53 домашка
* ###### nginx
* 0:20 масштабирование
* 0:36 docker-compose.yaml
* 0:40 ports expose
* 0:42 запуск db (docker-compose up --build)
* 0:45 создание settings
* 0:47 install psycopg2-binary
* 0:49 migrate
* 0:53 вернуть SECRET_KEY
* 1:00 Dockerfile

<br><br>

## Практическое задание

#### Этап 4

1. Развернуть Django приложение с помощью docker-compose и СУБД Postgresql. Использовать 3 контейнера, СУБД, приложение,
   nginx http-сервер.
2. *(Усложненное, по желанию) Добавить в модель товара поле ImageField для хранения фото товара. Добавить в шаблон
   товара ссылку на изображение. Модифицировать контейнер nginx для того чтобы он корректно обслуживал media файлы.
   Важно: нельзя хранить папку media внутри контейнера, т.к. это не позволяет делать бекап данных и использовать
   несколько экземпляров контейнера nginx для балансировки нагрузки. (Подсказка: гуглить volumes, driver, local)

<br><br>
Чтобы закрепить знания по фреймворку Django и подготовиться к собеседованию, предлагаем реализовать несложное
приложение. Практическим заданием будет каталог товаров, состоящий из двух страниц:

* главной со списком товаров и кнопкой их добавления;
* и страницы добавления товара

<p>
Приложение должно функционировать в синхронном режиме: пользователь нажимает кнопку «Добавить товар», переходит на предназначенную для этого страницу, указывает в форме необходимые данные и нажимает «Сохранить». После этого он перенаправляется на главную страницу, где в табличной форме отображается список всех товаров. Проект должен быть привязан к базе данных SQLite3 (БД по умолчанию) и иметь минимальную сложность стилевого оформления.
На первом этапе необходимо реализовать список товаров, а добавление самих товаров осуществлять через админку приложения
