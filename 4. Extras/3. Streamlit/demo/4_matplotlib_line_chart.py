# Run in terminal with streamlit run 4_matplotlib_line_chart.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Display app title and description. 
st.title('Our First Streamlit App')
st.write('The description of our app, or some explanatory text.')

# Create sliders.
st.sidebar.markdown('# Controls')
amplitude = st.sidebar.slider('Amplitude', min_value=0, max_value=10, value=1)
period = st.sidebar.slider('Period', min_value=0, max_value=10, value=1)

# Use information from sliders in text.
st.write(f'This is a sine with amplitude **{amplitude}** and period **{period}**.')

# Use information from the sliders to create a plot with matplotlib.
x = np.arange(0, 2*np.pi, 0.01)
y = amplitude * np.sin(x * period)

# streamlit needs an object to plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Reveal the plot to streamlit.
st.pyplot(fig)
