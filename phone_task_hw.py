contacts = []


def add_contact(last_name, first_name, middle_name, phone_number):
    contact = {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name,
               'phone_number': phone_number}
    contacts.append(contact)

    return contacts


def remove_contact(last_name):
    for contact in contacts:
        if contact['last_name'] == last_name:
            contacts.remove(contact)
            return True
    return False


def import_contacts_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                last_name, first_name, middle_name, phone_number = data
                add_contact(last_name, first_name, middle_name, phone_number)
    except FileNotFoundError:
        print('Файл не найден')


def export_contacts_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            for contact in contacts:
                line = ','.join([contact['last_name'], contact['first_name'],
                                 contact['middle_name'], contact['phone_number']])
                file.write(line + '\n')
    except FileNotFoundError:
        print('Ошибка записи файла')


def search_contact(last_name):
    for contact in contacts:
        if contact['last_name'] == last_name:
            return contact
    return None


def print_contacts(contacts):
    for contact in contacts:
        print(f"Фамилия: {contact['last_name']}")
        print(f"Имя: {contact['first_name']}")
        print(f"Отчество: {contact['middle_name']}")
        print(f"Номер телефона: {contact['phone_number']}")
        print("=====")


while True:
    print('1. Добавить контакт')
    print('2. Удалить контакт')
    print('3. Импорт контактов из файла')
    print('4. Экспорт контактов в файл')
    print('5. Поиск контакта')
    print('6. Печать справочника')
    print('7. Выйти')
    choice = input('Выберите действие: ')

    if choice == '1':
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        middle_name = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        add_contact(last_name, first_name, middle_name, phone_number)

    elif choice == '2':
        last_name = input('Введите фамилию контакта для удаления: ')
        if remove_contact:
            print('Контакт удален')
        else:
            print('Контакт не найден')

    elif choice == '3':
        file_name = input('Введите имя файла для импорта: ')
        import_contacts_from_file(file_name)

    elif choice == '4':
        file_name = input('Введите имя файла для экспорта: ')
        export_contacts_to_file(file_name)

    elif choice == '5':
        last_name = input('Введите фамилию контакта для поиска: ')
        contact = search_contact(last_name)
        if contact:
            print('Найден контакт:')
            print('Фамилия:', contact['last_name'])
            print('Имя:', contact['first_name'])
            print('Отчество:', contact['middle_name'])
            print('Номер телефона:', contact['phone_number'])
        else:
            print('Контакт не найден')

    elif choice == '6':
        print_contacts(contacts)

    elif choice == '7':
        break

    else:
        print('Неверный выбор')
