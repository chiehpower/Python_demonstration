import streamlit as st
from streamlit_option_menu import option_menu

main_menu_option = ["Home", "Models", "Inference", "Project", "Log", "Analytics", "Setting"]
main_menu_option_icon = ['house', 'sliders', 'person-bounding-box', 'kanban', 'file-text', 'graph-up', 'gear-wide-connected']

with st.sidebar:
    app_mode = option_menu(None, main_menu_option,
                        icons=main_menu_option_icon,
                        menu_icon="app-indicator", default_index=0,
                        styles={
        # "container": {"padding": "5!important", "background-color": "#fafafa"},
        "container": {"padding": "0!important", "background-color": "#f0f2f6"},
        "icon": {"color": "orange", "font-size": "28px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "display": "flex", "align-items": "center"},
        "nav-link-selected": {"background-color": "#2C3845"},
    }
    )

if app_mode == "Models":

    with st.sidebar:
        menu_option = ['Check models', 'Upload models', 'Download models', 'Remove models']
        menu_option_icon = ['eye', 'cloud-upload', 'cloud-download', 'file-excel']
        models_mode = option_menu(None, menu_option,
                            icons=menu_option_icon,
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            # "container": {"padding": "5!important", "background-color": "#f0f2f6"},
            "icon": {"color": "orange", "font-size": "28px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "display": "flex", "align-items": "center"},
            "nav-link-selected": {"color":"black", "background-color": "#dde3eb"},
        }
        )

    if models_mode == "Check models":
        st.header("Checl models")
