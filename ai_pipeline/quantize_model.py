import tensorflow as tf
import tensorflow_model_optimization as tfmot

def create_quant_model(input_shape, num_classes):
    """Tạo model với quantization aware training"""
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_shape),
        tfmot.quantization.keras.quantize_annotate_layer(
            tf.keras.layers.Dense(32, activation='relu')
        ),
        tfmot.quantization.keras.quantize_annotate_layer(
            tf.keras.layers.Dense(24, activation='relu')
        ),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    return tfmot.quantization.keras.quantize_apply(model)

def convert_to_tflite(model, output_path):
    """Chuyển model sang định dạng TFLite"""
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    
    with open(output_path, 'wb') as f:
        f.write(tflite_model)
