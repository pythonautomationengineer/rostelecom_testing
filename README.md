#  Итоговый проект по автоматизации тестирования
## Объект тестирования: [Ростелеком](https://b2c.passport.rt.ru)

### Для тестирования сайта были использованы
- мануальные и автоматизированные тесты

### Используемые библиотеки и модули
Faker 19.1.0 \
Pytest 7.3.2 \
Selenium 4.10.0 

random \
platform \
getpass



При выборе инструментов для тестирования сайта учитывалась функциональность, удобство использования и соответствие требованиям проекта.

**Pytest** и **Selenium** позволяют автоматизировать тесты. \
**Faker** обеспечивает создание реалистичных тестовых данных. \
**random** помогает генерировать разнообразные случайные значения. \
**platform** необходим для определения OS на запускаемой машине для правильного подбора горячих клавиш Selenium. \
**getpass** используется, чтобы обратиться к запускающему лицу по имени пользователя его машины в некоторых skipif-тестах. Оставил его просто, чтобы попрактиковаться в его использовании.

### Используемые техники тест-дизайна
- Классы эквивалентности 
- Граничные значения
- Тестирование состояний и переходов

### Почему именно эти техники тест-дизайна использовались
* Техника классов эквивалентности позволяет разделить входные данные на группы, которые имеют одинаковое поведение. Это помогает сократить количество тестовых случаев, которые требуется проверить. 
* Тестирование граничных значений направлено на проверку поведения при крайних значениях входных данных или параметров. Например, минимальные и максимальные значения пароля при регистрации. Граничные значения часто вызывают особые ситуации или ошибки, и их тестирование позволяет выявить потенциальные проблемы на сайте.
* Техника тестирования состояний и переходов позволяет проверить какой-либо функционал сайта в разных состояниях системы или ее компонентов. Например, различные состояния формы ввода данных или навигации по страницам. Проверка переходов между состояниями помогает выявить ошибки, убедиться в правильном функционировании и корректности работы сайта при различных ситуациях.

В теории эти техники помогают обеспечить хорошее покрытие тестирования и эффективно выявлять дефекты на сайте.

