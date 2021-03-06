# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getClassSecurities.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getClassSecurities.proto',
  package='qlua.rpc.getClassSecurities',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x18getClassSecurities.proto\x12\x1bqlua.rpc.getClassSecurities\"\x1d\n\x07Request\x12\x12\n\nclass_code\x18\x01 \x01(\t\"\"\n\x06Result\x12\x18\n\x10\x63lass_securities\x18\x01 \x01(\tB\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.getClassSecurities.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_code', full_name='qlua.rpc.getClassSecurities.Request.class_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=57,
  serialized_end=86,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getClassSecurities.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_securities', full_name='qlua.rpc.getClassSecurities.Result.class_securities', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=88,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'getClassSecurities_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getClassSecurities.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'getClassSecurities_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getClassSecurities.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
