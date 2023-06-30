import streamlit as st
import pickle

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals',
         'Gujarat Lions']

city =['Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Delhi', 'Rajkot',
       'Indore', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai', 'Cape Town',
       'Port Elizabeth', 'Durban', 'Centurion', 'East London',
       'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
       'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Game Win Predictor')
col1, col2 = st.beta_columns(2)

with col1:
    batting_team = st.selectbox('select the batting team',sorted(teams))

with col2:
    bowling_team = st.selectbox('select bowling team',sorted(teams))