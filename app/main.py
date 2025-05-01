import streamlit as st


def main():
    """Main function to run Streamlit app."""
    st.set_page_config(
        page_title="GSP Garmin Data",
        page_icon="🏃🏼‍♂️",
        layout="wide",
        initial_sidebar_state="auto",
    )

    # Set the title of the app
    st.title("GSP Garmin Dataset Explorer")
