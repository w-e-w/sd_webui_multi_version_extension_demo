from .v1 import V1
from .v2 import V2
from .v3 import V3
from .v1_m import V1M
from .v2_m import V2M
from .v3_m import V3M

single_modules = {
    'v1': V1,
    'v2': V2,
    'v3': V3,
    'None': None,
}

multi_modules = {
    'v1': V1M,
    'v2': V2M,
    'v3': V3M,
}
