import pandas as pd

def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the input data by handling missing values and encoding categorical features.
    Cleans the dataset by handling missing values.
    
    Args:
        data (pd.DataFrame): Raw data to preprocess.
    
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    # Make a copy of the data to avoid in-place modifications
    data = data.copy()
        # Expected feature order based on training
    expected_features = [
        "bedrooms",
        "price_sqm",
        "terrace",
        "garden",
        "pool",
        "livingarea",
        "surfaceoftheplot",
        "gardensurface",
        "facades",
    ]

    # Align the input data to the expected feature order
    data = data.reindex(columns=expected_features, fill_value=0)
    
    # Handle missing values for numerical columns
    for col in data.select_dtypes(include=["float64", "int64"]).columns:
        data[col].fillna(data[col].median(), inplace=True)

    # Handle missing values for categorical columns
    for col in data.select_dtypes(include=["object"]).columns:
        data[col].fillna(data[col].mode()[0], inplace=True)

    # Drop unnecessary columns
    columns_to_drop = ["Unnamed: 0", "municipality_code", "locality", "postal_code"]
    data.drop(columns=columns_to_drop, errors="ignore", inplace=True)

    return data
