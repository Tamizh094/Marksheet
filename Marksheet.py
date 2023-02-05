

import streamlit as st
import pandas as pd

st.set_page_config(page_title='Mark Sheet2', layout='wide')

main,ps,lg,mt,mp = st.columns(5)
df = pd.read_csv("C:\\Users\\Tamizharasan\\Project_teamsup\\Version2\\MarkSheet.csv")

with st.form(key = 'test',clear_on_submit=True):
    with main:
        st.markdown("Main Details")
        name = st.text_input("please enter your name")
        bid = st.text_input("Please enter your bits id")
        df_main = pd.DataFrame({'Name':name,'Bits Id':bid},index=[0])
        
    with ps:
        st.markdown("Probability & Statistics")
        pq1 = st.number_input("Please enter your P&S Quiz 1 mark")
        pq2 = st.number_input("Please enter your P&S Quiz 2 mark")
        img = st.file_uploader("Please upload mark sheet")
        df_sub2 = pd.DataFrame({'Quiz 1':pq1,'Quiz 2':pq2},index=[0])
        df_main['Probability & Statistics'] = df_sub2['Quiz 1'] + df_sub2['Quiz 2']
        
    with lg:
        st.markdown("Linear Algebra")
        lq1 = st.number_input("Please enter your L&A Quiz 1 mark")
        lq2 = st.number_input("Please enter your L&A Quiz 2 mark")
        df_sub1 = pd.DataFrame({'Quiz 1':lq1,'Quiz 2':lq2},index=[0])
        df_main['Linear Algebra'] = df_sub1['Quiz 1'] + df_sub1['Quiz 2']
        
    with mt:
        st.markdown("Mechanical Technology")
        mq1 = st.number_input("Please enter your MT Quiz 1 mark")
        mq2 = st.number_input("Please enter your MT Quiz 2 mark")
        df_sub3 = pd.DataFrame({'Quiz 1':mq1,'Quiz 2':mq2},index=[0])
        df_main['Mech Technology'] = df_sub3['Quiz 1'] + df_sub3['Quiz 2']
    
    with mp:
        st.markdown("Mechanical Measurements")
        pq1 = st.number_input("Please enter your MM Quiz 1 mark")
        pq2 = st.number_input("Please enter your MM Quiz 2 mark")
        df_sub4 = pd.DataFrame({'Quiz 1':pq1,'Quiz 2':pq2},index=[0])
        df_main['Mech Measurement'] = df_sub4['Quiz 1'] + df_sub4['Quiz 2']
        
    if st.form_submit_button():
        st.dataframe(df_main)      
        df_final = pd.concat([df,df_main],ignore_index=True,axis=0,join='inner')
        df = df_final.to_csv('MarkSheet.csv')
