# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getTradeDate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getTradeDate.proto',
  package='qlua.rpc.getTradeDate',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x12getTradeDate.proto\x12\x15qlua.rpc.getTradeDate\"C\n\tTradeDate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04year\x18\x02 \x01(\r\x12\r\n\x05month\x18\x03 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\r\">\n\x06Result\x12\x34\n\ntrade_date\x18\x01 \x01(\x0b\x32 .qlua.rpc.getTradeDate.TradeDateB\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_TRADEDATE = _descriptor.Descriptor(
  name='TradeDate',
  full_name='qlua.rpc.getTradeDate.TradeDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='qlua.rpc.getTradeDate.TradeDate.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='qlua.rpc.getTradeDate.TradeDate.year', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='qlua.rpc.getTradeDate.TradeDate.month', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='qlua.rpc.getTradeDate.TradeDate.day', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=45,
  serialized_end=112,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getTradeDate.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trade_date', full_name='qlua.rpc.getTradeDate.Result.trade_date', index=0,
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
  serialized_start=114,
  serialized_end=176,
)

_RESULT.fields_by_name['trade_date'].message_type = _TRADEDATE
DESCRIPTOR.message_types_by_name['TradeDate'] = _TRADEDATE
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradeDate = _reflection.GeneratedProtocolMessageType('TradeDate', (_message.Message,), dict(
  DESCRIPTOR = _TRADEDATE,
  __module__ = 'getTradeDate_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getTradeDate.TradeDate)
  ))
_sym_db.RegisterMessage(TradeDate)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'getTradeDate_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getTradeDate.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
