import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import streamlit as st

def viz():
    st.subheader('Dataset')
    df = pd.read_csv("Dataset/penguins_size.csv")
    st.write(df)
    
    # clear data
    df = df.dropna(subset=['body_mass_g'])
    df['sex'].fillna('MALE', inplace=True)
    df['sex'] = df['sex'].replace({'.': 'FEMALE'})
    
    # Plotting
    st.subheader("PLot Diagrams")
    
    # plot 1
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "violin"}, {"type": "box"}]])
    fig.add_trace(go.Violin(x=df["species"], y=df["culmen_length_mm"], name="violin"), row=1, col=1)
    fig.add_trace(go.Box(x=df["species"], y=df["culmen_length_mm"], name="box"), row=1, col=2)
    fig.update_layout(title="Culmen Length by species")
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 2
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "violin"}, {"type": "box"}]])
    fig.add_trace(go.Violin(x=df["species"], y=df["culmen_depth_mm"], name="violin"), row=1, col=1)
    fig.add_trace(go.Box(x=df["species"], y=df["culmen_depth_mm"], name="box"), row=1, col=2)
    fig.update_layout(title="Culmen Depth by species")
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 3
    fig = px.histogram(df, x="flipper_length_mm", color="sex", title='Flipper Length by species')
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 4
    fig = px.histogram(df, x="body_mass_g", color="species", title='Body Mass Distribution')
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 5
    fig = px.scatter_3d(df, x='culmen_length_mm', y='culmen_depth_mm', z='flipper_length_mm', color='species', title='Culmen - Flipper')
    st.plotly_chart(fig, use_container_width=True)
    
    # Plot 6
    fig = px.scatter_3d(df, x='culmen_length_mm', y='culmen_depth_mm', z='body_mass_g', color='species', title='Culmen - Body mass')
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 7
    fig = px.histogram(df, x="island", color='species', title='Which island consists of most Penguins?')
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 8
    fig = px.bar(df, x="species", y='culmen_length_mm', color='sex', title ='Which species have highest culmen length?')
    st.plotly_chart(fig, use_container_width=True)
    
    # plot 8
    fig = px.pie(df, names="species", color='culmen_depth_mm', title ='Which species have highest culmen depth?')
    st.plotly_chart(fig, use_container_width=True)
    