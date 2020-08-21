'''
    CLI Currency Converter
    Created by Aghnat HS    
'''
#DATA
_USD="USD"
_IDR="IDR"
_EUR="EUR"
_JPY="JPY"
CURRENCY_RATES={
                _USD:{_IDR:14725,_EUR:0.84,_JPY:105},
                _IDR:{_USD:0.000068,_EUR:0.000057,_JPY:0.0072},
                _EUR:{_IDR:17469,_USD:1.19,_JPY:125.49},
                _JPY:{_IDR:139.37,_EUR:0.0080,_USD:0.0095}
                }   
list_of_currency=[_USD,_IDR,_EUR,_JPY]

#MAIN
print (list_of_currency)
_from=input("From Currency:").upper()
_to=input("To Currency:").upper()
_from_val=int(input("From Value:"))

def convert(_from=_from,_to=_to,_val=_from_val):
    _value=_val * CURRENCY_RATES[_from][_to]
    print ("{} {} is {} {} ".format(_val,_from,_value,_to))

convert()