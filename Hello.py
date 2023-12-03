import streamlit as st
import numpy as np
from PIL import Image

image = Image.open('img/quad_img.png')

# def solve_quadratic(a, b, c):
#     # Calculate the discriminant
#     D = b**2 - 4*a*c
#     # Compute the two solutions
#     sol1 = (-b - np.sqrt(D)) / (2*a)
#     sol2 = (-b + np.sqrt(D)) / (2*a)
#     return sol1, sol2

def solve_quadratic(a,b,c):
	x1 = 0.0
	x2 = 0.0
	d = (b**2 - 4*a*c)
	#2 real solutions
	if d > 0:
		x1 = (-b + np.sqrt(d))/(2*a)
		x2 = (-b - np.sqrt(d))/(2*a)
		return (f"x1 = {x1}<br>x2 = {x2}")
	elif d == 0:
		x1 = (-b)/(2*a)
		return (f"x1 & x2 = {x1}")
	else:
		Re = (-b)/(2*a)
		Im = np.sqrt(-d)/(2*a)
		return (f"$$x_1 = {Re} + {Im}i$$<br>$$x_2 = {Re} - {Im}i$$")



# Streamlit app
st.title('Quadratic Equation Solver')
#Image
st.image(image, caption='Mathematical Elegance')

# Getting user input
a = st.number_input('Enter coefficient a', value=1.0)
b = st.number_input('Enter coefficient b', value=0.0)
c = st.number_input('Enter coefficient c', value=0.0)

# Solve button
if st.button('Solve'):
    # Handle cases where the equation is not quadratic
    if a == 0:
        st.error("Coefficient a cannot be zero for a quadratic equation.")
    else:
        try:
            sol = solve_quadratic(a, b, c)
            st.markdown(f"The solutions are:<br> {sol}", unsafe_allow_html=True)
        except ValueError as e:
            st.error(f"Error: {e}")

# Instructions for running the app
st.sidebar.write("To run this app, use the command: `streamlit run your_script_name.py`")
