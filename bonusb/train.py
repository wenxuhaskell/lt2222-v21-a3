import os

os.environ["CUDA_VISIBLE_DEVICES"]=""
os.environ["USE_CPU"]="1"

import sys
import argparse
import numpy as np
import pandas as pd
from model import train
import torch

vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])

def a(f):
    mm = []
    with open(f, "r") as q:
        for l in q:
            mm += [c for c in l]

    mm = ["<s>", "<s>", "<s>", "<s>"] + mm + ["<e>", "<e>", "<e>", "<e>"]
    return mm, list(set(mm))

def g(x, p):
    z = np.zeros(len(p))
    z[p.index(x)] = 1
    return z

def b(u, p):
    gt = []
    gr = []
    for v in range(len(u) - 8):
        if u[v+4] not in vowels:
            continue
        
        h2 = vowels.index(u[v+4])
        r = np.concatenate([g(x, p) for x in [u[v], u[v+1], u[v+2], u[v+3]]])
        
        gr.append(r)
        
        t = np.concatenate([g(x, p) for x in [u[v+1], u[v+2], u[v+3], u[v+4]]])
        gt.append(t)
        
    return np.array(gr), np.array(gt)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", dest="k", type=int, default=100)
    parser.add_argument("--r", dest="r", type=int, default=50)
    parser.add_argument("m", type=str)
    parser.add_argument("h", type=str)
    
    args = parser.parse_args()

    q = a(args.m)
    w = b(q[0], q[1])
    print(w[0].shape)
    print(w[1].shape)
    t = train(w[0], w[1], q[1], args.k, args.r)

    torch.save(t, args.h)
