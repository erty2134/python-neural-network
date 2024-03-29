import math

__author__ = "erty"
__name__ = "neural network"
__file__ = "main.py"

def sigmoid(x:"float") -> float:
    """
    makes any number a sigma
    """
    return 1 / (1 + math.exp(-x))

class layer:
    def __init__(self, nodes: "int", input=False, output=False) -> None:
        """
        set input to true if input layer,   
        set output to true if output layer
        else hidden layer.
        set nodes to how many nodes you want in the layer
        """
        self.layer = []
        self.weights = []
        for i in range(nodes):
            self.layer.append(0)
            self.weights.append(1)

    def calculateNodeOutput(inputs:"int", inputnodes:"list", weightsfornodes:"list", bias:"float", activation:"str") -> float:
        """
            inputs is how many input nodes you are feeding in
        """
        output = 0
        for i in range(inputs):
            output += (inputnodes[0] + weightsfornodes[0])
        output += bias
        if activation == "sigmoid" : return sigmoid(output)
        else: return sigmoid(output)

inputLayer = layer(2, input=True)
hiddenLayer = layer(3)
outputlayer = layer(2, output=True)

inputLayer.layer[0] = float(input("enter a number for input layer: "))
inputLayer.layer[1] = float(input("enter another number for input layer: "))

# HIDDEN LAYER
hiddenLayer.layer[0] = layer.calculateNodeOutput(
    2,
    inputLayer.layer,
    inputLayer.weights,
    0,
    "sigmoid"
)
hiddenLayer.layer[1] = layer.calculateNodeOutput(
    2,
    inputLayer.layer,
    inputLayer.weights,
    0,
    "sigmoid"
)
hiddenLayer.layer[2] = layer.calculateNodeOutput(
    2,
    inputLayer.layer,
    inputLayer.weights,
    0,
    "sigmoid"
)


# OUTPUT LAYER
outputlayer.layer[0] = layer.calculateNodeOutput(
    3,
    hiddenLayer.layer,
    hiddenLayer.weights,
    0,
    "sigmoid"
)
outputlayer.layer[1] = layer.calculateNodeOutput(
    3,
    hiddenLayer.layer,
    hiddenLayer.weights,
    0,
    "sigmoid"
)


print(outputlayer.layer)
