def get_sampling_config(mode="prototype"):
    """Cấu hình sampling rate theo chế độ hoạt động"""
    config = {
        "prototype": {
            "nsl19m51": 10,    # 10Hz
            "dht22": 0.5,       # 2s/reading
            "sgp30": 1          # 1Hz
        },
        "production": {
            "nsl19m51": 200,    # 200Hz
            "dht22": 0.5,       # Giữ nguyên
            "sgp30": 5          # 5Hz
        },
        "stress_test": {
            "nsl19m51": 500,    # 500Hz
            "dht22": 0.2,       # 5 readings/s
            "sgp30": 10         # 10Hz
        }
    }
    return config[mode]

def configure_sampling(scenario, mode="prototype"):
    """Áp dụng cấu hình cho từng kịch bản"""
    base_config = get_sampling_config(mode)
    
    # Tuỳ chỉnh theo kịch bản
    if scenario == "rapid_change":
        base_config["nsl19m51"] = min(300, base_config["nsl19m51"] * 1.5)
    
    return base_config
