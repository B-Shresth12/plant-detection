# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plantdisease.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'plantdisease.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12plantdisease.proto\x12\x0cplantdisease\".\n\x0f\x43lassifyRequest\x12\x0c\n\x04\x63rop\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"#\n\x10\x43lassifyResponse\x12\x0f\n\x07\x64isease\x18\x01 \x01(\t2e\n\x11\x44iseaseClassifier\x12P\n\x0f\x43lassifyDisease\x12\x1d.plantdisease.ClassifyRequest\x1a\x1e.plantdisease.ClassifyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plantdisease_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLASSIFYREQUEST']._serialized_start=36
  _globals['_CLASSIFYREQUEST']._serialized_end=82
  _globals['_CLASSIFYRESPONSE']._serialized_start=84
  _globals['_CLASSIFYRESPONSE']._serialized_end=119
  _globals['_DISEASECLASSIFIER']._serialized_start=121
  _globals['_DISEASECLASSIFIER']._serialized_end=222
# @@protoc_insertion_point(module_scope)
