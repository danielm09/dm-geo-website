import streamlit as st

st.title("CCD-Plugin for QGIS")
st.caption("(Co-developer)")


col1, col2 = st.columns([1.75,1], vertical_alignment="center")
with col1:
    st.markdown("### Overview")
    st.markdown("""
                The plugin was developed with the purpose of integrating the **Continuous Change Detection**
                algorithm to the QGIS environment. It relies on the **Google Earth Engine** platform to 
                retrieve and process Landsat and Sentinel-2 data, providing a fast and simple way to detect
                changes and explore pixel time series on QGIS. The plugin is publicly available and can be
                downloaded on QGIS from the official plugins repository.  
  
                [![View Project](https://img.shields.io/badge/GitHub-View_Project-blue?logo=GitHub)](https://github.com/SMByC/CCD-Plugin) ![Open_Source_Contrib](https://img.shields.io/badge/QGIS-Open_Source_Contribution-brightgreen?logo=qgis)

                """)
    
with col2:
    st.write("\n")
    st.image("./assets/ccd_plugin/ccd_icon.svg", width=150)

st.divider()

st.markdown("""
            ## About the CCD algorithm

            The Continuous Change Detection algorithm was introduced by [Zhu & Woodcock (2014)](https://www.sciencedirect.com/science/article/abs/pii/S0034425714000248)
            with the aim to model time series of satellite data. The algorithm adjusts a harmonic 
            regression to the time series, allowing to decompose it into trend, seasonality and breaks. 
            A break in the time series is identified if the deviation from observations and model predicted 
            values surpasses a given statistical limit. These capabilities have prompted the use of the method 
            for a variety of applications in the remote sensing community, especially for monitoring 
            disturbances in the vegetation.

            """)

st.markdown("""
            ## The CCD-Plugin

            Although in most cases we are interested in numerical results, visualizing CCD's regression
             adjustment and breaks in a chart helps understand what the model is actually doing and how 
            well its job is being done. Additionally, having a tool integrated into a GIS environment that
            quickly and flexibly provides a glimpse of what the adjustment looks like at various locations
            can come in handy. With that in mind, the QGIS CCD Plugin was introduced.
            """)
st.image("./assets/ccd_plugin/ccd_example.png",
         caption="CCD-Plugin interface and example of a generated plot exhibiting CCD adjustment and break date.")
