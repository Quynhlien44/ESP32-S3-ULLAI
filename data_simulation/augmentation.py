import numpy as np
import pandas as pd

def time_warping(df, factor=0.2):
    """Biến dạng trục thời gian để tăng tính thực tế"""
    # Implementation...
    return warped_df

def add_sensor_dropout(df, sensor, dropout_prob=0.01, max_duration=5):
    """Mô phỏng cảm biến mất tín hiệu"""
    # Implementation...
    return df

def cross_sensor_interference(df):
    """Mô phỏng nhiễu chéo giữa các cảm biến"""
    df['temp_c'] += 0.01 * df['light_v'] * np.random.normal(0, 0.5, len(df))
    df['humidity_pct'] -= 0.005 * df['temp_c'] * np.random.uniform(-1, 1, len(df))
    return df

def enhance_data_augmentation(df):
    """Tổng hợp các kỹ thuật tăng cường dữ liệu"""
    df = time_warping(df, factor=0.15)
    
    if random.random() < 0.05:
        df = add_sensor_dropout(df, 'light_v')
        
    return cross_sensor_interference(df)
