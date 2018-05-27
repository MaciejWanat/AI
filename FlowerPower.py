import pickle
import cv2
import numpy as np
import mahotas

bins = 8
test_labels = {
    0 : 'Bluebell',
    1 : 'Daffodil',
    2 : 'Snowdrop'
}

# feature-descriptor-1: Hu Moments
def fd_hu_moments(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature

# feature-descriptor-2: Haralick Texture
def fd_haralick(image):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # compute the haralick texture feature vector
    haralick = mahotas.features.haralick(gray).mean(axis=0)
    # return the result
    return haralick

# feature-descriptor-3: Color Histogram
def fd_histogram(image, mask=None):
    # convert the image to HSV color-space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # compute the color histogram
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    # normalize the histogram
    cv2.normalize(hist, hist)
    # return the histogram
    return hist.flatten() 

class FlowerPower:
    def __init__(self):
        modelFile = open('./model/flowerModelRF.model', 'rb')
        self.clf = pickle.load(modelFile)
        modelFile.close()
    
    def predict(self, test):
        imageFile = './flowerTest/image_' + str(test.picNum) + '.jpg'

        fixed_size = tuple((500, 500))

        # read & resize the image
        image = cv2.imread(imageFile)
        image = cv2.resize(image, fixed_size)

        ####################################
        # Global Feature extraction
        ####################################
        fv_hu_moments = fd_hu_moments(image)
        fv_haralick   = fd_haralick(image)
        fv_histogram  = fd_histogram(image)

        ###################################
        # Concatenate global features
        ###################################
        global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments])

        # predict label of test image
        prediction = self.clf.predict(global_feature.reshape(1,-1))[0]

        return test_labels[prediction]

    def getName(self,test):
        return str(self.predict(test))

    def isProtected(self,test):
        flowerName = self.getName(test)

        if (flowerName == 'Snowdrop'):
            return 1
        else:
            return 0
          