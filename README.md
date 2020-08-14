1. Умный сервис прогноза погоды. (Базовый уровень).

2. Проектирование сервиса:
  - язык программирования Python версия 3.8
  - фреймворк Django версии 3.1
  - пользовательский интерфейс выполнен в виде сайта
  - результатом работы сервиса является получение информации о погоде в городе Воронеже
  
3. Процесс работы:
  - пользователь в браузере в поисковой строке вводит запрос http://127.0.0.1:8000
  - переходит на главную страницу сайта
  - при нажатии кнопки получает информацию о погоде в Воронеже
  
4. Как запустить программу:
  - выполнить клонирование репозитория, находящегося по адресу: https://github.com/andrewlerner/weather_project.git
  - произвести установку python3.8, pip, virtualenv
  - создать виртуальное окружение, для этого выполнить команду:
     - mkvirtualenv -p [путь_до_python.exe_версии_3.8] -a [путь_до_скачанной_папки] -r [путь_до_файла_requirements_в_скачанной_папке] [имя_виртуального_окружения]
  - перейти в скачанной папке в папку weather
  - запустить web сервер командой: python manage.py runserver
  - открыть браузер
  - в командной строке ввести запрос http://127.0.0.1:8000
  - на главной странице открывшегося сайта, нажать кнопку "Узнать."
