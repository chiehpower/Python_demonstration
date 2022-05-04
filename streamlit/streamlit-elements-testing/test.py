"""
Referred from official Github repo.
"""
# First, import the elements you need

import streamlit as st

from streamlit_elements import elements, mui, html, lazy, sync, nivo
from functools import partial

from uuid import uuid4
from abc import ABC, abstractmethod
from streamlit_elements import dashboard, mui
from contextlib import contextmanager

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace
import json
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

with elements("style_mui_sx"):

    # For Material UI elements, use the 'sx' property.
    #
    # <Box
    #   sx={{
    #     bgcolor: 'background.paper',
    #     boxShadow: 1,
    #     borderRadius: 2,
    #     p: 2,
    #     minWidth: 300,
    #   }}
    # >
    #   Some text in a styled box
    # </Box>

    mui.Box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 1,
            "borderRadius": 2,
            "p": 2,
            "minWidth": 300,
        }
    )

with elements("style_elements_css"):

    # For any other element, use the 'css' property.
    #
    # <div
    #   css={{
    #     backgroundColor: 'hotpink',
    #     '&:hover': {
    #         color: 'lightgreen'
    #     }
    #   }}
    # >
    #   This has a hotpink background
    # </div>

    html.div(
        "This has a hotpink background",
        css={
            "backgroundColor": "hotpink",
            "&:hover": {
                "color": "lightgreen"
            }
        }
    )

# with elements("dashboard"):

#     # You can create a draggable and resizable dashboard using
#     # any element available in Streamlit Elements.

#     from streamlit_elements import dashboard

#     # First, build a default layout for every element you want to include in your dashboard

#     layout = [
#         # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
#         dashboard.Item("first_item", 0, 0, 2, 2),
#         dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
#         dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
#     ]

#     # Next, create a dashboard layout using the 'with' syntax. It takes the layout
#     # as first parameter, plus additional properties you can find in the GitHub links below.

#     # with dashboard.Grid(layout):
#     #     mui.Paper("First item", key="first_item")
#     #     mui.Paper("Second item (cannot drag)", key="second_item")
#     #     mui.Paper("Third item (cannot resize)", key="third_item")

#     # If you want to retrieve updated layout values as the user move or resize dashboard items,
#     # you can pass a callback to the onLayoutChange event parameter.

#     def handle_layout_change(updated_layout):
#         # You can save the layout in a file, or do anything you want with it.
#         # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
#         print(updated_layout)

#     with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
#         mui.Paper("First item", key="first_item")
#         mui.Paper("Second item (cannot drag)", key="second_item")
#         mui.Paper("Third item (cannot resize)", key="third_item")

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


class Dashboard:
    
    DRAGGABLE_CLASS = "draggable"

    _layout = []

    @contextmanager
    def __call__(self, **props):
        # Draggable classname query selector.
        props["draggableHandle"] = f".{Dashboard.DRAGGABLE_CLASS}"

        with dashboard.Grid(Dashboard._layout, **props):
            yield

    class Item(ABC):

        def __init__(self, x, y, w, h, **item_props):
            self._key = str(uuid4())
            self._draggable_class = Dashboard.DRAGGABLE_CLASS
            self._dark_mode = True
            Dashboard._layout.append(dashboard.Item(self._key, x, y, w, h, **item_props))

        def _switch_theme(self):
            self._dark_mode = not self._dark_mode

        @contextmanager
        def title_bar(self, padding="5px 15px 5px 15px", dark_switcher=True):
            with mui.Stack(
                className=self._draggable_class,
                alignItems="center",
                direction="row",
                spacing=1,
                sx={
                    "padding": padding,
                    "borderBottom": 1,
                    "borderColor": "divider",
                },
            ):
                yield

                if dark_switcher:
                    if self._dark_mode:
                        mui.IconButton(mui.icon.DarkMode, onClick=self._switch_theme)
                    else:
                        mui.IconButton(mui.icon.LightMode, sx={"color": "#ffc107"}, onClick=self._switch_theme)

        @abstractmethod
        def __call__(self):
            """Show elements."""
            raise NotImplementedError


