# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ie_serving/messaging/endpoint_responses.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ie_serving.messaging import data_attributes_pb2 as ie__serving_dot_messaging_dot_data__attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ie_serving/messaging/endpoint_responses.proto',
  package='ovms_ipc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n-ie_serving/messaging/endpoint_responses.proto\x12\x08ovms_ipc\x1a*ie_serving/messaging/data_attributes.proto\"\x88\x02\n\x10\x45ndpointResponse\x12\x35\n\x10predict_response\x18\x01 \x01(\x0b\x32\x19.ovms_ipc.PredictResponseH\x00\x12\x42\n\x17model_metadata_response\x18\x02 \x01(\x0b\x32\x1f.ovms_ipc.ModelMetadataResponseH\x00\x12>\n\x15model_status_response\x18\x03 \x01(\x0b\x32\x1d.ovms_ipc.ModelStatusResponseH\x00\x12\x31\n\x0e\x65rror_response\x18\x04 \x01(\x0b\x32\x17.ovms_ipc.ErrorResponseH\x00\x42\x06\n\x04type\"\xbf\x02\n\x0fPredictResponse\x12/\n\x07outputs\x18\x01 \x03(\x0b\x32\x1e.ovms_ipc.PredictResponse.Data\x12\x1a\n\x12responding_version\x18\x02 \x01(\x05\x1a\xde\x01\n\x04\x44\x61ta\x12\x35\n\x10numpy_attributes\x18\x01 \x01(\x0b\x32\x19.ovms_ipc.NumpyAttributesH\x00\x12\x37\n\x11string_attributes\x18\x02 \x01(\x0b\x32\x1a.ovms_ipc.StringAttributesH\x00\x12\x37\n\x11\x62inary_attributes\x18\x03 \x01(\x0b\x32\x1a.ovms_ipc.BinaryAttributesH\x00\x12\x13\n\x0boutput_name\x18\x04 \x01(\t\x12\x10\n\x08shm_name\x18\x05 \x01(\tB\x06\n\x04type\"\xc7\x02\n\x15ModelMetadataResponse\x12\x43\n\x10inputs_signature\x18\x01 \x03(\x0b\x32).ovms_ipc.ModelMetadataResponse.Signature\x12\x44\n\x11outputs_signature\x18\x02 \x03(\x0b\x32).ovms_ipc.ModelMetadataResponse.Signature\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x1a=\n\x05Layer\x12\x12\n\nlayer_name\x18\x01 \x01(\t\x12\x11\n\tprecision\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x03(\x05\x1aO\n\tSignature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x05layer\x18\x02 \x01(\x0b\x32%.ovms_ipc.ModelMetadataResponse.Layer\"\x91\x03\n\x13ModelStatusResponse\x1a\x85\x01\n\x06Status\x12\x42\n\nerror_code\x18\x01 \x01(\x0e\x32..ovms_ipc.ModelStatusResponse.Status.ErrorCode\x12\x15\n\rerror_message\x18\x02 \x01(\t\" \n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x1a\xa9\x01\n\x12ModelVersionStatus\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rmodel_version\x18\x02 \x01(\x05\x12\x32\n\x05state\x18\x03 \x01(\x0e\x32#.ovms_ipc.ModelStatusResponse.State\x12\x34\n\x06status\x18\x04 \x01(\x0b\x32$.ovms_ipc.ModelStatusResponse.Status\"F\n\x05State\x12\t\n\x05START\x10\x00\x12\x0b\n\x07LOADING\x10\x01\x12\r\n\tAVAILABLE\x10\x02\x12\r\n\tUNLOADING\x10\x03\x12\x07\n\x03\x45ND\x10\x04\":\n\rErrorResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\tb\x06proto3'
  ,
  dependencies=[ie__serving_dot_messaging_dot_data__attributes__pb2.DESCRIPTOR,])



_MODELSTATUSRESPONSE_STATUS_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='ovms_ipc.ModelStatusResponse.Status.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1148,
  serialized_end=1180,
)
_sym_db.RegisterEnumDescriptor(_MODELSTATUSRESPONSE_STATUS_ERRORCODE)

_MODELSTATUSRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='ovms_ipc.ModelStatusResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOADING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOADING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1354,
  serialized_end=1424,
)
_sym_db.RegisterEnumDescriptor(_MODELSTATUSRESPONSE_STATE)


_ENDPOINTRESPONSE = _descriptor.Descriptor(
  name='EndpointResponse',
  full_name='ovms_ipc.EndpointResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predict_response', full_name='ovms_ipc.EndpointResponse.predict_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_metadata_response', full_name='ovms_ipc.EndpointResponse.model_metadata_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_status_response', full_name='ovms_ipc.EndpointResponse.model_status_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_response', full_name='ovms_ipc.EndpointResponse.error_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='ovms_ipc.EndpointResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=104,
  serialized_end=368,
)


_PREDICTRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='ovms_ipc.PredictResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numpy_attributes', full_name='ovms_ipc.PredictResponse.Data.numpy_attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_attributes', full_name='ovms_ipc.PredictResponse.Data.string_attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_attributes', full_name='ovms_ipc.PredictResponse.Data.binary_attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_name', full_name='ovms_ipc.PredictResponse.Data.output_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shm_name', full_name='ovms_ipc.PredictResponse.Data.shm_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='type', full_name='ovms_ipc.PredictResponse.Data.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=468,
  serialized_end=690,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='ovms_ipc.PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='ovms_ipc.PredictResponse.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responding_version', full_name='ovms_ipc.PredictResponse.responding_version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=690,
)


_MODELMETADATARESPONSE_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='ovms_ipc.ModelMetadataResponse.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layer_name', full_name='ovms_ipc.ModelMetadataResponse.Layer.layer_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precision', full_name='ovms_ipc.ModelMetadataResponse.Layer.precision', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='ovms_ipc.ModelMetadataResponse.Layer.shape', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=878,
  serialized_end=939,
)

_MODELMETADATARESPONSE_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='ovms_ipc.ModelMetadataResponse.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ovms_ipc.ModelMetadataResponse.Signature.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layer', full_name='ovms_ipc.ModelMetadataResponse.Signature.layer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=941,
  serialized_end=1020,
)

_MODELMETADATARESPONSE = _descriptor.Descriptor(
  name='ModelMetadataResponse',
  full_name='ovms_ipc.ModelMetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs_signature', full_name='ovms_ipc.ModelMetadataResponse.inputs_signature', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs_signature', full_name='ovms_ipc.ModelMetadataResponse.outputs_signature', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='ovms_ipc.ModelMetadataResponse.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MODELMETADATARESPONSE_LAYER, _MODELMETADATARESPONSE_SIGNATURE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=1020,
)


_MODELSTATUSRESPONSE_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='ovms_ipc.ModelStatusResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='ovms_ipc.ModelStatusResponse.Status.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='ovms_ipc.ModelStatusResponse.Status.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODELSTATUSRESPONSE_STATUS_ERRORCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1047,
  serialized_end=1180,
)

_MODELSTATUSRESPONSE_MODELVERSIONSTATUS = _descriptor.Descriptor(
  name='ModelVersionStatus',
  full_name='ovms_ipc.ModelStatusResponse.ModelVersionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='ovms_ipc.ModelStatusResponse.ModelVersionStatus.model_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='ovms_ipc.ModelStatusResponse.ModelVersionStatus.model_version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='ovms_ipc.ModelStatusResponse.ModelVersionStatus.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ovms_ipc.ModelStatusResponse.ModelVersionStatus.status', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1183,
  serialized_end=1352,
)

