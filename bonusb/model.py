import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import random

class VowelModel(nn.Module):
    def __init__(self, featuresize, hiddensize, outputsize, nlayers, vocab):
        super().__init__()

        # Defining some parameters
        self.hiddensize = hiddensize
        self.nlayers = nlayers

        #Defining the layers
        # RNN Layer
        self.rnn = nn.RNN(featuresize, hiddensize, nlayers, batch_first=True)   
        # Fully connected layer
        self.fc = nn.Linear(hiddensize, outputsize)
#        self.softmax = nn.LogSoftmax(dim=1)

        self.vocab = vocab

    def forward(self, x):
        batchsize = x.size(0)

        # Initializing hidden state for first input using method defined below
        hidden = self.init_hidden(batchsize)
        # Passing in the input and hidden state into the model and obtaining outputs
        out, hidden = self.rnn(x, hidden)
        # Reshaping the outputs such that it can be fit into the fully connected layer
        out = out.contiguous().view(-1, self.hiddensize)
        out = self.fc(out)
#        out = self.softmax(out)
        return out, hidden

    def init_hidden(self, batchsize):
        # This method generates the first hidden state of zeros which we'll use in the forward pass
        # We'll send the tensor holding the hidden state to the device we specified earlier as well
        hidden = torch.zeros(self.nlayers, batchsize, self.hiddensize)
        return hidden

def __shuffler__(X, y):
#    dx = pd.DataFrame(X)
#   dy = pdf.DataFrame
#    df['class'] = y
    indices = list(range(X.shape[0]))
    total_len = int(len(indices))
    h = int(total_len/10)
    while True:
        s = random.randint(0,total_len - h - 1)
#       rearrangedf = df.iloc[indices[s : (s+h)]]
#       featuredf = rearrangedf.drop('class', axis=1)
#       classdf = rearrangedf['class']
        featuredf = X[s:(s+h)]
        classdf = y[s:(s+h)]
        yield torch.Tensor(featuredf), torch.LongTensor(classdf)
        

def train(X, y, vocab, hiddensize, epochs=50):
    inputsize = X.shape[1]
    #outputsize = int(y.max()) + 1
    outputsize = len(vocab)
    # RNN with 1 fully connected layer
    model = VowelModel(inputsize, hiddensize, outputsize, 1, vocab)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    shuffler = __shuffler__(X, y)

    for epoch in range(epochs):
        Xt, yt = next(shuffler)
        
        optimizer.zero_grad()
        outputs, hidden = model(Xt.unsqueeze(0))

        print(outputs.squeeze(0).shape)
        print(yt.shape)
        
        loss = criterion(outputs.squeeze(0), yt)
#        loss.requires_grad = True
        loss.backward()
        optimizer.step()

        print("In epoch {}, the loss was {}.".format(epoch, loss))

    return model

 

