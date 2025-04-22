import streamlit as st

st.title("S2CHANGE")

st.caption("(Colaborator)")

col1, col2 = st.columns([1.75,1], vertical_alignment="center")
with col1:
    st.markdown("### Overview")
    st.markdown("""
                Project developed in collaboration with the General-Directorate of the Territory and the 
                School of Agriculture (University of Lisbon) in Portugal, aiming to map vegetation loss at 
                country scale using the Continuous Change Detection (CCD) algorithm and Sentinel-2 data. 
                Adaptations were made to the **pyccd** implementation of the CCD algorithm in order to allow 
                it to work with **Sentinel-2** images. After an initial stage of development, experimentation 
                and parameter tuning, the project is currently in a phase of tests that include deploying the 
                algorithm countrywide using resources from a **HPC** cluster.

                [![View Project](https://img.shields.io/badge/GitHub-View_Project-blue?logo=GitHub)](https://github.com/manuelcampagnolo/S2CHANGE)
                
                """)
    
with col2:
    st.write("\n")
    st.image("./assets/s2change/s2change_logo.png", width=200)

