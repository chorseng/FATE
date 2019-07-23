# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-binning-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-binning-meta.proto',
  package='com.webank.ai.fate.common.mlmodel.buffer',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x66\x65\x61ture-binning-meta.proto\x12(com.webank.ai.fate.common.mlmodel.buffer\"?\n\rTransformMeta\x12\x16\n\x0etransform_cols\x18\x01 \x03(\x03\x12\x16\n\x0etransform_type\x18\x02 \x01(\t\"\x90\x02\n\x12\x46\x65\x61tureBinningMeta\x12\x10\n\x08need_run\x18\x01 \x01(\x08\x12\x0e\n\x06method\x18\n \x01(\t\x12\x16\n\x0e\x63ompress_thres\x18\x02 \x01(\x03\x12\x11\n\thead_size\x18\x03 \x01(\x03\x12\r\n\x05\x65rror\x18\x04 \x01(\x01\x12\x0f\n\x07\x62in_num\x18\x05 \x01(\x03\x12\x0c\n\x04\x63ols\x18\x06 \x03(\t\x12\x19\n\x11\x61\x64justment_factor\x18\x07 \x01(\x01\x12\x12\n\nlocal_only\x18\x08 \x01(\x08\x12P\n\x0ftransform_param\x18\t \x01(\x0b\x32\x37.com.webank.ai.fate.common.mlmodel.buffer.TransformMetaB\x19\x42\x17\x46\x65\x61tureBinningMetaProtob\x06proto3')
)




_TRANSFORMMETA = _descriptor.Descriptor(
  name='TransformMeta',
  full_name='com.webank.ai.fate.common.mlmodel.buffer.TransformMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform_cols', full_name='com.webank.ai.fate.common.mlmodel.buffer.TransformMeta.transform_cols', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform_type', full_name='com.webank.ai.fate.common.mlmodel.buffer.TransformMeta.transform_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=135,
)


_FEATUREBINNINGMETA = _descriptor.Descriptor(
  name='FeatureBinningMeta',
  full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='need_run', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.need_run', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.method', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compress_thres', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.compress_thres', index=2,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_size', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.head_size', index=3,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.error', index=4,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bin_num', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.bin_num', index=5,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cols', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.cols', index=6,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adjustment_factor', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.adjustment_factor', index=7,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_only', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.local_only', index=8,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transform_param', full_name='com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta.transform_param', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=410,
)

_FEATUREBINNINGMETA.fields_by_name['transform_param'].message_type = _TRANSFORMMETA
DESCRIPTOR.message_types_by_name['TransformMeta'] = _TRANSFORMMETA
DESCRIPTOR.message_types_by_name['FeatureBinningMeta'] = _FEATUREBINNINGMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransformMeta = _reflection.GeneratedProtocolMessageType('TransformMeta', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORMMETA,
  __module__ = 'feature_binning_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.common.mlmodel.buffer.TransformMeta)
  ))
_sym_db.RegisterMessage(TransformMeta)

FeatureBinningMeta = _reflection.GeneratedProtocolMessageType('FeatureBinningMeta', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREBINNINGMETA,
  __module__ = 'feature_binning_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.common.mlmodel.buffer.FeatureBinningMeta)
  ))
_sym_db.RegisterMessage(FeatureBinningMeta)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\027FeatureBinningMetaProto'))
# @@protoc_insertion_point(module_scope)
