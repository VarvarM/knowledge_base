# Структура
  - .idea/: Настройки проекта PyCharm
  - base/: Основной код приложения
    - queries/: Папка с функциями запросов к базе данных
    - routers/: Папка с обработчиками маршрутов API
    - config.py: Конфигурационные настройки проекта
    - database.py/: Создание движка для работы с базой данных
    - models/: Таблицы и типы для базы данных
  - main.py: Точка входа для приложения FastAPI
  - requirements.txt: Список зависимостей, необходимых для проекта.
# Как запустить проект


1. **Клонируйте репозиторий:**\
git clone https://github.com/VarvarM/knowledge_base.git \
cd knowledge_base
2. **Установите зависимости в виртуальное окружение:**\
pip install -r requirements.txt
3. **Настройте базу данных:**\
Создайте файл .env, в котором будут написать параметры базы данных (host, port, username, password, db_name)\
Убедитесь, что настройки базы данных указаны в файле base/config.py.
4. **Запустите приложение:**\
uvicorn main:app --reload
5. **Доступ к API:**\
Откройте браузер и перейдите по адресу http://127.0.0.1:8000.