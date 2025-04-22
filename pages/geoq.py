import streamlit as st

st.title("GeoQuery")


st.markdown("### Overview")
st.image("./assets/geoquery/diagram.png")
st.markdown("""
            This is a **prototype** of a chatbot app designed to answer geospatial questions. 
            It uses an **LLM Agent** powered by **LangChain**, with a set of tools that allow 
            querying reference geospatial datasets, such as a spatial database and geotiff images. 
            Based on a user prompt, the agent decides autonomously which tools and datasets to use 
            in order to answer the question. The app uses the **OpenAI API** but it can also be 
            configured to use local LLMs via **Ollama**. The chat UI is based on **streamlit** and 
            the app is encapsulated in a **docker container**.

            [![View_App](https://img.shields.io/badge/GeoQuery-View_app-white?logo=streamlit)](http://www.dm-geo.com/geoquery) ![Check_status](https://img.shields.io/website?url=https%3A%2F%2Fdm-geo.com%2Fgeoquery%2Fhealthz&label=App%20status)
            """)
