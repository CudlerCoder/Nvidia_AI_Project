#!/usr/bin/python3

import jetson_inference
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type = str, help = "filename of the image process")
parser.add_argument("--network", type = str, default = "googlenet", help = "model to use where google net is default")

img = jetson_utils.loadimage(opt.filename)

jetson_inference.imageNot(opt.filename)

class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idk)

print( str(class_idx) + " " + str(class_desk) + " " + " Recognized with " + str(confidence * 100) + "%" + "confidence")