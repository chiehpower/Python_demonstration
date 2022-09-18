import streamlit as st
from streamlit_elements import elements, mui

if __name__ == '__main__':

    if "open2" not in st.session_state:
        st.session_state.open2 = False
        st.session_state.open3 = False

    if "item" not in st.session_state:
        st.session_state.item = ""
    
    class handle:
        def handle_menu1(self):
            st.session_state.item = 'Item1'

        def handle_open2(event):
            if st.session_state.open2 == False:
                st.session_state.open2 = True
            else:
                st.session_state.open2 = False
        
        def handle_menu2(self):
            st.session_state.item = 'Item2-1'
        def handle_menu3(self):
            st.session_state.item = 'Item2-2'

        def handle_menu4(self):
            st.session_state.item = 'Item3-1'
        def handle_menu5(self):
            st.session_state.item = 'Item3-2'
        def handle_open3(self):
            if st.session_state.open3 == False:
                st.session_state.open3 = True
            else:
                st.session_state.open3 = False

    # Ref:
    # - Icon: https://mui.com/zh/material-ui/material-icons/
    with st.sidebar:
        handle_menu = handle()
        with elements("style_elements_cssss"):
            with st.sidebar:
                with mui.List(component="nav", sx={".Mui-selected": {"backgroundColor": "#EBD6D6 !important"}}):
                    ### First
                    with mui.ListItemButton(selected=True if st.session_state.item == 'Item1' else False):
                        with mui.ListItemIcon:
                            # mui.icon.Send(sx={"color": "#ba68c8"})
                            mui.icon.Add(sx={"color": "#eb8c07"}) # sx={"color": "#eb8c07"
                        mui.ListItemText('Item1', onClick=handle_menu.handle_menu1)

                    ### Second
                    with mui.ListItemButton(onClick=handle_menu.handle_open2):
                        with mui.ListItemIcon:
                            mui.icon.Send(sx={"color": "#eb8c07"})
                        mui.ListItemText('Item2')
                        if st.session_state.open2:
                            mui.icon.ExpandLess()
                        else:
                            mui.icon.ExpandMore()
                    with mui.Collapse(in_=st.session_state.open2):
                        with mui.List(component="div", disablePadding=True):
                            with mui.ListItemButton(onClick=handle_menu.handle_menu2, sx={"pl": 4}, selected=True if st.session_state.item == 'Item2-1' else False):
                                with mui.ListItemIcon:
                                    mui.icon.Send(sx={"color": "#eb8c07"})
                                mui.ListItemText('Item2-1')
                            with mui.ListItemButton(onClick=handle_menu.handle_menu3, sx={"pl": 4}, selected=True if st.session_state.item == 'Item2-2' else False):
                                with mui.ListItemIcon:
                                    mui.icon.Send(sx={"color": "#eb8c07"})
                                mui.ListItemText('Item2-2')

                    ### Third
                    with mui.ListItemButton(onClick=handle_menu.handle_open3):
                        with mui.ListItemIcon:
                            mui.icon.Send(sx={"color": "#eb8c07"})
                        mui.ListItemText('Item3')
                        if st.session_state.open3:
                            mui.icon.ExpandLess()
                        else:
                            mui.icon.ExpandMore()
                    with mui.Collapse(in_=st.session_state.open3):
                        with mui.List(component="div", disablePadding=True):
                            with mui.ListItemButton(onClick=handle_menu.handle_menu4, sx={"pl": 4}, selected=True if st.session_state.item == 'Item3-1' else False):
                                with mui.ListItemIcon:
                                    mui.icon.Send(sx={"color": "#eb8c07"})
                                mui.ListItemText('Item3-1')
                            with mui.ListItemButton(onClick=handle_menu.handle_menu5, sx={"pl": 4}, selected=True if st.session_state.item == 'Item3-2' else False):
                                with mui.ListItemIcon:
                                    mui.icon.Send(sx={"color": "#eb8c07"})
                                mui.ListItemText('Item3-2')

    st.write(st.session_state.item)
    if st.session_state.item == 'Item1':
        st.write("---")
        tool_name = st.selectbox("Choose the tool.", ["Test"])
        st.write(tool_name)
