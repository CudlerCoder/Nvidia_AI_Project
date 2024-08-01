# AI Age detector Project
# ./my-recognition.py --network=resnet-18 my_image.jpg <-- this command to give the code a picture to identify
# Jetson Models that allow the program to recognmize and load images
import jetson_inference
import jetson_utils
#argparse: makes parsing command line interfaces easier
import argparse

 # parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
args = parser.parse_args()

#loads the image
img = jetson_utils.loadImage(args.filename)

# load the recognition network
net = jetson_inference.imageNet(model="resnet18.onnx", labels="labels.txt", input_blob="input_0", output_blob="output_0")

# classify the image (Returns a tuple: Image Index(what it thinks the object is) along with confidence)
class_idx, confidence = net.Classify(img)

#Finds the Description of the Detected index in this case its age
class_desc = net.GetClassDesc(class_idx)

print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))

