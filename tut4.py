from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL
server = Server('ipa.demo1.freeipa.org', get_info=ALL)
conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', auto_bind=True)
obj_person = ObjectDef('person', conn)
print(obj_person)
print(obj_person.sn)
obj_inetorgperson = ObjectDef('inetOrgPerson', conn)
r = Reader(conn, obj_inetorgperson, 'ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
print(r)
r.search()
print(r)
print(r[0])
print(r[0].entry_dn)
print(r[0].entry_attributes)
print(r[0].entry_attributes_as_dict)
print(r[0].entry_mandatory_attributes)
print(r[0].entry_to_ldif())
print(r[0].entry_to_json(include_empty=False))

print(obj_person)
obj_person += 'uid'
print(obj_person)
r = Reader(conn, obj_person, 'cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'uid:=admin')
print(r)
r.search()
print(r[0])
obj_person = ObjectDef(['person', 'posixaccount', 'krbprincipalaux'], conn)
print(obj_person)
r = Reader(conn, obj_person, 'dc=demo1,dc=freeipa,dc=org', 'uid:=admin')
r.search()
print(r[0])
print(r[0].krblastpwdchange.raw_values)
print(r[0].krbloginfailedcount.value)
print(r[0].krbloginfailedcount.raw_values)
r.search_level()
print(r)
print(len(r))
r.search_subtree()
print(len(r))

r = Reader(conn, obj_inetorgperson, 'ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
r.search()
w = Writer.from_cursor(r)
print(w)
print(w[0])
w[0].sn += 'Smyth'
w[0].sn += 'Johnson'
w[0].sn -= 'Young'
print(w[0].entry_changes)
print(w[0])
w[0].sn.discard()
w[0].sn += ['Smith', 'Johnson']
w[0].sn -= 'Young'
print(w[0])
w.commit()
print(w[0])
