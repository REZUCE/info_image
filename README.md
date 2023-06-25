
# Информация о картинке
## Запуск проекта в dev-режиме

1. Клонировать репозиторий и перейти в него в командной строке:

    ```bash
        git clone <ссылка с git-hub>
    ```

2. Cоздать виртуальное окружение:

    windows

    ```bash
        python -m venv venv
    ```

    linux

    ```bash
        python3 -m venv venv
    ```

3. Активируйте виртуальное окружение

    windows

    ```bash
        source venv/Scripts/activate
    ```

    linux

    ```bash
        source venv/bin/activate
    ```

4. Установите зависимости из файла requirements.txt

    ```bash
        pip install -r requirements.txt
    ```

5. В папке с файлом manage.py выполните команду:

    windows

    ```bash
        python manage.py runserver
    ```

    linux

    ```bash
        python3 manage.py runserver
    ```
