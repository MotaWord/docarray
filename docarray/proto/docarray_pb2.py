# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: docarray.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='docarray.proto',
  package='docarray',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x64ocarray.proto\x12\x08\x64ocarray\x1a\x1cgoogle/protobuf/struct.proto\"A\n\x11\x44\x65nseNdArrayProto\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\r\n\x05shape\x18\x02 \x03(\r\x12\r\n\x05\x64type\x18\x03 \x01(\t\"\xb6\x01\n\x0cNdArrayProto\x12,\n\x05\x64\x65nse\x18\x01 \x01(\x0b\x32\x1b.docarray.DenseNdArrayProtoH\x00\x12.\n\x06sparse\x18\x02 \x01(\x0b\x32\x1c.docarray.SparseNdArrayProtoH\x00\x12\x10\n\x08\x63ls_name\x18\x03 \x01(\t\x12+\n\nparameters\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\t\n\x07\x63ontent\"~\n\x12SparseNdArrayProto\x12,\n\x07indices\x18\x01 \x01(\x0b\x32\x1b.docarray.DenseNdArrayProto\x12+\n\x06values\x18\x02 \x01(\x0b\x32\x1b.docarray.DenseNdArrayProto\x12\r\n\x05shape\x18\x03 \x03(\r\"\x83\x01\n\x0fNamedScoreProto\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12+\n\x08operands\x18\x04 \x03(\x0b\x32\x19.docarray.NamedScoreProto\x12\x0e\n\x06ref_id\x18\x05 \x01(\t\"\xc1\x05\n\rDocumentProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x06\x62uffer\x18\x02 \x01(\x0cH\x00\x12&\n\x04\x62lob\x18\x03 \x01(\x0b\x32\x16.docarray.NdArrayProtoH\x00\x12\x0e\n\x04text\x18\x04 \x01(\tH\x00\x12\x13\n\x0bgranularity\x18\x05 \x01(\r\x12\x11\n\tadjacency\x18\x06 \x01(\r\x12\x11\n\tparent_id\x18\x07 \x01(\t\x12\x0e\n\x06weight\x18\x08 \x01(\x02\x12\x0b\n\x03uri\x18\t \x01(\t\x12\x10\n\x08modality\x18\n \x01(\t\x12\x11\n\tmime_type\x18\x0b \x01(\t\x12\x0e\n\x06offset\x18\x0c \x01(\x02\x12\x10\n\x08location\x18\r \x03(\x02\x12\'\n\x06\x63hunks\x18\x0e \x03(\x0b\x32\x17.docarray.DocumentProto\x12(\n\x07matches\x18\x0f \x03(\x0b\x32\x17.docarray.DocumentProto\x12)\n\tembedding\x18\x10 \x01(\x0b\x32\x16.docarray.NdArrayProto\x12%\n\x04tags\x18\x11 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x33\n\x06scores\x18\x12 \x03(\x0b\x32#.docarray.DocumentProto.ScoresEntry\x12=\n\x0b\x65valuations\x18\x13 \x03(\x0b\x32(.docarray.DocumentProto.EvaluationsEntry\x1aH\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.docarray.NamedScoreProto:\x02\x38\x01\x1aM\n\x10\x45valuationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.docarray.NamedScoreProto:\x02\x38\x01\x42\t\n\x07\x63ontent\";\n\x12\x44ocumentArrayProto\x12%\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x17.docarray.DocumentProtob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_DENSENDARRAYPROTO = _descriptor.Descriptor(
  name='DenseNdArrayProto',
  full_name='docarray.DenseNdArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='docarray.DenseNdArrayProto.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='docarray.DenseNdArrayProto.shape', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='docarray.DenseNdArrayProto.dtype', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=58,
  serialized_end=123,
)


_NDARRAYPROTO = _descriptor.Descriptor(
  name='NdArrayProto',
  full_name='docarray.NdArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dense', full_name='docarray.NdArrayProto.dense', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sparse', full_name='docarray.NdArrayProto.sparse', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls_name', full_name='docarray.NdArrayProto.cls_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='docarray.NdArrayProto.parameters', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='content', full_name='docarray.NdArrayProto.content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=126,
  serialized_end=308,
)


_SPARSENDARRAYPROTO = _descriptor.Descriptor(
  name='SparseNdArrayProto',
  full_name='docarray.SparseNdArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indices', full_name='docarray.SparseNdArrayProto.indices', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='docarray.SparseNdArrayProto.values', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='docarray.SparseNdArrayProto.shape', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=310,
  serialized_end=436,
)


