import streamlit as st
import xlwings as xw
from data_cleaner import data_cleaner

st.header("Expense Handler")
st.subheader('''Please Select From The Following Functionalities:
             1. POWERBI
    2. Data Reading and Cleaning''')

options = st.selectbox('Please Select', ['PowerBI', 'Generate and Clean Data and Run SQL'])

if options == 'PowerBI':
    print("Getting Report Data")
    st.markdown('<iframe title="PF_BI - Git" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=49a3932e-6e4f-4f51-8611-f42b1cae25bb&autoAuth=true&ctid=d9ea170a-8537-4b78-9cb4-664401b48d6f" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)

elif options == 'Generate and Clean Data and Run SQL':
    print("Cleaning Data")
    wb = xw.Book('Master_PF.xlsm')
    wb.macro('statement_reader')()
    wb.macro('save_data_to_existing_CSV')()
    wb.close()
    data_cleaner()
#SQLCMD -S localhost\MSSQLSERVER01 -i Automation_Run_Job.sql


#= Table.TransformColumnTypes(dbo_PF_DATA,{{"Date", type date}, {"Withdrawal Amt", type number}, {"Deposit Amt", type number}, {"Closing Balance", type number}, {"Review Status", type logical}})