from address_book import AddressBook
from notebook import Notebook
from methods import *

def main():
    print('Welcome to the Contact Assistant!')

    contacts = AddressBook()
    notes = Notebook()

    methods = {
        'add-address': {'name': add_address, 'obj': contacts},
        'add-birthday': {'name': add_birthday, 'obj': contacts},
        'add-contact': {'name': add_contact, 'obj': contacts},
        'add-email': {'name': add_email, 'obj': contacts},
        'all-contacts': {'name': show_all, 'obj': contacts},
        'birthdays': {'name': birthdays, 'obj': contacts},
        'change-address': {'name': change_address, 'obj': contacts},
        'change-birthday': {'name': change_birthday, 'obj': contacts},
        'change-email': {'name': change_email, 'obj': contacts},
        'change-phone': {'name': change_contact, 'obj': contacts},
        'delete-address': {'name': delete_address, 'obj': contacts},
        'delete-birthday': {'name': delete_birthday, 'obj': contacts},
        'delete-contact': {'name': delete_contact, 'obj': contacts},
        'delete-email': {'name': delete_email, 'obj': contacts},
        'show-address': {'name': show_address, 'obj': contacts},
        'search-contact': {'name': search_contact, 'obj': contacts},
        'show-birthday': {'name': show_birthday, 'obj': contacts},
        'show-contact': {'name': show_contact, 'obj': contacts},
        'show-email': {'name': show_email, 'obj': contacts},
        'show-phone': {'name': show_phone, 'obj': contacts},

        'add-note': {'name': add_note, 'obj': notes},
        'add-tags': {'name': add_tags, 'obj': notes},
        'all-notes': {'name': all_notes, 'obj': notes},
        'delete-note': {'name': delete_note, 'obj': notes},
        'delete-tag': {'name': delete_tag, 'obj': notes},
        'search-note': {'name': search_note, 'obj': notes},
        'search-tags': {'name': search_tags, 'obj': notes},
        'update-note': {'name': update_note, 'obj': notes},
    }

    while (True):
        cmd, args = parseCommands(input('> '))
        # clear_console()
        if cmd == 'hello':
            print('How can I help you?')
        elif (cmd == 'close' or cmd == 'exit'):
            print('Good bye!')
            break
        else:
            if cmd in methods:
                if len(args) > 0:
                    print(methods[cmd]['name'](
                        args, methods[cmd]['obj']))
                else:
                    try:
                        print(methods[cmd]['name'](methods[cmd]['obj']))
                    except TypeError:
                        print('Please provide full info')
            else:
                print(check_suggestion(cmd, methods.keys()))


if __name__ == '__main__':
    main()
