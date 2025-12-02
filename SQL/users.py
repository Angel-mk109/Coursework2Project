import sqlite3
conn = sqlite3.connect('../users.db')
c = conn.cursor()
createScript = """create table if not exists users(
          id integer primary key autoincrement,
          username text not null unique,
          password_hash text not null,
          role text default 'user'           )"""

c.execute(createScript)
conn.commit()