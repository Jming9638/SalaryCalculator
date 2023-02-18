import streamlit as st
import pandas as pd


def monthly_salary(salary):
    st.subheader(f'Salary: RM {salary:.2f}')
        
    employer_epf = salary * 0.13
    employee_epf = salary * 0.11
    
    socso_df = pd.read_csv('socso_contribution.csv')
    socso_salary_rate = socso_df[socso_df['upper'] <= salary].iloc[-1]
    employer_socso = socso_salary_rate['employer']
    employee_socso = socso_salary_rate['employee']
    
    overall_eis = salary * 0.4 / 100
    employer_eis = overall_eis / 2 - 0.1
    employee_eis = overall_eis / 2 - 0.1
    
    total_employer_deduction = employer_epf + employer_socso + employer_eis
    total_employee_deduction = employee_epf + employee_socso + employee_eis
    
    net_salary_df = pd.DataFrame(
        data=[[employer_epf, employee_epf], 
                [employer_socso, employee_socso], 
                [employer_eis, employee_eis], 
                [total_employer_deduction, total_employee_deduction]],
        columns=["Employer's", "Employee's"],
        index=['EPF', 'SOCSO', 'EIS', 'Total Deduction'],
    )
    
    st.table(net_salary_df.style.format({"Employer's": "{:.2f}", "Employee's": "{:.2f}"}))
    st.subheader(f'Nett Pay (exclusive Income Tax): RM {(salary - total_employee_deduction):.2f}')
    
    
def bonus(bonus_mth):
    cols = st.columns((1, 1, 1))
    with cols[0]:
        salary_jan = st.number_input(
            label='January Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='jan'
        )
        
        salary_apr = st.number_input(
            label='April Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='apr'
        )
        
        salary_july = st.number_input(
            label='July Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='july'
        )
        
        salary_oct = st.number_input(
            label='October Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='oct'
        )
        
    with cols[1]:
        salary_feb = st.number_input(
            label='Febuary Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='feb'
        )
        
        salary_may = st.number_input(
            label='May Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='may'
        )
        
        salary_aug = st.number_input(
            label='August Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='aug'
        )
        
        salary_nov = st.number_input(
            label='November Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='nov'
        )
        
    with cols[2]:
        salary_mar = st.number_input(
            label='March Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='mar'
        )
        
        salary_june = st.number_input(
            label='June Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='june'
        )
        
        salary_sep = st.number_input(
            label='September Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='sep'
        )
        
        salary_dec = st.number_input(
            label='December Salary',
            min_value=0,
            max_value=None,
            value=0,
            step=100,
            key='dec'
        )
        
    annual_salary = salary_jan + \
                    salary_feb + \
                    salary_mar + \
                    salary_apr + \
                    salary_may + \
                    salary_june + \
                    salary_july + \
                    salary_aug + \
                    salary_sep + \
                    salary_oct + \
                    salary_nov + \
                    salary_dec
                    
    if annual_salary > 0:
        gross_bonus = round((annual_salary / 12) * bonus_mth, 2)
        st.subheader(f'Gross Bonus: RM {gross_bonus:.2f}')
    