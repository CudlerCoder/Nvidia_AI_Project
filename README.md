# AGE DETECTOR


The Project uses the Jetson Nano and machine learning to give an age prediction of an individual in a given image and outputs the age range it thinks the person is most likely a part of:
 10-12, 12-15, 15-17, 18-19, 20-25,25-35, 42-60, 60+

In a year there is an average of 4000 deaths caused by minors drinking alcohol! When it comes to judging age based an appearance its difficult for humans to do that at a glance, my goal with this project was to lay the frame work for possibly solving this problem with Artificial intelligence


![image](https://github.com/user-attachments/assets/311af3da-f469-4912-a54a-d612cb5c360d)

![image](https://github.com/user-attachments/assets/64970891-cdf7-4e61-ba79-a15d1c41bc2b)




## The Algorithm

### libraries:
jetson_inference: Provides tools for loading and running inference with neural networks.

jetson_utils: Provides utilities for loading and manipulating images.

argparse: A standard library for parsing command-line arguments.


The script is for image recognition on a Jetson Nano device. It parses command line arguments to get the image filename and network, loads the image, and uses a neural network model to detect the classification of a provided image. The script then prints the recognized class and confidence level of the classification.



## Running this project

1. Add the image to the directory of the Program and the Resnet.18 model that is trained to detect the age of different people
2. the code uses the Jetson Inference, and Jetson Utils libraries along with the argparse library.
3. in the terminal execute the code using the test image by using the command python3 (filename) (imagename) in the directory with the program

Here is a demonstration!
https://youtu.be/eiOLTYf7Kas (video link) 
