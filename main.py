from data_simulation.sensor_simulator import main as run_simulation
from ai_pipeline.model_builder import train_model

def main():
    # Giai đoạn 1: Mô phỏng dữ liệu
    print("Running sensor data simulation...")
    simulation_report = run_simulation()
    
    # Giai đoạn 2: Huấn luyện model
    print("\nTraining AI model...")
    model, metrics = train_model(
        data_path=simulation_report['data_file']
    )
    
    # Giai đoạn 3: Tối ưu cho ESP32
    print("\nOptimizing for ESP32-S3...")
    optimized_model = quantize_and_convert(model)
    
    print("\nULLAI Pipeline Completed!")

if __name__ == "__main__":
    main()
