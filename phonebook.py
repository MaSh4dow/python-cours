import logger as l

def create_contact(name, phone_number, is_favorite):
    c = {
        'name': name,
        'phone_number': phone_number,
        'is_favorite': is_favorite,
    }
    return c

annuaire = {}

def add_contact(contact):
    cle = contact['phone_number']
    annuaire[cle] = contact
    l.save_log(str(contact))
def get_names():
    names = []
    for phone_number in annuaire:
        contact = annuaire[phone_number]
        names.append(contact['name'])
    names.sort()
    return names

def display_all():
    for phone_number in annuaire:
        contact = annuaire[phone_number]
        print(contact)
        l.save_log(str(contact))

def get_contact(phone_number):
    contact = annuaire[phone_number]
    l.save_log(f'Getting contact={contact}')
    return contact

