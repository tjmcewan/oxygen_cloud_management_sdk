#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ApiSpaceSubscription:
  """
  Attributes:
   - oid
   - oxygenId
   - displayName
   - email
   - spaceOid
   - repositoryNodeId
   - canWrite
   - canManage
   - isOwner
   - spaceName
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'oid', None, None, ), # 1
    (2, TType.STRING, 'oxygenId', None, None, ), # 2
    (3, TType.STRING, 'displayName', None, None, ), # 3
    (4, TType.STRING, 'email', None, None, ), # 4
    (5, TType.STRING, 'spaceOid', None, None, ), # 5
    (6, TType.STRING, 'repositoryNodeId', None, None, ), # 6
    (7, TType.BOOL, 'canWrite', None, None, ), # 7
    (8, TType.BOOL, 'canManage', None, None, ), # 8
    (9, TType.BOOL, 'isOwner', None, None, ), # 9
    (10, TType.STRING, 'spaceName', None, None, ), # 10
  )

  def __init__(self, oid=None, oxygenId=None, displayName=None, email=None, spaceOid=None, repositoryNodeId=None, canWrite=None, canManage=None, isOwner=None, spaceName=None,):
    self.oid = oid
    self.oxygenId = oxygenId
    self.displayName = displayName
    self.email = email
    self.spaceOid = spaceOid
    self.repositoryNodeId = repositoryNodeId
    self.canWrite = canWrite
    self.canManage = canManage
    self.isOwner = isOwner
    self.spaceName = spaceName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.oid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.oxygenId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.displayName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.email = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.spaceOid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.repositoryNodeId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.canWrite = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.canManage = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.BOOL:
          self.isOwner = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.spaceName = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ApiSpaceSubscription')
    if self.oid != None:
      oprot.writeFieldBegin('oid', TType.STRING, 1)
      oprot.writeString(self.oid)
      oprot.writeFieldEnd()
    if self.oxygenId != None:
      oprot.writeFieldBegin('oxygenId', TType.STRING, 2)
      oprot.writeString(self.oxygenId)
      oprot.writeFieldEnd()
    if self.displayName != None:
      oprot.writeFieldBegin('displayName', TType.STRING, 3)
      oprot.writeString(self.displayName)
      oprot.writeFieldEnd()
    if self.email != None:
      oprot.writeFieldBegin('email', TType.STRING, 4)
      oprot.writeString(self.email)
      oprot.writeFieldEnd()
    if self.spaceOid != None:
      oprot.writeFieldBegin('spaceOid', TType.STRING, 5)
      oprot.writeString(self.spaceOid)
      oprot.writeFieldEnd()
    if self.repositoryNodeId != None:
      oprot.writeFieldBegin('repositoryNodeId', TType.STRING, 6)
      oprot.writeString(self.repositoryNodeId)
      oprot.writeFieldEnd()
    if self.canWrite != None:
      oprot.writeFieldBegin('canWrite', TType.BOOL, 7)
      oprot.writeBool(self.canWrite)
      oprot.writeFieldEnd()
    if self.canManage != None:
      oprot.writeFieldBegin('canManage', TType.BOOL, 8)
      oprot.writeBool(self.canManage)
      oprot.writeFieldEnd()
    if self.isOwner != None:
      oprot.writeFieldBegin('isOwner', TType.BOOL, 9)
      oprot.writeBool(self.isOwner)
      oprot.writeFieldEnd()
    if self.spaceName != None:
      oprot.writeFieldBegin('spaceName', TType.STRING, 10)
      oprot.writeString(self.spaceName)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ApiGroupInfo:
  """
  Attributes:
   - id
   - name
   - type
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'type', None, None, ), # 3
  )

  def __init__(self, id=None, name=None, type=None,):
    self.id = id
    self.name = name
    self.type = type

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ApiGroupInfo')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.type != None:
      oprot.writeFieldBegin('type', TType.STRING, 3)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
