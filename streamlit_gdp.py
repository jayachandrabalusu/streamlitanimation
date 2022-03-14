import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()
st.write(df)

#year_options = df['year'].unique().tolist()
#year = st.selectbox('which year would you like to see ?',year_options,0)
#df = df[df['year'] == year]

fig = px.scatter(df,x="gdpPercap", y="lifeExp", size="pop", color="continent", 
        hover_name="country", log_x=True, size_max=55, animation_frame="year", 
        animation_group="country",
        range_x=[100,100000], range_y=[25,90])
fig.update_layout(width= 800)
st.write(fig)