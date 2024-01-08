import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt

def pred():
# Load the saved model
    cnn = load_model("object_detection.h5")

# Load image
    img = '/home/Alusya/Desktop/inzynierka/robot/zdj/new.jpg'
    test_img_main = image.load_img(img, target_size=(64, 64))
    test_img = image.img_to_array(test_img_main)
    test_img = np.expand_dims(test_img, axis=0)

# Make predictions
    result = cnn.predict(test_img)

    predicted_category = np.argmax(result)
    print(predicted_category)

    categories = ['bialy kolcek', 'czerowny kolcek', 'niebieski kolcek']
    predicted_label = categories[predicted_category]

    #plt.imshow(test_img_main)
    #plt.title(predicted_label)
    #plt.show()
    
    return predicted_category

    




