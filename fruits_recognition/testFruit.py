from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from Fruit import Fruit
from FruitRecognition import FruitRecognition

img_height=100
img_width=100
validation_data_dir = 'F:/fruits/fruits-360/Test'
batch_size = 3
img = load_img(validation_data_dir+'/Banana/103_100.jpg') # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)
recAlg = FruitRecognition()
# test_datagen = ImageDataGenerator(rescale=1. / 255)
# validation_generator = test_datagen.flow_from_directory(validation_data_dir, target_size = (img_height, img_width), batch_size = batch_size, class_mode = 'categorical')
# print(validation_generator[1])

print(recAlg.predict(x))
# print(max(recAlg.predict(validation_generator)[1]))