class Editor(Dashboard.Item):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._dark_theme = False
        self._index = 0
        self._tabs = {}
        self._editor_box_style = {
            "flex": 1,
            "minHeight": 0,
            "borderBottom": 1,
            "borderTop": 1,
            "borderColor": "divider"
        }

    def _change_tab(self, _, index):
        self._index = index

    def update_content(self, label, content):
        self._tabs[label]["content"] = content

    def add_tab(self, label, default_content, language):
        self._tabs[label] = {
            "content": default_content,
            "language": language
        }

    def get_content(self, label):
        return self._tabs[label]["content"]

    def __call__(self):
        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):

            with self.title_bar("0px 15px 0px 15px"):
                mui.icon.Terminal()
                mui.Typography("Editor")

                with mui.Tabs(value=self._index, onChange=self._change_tab, scrollButtons=True, variant="scrollable", sx={"flex": 1}):
                    for label in self._tabs.keys():
                        mui.Tab(label=label)

            for index, (label, tab) in enumerate(self._tabs.items()):
                with mui.Box(sx=self._editor_box_style, hidden=(index != self._index)):
                    editor.Monaco(
                        css={"padding": "0 2px 0 2px"},
                        defaultValue=tab["content"],
                        language=tab["language"],
                        onChange=lazy(partial(self.update_content, label)),
                        theme="vs-dark" if self._dark_mode else "light",
                        path=label,
                        options={
                            "wordWrap": True
                        }
                    )

            with mui.Stack(direction="row", spacing=2, alignItems="center", sx={"padding": "10px"}):
                mui.Button("Apply", variant="contained", onClick=sync())
                mui.Typography("Or press ctrl+s", sx={"flex": 1})

class Pie(Dashboard.Item):
    
    DEFAULT_DATA = [
        { "id": "java", "label": "java", "value": 465, "color": "hsl(128, 70%, 50%)" },
        { "id": "rust", "label": "rust", "value": 140, "color": "hsl(178, 70%, 50%)" },
        { "id": "scala", "label": "scala", "value": 40, "color": "hsl(322, 70%, 50%)" },
        { "id": "ruby", "label": "ruby", "value": 439, "color": "hsl(117, 70%, 50%)" },
        { "id": "elixir", "label": "elixir", "value": 366, "color": "hsl(286, 70%, 50%)" }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                # "background": "#FF975D",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        # "background": "#FF975D",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.PieChart()
                mui.Typography("Pie chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Pie(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                    innerRadius=0.5,
                    padAngle=0.7,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="grey",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={ "from": "color" },
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        { "match": { "id": "ruby" }, "id": "dots" },
                        { "match": { "id": "c" }, "id": "dots" },
                        { "match": { "id": "go" }, "id": "dots" },
                        { "match": { "id": "python" }, "id": "dots" },
                        { "match": { "id": "scala" }, "id": "lines" },
                        { "match": { "id": "lisp" }, "id": "lines" },
                        { "match": { "id": "elixir" }, "id": "lines" },
                        { "match": { "id": "javascript" }, "id": "lines" }
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )


class Card(Dashboard.Item):

    DEFAULT_CONTENT = (
        "This impressive paella is a perfect party dish and a fun meal to cook "
        "together with your guests. Add 1 cup of frozen peas along with the mussels, "
        "if you like."
    )

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="Shrimp and Chorizo Paella",
                subheader="September 14, 2016",
                avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class,
            )
            mui.CardMedia(
                component="img",
                height=194,
                image="https://mui.com/static/images/cards/paella.jpg",
                alt="Paella dish",
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(content)

            with mui.CardActions(disableSpacing=True):
                mui.IconButton(mui.icon.Favorite)
                mui.IconButton(mui.icon.Share)

class ChiehCard(Dashboard.Item):
    
    DEFAULT_CONTENT = (
        "if you like."
    )

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="Shrimp and Chorizo Paella",
                subheader="September 14, 2016",
                avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class,
            )
            mui.CardMedia(
                component="img",
                height=194,
                image="https://mui.com/static/images/cards/paella.jpg",
                alt="Paella dish",
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography(content)

            with mui.CardActions(disableSpacing=True):
                mui.IconButton(mui.icon.Favorite)
                mui.IconButton(mui.icon.Share)

if __name__ == '__main__':

    if "w" not in state:
        w = SimpleNamespace(
            dashboard=Dashboard(),
            card=Card(6, 7, 3, 7, minW=2, minH=4),
            chieh=ChiehCard(0, 7, 6, 7, minW=1, minH=2),
        )
        state.w = w
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)
        with w.dashboard(rowHeight=57):
            w.card(Card.DEFAULT_CONTENT)
            w.chieh('hi')