import pandas as pd
from datetime import datetime

def process_data(input_path, output_path):
    """Process the input data and save to output path"""
    
    # Read input data
    df = pd.read_csv(input_path)
    
    # Add processing timestamp
    df['processing_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Calculate days since joining
    df['join_date'] = pd.to_datetime(df['join_date'])
    df['days_since_joining'] = (pd.to_datetime('today') - df['join_date']).dt.days
    
    # Save processed data
    df.to_csv(output_path, index=False)
    
    return f"Data processed and saved to {output_path}"