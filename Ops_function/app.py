"""
Author: Chieh
Based on Streamlit web page to do the ops calculating.
"""

import streamlit as st

symbol_calculator = {'>':0, '<':1, '==':2, '>=':3, '<=':4}
Class_ = ['Apple', 'Boxes', 'Papers']

if __name__ == '__main__':

    number_states = st.number_input("How many states are used for this project?", 1, 20,3)
    for lop in range(number_states):
        st.markdown("# No. {}".format(lop))
        iforandcol1, iforandcol2 = st.columns([1,1]) 
        with iforandcol1:
            iforand = st.checkbox('Advanced conditions', key='AC_'+str(lop))
        with iforandcol2:
            if iforand:
                number_iforand = st.number_input("How many conditions are used for this project?", 1, 20, 1, key='Conditions'+str(lop))
            else:
                pass
        st.markdown("---")
        if iforand:
            # st.write("IF ...")
            collect_ = []
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
                        And_or_cond = st.selectbox("Choose the operator.", ["Or", "And"], key='COND'+str(lop)+str(nuIforand))
                    start_nuIforand += '{} '.format(And_or_cond)
                    with And_or_cond1:
                        st.write("# {}".format(And_or_cond))
                    with And_or_cond3:
                        if_cond = st.number_input("Add Ops number", 0, None, 1, key='COND_if'+str(lop)+str(nuIforand))
                else:
                    with CScol1:
                        if_cond = st.number_input("Add Ops number", 0, None, 1, key='COND_if'+str(lop)+str(nuIforand))

                Ccol1, Scol1, Ncol1 = st.columns(3) 
                with Ccol1:
                    Class_cond = st.selectbox("Choose the operator.", Class_, key='COND'+str(lop)+str(nuIforand)+'class')
                with Scol1:
                    sym_cond = st.selectbox("Choose a condition.", list(symbol_calculator.keys()), key='COND'+str(lop)+str(nuIforand)+'cond')
                with Ncol1:
                    number_cond = st.number_input("Number", 0, None, 1, key='COND'+str(lop)+str(nuIforand)+'number')
                
                start_nuIforand += str(Class_cond) + ' ' + str(sym_cond) + ' ' + str(number_cond) + ' '
                if if_cond > 0:
                    for New_if_cond in range(if_cond):
                        Nifcol1, NCcol1, NScol1, NNcol1 = st.columns(4) 
                        with Nifcol1:
                            New_if_cond_ops = st.selectbox("Choose the operator.", ["And", "Or"], key='COND'+str(lop)+str(nuIforand)+str(New_if_cond))
                        with NCcol1:
                            Class_cond = st.selectbox("Choose the operator.", Class_, key='COND'+str(lop)+str(nuIforand)+'class'+str(New_if_cond))
                        with NScol1:
                            sym_cond = st.selectbox("Choose a condition.", list(symbol_calculator.keys()), key='COND'+str(lop)+str(nuIforand)+'cond'+str(New_if_cond))
                        with NNcol1:
                            number_cond = st.number_input("Number", 0, None, 1, key='COND'+str(lop)+str(nuIforand)+'number'+str(New_if_cond))

                        start_nuIforand += str(New_if_cond_ops).lower() + ' ' + str(Class_cond) + ' ' + str(sym_cond) + ' ' + str(number_cond)
                
                TorFcond = st.selectbox("As OK or NG?", ["OK", "NG"], key='COND'+str(lop)+str(nuIforand)+'okng')

                collect_.append(start_nuIforand)
                start_nuIforand += ' :'
                st.write(start_nuIforand)
                st.write("As {}".format(TorFcond))

            st.markdown("---")