_MODELSTATUSRESPONSE = _descriptor.Descriptor(
  name='ModelStatusResponse',
  full_name='ovms_ipc.ModelStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_MODELSTATUSRESPONSE_STATUS, _MODELSTATUSRESPONSE_MODELVERSIONSTATUS, ],
  enum_types=[
    _MODELSTATUSRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1023,
  serialized_end=1424,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='ovms_ipc.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='ovms_ipc.ErrorResponse.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='ovms_ipc.ErrorResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1426,
  serialized_end=1484,
)

_ENDPOINTRESPONSE.fields_by_name['predict_response'].message_type = _PREDICTRESPONSE
_ENDPOINTRESPONSE.fields_by_name['model_metadata_response'].message_type = _MODELMETADATARESPONSE
_ENDPOINTRESPONSE.fields_by_name['model_status_response'].message_type = _MODELSTATUSRESPONSE
_ENDPOINTRESPONSE.fields_by_name['error_response'].message_type = _ERRORRESPONSE
_ENDPOINTRESPONSE.oneofs_by_name['type'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['predict_response'])
_ENDPOINTRESPONSE.fields_by_name['predict_response'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['type']
_ENDPOINTRESPONSE.oneofs_by_name['type'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['model_metadata_response'])
_ENDPOINTRESPONSE.fields_by_name['model_metadata_response'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['type']
_ENDPOINTRESPONSE.oneofs_by_name['type'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['model_status_response'])
_ENDPOINTRESPONSE.fields_by_name['model_status_response'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['type']
_ENDPOINTRESPONSE.oneofs_by_name['type'].fields.append(
  _ENDPOINTRESPONSE.fields_by_name['error_response'])
_ENDPOINTRESPONSE.fields_by_name['error_response'].containing_oneof = _ENDPOINTRESPONSE.oneofs_by_name['type']
_PREDICTRESPONSE_DATA.fields_by_name['numpy_attributes'].message_type = ie__serving_dot_messaging_dot_data__attributes__pb2._NUMPYATTRIBUTES
_PREDICTRESPONSE_DATA.fields_by_name['string_attributes'].message_type = ie__serving_dot_messaging_dot_data__attributes__pb2._STRINGATTRIBUTES
_PREDICTRESPONSE_DATA.fields_by_name['binary_attributes'].message_type = ie__serving_dot_messaging_dot_data__attributes__pb2._BINARYATTRIBUTES
_PREDICTRESPONSE_DATA.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE_DATA.oneofs_by_name['type'].fields.append(
  _PREDICTRESPONSE_DATA.fields_by_name['numpy_attributes'])
_PREDICTRESPONSE_DATA.fields_by_name['numpy_attributes'].containing_oneof = _PREDICTRESPONSE_DATA.oneofs_by_name['type']
_PREDICTRESPONSE_DATA.oneofs_by_name['type'].fields.append(
  _PREDICTRESPONSE_DATA.fields_by_name['string_attributes'])
_PREDICTRESPONSE_DATA.fields_by_name['string_attributes'].containing_oneof = _PREDICTRESPONSE_DATA.oneofs_by_name['type']
_PREDICTRESPONSE_DATA.oneofs_by_name['type'].fields.append(
  _PREDICTRESPONSE_DATA.fields_by_name['binary_attributes'])
_PREDICTRESPONSE_DATA.fields_by_name['binary_attributes'].containing_oneof = _PREDICTRESPONSE_DATA.oneofs_by_name['type']
_PREDICTRESPONSE.fields_by_name['outputs'].message_type = _PREDICTRESPONSE_DATA
_MODELMETADATARESPONSE_LAYER.containing_type = _MODELMETADATARESPONSE
_MODELMETADATARESPONSE_SIGNATURE.fields_by_name['layer'].message_type = _MODELMETADATARESPONSE_LAYER
_MODELMETADATARESPONSE_SIGNATURE.containing_type = _MODELMETADATARESPONSE
_MODELMETADATARESPONSE.fields_by_name['inputs_signature'].message_type = _MODELMETADATARESPONSE_SIGNATURE
_MODELMETADATARESPONSE.fields_by_name['outputs_signature'].message_type = _MODELMETADATARESPONSE_SIGNATURE
_MODELSTATUSRESPONSE_STATUS.fields_by_name['error_code'].enum_type = _MODELSTATUSRESPONSE_STATUS_ERRORCODE
_MODELSTATUSRESPONSE_STATUS.containing_type = _MODELSTATUSRESPONSE
_MODELSTATUSRESPONSE_STATUS_ERRORCODE.containing_type = _MODELSTATUSRESPONSE_STATUS
_MODELSTATUSRESPONSE_MODELVERSIONSTATUS.fields_by_name['state'].enum_type = _MODELSTATUSRESPONSE_STATE
_MODELSTATUSRESPONSE_MODELVERSIONSTATUS.fields_by_name['status'].message_type = _MODELSTATUSRESPONSE_STATUS
_MODELSTATUSRESPONSE_MODELVERSIONSTATUS.containing_type = _MODELSTATUSRESPONSE
_MODELSTATUSRESPONSE_STATE.containing_type = _MODELSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['EndpointResponse'] = _ENDPOINTRESPONSE
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
DESCRIPTOR.message_types_by_name['ModelMetadataResponse'] = _MODELMETADATARESPONSE
DESCRIPTOR.message_types_by_name['ModelStatusResponse'] = _MODELSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndpointResponse = _reflection.GeneratedProtocolMessageType('EndpointResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTRESPONSE,
  '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
  # @@protoc_insertion_point(class_scope:ovms_ipc.EndpointResponse)
  })
_sym_db.RegisterMessage(EndpointResponse)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTRESPONSE_DATA,
    '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
    # @@protoc_insertion_point(class_scope:ovms_ipc.PredictResponse.Data)
    })
  ,
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
  # @@protoc_insertion_point(class_scope:ovms_ipc.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.Data)

ModelMetadataResponse = _reflection.GeneratedProtocolMessageType('ModelMetadataResponse', (_message.Message,), {

  'Layer' : _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), {
    'DESCRIPTOR' : _MODELMETADATARESPONSE_LAYER,
    '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
    # @@protoc_insertion_point(class_scope:ovms_ipc.ModelMetadataResponse.Layer)
    })
  ,

  'Signature' : _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), {
    'DESCRIPTOR' : _MODELMETADATARESPONSE_SIGNATURE,
    '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
    # @@protoc_insertion_point(class_scope:ovms_ipc.ModelMetadataResponse.Signature)
    })
  ,
  'DESCRIPTOR' : _MODELMETADATARESPONSE,
  '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
  # @@protoc_insertion_point(class_scope:ovms_ipc.ModelMetadataResponse)
  })
