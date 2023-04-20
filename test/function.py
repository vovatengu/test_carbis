from dadata import Dadata
from db import Database 

connect = Database()

def search():
    query = input("Введите адрес: ")
    dadata = Dadata(connect.get_token(), connect.get_secret())
    result = dadata.suggest(name="address", query=query, languge=connect.get_language())
    if result:
        for count, item in enumerate(result, start=1):
            print(f'{count}) - {item["value"]}')
        choice = input("Выберите нужный адрес: ")
        finanal_result = dadata.clean(
            name="address", source=result[int(choice) - 1]["value"]
        )
        full_address = finanal_result["result"]
        lat = finanal_result["geo_lat"]
        lon = finanal_result["geo_lon"]
        print(f"\nКоординаты {full_address}: Широта - {lat}, Долгота - {lon}")
    else:
        print("Не удалось найти адрес")

def set_token():
    token = input("Введите Tокен: ")
    connect.set_token(token=token)

def set_secret():
    secret = input("Введите Секрет: ")
    connect.set_secret(secret=secret)

def set_language():
    language = input("Введите Язык (en/ru): ")
    connect.set_language(language=language)
