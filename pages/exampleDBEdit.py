import streamlit as st
import db


st.title('Editing DB content with streamlit')


conn = dbHelper.connect_database()
c = conn.cursor()
c.execute("""create table if not exists testing(
     id INTEGER PRIMARY KEY AUTOINCREMENT
     description TEXT)""")
conn.commit()
if st.button('Load Data'):
    st.session_state.message = []



















if'records' not in st.session_state:
    st.session_state.records = []




df = pd.Dataframe.from_records(
    st.session_state.records,
columns=['id', 'description'])

st.dataframe(df, use_container_width=True)


ids = [r["id"] for r in st.session_state.records]