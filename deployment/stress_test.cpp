#include "esp_timer.h"
#include "inference_engine.h"

void run_stress_test(InferenceEngine& engine) {
    // 1. Tạo dữ liệu đầu vào cực đoan
    std::vector<std::vector<float>> test_cases = {
        {2.7f, 80.0f, 100.0f, 60000.0f, 60000.0f}, // Max values
        {0.18f, -40.0f, 0.0f, 0.0f, 400.0f},        // Min values
        // ... các trường hợp biên khác
    };
    
    // 2. Đo thời gian inference
    for (auto& test_case : test_cases) {
        uint32_t start = esp_timer_get_time();
        auto result = engine.predict(test_case);
        uint32_t duration = esp_timer_get_time() - start;
        
        printf("Input: [");
        for (auto val : test_case) printf("%.2f ", val);
        printf("] | Inference: %d μs | Output: ", duration);
        for (auto out : result) printf("%.3f ", out);
        printf("\n");
    }
    
    // 3. Kiểm tra bộ nhớ
    printf("Free heap: %d bytes\n", esp_get_free_heap_size());
    printf("Min free heap: %d bytes\n", esp_get_minimum_free_heap_size());
}
