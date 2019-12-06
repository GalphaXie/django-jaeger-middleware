
import os

from jaeger_client.config import Config
from jaeger_client.constants import TRACE_ID_HEADER as DEFAULT_TRACE_ID_HEADER

# global jaeger config
JAEGER_SERVICE_NAME = os.getenv('JAEGER_SERVICE_NAME', "default_jaeger_service_name")
TRACE_ID_HEADER = os.getenv('TRACE_ID_HEADER', DEFAULT_TRACE_ID_HEADER)
OPERATION_NAME = os.getenv('OPERATION_NAME', "default_operation_name")

config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name=JAEGER_SERVICE_NAME,
)
# global tracer
tracer = config.initialize_tracer()


__all__ = [
    "tracer"
]
