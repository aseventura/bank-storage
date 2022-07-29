# Пульт охраны банка
## Описание:
Пульт охраны - мини-сайтик для охранника банка. Сайт покажет кто сейчас в хранилище с деньгами, сколько раз сотрудники ходили в хранилище, а если кто-то украл деньги — с кем он там был.
## Окружение:
* Linux
* Python 3.8+
* Пакетный менеджер `pip`
* Виртуальное окружение `venv`
## Подготовка к запуску:
Для запуска проекта установите [Python3](https://www.python.org/) **не ниже** версии `3.8`. Перейдите в каталог, куда скачали проект командой `cd` и сделайте следующее:
- Активируйте виртуальное окружение
- Установите все зависимости для корректной работы проекта
```sh
cd DOWNLOAD_PATH
python3 -m venv env && source ./env/bin/activate
python3 -m pip install -r requirements.txt
```
## Пример запуска проекта:
```sh
python3 main.py # Запуск сервера. Сайт будет находиться по адресу: http://0.0.0.0:8000/
```
## Лицензия:
Проект находится под лицензией MIT. Его можно повторно использовать в проприетарном программном обеспечении при условии, что все копии лицензионного программного обеспечения включают копию условий лицензии MIT и уведомление об авторских правах.