import sqlite3


conn = sqlite3.connect('cities.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE cities (
                country text,
                city text,
                city_id integer
                )""")
    conn.commit()
except Exception as error:
    print(error)


def add_new_city(country, city, city_id):
    with conn:
        try:
            c.execute("INSERT INTO cities VALUES (?, ?, ?)", (
                country, city, city_id))
        except Exception as error:
            print(error)
        conn.commit()


if '__name__' == '__main__':
    print(add_new_city('Ukraine', 'Bobrinets', 27200))
    conn.close()
