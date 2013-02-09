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



class ApiLogin:
  """
  Login info

  <dl>
   <dt><strong>Fields:</strong></dt>
   <dd>
    <dl>
     <dt><code>loginURL</code> (String)</dt>
     <dd>One-time-use URL of login screen UI</dd>

     <dt><code>tokenId</code> (String)</dt>
     <dd>id of authentication token</dd>
    </dl>
   </dd>
  </dl>

  Attributes:
   - loginURL
   - tokenId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'loginURL', None, None, ), # 1
    (2, TType.STRING, 'tokenId', None, None, ), # 2
  )

  def __init__(self, loginURL=None, tokenId=None,):
    self.loginURL = loginURL
    self.tokenId = tokenId

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
          self.loginURL = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.tokenId = iprot.readString();
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
    oprot.writeStructBegin('ApiLogin')
    if self.loginURL != None:
      oprot.writeFieldBegin('loginURL', TType.STRING, 1)
      oprot.writeString(self.loginURL)
      oprot.writeFieldEnd()
    if self.tokenId != None:
      oprot.writeFieldBegin('tokenId', TType.STRING, 2)
      oprot.writeString(self.tokenId)
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

class ApiSession:
  """
  Session info

  <dl>
   <dt><strong>Fields:</strong></dt>
   <dd>
    <dl>
     <dt><code>id</code> (String)</dt>
     <dd>id of active user session</dd>

     <dt><code>loginId</code> (String)</dt>
     <dd>login id of user bound to this session</dd>
    </dl>
   </dd>
  </dl>

  Attributes:
   - id
   - loginId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'loginId', None, None, ), # 2
  )

  def __init__(self, id=None, loginId=None,):
    self.id = id
    self.loginId = loginId

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
          self.loginId = iprot.readString();
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
    oprot.writeStructBegin('ApiSession')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.loginId != None:
      oprot.writeFieldBegin('loginId', TType.STRING, 2)
      oprot.writeString(self.loginId)
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

class ApiUserInfo:
  """
  Attributes:
   - oid
   - oxygenId
   - firstName
   - lastName
   - displayName
   - email
   - isExternal
   - isDeleted
   - lastLoginDateTime
   - networkAccountOid
   - isDisabled
   - externalId
   - isPending
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'oid', None, None, ), # 1
    (2, TType.STRING, 'oxygenId', None, None, ), # 2
    (3, TType.STRING, 'firstName', None, None, ), # 3
    (4, TType.STRING, 'lastName', None, None, ), # 4
    (5, TType.STRING, 'displayName', None, None, ), # 5
    (6, TType.STRING, 'email', None, None, ), # 6
    (7, TType.BOOL, 'isExternal', None, None, ), # 7
    (8, TType.BOOL, 'isDeleted', None, None, ), # 8
    (9, TType.I64, 'lastLoginDateTime', None, None, ), # 9
    (10, TType.STRING, 'networkAccountOid', None, None, ), # 10
    (11, TType.BOOL, 'isDisabled', None, None, ), # 11
    (12, TType.STRING, 'externalId', None, None, ), # 12
    (13, TType.BOOL, 'isPending', None, None, ), # 13
  )

  def __init__(self, oid=None, oxygenId=None, firstName=None, lastName=None, displayName=None, email=None, isExternal=None, isDeleted=None, lastLoginDateTime=None, networkAccountOid=None, isDisabled=None, externalId=None, isPending=None,):
    self.oid = oid
    self.oxygenId = oxygenId
    self.firstName = firstName
    self.lastName = lastName
    self.displayName = displayName
    self.email = email
    self.isExternal = isExternal
    self.isDeleted = isDeleted
    self.lastLoginDateTime = lastLoginDateTime
    self.networkAccountOid = networkAccountOid
    self.isDisabled = isDisabled
    self.externalId = externalId
    self.isPending = isPending

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
          self.firstName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.lastName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.displayName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.email = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.isExternal = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.isDeleted = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.lastLoginDateTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.networkAccountOid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.BOOL:
          self.isDisabled = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.STRING:
          self.externalId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.BOOL:
          self.isPending = iprot.readBool();
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
    oprot.writeStructBegin('ApiUserInfo')
    if self.oid != None:
      oprot.writeFieldBegin('oid', TType.STRING, 1)
      oprot.writeString(self.oid)
      oprot.writeFieldEnd()
    if self.oxygenId != None:
      oprot.writeFieldBegin('oxygenId', TType.STRING, 2)
      oprot.writeString(self.oxygenId)
      oprot.writeFieldEnd()
    if self.firstName != None:
      oprot.writeFieldBegin('firstName', TType.STRING, 3)
      oprot.writeString(self.firstName)
      oprot.writeFieldEnd()
    if self.lastName != None:
      oprot.writeFieldBegin('lastName', TType.STRING, 4)
      oprot.writeString(self.lastName)
      oprot.writeFieldEnd()
    if self.displayName != None:
      oprot.writeFieldBegin('displayName', TType.STRING, 5)
      oprot.writeString(self.displayName)
      oprot.writeFieldEnd()
    if self.email != None:
      oprot.writeFieldBegin('email', TType.STRING, 6)
      oprot.writeString(self.email)
      oprot.writeFieldEnd()
    if self.isExternal != None:
      oprot.writeFieldBegin('isExternal', TType.BOOL, 7)
      oprot.writeBool(self.isExternal)
      oprot.writeFieldEnd()
    if self.isDeleted != None:
      oprot.writeFieldBegin('isDeleted', TType.BOOL, 8)
      oprot.writeBool(self.isDeleted)
      oprot.writeFieldEnd()
    if self.lastLoginDateTime != None:
      oprot.writeFieldBegin('lastLoginDateTime', TType.I64, 9)
      oprot.writeI64(self.lastLoginDateTime)
      oprot.writeFieldEnd()
    if self.networkAccountOid != None:
      oprot.writeFieldBegin('networkAccountOid', TType.STRING, 10)
      oprot.writeString(self.networkAccountOid)
      oprot.writeFieldEnd()
    if self.isDisabled != None:
      oprot.writeFieldBegin('isDisabled', TType.BOOL, 11)
      oprot.writeBool(self.isDisabled)
      oprot.writeFieldEnd()
    if self.externalId != None:
      oprot.writeFieldBegin('externalId', TType.STRING, 12)
      oprot.writeString(self.externalId)
      oprot.writeFieldEnd()
    if self.isPending != None:
      oprot.writeFieldBegin('isPending', TType.BOOL, 13)
      oprot.writeBool(self.isPending)
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
