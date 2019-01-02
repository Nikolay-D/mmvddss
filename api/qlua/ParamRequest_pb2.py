# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ParamRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ParamRequest.proto',
  package='qlua.rpc.ParamRequest',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x12ParamRequest.proto\x12\x15qlua.rpc.ParamRequest\"@\n\x07Request\x12\x12\n\nclass_code\x18\x01 \x01(\t\x12\x10\n\x08sec_code\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x62_name\x18\x03 \x01(\t\"\x18\n\x06Result\x12\x0e\n\x06result\x18\x01 \x01(\x08\x42\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.ParamRequest.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_code', full_name='qlua.rpc.ParamRequest.Request.class_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec_code', full_name='qlua.rpc.ParamRequest.Request.sec_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='db_name', full_name='qlua.rpc.ParamRequest.Request.db_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=109,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.ParamRequest.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='qlua.rpc.ParamRequest.Result.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=111,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'ParamRequest_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.ParamRequest.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'ParamRequest_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.ParamRequest.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
