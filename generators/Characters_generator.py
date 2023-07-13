class CharactersGenerator:
    """Генераторы некоторых паролей и отдельных символов, для которых не подходит библиотека Faker"""

    @staticmethod
    def not_latin_password_generator():
        numbers = '1234567890'
        russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        special_characters = '#$%^&*'
        first_symbol = set(russian_alphabet).pop().upper()
        one_numbers = set(numbers).pop().upper()
        one_special_characters = set(special_characters).pop().upper()
        for i in set(russian_alphabet):
            first_symbol += one_numbers + one_special_characters + i
            if len(first_symbol) > 7:  # 8 символов
                break

        return first_symbol

    @staticmethod
    def one_symbol_generator():
        main_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        first_symbol = set(main_str).pop().upper()  # 1 символ
        return first_symbol

    @staticmethod
    def short_password_generator():
        numbers = '1234567890'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        special_characters = '#$%^&*'
        first_symbol = set(english_alphabet).pop().upper()
        one_numbers = set(numbers).pop().upper()
        one_special_characters = set(special_characters).pop().upper()
        for i in set(english_alphabet):
            first_symbol += one_numbers + one_special_characters + i
            if len(first_symbol) == 7:  # 7 символов
                break

        return first_symbol

    @staticmethod
    def small_letter_password_generator():
        numbers = '1234567890'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        special_characters = '#$%^&*'
        one_sp_char = set(special_characters).pop()
        one_numb = set(numbers).pop()
        first_symbol = ''
        for i in set(english_alphabet):
            first_symbol += one_sp_char + one_numb + i
            if len(first_symbol) > 7:  # 8 символов
                break

        return first_symbol

    @staticmethod
    def p_password_generator():
        numbers = '1234567890'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        special_characters = '#$%^&*'
        first_symbol = set(english_alphabet).pop().upper()
        one_numbers = set(numbers).pop().upper()
        one_special_characters = set(special_characters).pop().upper()
        for i in set(english_alphabet):
            first_symbol += one_numbers + one_special_characters + i
            if len(first_symbol) > 12:  # 13 символов
                break

        return first_symbol

    @staticmethod
    def p2_password_generator():
        numbers = '1234567890'
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        special_characters = '#$%^&*'
        first_symbol = set(english_alphabet).pop().upper()
        one_numbers = set(numbers).pop().upper()
        one_special_characters = set(special_characters).pop().upper()
        for i in set(english_alphabet):
            first_symbol += one_numbers + one_special_characters + i
            if len(first_symbol) > 14:  # 15 символов
                break

        return first_symbol

    @staticmethod
    def very_long_first_name_generation():
        main_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        first_symbol = set(main_str).pop().upper()
        for i in set(main_str):
            first_symbol += i
            if len(first_symbol) > 30:  # 31 символ
                break

        return first_symbol

    @staticmethod
    def very_long_last_name_generation():
        main_str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        first_symbol = set(main_str).pop().upper()
        for i in set(main_str):
            first_symbol += i
            if len(first_symbol) > 30:  # 31 символ
                break

        return first_symbol