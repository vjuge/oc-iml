import tensorflow as tf
import gradio as gr
import pickle
import numpy as np

IMG_SIZE = 299
NO_BREEDS = 120

model = tf.keras.models.load_model('xception_trained_model.h5')

with open('./ds_info_features.pkl', 'rb') as f:
    ds_info_features = pickle.load(f)

def predict(image):
    image = tf.expand_dims(image, axis=0)
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    # image = keras.preprocessing.image.img_to_array(image)

    # Apply preprocess Xception
    # img_array = img_array.reshape((-1, 299, 299, 3))
    image = tf.keras.applications.xception.preprocess_input(image)

    # # Predictions
    prediction = model.predict(image).flatten()
    # print(prediction)
    return {ds_info_features[i]: float(prediction[i]) for i in range(NO_BREEDS)}


if __name__ == "__main__":
    gr.Interface(
        fn=predict,
        inputs=gr.inputs.Image(shape=(IMG_SIZE, IMG_SIZE)),
        outputs=gr.outputs.Label(num_top_classes=3),
        capture_session=True
    ).launch(share=True)
