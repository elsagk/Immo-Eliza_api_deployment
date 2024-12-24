import joblib
import pandas as pd
from preprocessing.cleaning_data import preprocess

def predict(data: pd.DataFrame) -> float:
    """
    Predict the house price based on the preprocessed input data.
    
    Args:
        data (pd.DataFrame): Data for which prediction is needed.
    
    Returns:
        float: Predicted price of the house.
    """
    # Load the trained model
    model = joblib.load('model/saved_model.pkl')
    
    # Ensure data is preprocessed before prediction
    preprocessed_data = preprocess(data)
    
    # Make prediction
    price = model.predict(preprocessed_data)
    
    return price[0]
