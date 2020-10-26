#def say_hello(name):
#    print("Hello " + name)
#    print(f"How are you {name} ?")

#n = "Kilian"
#say_hello(n)
#h = art("Hello")
# print(h)
# print(text2art("Hello",))
# print("Yo")
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

c = create_contact('Kilian', '0769062552', True)
add_contact(c)
c = create_contact('Max', '0145935203', False)
add_contact(c)
c = create_contact('Lucie', '0967203628', False)
add_contact(c)
c = create_contact('Faycal', '0783429508', True)
add_contact(c)
print(annuaire)

def get_names():
    names = []
    for phone_number in annuaire:
        contact = annuaire[phone_number]
        names.append(contact['name'])
    names.sort()
    return names

print(get_names())