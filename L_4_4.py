import module_utils
c_code = "EUR"
currency_rate = module_utils.currency_rates(c_code)
print(currency_rate)
c_code = "USD"
currency_rate = module_utils.currency_rates(c_code)
print(currency_rate)
c_code = "EEE"
currency_rate = module_utils.currency_rates(c_code)
print(currency_rate)
