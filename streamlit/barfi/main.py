"""
Check: https://barfi.readthedocs.io/en/latest/streamlit-widget.html
"""
import streamlit as st
st.set_page_config(layout="wide")

from barfi import st_barfi, barfi_schemas, Block

st.title("Web Page")
def feed_func(self):
    in_1 = self.get_interface(name='Input 1')
    self.set_interface(name='Output 1', value=in_1)


st.sidebar.write("Hi")
Tools = { 'A': ['Nespresso', 'Snack'], 
        'B': ['OCR', 'Classify']} 

new_tools = {}
for i in Tools:
    col = []
    for j in Tools[i]:
        block = Block(name=j)
        block.add_input()
        # block.add_input()
        block.add_output()
        # block.add_compute(feed_func)
        col.append(block)
    new_tools[i] = col


Tools = { 'Bridge': ['Combine', 'Split'], 
        'Tool': ['Crop', 'Filter'],
        'Root': ['Start', 'End']} 

for i in Tools:
    col = []
    for j in Tools[i]:
        ## Define each action
        block = Block(name=j)

        if j == 'Combine':    
            block.add_input()
            block.add_input()
            block.add_output()
        elif j == 'Split':
            block.add_input()
            block.add_output()
            block.add_output()
        elif j == 'Start':
            block.add_output()
        elif j == 'End':
            block.add_input()
        else:
            block.add_input()
            block.add_output()

        # block.add_compute(feed_func)
        col.append(block)
    new_tools[i] = col



# from barfi import Block

# feed = Block(name='Feed')
# feed.add_output()

# feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

# mixer = Block(name='Mixer')
# mixer.add_input()
# mixer.add_input()
# mixer.add_output()
# def mixer_func(self):
#     in_1 = self.get_interface(name='Input 1')
#     in_2 = self.get_interface(name='Input 2')
#     value = (in_1 + in_2)
#     self.set_interface(name='Output 1', value=value)
# mixer.add_compute(mixer_func)

# result = Block(name='Result')
# result.add_input()
# def result_func(self):
#     in_1 = self.get_interface(name='Input 1')
# result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

# barfi_result = st_barfi(base_blocks= new_tools)

barfi_result = st_barfi(base_blocks=new_tools,
                    compute_engine=compute_engine, 
                    load_schema=load_schema)

if barfi_result:
    st.write("Result:")
    st.write(barfi_result)
    st.write(barfi_result['editor_state'])

    