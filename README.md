# Дипломный проект "Регистрация по смс"

### *Данный проект Реализует логику* :

- Авторизация по номеру телефона. Первый запрос на ввод номера телефона. Имитируется отправка четырехзначного кода авторизации(с задержкой на сервере 1-2 сек). Второй запрос на ввод код

- Если пользователь ранее не авторизовывался, то записатся в БД

- Получение Access token 

- Запрос на профиль пользователя

- Пользователю, при первой авторизации, присваивается рандомно сгенерированный 6-значный инвайт-код(цифры и символы)

- В профиле у пользователя есть возможность ввести чужой инвайт-код(при вводе проверяется на существование)

- Активация инвайт-кода

- В API профиля выводиться список пользователей, которые ввели инвайт код текущего пользователя

### *Api для всего функционала* 

1. POST localhost:8000/users/phone-authorization/ - Запрос кода авторизации по номеру телефона
    {
    "phone_number": Ваш номер
    }

2. PUT localhost:8000/users/phone-authorization/ - Авторизация по номеру телефона и присланному коду
    {
    "phone_number": ваш номер,
    "authorization_code": ваш код авторизации
    }

3. POST localhost:8000/users/phone-token/ - Получение access токена 

    {
    "password": Ваш временный пароль он же код авторизации,
    "phone_number": ваш номер
    }

4. POST localhost:8000/users/change-password/ - Смена временного пароля 
    *В следующих запросах, незабываем вводить access токен в Authorization и перед токеном вводить bearer*

    {
    "old_password": "Старый пароль",
    "new_password1": "Новый пароль",
    "new_password2": "Новый пароль"
    }

5. GET localhost:8000/users/user/id/ - просмотр своего профиля 

6. PATCH localhost:8000/users/user/update/id/ - Редактирование своего профиля 

    {
    "email": "Ваша почта",
    "first_name": "Имя",
    "last_name": "Фамилия",
    "country": "Страна",
    "city": "Город",
    "date_of_birth": Дата рождения в формате "ГГГГ-ММ-ДД",
    "avatar": Ваше фото
    }

7. POST localhost:8000/users/check-referral/ - Вводим referral_code который вам дал зарегистрированный пользователь

    {
    "referral_code": "Код который вам предоставили"
    }

8. GET localhost:8000/users/referred-users/ - Заходим зарегистрированным пользователем и просматриваем кто ввёл ваш реферальный код 

### *Установка*

1. Установите Python 3.10 и выше

2. Создайте папку, куда будете клонировать проект

3. Скачайте репозиторий проекта:
   git clone https://github.com/andre059/thesis_project

4. Установите виртуальное окружение venv: 
   python -m venv venv 
   активируйте его: .\env\Scripts\Activate.ps1

5. Установите зависимости из файла requirements.txt:
   pip install -r requirements.txt

6. Настройте файл settings.py находящийся в папке config: 
    - *DATABASES_NAME = Название папки куда вы клонировали проект*
    
    - *DATABASES_USER = Переменная, которая должна содержать имя пользователя для подключения к базе данных PostgreSQL*
    
    - *DATABASES_PASSWORD = Пароль к вашей базе данных*
    
    - *SECRET_KEY = 'тут должен быть ваш секретный ключь'*
    
    - *CSU_SET_PASSWORD = 'Пароль для файла csu.py*

7. Можете создать суперпользователя:
    python manage.py CSU

8. Запустите проект: 
    python manage.py runserver

9. Доступ к веб-интерфейсу: 
    Откройте браузер и перейдите по адресу http://localhost:8000/admin