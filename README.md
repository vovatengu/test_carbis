# Test_carbis
Программа для поиска адресов и их координат

# Необходимые требования для запуска программы

Операционная система Windows/Linux/Mac os

Python 3.+

# Установка программы

0. Перейдите в папку, где хотите хранить программу
```
# Linux/Mac os
cd ~
# Windows PowerShell
cd C:/
```
1. Клонируйте репозиторий 
```
git clone https://github.com/vovatengu/test_carbis.git
```
2. Войдите в папку
```
cd test_carbis
```
2. Создайте виртуальное окружение
```
# Linux/Mac os
python3 -m venv carbis
source ./carbis/bin/activate

# Windows PowerShell
python -m venv carbis
.\carbis\Scripts\activate
```
3. Установите зависимости
```
pip install -r requirements.txt
```
4. Запустите приложениe
```
# Linux/Mac os
python3 main.py

# Windows PowerShell
python main.py
```

# Пример работы программы
При запуске появляется стартовое меню с выбором.

![screenshot](pic/1.png)

При первом запуске программы нужно зарегистрироваться.
Чтобы получить API-ключ и секретный ключ, нужно зарегистрироваться на DaData.ru https://dadata.ru/profile/#info и скопировать из личного кабинета.

![screenshot](pic/2.png)

Далле возвратится в стартовое меню. Из него нажимаем кнопку для входа.

![screenshot](pic/3.png)

Появляется меню действий для авторизованного пользователя.

![screenshot](pic/4.png)

В поиске выполняем действия с выбором поэтапно. 
После выведет, что выполение закончилось и вернётся в предыдущее меню для дальнейщих действий.

![screenshot](pic/5.png)

# Разработка программы 

В ходе разработки использовались паттерны объектно-ориентированного программирования: 
```
Singltone
State
```
