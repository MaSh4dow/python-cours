import phonebook as p
import logger as l
k = "0145935203"
c = p.create_contact('Kilian', '0769062552', True)
p.add_contact(c)
c = p.create_contact('Max', '0145935203', False)
p.add_contact(c)
c = p.create_contact('Lucie', '0967203628', False)
p.add_contact(c)
c = p.create_contact('Faycal', '0783429508', True)
p.add_contact(c)
print(p.annuaire)

print(p.get_names())

p.display_all()

p.get_contact(k,p.annuaire)

l.dump_log()





