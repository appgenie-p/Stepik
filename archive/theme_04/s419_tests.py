from typing import TypeVar
from s419 import Dense, Input, Layer, NetworkIterator

LayerT = TypeVar("LayerT", bound="Layer")


def test_input() -> None:
    inputs = 10
    layer = Input(inputs)
    assert layer.inputs == inputs
    assert layer.name == "Input"
    assert repr(layer) == f"Input({inputs})"


def test_dense() -> None:
    inputs = 10
    outputs = 20
    activation = "relu"
    layer = Dense(inputs, outputs, activation)
    assert layer.inputs == inputs
    assert layer.outputs == outputs
    assert layer.activation == activation
    assert layer.name == "Dense"
    assert repr(layer) == f"Dense({inputs}, {outputs}, {activation})"


def test_network_iterator() -> None:
    inputs = 10
    outputs = 20
    activation = "relu"
    input_layer = Input(inputs)
    dense_layer = Dense(inputs, outputs, activation)
    input_layer.next_layer = dense_layer
    iterator = NetworkIterator(input_layer)
    layers = list(iterator)
    assert len(layers) == 2
    assert isinstance(layers[0], Input)
    assert isinstance(layers[1], Dense)
    assert layers[0].inputs == inputs
    assert layers[1].inputs == inputs
    assert layers[1].outputs == outputs
    assert layers[1].activation == activation
