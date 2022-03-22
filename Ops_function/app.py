"""
Author: Chieh
Based on Streamlit web page to do the ops calculating.
"""

import streamlit as st

class ops_dev(object):
    def __init__(self, Class_):
        self.class_ = Class_
        # self.symbol_calculator = {'>':0, '<':1, '==':2, '>=':3, '<=':4}
        self.symbol_calculator = ['>', '<', '==', '>=', '<=']
    
    def Calculator(self, number_iforand):
        collect_ = []
        Graph_display_expander = st.expander(label='Expand me')
        with Graph_display_expander:
            for nuIforand in range(number_iforand):
                
                start_nuIforand = ''
                CCcol1, CScol1 = st.columns(2) 
                with CCcol1:
                    if nuIforand == 0:
                        start_nuIforand += 'If '
                        st.write("# If ")
                        turn_on_And_or_cond = False
                    else:
                        turn_on_And_or_cond = True

                if turn_on_And_or_cond:
                    And_or_cond1, And_or_cond2, And_or_cond3 = st.columns(3) 
                    with And_or_cond2:
                        And_or_cond = st.selectbox("Operator", ["Or", "And"], key='COND'+str(lop)+str(nuIforand))
                    start_nuIforand += '{} '.format(And_or_cond)
                    with And_or_cond1:
                        st.write("# {}".format(And_or_cond))
                    with And_or_cond3:
                        if_cond = st.number_input("Add Ops number", 0, None, 1, key='COND_if'+str(lop)+str(nuIforand))
                else:
                    with CScol1:
                        if_cond = st.number_input("Add Ops number", 0, None, 1, key='COND_if'+str(lop)+str(nuIforand))

                Tcol1, Ccol1, Scol1, Ncol1 = st.columns([2,2,1,2])
                with Tcol1:
                    Types_cond = st.selectbox("Type", ['Class', 'Scores','BBox_size'], key='COND'+str(lop)+str(nuIforand)+'class')
                if Types_cond == 'Class':
                    with Ccol1:
                        Class_cond = st.selectbox("Class", Class_, key='COND'+str(lop)+str(nuIforand)+'class')
                else:
                    with Ccol1:
                        Class_cond = Types_cond

                with Scol1:
                    # sym_cond = st.selectbox("Choose a condition.", list(self.symbol_calculator.keys()), key='COND'+str(lop)+str(nuIforand)+'cond')
                    sym_cond = st.selectbox("Symbol", self.symbol_calculator, key='COND'+str(lop)+str(nuIforand)+'cond')
                with Ncol1:
                    if Types_cond == 'Class':
                        number_cond = st.number_input("Number", 0, None, 1, key='COND'+str(lop)+str(nuIforand)+'number')
                    elif Types_cond == 'Scores':
                        number_cond = st.slider("Score threshold", 0.00, 1.00, 0.7, 0.01, format="%f", key='scoreCOND'+str(lop)+str(nuIforand)+'number')
                    elif Types_cond == 'BBox_size':
                        number_cond = st.slider("BBox size threshold (%)", 0, 100, 80, 1, format="%d", key='bboxCOND'+str(lop)+str(nuIforand)+'number')
                        number_cond *= 0.01
                        
                start_nuIforand += str(Class_cond) + ' ' + str(sym_cond) + ' ' + str(number_cond) + ' '
                
                if if_cond > 0:
                    for New_if_cond in range(int(if_cond)):
                        # Nifcol1, NCcol1, NScol1, NNcol1 = st.columns([1,2,1,2]) 
                        # with Nifcol1:
                        #     New_if_cond_ops = st.selectbox("Operator", ["And", "Or"], key='COND'+str(lop)+str(nuIforand)+str(New_if_cond))
                        # with NCcol1:
                        #     Class_cond = st.selectbox("Class", Class_, key='COND'+str(lop)+str(nuIforand)+'class'+str(New_if_cond))
                        # with NScol1:
                        #     # sym_cond = st.selectbox("Choose a condition.", list(self.symbol_calculator.keys()), key='COND'+str(lop)+str(nuIforand)+'cond'+str(New_if_cond))
                        #     sym_cond = st.selectbox("Symbol", self.symbol_calculator, key='COND'+str(lop)+str(nuIforand)+'cond'+str(New_if_cond))
                        # with NNcol1:
                        #     number_cond = st.number_input("Number", 0, None, 1, key='COND'+str(lop)+str(nuIforand)+'number'+str(New_if_cond))

                        Nifcol1, TCcol1, NCcol1, NScol1, NNcol1 = st.columns([1.5, 2, 2, 1, 2]) ### Ops, Type, Class, Symbol, Number
                        with Nifcol1:
                            New_if_cond_ops = st.selectbox("Operator", ["And", "Or"], key='COND'+str(lop)+str(nuIforand)+str(New_if_cond))
                        with TCcol1:
                            Types_cond = st.selectbox("Type", ['Class', 'Scores','BBox_size'], key='type_COND'+str(lop)+str(nuIforand)+str(New_if_cond))
                        
                        if Types_cond == 'Class':
                            with NCcol1:
                                Class_cond = st.selectbox("Class", Class_, key='COND'+str(lop)+str(nuIforand)+'class'+str(New_if_cond))
                        else:
                            Class_cond = Types_cond
                        with NScol1:
                            # sym_cond = st.selectbox("Choose a condition.", list(self.symbol_calculator.keys()), key='COND'+str(lop)+str(nuIforand)+'cond'+str(New_if_cond))
                            sym_cond = st.selectbox("Symbol", self.symbol_calculator, key='COND'+str(lop)+str(nuIforand)+'cond'+str(New_if_cond))
                        with NNcol1:
                            if Types_cond == 'Class':
                                number_cond = st.number_input("Number", 0, None, 1, key='COND'+str(lop)+str(nuIforand)+'number'+str(New_if_cond))
                            elif Types_cond == 'Scores':
                                    Class_cond = st.slider("Score threshold", 0.00, 1.00, 0.7, 0.01, format="%f", key='COND'+str(lop)+str(nuIforand)+'number'+str(New_if_cond))
                            elif Types_cond == 'BBox_size':
                                number_cond = st.slider("BBox size threshold (%)", 0, 100, 80, 1, format="%d", key='COND'+str(lop)+str(nuIforand)+'number'+str(New_if_cond))
                                number_cond *= 0.01
                    
                        start_nuIforand += str(New_if_cond_ops).lower() + ' ' + str(Class_cond) + ' ' + str(sym_cond) + ' ' + str(number_cond) + ' '
                
                TorFcond = st.selectbox("As OK or NG?", ["OK", "NG"], key='COND'+str(lop)+str(nuIforand)+'okng')

                collect_.append(start_nuIforand.rstrip())
                start_nuIforand += ' :'
                st.markdown("> {} as {}".format(start_nuIforand, TorFcond))

                if (nuIforand+1) != number_iforand: 
                    st.markdown("---")

        return collect_

if __name__ == '__main__':

    Class_ = ['Apple', 'Pens', 'Papers']
    
    ops_dev = ops_dev(Class_)
    number_states = st.number_input("How many states are used for this project?", 1, 20, 1)
    for lop in range(number_states):
        st.markdown("# No. {}".format(lop))
        iforandcol1, iforandcol2 = st.columns([1,1]) 
        with iforandcol1:
            iforand = st.checkbox('Advanced conditions', key='AC_'+str(lop))
        with iforandcol2:
            if iforand:
                number_iforand = st.number_input("Add one more condition?", 1, 20, 1, key='Conditions'+str(lop))
            else:
                pass
        st.markdown("---")
        if iforand:
            # st.write("IF ...")
            collect_ = ops_dev.Calculator(number_iforand)
            # st.write(collect_)