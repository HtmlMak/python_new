def currency_rates(currency_code):
    from requests import get, utils
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    code_pos = content.find(currency_code)
    if code_pos == -1:
        rate = None
    else:
        rate_pos = content.find("<Value>",code_pos)+7
        rate_list = content[rate_pos:rate_pos+7].split(",")
        rate = float(f'{rate_list[0]}.{rate_list[1]}')
    return rate
