# Run in terminal with streamlit run 2_line_chart_interaction.py
import streamlit as st
import numpy as np

# Display title and description. 
st.title('Our First Streamlit App')
st.write('The description of our app, or some explanatory text.')

# Create sliders.
amplitude = st.slider('Amplitude', min_value=0, max_value=10, value=1)
period = st.slider('Period', min_value=0, max_value=10, value=1)

# Use information from sliders in text.
st.write(f'This is a sine with amplitude **{amplitude}** and period **{period}**.')

# Create a line chart with streamlit.
x = np.arange(0, 2*np.pi, 0.01)
y = amplitude * np.sin(x * period)
st.line_chart(y)