_sym_db.RegisterMessage(ModelMetadataResponse)
_sym_db.RegisterMessage(ModelMetadataResponse.Layer)
_sym_db.RegisterMessage(ModelMetadataResponse.Signature)

ModelStatusResponse = _reflection.GeneratedProtocolMessageType('ModelStatusResponse', (_message.Message,), {

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _MODELSTATUSRESPONSE_STATUS,
    '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
    # @@protoc_insertion_point(class_scope:ovms_ipc.ModelStatusResponse.Status)
    })
  ,

  'ModelVersionStatus' : _reflection.GeneratedProtocolMessageType('ModelVersionStatus', (_message.Message,), {
    'DESCRIPTOR' : _MODELSTATUSRESPONSE_MODELVERSIONSTATUS,
    '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
    # @@protoc_insertion_point(class_scope:ovms_ipc.ModelStatusResponse.ModelVersionStatus)
    })
  ,
  'DESCRIPTOR' : _MODELSTATUSRESPONSE,
  '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
  # @@protoc_insertion_point(class_scope:ovms_ipc.ModelStatusResponse)
  })
_sym_db.RegisterMessage(ModelStatusResponse)
_sym_db.RegisterMessage(ModelStatusResponse.Status)
_sym_db.RegisterMessage(ModelStatusResponse.ModelVersionStatus)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), {
  'DESCRIPTOR' : _ERRORRESPONSE,
  '__module__' : 'ie_serving.messaging.endpoint_responses_pb2'
  # @@protoc_insertion_point(class_scope:ovms_ipc.ErrorResponse)
  })
_sym_db.RegisterMessage(ErrorResponse)


# @@protoc_insertion_point(module_scope)