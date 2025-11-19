import pandas as pd
import dbHelper

conn = .connect('test.db')
c = conn.cursor()

df = pd.read_csv('cyber_incidents.csv')

df.to_sql('cyber_incidents', con=conn,
        if_exists = 'append',index=False)