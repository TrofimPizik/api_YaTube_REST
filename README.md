Yatube

Проект Yatube - это социальная сеть при помощи которой пользователи смогу создавать посты, разделять посты на группы для удобной сортировки контента, подписываться на других авторов для отслеживания их публикаций.

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/TrofimPizik/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
Если у вас Linux/macOS

source env/bin/activate
Если у вас windows

source env/scripts/activate
python3 -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Примеры запросов API:

http://127.0.0.1:8000/api/v1/posts/ - Получить список всех публикаций

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - Добавление нового комментария к публикации