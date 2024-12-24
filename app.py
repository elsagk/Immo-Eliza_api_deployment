import streamlit as st
import pandas as pd
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict


def get_user_input():
    """
    Collects user input for house features.
    
    Returns:
        pd.DataFrame: Dataframe containing user input.
    """
    bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=5)
    price_sqm = st.number_input('Price per Square Meter', min_value=1000, max_value=20000, value=5000)
    terrace = st.selectbox('Terrace', ['No', 'Yes'])
    garden = st.selectbox('Garden', ['No', 'Yes'])
    pool = st.selectbox('Pool', ['No', 'Yes'])
    livingarea = st.number_input('Living Area (m²)', min_value=20, max_value=1000, value=80)
    surfaceoftheplot = st.number_input('Surface of the Plot (m²)', min_value=50, max_value=2000, value=300)
    facades = st.number_input('Number of Facades', min_value=1, max_value=4, value=2)  # Add this
    gardensurface = st.number_input('Garden Surface (m²)', min_value=0, max_value=2000, value=50)  # Add this

    data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'price_sqm': [price_sqm],
        'terrace': [1 if terrace == 'Yes' else 0],
        'garden': [1 if garden == 'Yes' else 0],
        'pool': [1 if pool == 'Yes' else 0],
        'livingarea': [livingarea],
        'surfaceoftheplot': [surfaceoftheplot],
        'facades': [facades],  # Add this
        'gardensurface': [gardensurface]  # Add this
    })

    return data

def main():
    st.title('Real Estate Price Prediction')
    st.write("Input the details of a house below to predict its market price.")
    st.subheader("Project Overview")
    st.markdown(
        """
        *The app is designed to help sellers evaluate their property price.
        *Its objective is to provide a reliable price estimation:
        - Based on the most impactful property features of the real estate market.
        - Generated through a machine learning model.
        """
    )

    user_data = get_user_input()

    st.subheader('House Features')
    st.write(user_data)

    if st.button('Predict Price'):
        try:
            # Preprocess user input data
            preprocessed_data = preprocess(user_data)
            
            # Predict price
            price = predict(preprocessed_data)
            
            # Display prediction
            st.success(f'Predicted Price: ${price:,.2f}')
        except Exception as e:
            st.error(f"Prediction Error: {e}")



if __name__ == "__main__":
    main()
