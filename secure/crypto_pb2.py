# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63rypto.proto\"\x19\n\x07Request\x12\x0e\n\x06number\x18\x01 \x01(\x03\"\x1a\n\x08Response\x12\x0e\n\x06number\x18\x01 \x01(\x03\x32-\n\x06\x43rypto\x12#\n\nGetPlusOne\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

_CRYPTO = DESCRIPTOR.services_by_name['Crypto']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=16
  _REQUEST._serialized_end=41
  _RESPONSE._serialized_start=43
  _RESPONSE._serialized_end=69
  _CRYPTO._serialized_start=71
  _CRYPTO._serialized_end=116
# @@protoc_insertion_point(module_scope)
