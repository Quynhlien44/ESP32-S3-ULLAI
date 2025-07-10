import tensorflow as tf

def create_tf_dataset(features, labels, batch_size=128, shuffle_buffer=10000):
    """Tạo TensorFlow Dataset hiệu quả cho training"""
    dataset = tf.data.Dataset.from_tensor_slices((features, labels))
    
    return dataset \
        .cache() \
        .shuffle(shuffle_buffer) \
        .batch(batch_size) \
        .prefetch(tf.data.AUTOTUNE) \
        .map(normalize_features, num_parallel_calls=tf.data.AUTOTUNE)

def normalize_features(features, label):
    """Chuẩn hóa dữ liệu cảm biến"""
    # Implementation...
    return normalized_features, label
