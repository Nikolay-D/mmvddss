# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getClassInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from qlua.rpc import qlua_structures_pb2 as qlua_dot_rpc_dot_qlua__structures__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='getClassInfo.proto',
  package='qlua.rpc.getClassInfo',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x12getClassInfo.proto\x12\x15qlua.rpc.getClassInfo\x1a\x1eqlua/rpc/qlua_structures.proto\"\x1d\n\x07Request\x12\x12\n\nclass_code\x18\x01 \x01(\t\"1\n\x06Result\x12\'\n\nclass_info\x18\x01 \x01(\x0b\x32\x13.qlua.structs.KlassB\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
  ,
  dependencies=[qlua_dot_rpc_dot_qlua__structures__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.getClassInfo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_code', full_name='qlua.rpc.getClassInfo.Request.class_code', index=0,
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
  serialized_start=77,
  serialized_end=106,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getClassInfo.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_info', full_name='qlua.rpc.getClassInfo.Result.class_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=108,
  serialized_end=157,
)

_RESULT.fields_by_name['class_info'].message_type = qlua_dot_rpc_dot_qlua__structures__pb2._KLASS
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'getClassInfo_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getClassInfo.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'getClassInfo_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getClassInfo.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
