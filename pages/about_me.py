import streamlit as st


# --- HERO SECTION ---
col1, col2 = st.columns([1,2], gap="small", vertical_alignment="center")
with col1:
    st.image("https://danielm09.github.io/assets/img/profile_pic.png")

with col2:
    st.title("Daniel Moraes", anchor=False)
    st.write("Geospatial Data Scientist")
    st.write("Machine learning and Earth Observation enthusiast")
    st.write('<i class="fa-solid fa-location-dot fa-fw"></i> Lisbon, Portugal', unsafe_allow_html=True)

#SKILLS AND EDUCATION
st.markdown("""
            ### Technical Skills
            - Deep learning, self-supervised learning, masked autoencoders, convolutional neural networks, random forest
            - Python: pandas, geopandas, rasterio, gdal, xarray, dask, pytorch, tensorflow, scikit-learn
            - PostgreSQL, PostGIS
            - Cloud computing (AWS Cloud Practitioner Certificate)
            - Docker, CI/CD
            - QGIS, ArcGIS, Google Earth Engine
            """)

st.markdown("""
            ## Education
            - PhD Candidate in Geoinformatics @ Nova IMS, Universidade Nova de Lisboa
            - Master’s degree in Geographic Information Systems and Science @ Nova IMS, Universidade Nova de Lisboa
            """)

st.markdown("""
            ## Experience
            - 6 years of research experience working at the intersection of data science and remote sensing
            - 1 year of experience working as a GIS Analyst
            """)

