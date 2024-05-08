import folium
import streamlit as st
from streamlit_folium import st_folium

import streamlit as st
import folium

map = folium.Map(location=[-25.441105, -49.276855], zoom_start=12)

st.header('Depois de muita dor de cabeça, o mapa.')
st_folium(map, width=700)
