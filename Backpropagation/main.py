import random

from networkx import DiGraph


def createData():
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
        data.append((x, y))  # list of
        ans.append(label)  # list of nodes' weight
    return data, ans


def buildNetwork(numOfHiddenLayers: int) -> DiGraph:
    """
    Function build network i.e. DiGraph with nodes and edges.
    Each node contains: weight,bias,Layer.
    Each edge contains: weight, source node, destination node.
    :return: Network (i.e. directed graph with nodes and edges).
    """
    data, answers = createData()  # create new data
    network = DiGraph()  # Create new directed graph
    for layer in range(numOfHiddenLayers):  # input layer,hidden layer,output layer
        for i in range(len(data)):  # move over all data
            network.add_node(i, neuronWeight=answers[i], bias=random.uniform(0, 1), Layer=layer)  # add node (neuron) with this information
    network = addEdges(network)
    return network


def addEdges(network: DiGraph) -> DiGraph:
    """
    Function add edges to network
    :param network: given network
    :return: the updated network (with edges)
    """
    layer0 = [x for x, y in network.nodes(data=True) if y['layer'] == 0]
    layer1 = [x for x, y in network.nodes(data=True) if y['layer'] == 1]
    layer2 = [x for x, y in network.nodes(data=True) if y['layer'] == 2]
    layers = [layer0, layer1, layer2]
    layerTemp = []  # define temporary layer as an empty list
    for layer in layers:  # for all layers in network
        if len(layerTemp) == 0:  # if temporary layer is empty, we will save the previous layer
            layerTemp = layer
            continue  # and continue to next layer
        for nodeLowLayer in layerTemp:  # for all node in lower layer, we will connect an edge to each node in higher level
            for nodeHighLayer in layer:
                network.add_edge(nodeLowLayer, nodeHighLayer, weight=random.uniform(0, 1))
        layerTemp = []  # after we finished with both layers we will empty the temp, so we can determine the following layer as the lower layer in the next iteration
    return network


def train(network: DiGraph, numOfLayers: int):
    """
    Function get network and number of layers and train the net on data
    :param network: network already build ny using 'buildNetwork'
    :param numOfLayers:
    :return:
    """
    for layerIndex in range(numOfLayers):
        layer = [x for x, y in network.nodes(data=True) if y['layer'] == 1]
        for neuronIndex in range(len(layer)):
            currNeuron = layer[neuronIndex]
            newZ_i = 0
            for u, v, data in network.in_edges(neuronIndex, data=True):
                newZ_i += network.nodes[u]['weight'] * data['weight']
            # newZ_i += network.nodes[


def main():
    network = DiGraph()


if __name__ == '__main__':
    main()
