import streamlit as st
import numpy as np

st.set_page_config(page_title="coordinates generator")
st.markdown("## This is a coordinates generator.")
st.markdown("#### It generates coordinates for a grid chart.")

col1, col2 = st.columns([1, 1])

col1.markdown("#### Please fill in the blanks :")
a = col1.number_input("Min x coordinate : ", value=0)
b = col1.number_input("Max x coordinate : ", value=0)
c = col1.number_input("Min y coordinate : ", value=0)
d = col1.number_input("Max y coordinate : ", value=0)
e = col1.selectbox("x incrementation", options=[0.5, 1, 2, 3], index=1)
f = col1.selectbox("y incrementation", options=[0.5, 1, 2, 3], index=1)

if a:
    a = int(a)
if b:
    b = int(b) + 1
if c:
    c = int(c)
if d:
    d = int(d) + 1
if e:
    e = float(e)
if f:
    f = float(f)

if col1.button("click to generate coordinates"):
    if a > b or c > d:
        col2.markdown("#### Enter valid values") 
        col2.markdown("##### (min has to be smaller than max)")
    else:
        col2.empty()  
        for x in np.arange(a, b, e):
            for y in np.arange(c, d, f):
                col2.markdown(f"##### ({x} , {y})")

if col1.button("click to clear coordinates"):
    col2.empty()
