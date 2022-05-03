"""
Referred from official Github repo.
"""
# First, import the elements you need

import streamlit as st
from streamlit_elements import elements, mui, html, lazy, sync

# Create a frame where Elements widgets will be displayed.
#
# Elements widgets will not render outside of this frame.
# Native Streamlit widgets will not render inside this frame.
#
# elements() takes a key as parameter.
# This key can't be reused by another frame or Streamlit widget.

# with elements("new_element"):

#     # Let's create a Typography element with "Hello world" as children.
#     # The first step is to check Typography's documentation on MUI:
#     # https://mui.com/components/typography/
#     #
#     # Here is how you would write it in React JSX:
#     #
#     # <Typography>
#     #   Hello world
#     # </Typography>

#     mui.Typography("Hello world")

# with elements("nivo_charts"):

#     # Streamlit Elements includes 45 dataviz components powered by Nivo.

#     from streamlit_elements import nivo

#     DATA = [
#         { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
#         { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
#         { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
#         { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
#         { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
#     ]

#     with mui.Box(sx={"height": 500}):
#         nivo.Radar(
#             data=DATA,
#             keys=[ "chardonay", "carmenere", "syrah" ],
#             indexBy="taste",
#             valueFormat=">-.2f",
#             margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
#             borderColor={ "from": "color" },
#             gridLabelOffset=36,
#             dotSize=10,
#             dotColor={ "theme": "background" },
#             dotBorderWidth=2,
#             motionConfig="wobbly",
#             legends=[
#                 {
#                     "anchor": "top-left",
#                     "direction": "column",
#                     "translateX": -50,
#                     "translateY": -40,
#                     "itemWidth": 80,
#                     "itemHeight": 20,
#                     "itemTextColor": "#999",
#                     "symbolSize": 12,
#                     "symbolShape": "circle",
#                     "effects": [
#                         {
#                             "on": "hover",
#                             "style": {
#                                 "itemTextColor": "#000"
#                             }
#                         }
#                     ]
#                 }
#             ],
#             theme={
#                 "background": "#FFFFFF",
#                 "textColor": "#31333F",
#                 "tooltip": {
#                     "container": {
#                         "background": "#FFFFFF",
#                         "color": "#31333F",
#                     }
#                 }
#             }
#         )

# with elements("monaco_editors"):

#     # Streamlit Elements embeds Monaco code and diff editor that powers Visual Studio Code.
#     # You can configure editor's behavior and features with the 'options' parameter.
#     #
#     # Streamlit Elements uses an unofficial React implementation (GitHub links below for
#     # documentation).

#     from streamlit_elements import editor

#     if "content" not in st.session_state:
#         st.session_state.content = "Default value"

#     mui.Typography("Content: ", st.session_state.content)

#     def update_content(value):
#         st.session_state.content = value

#     editor.Monaco(
#         height=300,
#         defaultValue=st.session_state.content,
#         onChange=lazy(update_content)
#     )

#     mui.Button("Update content", onClick=sync())

#     editor.MonacoDiff(
#         original="Happy Streamlit-ing!",
#         modified="Happy Streamlit-in' with Elements!",
#         height=300,
#     )

# with elements("multiple_children"):

#     # You have access to Material UI icons using: mui.icon.IconNameHere
#     #
#     # Multiple children can be added in a single element.
#     #
#     # <Button>
#     #   <EmojiPeople />
#     #   <DoubleArrow />
#     #   Hello world
#     # </Button>

#     mui.Button(
#         mui.icon.EmojiPeople,
#         mui.icon.DoubleArrow,
#         "Button with multiple children"
#     )

#     # You can also add children to an element using a 'with' statement.
#     #
#     # <Button>
#     #   <EmojiPeople />
#     #   <DoubleArrow />
#     #   <Typography>
#     #     Hello world
#     #   </Typography>
#     # </Button>

#     with mui.Button:
#         mui.icon.EmojiPeople()
#         mui.icon.DoubleArrow()
#         mui.Typography("Button with multiple children")
#     # with mui.Button:
#     #     mui.icon.EmojiPeople()
#     #     mui.icon.DoubleArrow()
#     #     mui.Typography("Button with multiple children")
#     # with mui.Button:
#     #     mui.icon.EmojiPeople()
#     #     mui.icon.DoubleArrow()
#     #     mui.Typography("Button with multiple children")

# with elements("nested_children"):

#     # You can nest children using multiple 'with' statements.
#     #
#     # <Paper>
#     #   <Typography>
#     #     <p>Hello world</p>
#     #     <p>Goodbye world</p>
#     #   </Typography>
#     # </Paper>

#     with mui.Paper:
#         with mui.Typography:
#             html.p("Hello world")
#             html.p("Goodbye world")

# with elements("properties"):

#     # You can add properties to elements with named parameters.
#     #
#     # To find all available parameters for a given element, you can
#     # refer to its related documentation on mui.com for MUI widgets,
#     # on https://microsoft.github.io/monaco-editor/ for Monaco editor,
#     # and so on.
#     #
#     # <Paper elevation={3} variant="outlined" square>
#     #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
#     # </Paper>

#     with mui.Paper(elevation=3, variant="outlined", square=True):
#         mui.TextField(
#             label="My text input",
#             defaultValue="Type here",
#             variant="outlined",
#         )

#     # If you must pass a parameter which is also a Python keyword, you can append an
#     # underscore to avoid a syntax error.
#     #
#     # <Collapse in />

#     mui.Collapse(in_=True)

#     # mui.collapse(in=True)
#     # > Syntax error: 'in' is a Python keyword:

# with elements("style_mui_sx"):

#     # For Material UI elements, use the 'sx' property.
#     #
#     # <Box
#     #   sx={{
#     #     bgcolor: 'background.paper',
#     #     boxShadow: 1,
#     #     borderRadius: 2,
#     #     p: 2,
#     #     minWidth: 300,
#     #   }}
#     # >
#     #   Some text in a styled box
#     # </Box>

#     mui.Box(
#         "Some text in a styled box",
#         sx={
#             "bgcolor": "background.paper",
#             "boxShadow": 1,
#             "borderRadius": 2,
#             "p": 2,
#             "minWidth": 300,
#         }
#     )

with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    # with dashboard.Grid(layout):
    #     mui.Paper("First item", key="first_item")
    #     mui.Paper("Second item (cannot drag)", key="second_item")
    #     mui.Paper("Third item (cannot resize)", key="third_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

# with elements("monaco_editors"):

#     # Streamlit Elements embeds Monaco code and diff editor that powers Visual Studio Code.
#     # You can configure editor's behavior and features with the 'options' parameter.
#     #
#     # Streamlit Elements uses an unofficial React implementation (GitHub links below for
#     # documentation).

#     from streamlit_elements import editor

#     if "content" not in st.session_state:
#         st.session_state.content = "Default value"

#     mui.Typography("Content: ", st.session_state.content)

#     def update_content(value):
#         st.session_state.content = value

#     editor.Monaco(
#         height=300,
#         defaultValue=st.session_state.content,
#         onChange=lazy(update_content)
#     )

#     mui.Button("Update content", onClick=sync())

#     editor.MonacoDiff(
#         original="Happy Streamlit-ing!",
#         modified="Happy Streamlit-in' with Elements!",
#         height=300,
#     )