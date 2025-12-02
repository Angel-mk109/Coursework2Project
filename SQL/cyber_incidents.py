import sqlite3
conn = sqlite3.connect('../users.db')
c = conn.cursor()
c.execute("""create table if not exists cyber_incidents
     id INTEGER PRIMARY KEY AUTOINCREMENT
     incident_date TEXT,
     incident_type TEXT, 
     severity TEXT ,
     status TEXT ,
     description TEXT,
     reported_by TEXT,
     created_at  TEXT""")
conn.commit()

reported_by = 'system_upload'
with open("cyber_incidents.csv","r") as incFile:
    for line in incFile.readlines():

        line = line.strip()
        vals = line.split(',')
        #vals[0],   vals[1],   vals[2]   vals[3],   vals[4],   vals[5]
        #incident_id, timestamp, ser

        c.execute("""insert into cyber_incidents 
                         (id, incident_date, incident_type, severity, status, description, 
                          reported_by,   created_at)
                          values(?,?,?,?,?,?,?, datetime())"""),
conn.commit()