_NAMEDSCOREPROTO = _descriptor.Descriptor(
  name='NamedScoreProto',
  full_name='docarray.NamedScoreProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='docarray.NamedScoreProto.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='op_name', full_name='docarray.NamedScoreProto.op_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='docarray.NamedScoreProto.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operands', full_name='docarray.NamedScoreProto.operands', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref_id', full_name='docarray.NamedScoreProto.ref_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=439,
  serialized_end=570,
)


_DOCUMENTPROTO_SCORESENTRY = _descriptor.Descriptor(
  name='ScoresEntry',
  full_name='docarray.DocumentProto.ScoresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='docarray.DocumentProto.ScoresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='docarray.DocumentProto.ScoresEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1188,
)

_DOCUMENTPROTO_EVALUATIONSENTRY = _descriptor.Descriptor(
  name='EvaluationsEntry',
  full_name='docarray.DocumentProto.EvaluationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='docarray.DocumentProto.EvaluationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='docarray.DocumentProto.EvaluationsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1190,
  serialized_end=1267,
)

_DOCUMENTPROTO = _descriptor.Descriptor(
  name='DocumentProto',
  full_name='docarray.DocumentProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='docarray.DocumentProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer', full_name='docarray.DocumentProto.buffer', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blob', full_name='docarray.DocumentProto.blob', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='docarray.DocumentProto.text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='docarray.DocumentProto.granularity', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjacency', full_name='docarray.DocumentProto.adjacency', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='docarray.DocumentProto.parent_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weight', full_name='docarray.DocumentProto.weight', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='docarray.DocumentProto.uri', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modality', full_name='docarray.DocumentProto.modality', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='docarray.DocumentProto.mime_type', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='docarray.DocumentProto.offset', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='docarray.DocumentProto.location', index=12,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='docarray.DocumentProto.chunks', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matches', full_name='docarray.DocumentProto.matches', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='embedding', full_name='docarray.DocumentProto.embedding', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='docarray.DocumentProto.tags', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='docarray.DocumentProto.scores', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluations', full_name='docarray.DocumentProto.evaluations', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DOCUMENTPROTO_SCORESENTRY, _DOCUMENTPROTO_EVALUATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='docarray.DocumentProto.content',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=573,
  serialized_end=1278,
)


_DOCUMENTARRAYPROTO = _descriptor.Descriptor(
  name='DocumentArrayProto',
  full_name='docarray.DocumentArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='docs', full_name='docarray.DocumentArrayProto.docs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1280,
  serialized_end=1339,
)

