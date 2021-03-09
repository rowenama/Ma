import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.utils.data as Data
import numpy as np


trainX = open("train_data.txt", 'r')
trainY = open("train_truth.txt", 'r')
testX = open("test_data.txt", 'r')
dataset_train = []
dataset_val = []

## file input
for i, line in enumerate(trainX):
    if i > 0:
        dataset_train.append([float(elt.strip()) for elt in line.split('\t')])

for i, line in enumerate(trainY):
    if i > 0:
        dataset_val.append(float(line.strip()))

print(dataset_train)

torch.manual_seed(1)    

x = torch.tensor(dataset_train)
y = torch.tensor(dataset_val)
#x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
#y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

# torch can only train on Variable, so convert them to Variable
x, y = Variable(x), Variable(y)

#define a network
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.hidden2 = torch.nn.Linear(n_hidden, n_hidden) 
        self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))      # activation function for hidden layer
        x = F.relu(self.hidden2(x)) 
        x = self.predict(x)             # linear output
        return x

net = Net(n_feature=3, n_hidden=10, n_output=1)     # define the network
# print(net)  # net architecture
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss


# train the network
print("Start training")

for t, data in enumerate(x):
  
    prediction = net(x)     # input x and predict based on x

    loss = loss_func(prediction, y)     

    optimizer.zero_grad()   # clear gradients for next train
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients
    
print("Finished training")


