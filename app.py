import streamlit as st

if"x" not in st.session_state:
     st.session_state.x=96

st.set_page_config(
    page_title = "My App",
    layout = "wide"
)

with st.sidebar:
    st.header("Login Menu")

st.title("Multi-Domain Intelligence")

col1, col2 = st.columns(2)

with col1:
 st.subheader("This is my page content")

with col2:
 st.subheader("Value of x:" , str(st.session_state.x))


name = st.text_input("Enter your username:")

password = st.text_input("Enter your password:", type="password")

age = st.number_input("Enter your age:")



color = st.selectbox(
"Favourite colour",
 ["Red", "Green", "Blue", "Purple", "Yellow", "White"]
 )


# This persists across reruns:

if"logged_in"not in st.session_state:
 st.session_state.logged_in = False

if st.button("Login"):
 st.session_state.logged_in = True
 st.write("Logged in!")

if st.session_state.logged_in:
 st.write("Welcome!")
 st.switch_page("pages/visual.py")
 st.stop()

st.page_link("pages/Home.py")

# Success: logged_in persists!
# "Welcome!" message appears on every rerun.