_NDARRAYPROTO.fields_by_name['dense'].message_type = _DENSENDARRAYPROTO
_NDARRAYPROTO.fields_by_name['sparse'].message_type = _SPARSENDARRAYPROTO
_NDARRAYPROTO.fields_by_name['parameters'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_NDARRAYPROTO.oneofs_by_name['content'].fields.append(
  _NDARRAYPROTO.fields_by_name['dense'])
_NDARRAYPROTO.fields_by_name['dense'].containing_oneof = _NDARRAYPROTO.oneofs_by_name['content']
_NDARRAYPROTO.oneofs_by_name['content'].fields.append(
  _NDARRAYPROTO.fields_by_name['sparse'])
_NDARRAYPROTO.fields_by_name['sparse'].containing_oneof = _NDARRAYPROTO.oneofs_by_name['content']
_SPARSENDARRAYPROTO.fields_by_name['indices'].message_type = _DENSENDARRAYPROTO
_SPARSENDARRAYPROTO.fields_by_name['values'].message_type = _DENSENDARRAYPROTO
_NAMEDSCOREPROTO.fields_by_name['operands'].message_type = _NAMEDSCOREPROTO
_DOCUMENTPROTO_SCORESENTRY.fields_by_name['value'].message_type = _NAMEDSCOREPROTO
_DOCUMENTPROTO_SCORESENTRY.containing_type = _DOCUMENTPROTO
_DOCUMENTPROTO_EVALUATIONSENTRY.fields_by_name['value'].message_type = _NAMEDSCOREPROTO
_DOCUMENTPROTO_EVALUATIONSENTRY.containing_type = _DOCUMENTPROTO
_DOCUMENTPROTO.fields_by_name['blob'].message_type = _NDARRAYPROTO
_DOCUMENTPROTO.fields_by_name['chunks'].message_type = _DOCUMENTPROTO
_DOCUMENTPROTO.fields_by_name['matches'].message_type = _DOCUMENTPROTO
_DOCUMENTPROTO.fields_by_name['embedding'].message_type = _NDARRAYPROTO
_DOCUMENTPROTO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DOCUMENTPROTO.fields_by_name['scores'].message_type = _DOCUMENTPROTO_SCORESENTRY
_DOCUMENTPROTO.fields_by_name['evaluations'].message_type = _DOCUMENTPROTO_EVALUATIONSENTRY
_DOCUMENTPROTO.oneofs_by_name['content'].fields.append(
  _DOCUMENTPROTO.fields_by_name['buffer'])
_DOCUMENTPROTO.fields_by_name['buffer'].containing_oneof = _DOCUMENTPROTO.oneofs_by_name['content']
_DOCUMENTPROTO.oneofs_by_name['content'].fields.append(
  _DOCUMENTPROTO.fields_by_name['blob'])
_DOCUMENTPROTO.fields_by_name['blob'].containing_oneof = _DOCUMENTPROTO.oneofs_by_name['content']
_DOCUMENTPROTO.oneofs_by_name['content'].fields.append(
  _DOCUMENTPROTO.fields_by_name['text'])
_DOCUMENTPROTO.fields_by_name['text'].containing_oneof = _DOCUMENTPROTO.oneofs_by_name['content']
_DOCUMENTARRAYPROTO.fields_by_name['docs'].message_type = _DOCUMENTPROTO
DESCRIPTOR.message_types_by_name['DenseNdArrayProto'] = _DENSENDARRAYPROTO
DESCRIPTOR.message_types_by_name['NdArrayProto'] = _NDARRAYPROTO
DESCRIPTOR.message_types_by_name['SparseNdArrayProto'] = _SPARSENDARRAYPROTO
DESCRIPTOR.message_types_by_name['NamedScoreProto'] = _NAMEDSCOREPROTO
DESCRIPTOR.message_types_by_name['DocumentProto'] = _DOCUMENTPROTO
DESCRIPTOR.message_types_by_name['DocumentArrayProto'] = _DOCUMENTARRAYPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DenseNdArrayProto = _reflection.GeneratedProtocolMessageType('DenseNdArrayProto', (_message.Message,), {
  'DESCRIPTOR' : _DENSENDARRAYPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.DenseNdArrayProto)
  })
_sym_db.RegisterMessage(DenseNdArrayProto)

NdArrayProto = _reflection.GeneratedProtocolMessageType('NdArrayProto', (_message.Message,), {
  'DESCRIPTOR' : _NDARRAYPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.NdArrayProto)
  })
_sym_db.RegisterMessage(NdArrayProto)

SparseNdArrayProto = _reflection.GeneratedProtocolMessageType('SparseNdArrayProto', (_message.Message,), {
  'DESCRIPTOR' : _SPARSENDARRAYPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.SparseNdArrayProto)
  })
_sym_db.RegisterMessage(SparseNdArrayProto)

NamedScoreProto = _reflection.GeneratedProtocolMessageType('NamedScoreProto', (_message.Message,), {
  'DESCRIPTOR' : _NAMEDSCOREPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.NamedScoreProto)
  })
_sym_db.RegisterMessage(NamedScoreProto)

DocumentProto = _reflection.GeneratedProtocolMessageType('DocumentProto', (_message.Message,), {

  'ScoresEntry' : _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTPROTO_SCORESENTRY,
    '__module__' : 'docarray_pb2'
    # @@protoc_insertion_point(class_scope:docarray.DocumentProto.ScoresEntry)
    })
  ,

  'EvaluationsEntry' : _reflection.GeneratedProtocolMessageType('EvaluationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTPROTO_EVALUATIONSENTRY,
    '__module__' : 'docarray_pb2'
    # @@protoc_insertion_point(class_scope:docarray.DocumentProto.EvaluationsEntry)
    })
  ,
  'DESCRIPTOR' : _DOCUMENTPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.DocumentProto)
  })
_sym_db.RegisterMessage(DocumentProto)
_sym_db.RegisterMessage(DocumentProto.ScoresEntry)
_sym_db.RegisterMessage(DocumentProto.EvaluationsEntry)

DocumentArrayProto = _reflection.GeneratedProtocolMessageType('DocumentArrayProto', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTARRAYPROTO,
  '__module__' : 'docarray_pb2'
  # @@protoc_insertion_point(class_scope:docarray.DocumentArrayProto)
  })
_sym_db.RegisterMessage(DocumentArrayProto)


_DOCUMENTPROTO_SCORESENTRY._options = None
_DOCUMENTPROTO_EVALUATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
