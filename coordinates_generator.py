import streamlit as st

st.set_page_config(page_title="coordinates generator")
st.markdown("## This is a coordinates generator.")

col1, col2 = st.columns([1, 1])

col1.markdown("#### Please fill in the blanks :")
a = col1.text_input("Min x coordinate : ")
b = col1.text_input("Max x coordinate : ")
c = col1.text_input("Min y coordinate : ")
d = col1.text_input("Max y coordinate : ")

if a:
    a = int(a)
if b:
    b = int(b) + 1
if c:
    c = int(c)
if d:
    d = int(d) + 1

if col1.button("click to generate coordinates"):
    for x in range(a , b):
        for y in range(c , d):
            col2.markdown(f"##### ({x} , {y})")

if col1.button("click to clear coordinates"):
    col2.empty()
