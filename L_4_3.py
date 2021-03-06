def currency_rates(currency_code):
    from requests import get, utils
    from datetime import datetime
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")   # Преобразуем содержимое файла в строку
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_pos = content.find("Date=")+6                          # Определяем позицию даты в строке
    date_list = content[date_pos:(date_pos+10)].split('.')
    date_rate = f'{date_list[2]}-{date_list[1]}-{date_list[0]}'
    code_pos = content.find(currency_code)                      # Определяем позицию кода валюты в строке
    if code_pos == -1:                                          # Если код не найден выводим None
        rate = None
    else:
        rate_pos = content.find("<Value>",code_pos)+7
        rate_str = content[rate_pos:rate_pos+7]
        rate_list = rate_str.split(",")
        rate = float(f'{rate_list[0]}.{rate_list[1]}')          # Преобразуем курс к типу float
    return rate, date_rate

c_code = "EUR"
currency_rate = currency_rates(c_code)
print(f"На {currency_rate[1]} курс {c_code} составляет {currency_rate[0]}")
