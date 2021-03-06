# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import routing_pb2 as routing__pb2


class TransportLayerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Send = channel.unary_unary(
        '/coop.rchain.comm.protocol.routing.TransportLayer/Send',
        request_serializer=routing__pb2.TLRequest.SerializeToString,
        response_deserializer=routing__pb2.TLResponse.FromString,
        )
    self.Stream = channel.stream_unary(
        '/coop.rchain.comm.protocol.routing.TransportLayer/Stream',
        request_serializer=routing__pb2.Chunk.SerializeToString,
        response_deserializer=routing__pb2.TLResponse.FromString,
        )


class TransportLayerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Send(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransportLayerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Send': grpc.unary_unary_rpc_method_handler(
          servicer.Send,
          request_deserializer=routing__pb2.TLRequest.FromString,
          response_serializer=routing__pb2.TLResponse.SerializeToString,
      ),
      'Stream': grpc.stream_unary_rpc_method_handler(
          servicer.Stream,
          request_deserializer=routing__pb2.Chunk.FromString,
          response_serializer=routing__pb2.TLResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'coop.rchain.comm.protocol.routing.TransportLayer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
