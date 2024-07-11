import altair as alt
import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


def number_to_text(x):
    return "Si" if x == 1 else "No"


@st.cache_data
def load_data(data_path):
    df = pd.read_csv(data_path)
    df.es_superhost = df.es_superhost.map(number_to_text)
    df.servicio_aire_acondicionado = df.servicio_aire_acondicionado.map(number_to_text)
    return df


def add_title_and_description():
    st.title("Airbnb")


def show_airbnb_dataframe(df):
    pass


def country_filter(df):
    pass


def show_airbnb_in_map(df, is_all_data):
    pass


def plot_days_of_week(df, column):
    pass


def plot_airbnb_by_superhost(df, column):
    pass


def interactive_view(df):
    pass


if __name__ == "__main__":
    df = load_data("Airbnb_Locations.csv")
    add_title_and_description()
    show_airbnb_dataframe(df)
    
    # Descomentar a medida que avancemos

    # filtered_df = country_filter(df)
    # show_airbnb_in_map(filtered_df, filtered_df.shape == df.shape)
    # column_1, column_2 = st.columns(2)
    # plot_days_of_week(filtered_df, column_1)
    # plot_airbnb_by_superhost(filtered_df, column_2)
    # interactive_view(filtered_df)
