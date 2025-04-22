import streamlit as st

st.title("IFN-WSL-SSL")

col1, col2 = st.columns([1.75,1], vertical_alignment="center")
with col1:
    st.markdown("### Overview")
    st.markdown("""
                This project aimed to create a countrywide land cover map of Portugal using data from the Portuguese National Forest Inventory (NFI) for semantic segmentation of Sentinel-2 images with **convolutional neural networks**. 
                NFI point data were used to create a training sample. NFI-derived sparse labels were used to train a **weakly supervised** semantic segmentation deep learning model based on the ConvNext-V2 architecture. 
                Additionally, a **self-supervised masked autoencoder** model was pretrained and subsequently finetuned using the weakly supervised approach. 
                Results showcased the benefits of the self-supervised pretraining, which improved the overall accuracy over the baseline model.
                
                [![View Project](https://img.shields.io/badge/GitHub-View_Project-blue?logo=GitHub)](https://github.com/danielm09/NFI-WSL-SSL) [![View DOI](https://img.shields.io/badge/doi-10.3390/rs17040711-lightgreen)](https://doi.org/10.3390/rs17040711)
                """)
    
with col2:
    st.write("\n")
    st.image("./assets/ifn_wsl_ssl/map_pt.png")

st.divider()

st.markdown("## The Specifics")
st.write("")

col3, col4 = st.columns([1.2,1], vertical_alignment="top")
with col3:
    st.image("./assets/ifn_wsl_ssl/nfi.png", caption=" Example of NFI photo-points: (a) with matching point-patch labels; (b) located at the interface between distinct land covers; and (c) with mismatching point-patch labels.")
with col4:
    st.markdown("""
                ### The National Forest Inventory (NFI)
                The Portuguese NFI consists of a grid of points spaced 500 m apart, covering the whole territory of
                continental Portugal. Points are called *photo-points* and are characterized according to a range of
                attributes, including land cover.

                Characterization of photo-points is based on the patch of land where the point occurs, meaning
                a homogeneous area in terms of land use and land cover.
                """)

st.subheader("")

col5, col6 = st.columns([1,1.2], vertical_alignment="center")
with col5:
    st.markdown("""
                ### Weakly Supervised Learning (WSL)
                Deep Learning models such as Convolutional Neural Networks (CNN) normally require fully annotated
                training data, meaning that every pixel should be labeled.
                Here, a different approach is adopted: NFI photo-points are used to derive sparse
                labels. This means the model learns from limited, incomplete training data - a weakly
                supervised learning.
                """)
with col6:
    st.image("./assets/ifn_wsl_ssl/wsl.png", caption="High-resolution image (a), dense labels used in typical fully supervised methods (b) and sparse labels used in our weakly supervised approach (c). Colored and grey pixels correspond to labeled and unlabeled pixels, respectively. The labels in (c) are derived from the photo-point, seen in the center of the 3 × 3 window.")


st.subheader("")

col7, col8 = st.columns([1.4,1], vertical_alignment="top")

with col7:
    st.write("")
    st.image("./assets/ifn_wsl_ssl/cnn.png", caption="Network architecture of the ConvNext-V2 Atto U-Net.")

with col8:
    st.markdown("""
                ### Network Architecture
                A U-Net architecture based on the ConvNext-V2 Atto model was used for semantic segmentation.
                ConvNext-V2 is a modern convolutional neural network architecture, which incorporates design improvements 
                inspired by the success of vision transformers while maintaining the simplicity and efficiency of 
                convolution-based networks.
                """)
    

st.subheader("")


st.markdown("""
            ### Self-Supervised Learning (SSL)
            A Masked Autoencoder (MAE), a special self-supervised technique, was trained. In computer vision, 
            MAEs learn by solving a pretext task, which consists of reconstructing masked parts of an image.
            Learned feature representations can be transferred and applied to downstream tasks, such as image 
            classification and semantic segmentation.
            """)
    

st.image("./assets/ifn_wsl_ssl/ssl.png", caption="MAE architecture, illustrating the reconstruction of masked patches. Image representations learned at the encoder can be transferred and applied to different downstream tasks.")
