import sqlite3
import re


def regexp(expr, item):
    """pomocnicza funkcja regexp dla sqlite3"""
    reg = re.compile(expr)
    return reg.search(item) is not None

	
if __name__ == '__main__':
    conn = sqlite3.connect(':memory:')
    conn.create_function("REGEXP", 2, regexp)
    
    miesiace = [('styczen',31),
		('luty',28),
		('marzec',31),
		('kwiecien',30),
		('maj',31),
		('czerwiec',30),
		('lipiec',31),
		('sierpien',31),
		('wrzesien',30),
		('pazdziernik',31),
		('listopad',30),
		('grudzien',31)]
    
    conn.execute('CREATE TABLE miesiace (miesiac,dni)')
    conn.executemany('INSERT INTO miesiace VALUES(?,?)',miesiace)
    conn.commit()
    miesiace_z_e = conn.execute('SELECT * FROM miesiace WHERE miesiac REGEXP "(?i)r"').fetchall()
    miesiace_bez_e = conn.execute('SELECT * FROM miesiace WHERE NOT miesiac REGEXP "(?i)r"').fetchall()
    print('*'*25, 'miesiace z litera r:','*'*25)
    print('\n'.join(['%s:%i'%(krotka) for krotka in miesiace_z_e]))
    print('*'*25, 'miesiace bez litery r:','*'*25)
    print('\n'.join(['%s:%i'%(krotka) for krotka in miesiace_bez_e]))
    
