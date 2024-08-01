# AGE DETECTOR


The Project uses the Jetson Nano and machine learning to give an age prediction of an individual in a given image and outputs the age range it thinks the person is most likely a part of:
 10-12, 12-15, 15-17, 18-19 , 20-25 ,25-35, 42-60, 60+

![add image descrition here](direct image link here)

## The Algorithm

# libraries:
jetson_inference: Provides tools for loading and running inference with neural networks.

jetson_utils: Provides utilities for loading and manipulating images.

argparse: A standard library for parsing command-line arguments.


The script is for image recognition on a Jetson Nano device. It parses command line arguments to get the image filename and neural network model, loads the image, and uses a specified neural network model to detect the classification of a provided image. The script then prints the recognized class and confidence level of the classification.



## Running this project

1. Add the image to the directory of the Program and the Resnet.18 model that is trained to detect the age of different people
2. the code uses the Jetson Inference, and Jetson Utils libraries along with the argparse library.
3. in the terminal execute the code using the test image by using the command python3 (filename) (imagename) in the directory with the program

Here is a demonstration!
https://youtu.be/eiOLTYf7Kas (video link) 
