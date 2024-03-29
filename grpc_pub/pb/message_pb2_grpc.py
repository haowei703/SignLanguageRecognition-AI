# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_pub.pb.message_pb2 as message__pb2


class MessageExchangeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/messageexchange.MessageExchange/SendMessage',
                request_serializer=message__pb2.MessageRequest.SerializeToString,
                response_deserializer=message__pb2.MessageResponse.FromString,
                )


class MessageExchangeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageExchangeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=message__pb2.MessageRequest.FromString,
                    response_serializer=message__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'messageexchange.MessageExchange', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageExchange(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/messageexchange.MessageExchange/SendMessage',
            message__pb2.MessageRequest.SerializeToString,
            message__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
