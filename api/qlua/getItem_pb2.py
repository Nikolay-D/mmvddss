# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getItem.proto',
  package='qlua.rpc.getItem',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\rgetItem.proto\x12\x10qlua.rpc.getItem\",\n\x07Request\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\"t\n\x06Result\x12\x39\n\ttable_row\x18\x01 \x03(\x0b\x32&.qlua.rpc.getItem.Result.TableRowEntry\x1a/\n\rTableRowEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.getItem.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='qlua.rpc.getItem.Request.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='qlua.rpc.getItem.Request.index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=35,
  serialized_end=79,
)


_RESULT_TABLEROWENTRY = _descriptor.Descriptor(
  name='TableRowEntry',
  full_name='qlua.rpc.getItem.Result.TableRowEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='qlua.rpc.getItem.Result.TableRowEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='qlua.rpc.getItem.Result.TableRowEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=197,
)

_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getItem.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_row', full_name='qlua.rpc.getItem.Result.table_row', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESULT_TABLEROWENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=197,
)

_RESULT_TABLEROWENTRY.containing_type = _RESULT
_RESULT.fields_by_name['table_row'].message_type = _RESULT_TABLEROWENTRY
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'getItem_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getItem.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(

  TableRowEntry = _reflection.GeneratedProtocolMessageType('TableRowEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESULT_TABLEROWENTRY,
    __module__ = 'getItem_pb2'
    # @@protoc_insertion_point(class_scope:qlua.rpc.getItem.Result.TableRowEntry)
    ))
  ,
  DESCRIPTOR = _RESULT,
  __module__ = 'getItem_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getItem.Result)
  ))
_sym_db.RegisterMessage(Result)
_sym_db.RegisterMessage(Result.TableRowEntry)


DESCRIPTOR._options = None
_RESULT_TABLEROWENTRY._options = None
# @@protoc_insertion_point(module_scope)
