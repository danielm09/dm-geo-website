import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "pages/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    "pages/ifn_wsl_ssl.py",
    title="IFN-WSL-SSL",
    icon=":material/map:",
)

project_2_page = st.Page(
    "pages/geoq.py",
    title="GeoQuery",
    icon=":material/chat:",
)

project_3_page = st.Page(
    "pages/ccd_plugin.py",
    title="CCD-Plugin for QGIS",
    icon=":material/route:",
)

project_4_page = st.Page(
    "pages/georasterRF.py",
    title="GeoRasterRF",
    icon=":material/nature:",
)

project_5_page = st.Page(
    "pages/s2change.py",
    title="S2CHANGE",
    icon=":material/satellite_alt:",
)

publications_page = st.Page(
    "pages/publications.py",
    title="Publications",
    icon=":material/article:"
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page, project_4_page, project_5_page],
        "Publications": [publications_page]
    }
)


# --- SHARED ON ALL PAGES ---
with st.sidebar:
    #st.write("My Links")
    #SM icons
    st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"/>', unsafe_allow_html=True)
    #bluesky
    st.write("""
            My Links
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

# --- RUN NAVIGATION ---
pg.run()



   

   
