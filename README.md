<h1 align="center"> api_for_friends </h1>

---

# ТЗ:

Задание
Нужно сделать API с функционалом добавления друзей, соблюдая следующие условия:

1) Возможность пользователю1 отправить/отменить/принять заявку "Добавить в друзья" пользователю2
2) Возможность пользователю получить список входящих заявок "Заявки в друзья"
3) Возможность пользователю получить список исходящих заявок "Запрос на дружбу"
4) Если пользователь1 отправил заявку "Добавить в друзья" пользователю2, а пользователь2 отправил заявку пользователю1,
   то заявка должна автоматически приняться
5) Возможность пользователю получить список "Друзей"
6) Возможность пользователю1 удалить пользователя2 из своего списка "Друзей"

# Настройки

---
Установка:

    git clone https://github.com/SugResso/tz_for_vk.git
    pip install requirements.txt

Перейдите в папку и выполните миграции:

      cd src
      python manage.py makemigrations
      python manage.py migrate

Создайте супер пользователя:

      python manage.py createsuperuser

Можно запускать:

      python manage.py runserver

### Документация по API расположена по следующей ссылке http://127.0.0.1:8000/swagger/ (работает только после запуска проекта) или можно не скачивая проект прочитать комментарии со всеми запросами и URLами в файле [urls.py](src/config/urls.py)