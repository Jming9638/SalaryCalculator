import streamlit as st
import pandas as pd
from module import *


def run():
    st.set_page_config(
        page_title='Salary Calculator',
        page_icon='📈',
        layout='centered',  # centered, wide
        initial_sidebar_state='auto'  # auto, expanded, collapsed
    )
    
    tabs = st.tabs(['Monthly Salary', 'Bonus Calculator'])
    
    with tabs[0]:
        st.title('Salary Calculator')
        with st.sidebar:
            salary = st.number_input(
                label='Salary',
                min_value=0,
                max_value=None,
                value=0,
                step=100,
            )
        
        if salary > 0:
            monthly_salary(salary)
            
    with tabs[1]:
        bonus_cols = st.columns((1, 1))
        
        with bonus_cols[0]:
            st.title('Bonus Calculator')
        with bonus_cols[1]:
            bonus_mth = st.number_input(
                label='No. of month(s)',
                min_value=1.0,
                max_value=None,
                value=1.0,
                step=0.5
            )
        bonus(bonus_mth)
        
    
if __name__ == "__main__":
    run()
    