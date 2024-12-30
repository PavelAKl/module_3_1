calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    print(len(string), string.upper(), string.lower())
string_info('Apple')
string_info('water')
string_info('Bear')
def is_contains(string, list_to_search):
    count_calls()
    if string.casefold() in (item.casefold() for item in list_to_search):
        print(True)
    else:
        print(False)
is_contains('King', ['ing', 'Kin', 'KiNG'])
is_contains('Limon', ['Limo', 'monli', 'nOmIl'])
is_contains('ApPle', ['apple', 'elppa', 'peppa'])
print(calls)