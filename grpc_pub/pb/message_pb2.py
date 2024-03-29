# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='messageexchange',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x0fmessageexchange\"E\n\x0eMessageRequest\x12\x14\n\x0c\x62inary_image\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\"2\n\x0fMessageResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0f\n\x07isEmpty\x18\x02 \x01(\x08\x32\x65\n\x0fMessageExchange\x12R\n\x0bSendMessage\x12\x1f.messageexchange.MessageRequest\x1a .messageexchange.MessageResponse\"\x00\x62\x06proto3'
)




_MESSAGEREQUEST = _descriptor.Descriptor(
  name='MessageRequest',
  full_name='messageexchange.MessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary_image', full_name='messageexchange.MessageRequest.binary_image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='messageexchange.MessageRequest.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='messageexchange.MessageRequest.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=103,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='messageexchange.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='messageexchange.MessageResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isEmpty', full_name='messageexchange.MessageResponse.isEmpty', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['MessageRequest'] = _MESSAGEREQUEST
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageRequest = _reflection.GeneratedProtocolMessageType('MessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:messageexchange.MessageRequest)
  })
_sym_db.RegisterMessage(MessageRequest)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:messageexchange.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)



_MESSAGEEXCHANGE = _descriptor.ServiceDescriptor(
  name='MessageExchange',
  full_name='messageexchange.MessageExchange',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=157,
  serialized_end=258,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='messageexchange.MessageExchange.SendMessage',
    index=0,
    containing_service=None,
    input_type=_MESSAGEREQUEST,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGEEXCHANGE)

DESCRIPTOR.services_by_name['MessageExchange'] = _MESSAGEEXCHANGE

# @@protoc_insertion_point(module_scope)
