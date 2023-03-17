from dadata import Dadata


class Api:
    """api Dadata"""

    @staticmethod
    def correct_data(token, secret, language):
        query = input("Введите адрес: ")
        dadata = Dadata(token, secret)
        result = dadata.suggest(name="address", query=query, languge=language)
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
