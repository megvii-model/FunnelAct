import sys
sys.path.insert(0, "resnet")
sys.path.insert(0, "shufflenetv2")

from resnet.resnet import (
    BasicBlock,
    Bottleneck,
    Bottleneck_FReLU,
    ResNet,
    resnet50_frelu,
)

from shufflenetv2.shufflenet_v2 import (
    shufflenet_v2_x0_5,
)
