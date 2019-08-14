import sqlite3

db = sqlite3.connect('phones.db', check_same_thread=False)

db.execute("create table if not exists phones (name varchar(30) unique, phone varchar(30))")


def create(name, phone):
    db.execute("insert into phones (name, phone) values (?, ?)", (name, phone))
    db.commit()


def delete(name):
    db.execute("delete from phones where name=?", (name,))
    db.commit()


def read(name):
    c = db.execute('select phone from phones where name=?', (name,))
    phone = c.fetchone()
    return phone


def list_():
    phones = db.execute('select name, phone from phones')
    return phones.fetchall()


def update(name, phone):
    db.execute("update phones set phone=? where name=?", (phone, name))
    db.commit()