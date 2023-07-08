def short_password_generator():
    numbers = '1234567890'
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = '#$%^&*'
    first_symbol = set(english_alphabet).pop().upper()
    one_numbers = set(numbers).pop().upper()
    one_special_characters = set(special_characters).pop().upper()
    for i in set(english_alphabet):
        first_symbol += one_numbers + one_special_characters + i
        if len(first_symbol) == 7:
            break

    return first_symbol
