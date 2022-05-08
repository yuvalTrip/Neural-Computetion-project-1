import random

from networkx import DiGraph


def addData(network: DiGraph):
    data = []
    ans = []
    amountOfData = 1000
    for i in range(amountOfData):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        if y > 1:
            label = 1
        else:
            label = -1
        data.append((x, y))
        ans.append(label)
    return data, label

def buildNetwork(data, answers):
    G = DiGraph() #Create new directed graph
    for layer in range(3):#input layer,hidden layer,output layer
        for i in range(len(data)): #move over all data
            G.add_node(i, neuronWeight = answers[i], bias = random.uniform(0,1),Layer=layer) #add node (neuron) with this information


def train(network: DiGraph, numOfLayers: int):
    """
    Function get network and number of layers and train the net on data
    :param network: network already build ny using 'buildNetwork'
    :param numOfLayers:
    :return:
    """
    for layerIndex in range(numOfLayers):
        layer = [x for x, y in network.nodes(data=True) if y['layer'] == 0]
        for neuronIndex in range(len(layer)):
            currNeuron = layer[neuronIndex]






def main():
    network = DiGraph()


if __name__ == '__main__':
    main()
