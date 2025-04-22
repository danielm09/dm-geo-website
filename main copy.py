import streamlit as st


st.title("Geospatial Data Scientist")
st.markdown("""
            Machine learning and Earth Observation enthusiast
            """)


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

tab1, tab2, tab3 = st.tabs(["IFN-WSL-SSL", "GeoQuery", "CCD-Plugin"])


with st.sidebar:
    st.image("https://danielm09.github.io/assets/img/profile_pic.png",width=150)
    st.title("Daniel Moraes")
    st.caption("Geospatial data scientist and PhD candidate")
   
    #SM icons
    st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"/>', unsafe_allow_html=True)
    #location, lisbon
    st.write('<i class="fa-solid fa-location-dot fa-fw"></i> Lisbon, Portugal', unsafe_allow_html=True)
    #bluesky
    st.write("""
            <div style="padding-bottom:2px;">
            <div style="padding-bottom:2px;">
            <span><i class="fa-brands fa-bluesky fa-fw" style="color: #1889fe;"></i></span>
            <a href="https://bsky.app/profile/danielmoraesofc.bsky.social" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">Bluesky</span>
            </a>
            </div>
             
            <div style="padding-bottom:2px;">
            <span><i class="fab fa-linkedin fa-fw" style="color: #086bc9;"></i></span>
            <a href="https://www.linkedin.com/in/danielmoraes09" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">LinkedIn</span>
            </a>
            </div>
            
            <div style="padding-bottom:2px;">
            <span><i class="fa-brands fa-medium fa-fw" style="color: #121413;"></i></span>
            <a href="https://medium.com/@moraesd90" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">Medium</span>
            </a>
            </div>
             
            <div style="padding-bottom:2px;">
            <span><i class="fab fa-github fa-fw" style="color: #121413;"></i></span>
            <a href="https://github.com/danielm09" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">GitHub</span>
            </a>
            </div>
             
            <div style="padding-bottom:2px;">
            <span><i class="fa-brands fa-google-scholar fa-fw" style="color: #121413;"></i></span>
            <a href="https://scholar.google.com/citations?user=rQ4chtwHwSwC" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">Google Scholar</span>
            </a>
            </div>
             
            <div style="padding-bottom:2px;">
            <span><i class="fa-brands fa-orcid fa-fw" style="color: #a9d03f;"></i></span>
            <a href="https://orcid.org/0000-0002-4568-8182" target="_blank">
            <span style="padding-left:5px; padding-top:0px;">ORCID</span>
            </a>
            </div>
            </div>
             """,
             unsafe_allow_html=True
    )
   
    