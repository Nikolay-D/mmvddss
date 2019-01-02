# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getBuySellInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='getBuySellInfo.proto',
  package='qlua.rpc.getBuySellInfo',
  syntax='proto3',
  serialized_options=_b('\n\010qlua.rpcH\001'),
  serialized_pb=_b('\n\x14getBuySellInfo.proto\x12\x17qlua.rpc.getBuySellInfo\"\xb7\x03\n\x0b\x42uySellInfo\x12\x15\n\ris_margin_sec\x18\x01 \x01(\t\x12\x14\n\x0cis_asset_sec\x18\x02 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61n_buy\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61n_sell\x18\x05 \x01(\t\x12\x1a\n\x12position_valuation\x18\x06 \x01(\t\x12\r\n\x05value\x18\x07 \x01(\t\x12\x12\n\nopen_value\x18\x08 \x01(\t\x12\x10\n\x08lim_long\x18\t \x01(\t\x12\x11\n\tlong_coef\x18\n \x01(\t\x12\x11\n\tlim_short\x18\x0b \x01(\t\x12\x12\n\nshort_coef\x18\x0c \x01(\t\x12\x12\n\nvalue_coef\x18\r \x01(\t\x12\x17\n\x0fopen_value_coef\x18\x0e \x01(\t\x12\r\n\x05share\x18\x0f \x01(\t\x12\x16\n\x0eshort_wa_price\x18\x10 \x01(\t\x12\x15\n\rlong_wa_price\x18\x11 \x01(\t\x12\x13\n\x0bprofit_loss\x18\x12 \x01(\t\x12\x11\n\tspread_hc\x18\x13 \x01(\t\x12\x13\n\x0b\x63\x61n_buy_own\x18\x14 \x01(\t\x12\x14\n\x0c\x63\x61n_sell_own\x18\x15 \x01(\t\"d\n\x07Request\x12\x0f\n\x07\x66irm_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63lient_code\x18\x02 \x01(\t\x12\x12\n\nclass_code\x18\x03 \x01(\t\x12\x10\n\x08sec_code\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\t\"E\n\x06Result\x12;\n\rbuy_sell_info\x18\x01 \x01(\x0b\x32$.qlua.rpc.getBuySellInfo.BuySellInfoB\x0c\n\x08qlua.rpcH\x01\x62\x06proto3')
)




_BUYSELLINFO = _descriptor.Descriptor(
  name='BuySellInfo',
  full_name='qlua.rpc.getBuySellInfo.BuySellInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_margin_sec', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.is_margin_sec', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_asset_sec', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.is_asset_sec', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balance', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.balance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_buy', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.can_buy', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_sell', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.can_sell', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_valuation', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.position_valuation', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open_value', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.open_value', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lim_long', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.lim_long', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_coef', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.long_coef', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lim_short', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.lim_short', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_coef', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.short_coef', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_coef', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.value_coef', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open_value_coef', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.open_value_coef', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='share', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.share', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_wa_price', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.short_wa_price', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_wa_price', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.long_wa_price', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profit_loss', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.profit_loss', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spread_hc', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.spread_hc', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_buy_own', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.can_buy_own', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_sell_own', full_name='qlua.rpc.getBuySellInfo.BuySellInfo.can_sell_own', index=20,
      number=21, type=9, cpp_type=9, label=1,
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
  serialized_start=50,
  serialized_end=489,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='qlua.rpc.getBuySellInfo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firm_id', full_name='qlua.rpc.getBuySellInfo.Request.firm_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_code', full_name='qlua.rpc.getBuySellInfo.Request.client_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_code', full_name='qlua.rpc.getBuySellInfo.Request.class_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sec_code', full_name='qlua.rpc.getBuySellInfo.Request.sec_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='qlua.rpc.getBuySellInfo.Request.price', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=491,
  serialized_end=591,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='qlua.rpc.getBuySellInfo.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buy_sell_info', full_name='qlua.rpc.getBuySellInfo.Result.buy_sell_info', index=0,
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
  serialized_start=593,
  serialized_end=662,
)

_RESULT.fields_by_name['buy_sell_info'].message_type = _BUYSELLINFO
DESCRIPTOR.message_types_by_name['BuySellInfo'] = _BUYSELLINFO
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuySellInfo = _reflection.GeneratedProtocolMessageType('BuySellInfo', (_message.Message,), dict(
  DESCRIPTOR = _BUYSELLINFO,
  __module__ = 'getBuySellInfo_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getBuySellInfo.BuySellInfo)
  ))
_sym_db.RegisterMessage(BuySellInfo)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'getBuySellInfo_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getBuySellInfo.Request)
  ))
_sym_db.RegisterMessage(Request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'getBuySellInfo_pb2'
  # @@protoc_insertion_point(class_scope:qlua.rpc.getBuySellInfo.Result)
  ))
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)