### Тест-кейсы и баг-репорты
[Доступны по ссылке](https://docs.google.com/spreadsheets/d/1R30jt8g9oHbXQ8hR1CeaHae3VhmGYdo9Al4J4S5tJjg/edit?usp=sharing) \
_Переключение между листами внизу документа_ 


### Используемые IDE
PyCharm Community 2023.1.4 \
Aqua 2023.1 Public Preview

### Окружение 
Google Chrome Версия 115.0.5790.102 (Официальная сборка), (64 бит)  
Windows 11, Версия 22H2

#### Папка Classes
* Characters_generator.py - содержит генераторы некоторых паролей и отдельных символов, для которых не подходит библиотека Faker
* Data_for_Assert.py - собраны тексты для ассертов в тестах
* FakePerson.py - генерация необходимых тестовых данных: имени, фамилии, отчества и телефона
* Stability - содержит классы, прямо либо косвенно связанных со стабильностью тестов

#### Папка tests
* test_changing_data_inside_your_account.py - Содержит позитивные и негативные тесты, изменяющие данные пользователя внутри личного кабинета
* test_create_account.py - Содержит негативные и позитивные тесты, связанные с регистрацией пользователя
* test_login_to_personal_account.py - Включает позитивные и негативные тесты, которые проверяют вход в личный кабинет
* test_others.py - Всё, что не вошло которые не вошли в другие модули

#### Содержание папки tests

##### Тесты в модуле test_changing_data_inside_your_account.py
* test_adding_a_patronymic - добавление/изменение отчества внутри личного кабинета
* test_change_of_first_and_last_name - изменение имени и фамилии внутри личного кабинета
* test_changing_passwords - невозможность изменения старого пароля на новый, если он полностью совпадает со старым

##### Тесты в модуле test_create_account.py
* test_invalid_registration - регистрация по ранее используемым и действующим логином и паролем
* test_returning_to_the_home_page - возвращение на главную страницу из модального окна с текстом 'Учетная запись уже используется'
* test_short_password - появление сообщения в форме регистрации с текстом "Длина пароля должна быть не менее 8 символов"
        под полем "Новый пароль" при вводе пароля из 7 символов
* test_big_letter - появление сообщения в форме регистрации с текстом "Пароль должен содержать хотя бы одну заглавную букву"
        под полем "Пароль" и "Подтверждение пароля" при введении 8 символов: маленьких букв и цифр
* test_latin_password - появление сообщения в форме регистрации с текстом "Пароль должен содержать только латинские буквы" под полем
        "Пароль" и "Подтверждение пароля при введении 9 символов кириллицы
* test_pass_dont_match - выводится "Пароли не совпадают" под полем "Подтверждение пароля", если пользователь ввел разные пароли
        при регистрации
* test_not_valid_registration - регистрация со всеми валидными полями кроме имени (слишком длинное имя)
* test_valid_registration - регистрация со всеми валидными полями кроме фамилии (слишком длинная фамилия)
* test_valid_registration_too - регистрация со всеми валидными полями кроме фамилии и имени (слишком короткая фамилия и имя)
* test_registration - наличие всех необходимых элементов регистрации пользователя на странице
* test_valid_registration - отправка сайтом кода подтверждения регистрации при всех введенных валидных данных, которые ранее
        не были использованы
* test_eye_icon_on_password - элемент <svg>, скрывающий видимость пароля, по клику открывает видимость пароля,
        а при повторном клике скрывает обратно

##### Тесты в модуле test_login_to_personal_account.py
* test_login_with_valid_phone_and_password - вход в личный кабинет по валидному телефону и паролю
* test_login_with_valid_email_and_password - вход в личный кабинет по валидному email и паролю
* test_login_with_valid_login_and_password - вход в личный кабинет по валидному логину и паролю
* test_phone_tabs - смена таба выбора аутентификации при вводе телефона в табе 'Почта'
* test_login_with_old_password - вход в ЛК с предыдущем паролем
* test_email_tabs - смена таба выбора аутентификации при вводе почты в табе 'Телефон'

##### Тесты в модуле test_others.py
* test_different_links - отличие ссылок на **Пользовательское соглашение** и **Политику конфиденциальности**
при переходе со страницы авторизации и отличие названий их вкладок в браузере

#### Версия драйвера

Фикстура в модуле conftest.py при запуске тестов автоматически скачивает последнюю версию драйвера и при первом запуске тесты могут упасть из-за таймаута. 
Это нормально, нужно просто перезапустить тесты после установки последней версии драйвера.

##### Запуск тестов в модуле test_changing_data_inside_your_account.py
* Способ 1. По кнопке **Run** на класс или отдельную функцию из PyCharm или Aqua (наиболее стабильный вариант) 
* Способ 2. Перейти в терминале в папку **tests** и выполнить команду **pytest -v test_changing_data_inside_your_account.py -s** 
* Способ 3. Выполнение только позитивных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestChangingDataInsideYourAccountPositive' -v -s** 
* Способ 4. Выполнение только негативных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestChangingDataInsideYourAccountNegative' -v -s** 

##### Запуск тестов в модуле test_create_account.py
* Способ 1. По кнопке **Run** на класс или отдельную функцию из PyCharm или Aqua (наиболее стабильный вариант)
* Способ 2. Перейти в терминале в папку **tests** и выполнить команду **pytest -v test_create_account.py -s** 
* Способ 3. Выполнение только позитивных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestCreateAccountPositive' -v -s** 
* Способ 4. Выполнение только негативных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestCreateAccountNegative' -v -s**

##### Запуск тестов в модуле test_login_to_personal_account
* Способ 1. По кнопке **Run** на класс или отдельную функцию из PyCharm или Aqua (наиболее стабильный вариант) 
* Способ 2. Перейти в терминале в папку **tests** и выполнить команду **pytest -v test_login_to_personal_account -s** 
* Способ 3. Выполнение только позитивных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestLoginPositive' -v -s** 
* Способ 4. Выполнение только негативных тестов. Находясь в корневой директории проекта выполнить команду **pytest -k 'TestLoginNegative' -v -s**

##### Запуск тестов в модуле test_others.py
* Способ 1. По кнопке **Run** из PyCharm или Aqua (наиболее стабильный вариант)
* Способ 2. Перейти в терминале в папку **tests** и выполнить команду **pytest -v test_others.py -s** 
* Способ 3. Находясь в любой директории внутри проекта выполнить команду **pytest -v -k 'others' -s** 
* Способ 4. Находясь в корневой директории выполнить команду **pytest -k 'TestOther' -v -s**

#### Папка Common_actions
* changing_data_inside_your_account_action_helpers.py - повторяющиеся типовые действия, выполняемые внутри личного кабинета
* create_account_action_helpers.py - повторяющиеся типовые действия при создании аккаунта
* login_to_personal_account_action_helpers.py - повторяющиеся типовые действия при логине в личный кабинет

#### Другие файлы в корневой папке
* conftest.py - содержит фикстуру инициализации и закрытия браузера
* requirements.py - используемые импортируемые библиотеки проекта
* credentials.py - адрес самого сайта, валидные и некоторые невалидные данные для входа в личный кабинет
* .gitignore - игнорируемые файлы и папки
* README.md - файл, описывающий проект, который вы сейчас прочитали
