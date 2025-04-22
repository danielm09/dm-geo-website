import streamlit as st

st.title("GeoRasterRF")

col1, col2 = st.columns([1.75,1], vertical_alignment="center")
with col1:
    st.markdown("### Overview")
    st.markdown("""
                App containing a graphical user interface to train **Random Forest** models to classify 
                geospatial images. The app also allows users to classify csv data for accuracy assessment. 
                It was developed as a Master's thesis project, which aimed to use Sentinel-2 images and the 
                RF algorithm to classify land cover in Portugal.

                [![View Project](https://img.shields.io/badge/GitHub-View_Project-blue?logo=GitHub)](https://github.com/danielm09/GeoRasterRF)
                """)
    
with col2:
    st.write("\n")
    st.image("./assets/georasterRF/GeoRFIcon.svg", width=150)

st.divider()

st.markdown("""
            ## A Random Forest Classifier with a Graphical User Interface

            GeoRasterRF makes the process of classifying GeoTiffs easier, by providing a graphical
            user interface. The app allows training a Random Forest model using training data from
            a CSV file and classifying images. The outputs include the predicted class and the 
            classification probabilities.
            """)
st.image("./assets/georasterRF/georasterRF_gui.JPG",
         caption="Graphical User Interface of the app.")
