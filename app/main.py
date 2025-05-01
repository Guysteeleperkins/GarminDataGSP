import streamlit as st
from data_processing import load_and_clean_data


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
    
    df = load_and_clean_data("./ActivitiesGarmin.csv")
    
    return st.dataframe(df)


if __name__ == "__main__":
    main()
