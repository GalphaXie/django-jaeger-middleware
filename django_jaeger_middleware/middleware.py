from django.http import HttpRequest
from opentracing import Format
from opentracing.ext import tags

from . import tracer, OPERATION_NAME, TRACE_ID_HEADER


class JaegerMiddleWare(object):
    """
        Simple jaeger middleware to trace the distributing system.
        depend on jaeger-client-python, opentracing-python packages, etc.

        PRDs :
        https://github.com/opentracing/opentracing-python
        https://github.com/jaegertracing/jaeger-client-python
        """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.extract_request_ctx(request)
        response = self.get_response(request)
        response[TRACE_ID_HEADER] = request.META.get(TRACE_ID_HEADER, "")
        return response

    def inject_span(self, span, request: HttpRequest):
        span.set_tag(tags.HTTP_METHOD, request.method)
        span.set_tag(tags.HTTP_URL, request.path)
        span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
        tracer.inject(span, Format.HTTP_HEADERS, request.META)

    def extract_request_ctx(self, request: HttpRequest):
        span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
        span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
        with tracer.start_span(operation_name=OPERATION_NAME, child_of=span_ctx, tags=span_tags) as gate_span:
            self.inject_span(gate_span, request)

    def process_request(self, request):
        pass
