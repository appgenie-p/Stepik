from typing import Iterator, TypeVar

LayerT = TypeVar("LayerT", bound="Layer")


class Layer:
    def __init__(self) -> None:
        self.next_layer = None
        self.name = "Layer"

    def __call__(self, next_layer: LayerT) -> LayerT:
        self.next_layer: LayerT | None = next_layer
        return next_layer


class Input(Layer):
    """Input layer"""

    InputNumber = int

    def __init__(self, inputs: InputNumber) -> None:
        self.inputs = inputs
        self.name = "Input"

    def __repr__(self) -> str:
        return f"{self.name}({self.inputs})"


class Dense(Layer):
    """Fully connected layer"""

    InputsInLayerNum = int
    OutputsLayerNum = int
    ActivationFunc = str

    def __init__(
        self,
        inputs: InputsInLayerNum,
        outputs: OutputsLayerNum,
        activation: ActivationFunc,
    ) -> None:
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = "Dense"

    def __repr__(self) -> str:
        return f"{self.name}({self.inputs}, {self.outputs}, {self.activation})"


class NetworkIterator:
    def __init__(self, network: Layer) -> None:
        self.network: Layer | None = network

    def __iter__(self) -> Iterator[Layer]:
        obj: Layer | None = self.network
        while obj is not None:
            yield obj
            try:
                obj = obj.next_layer
            except AttributeError:
                obj = None


nt = Input(12)
layer: Dense = nt(Dense(nt.inputs, 1024, "relu"))
layer = layer(Dense(layer.inputs, 2048, "relu"))
layer = layer(Dense(layer.inputs, 10, "softmax"))

n = 0
for x in NetworkIterator(network=nt):
    assert isinstance(
        x, Layer
    ), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"
