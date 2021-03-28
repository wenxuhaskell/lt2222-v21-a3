import os

os.environ["CUDA_VISIBLE_DEVICES"]=""
os.environ["USE_CPU"]="1"

import sys
import argparse
import numpy as np
import pandas as pd
from model import train
from train import a
from train import b
from train import g
import torch

vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o']) 


def rfile(f):
    mm = []
    with open(f, "r") as q:
        for l in q:
            mm += [c for c in l]
    
    return mm


def wfile(f, m, p):
    with open(f, "w") as q:
        index = 0
        for l in m:
            if l in vowels:
                q.write(vowels[p[index]])
                index = index+1
            else:
                q.write(l) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # test data for evaluation
    parser.add_argument("t", type=str)
    # model file
    parser.add_argument("m", type=str)
    # output 
    parser.add_argument("o", type=str)
    
    args = parser.parse_args()

    q = a(args.t)
    w = b(q[0], q[1])

    
    # load the model
    model = torch.load(args.m)
    
    shape_of_first_layer = list(model.parameters())[0].shape #shape_of_first_layer

    _, in_features = shape_of_first_layer[:2]
    
    _, dimension_of_features = w[0].shape
    
    d = in_features - dimension_of_features
    
    # padding if test data's feature has different dimension than the model's input feature dimension
    if d > 0:
        f = np.pad(w[0], [(0,0), (0,d)], mode='constant')
    
    x_t= torch.Tensor(f)
    y_t = torch.LongTensor(w[1])
    
    # set to evaluation mode
    model.eval()

    # predicts using the model
    outputs = model(x_t.unsqueeze(0))
    predictions = pd.Series(outputs.squeeze(0).argmax(dim=1).numpy())
    
    # read out the test data
    data = rfile(args.t)
    # write back with prediction
    wfile(args.o, data, predictions.to_numpy())
    print("The predictions are written back to " + args.o)
    
    # accuracy
    test_y_df = pd.Series(y_t)
    accuracy = len(test_y_df[predictions==test_y_df])/len(test_y_df)
    print("Accuracy of prediction is: " + str(accuracy))


