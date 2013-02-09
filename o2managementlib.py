import os, sys, inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"gen-py")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import hashlib
import mimetypes
import httplib
import o2exceptions

from O2Service import O2Service
from O2Service.ttypes import *
from O2Service.constants import *
from errors.ttypes import *
from cloudfs.ttypes import *
from auth.ttypes import *
from signup.ttypes import *
from gridironthrift import Gridironthrift
from gridironthrift.transport import TSocket
from gridironthrift.transport import THttpClient
from gridironthrift.transport import TTransport
from gridironthrift.protocol import TBinaryProtocol

class O2AgentFactory:

    def create_O2Agent(self, api_key, proxy_uri = None, proxy_username = None, proxy_password = None):
        return O2Agent(api_key, 'https://api.oxygencloud.com:443/gateway', proxy_uri, proxy_username, proxy_password)

    def create_custom_O2Agent(self, api_key, api_path, proxy_uri = None, proxy_username = None, proxy_password = None):
        return O2Agent(api_key, api_path, proxy_uri, proxy_username, proxy_password)


class O2GroupInfo:
    _id = ''
    _name = ''
    _type = ''

    def __repr__(self):
        return 'O2GroupInfo(' + str(self._name) + ')'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type


class O2GroupPermissions:
    _group_id = ''
    _admin = False
    _create_spaces = False
    _permanent_delete = False
    _invite_outside_guests = False

    def __repr__(self):
        return 'O2GroupPermissions(' + str(self._group_id) + ')'

    def get_id(self):
        return self._group_id

    def can_admin(self):
        return self._admin

    def can_create_spaces(self):
        return self._create_spaces

    def can_permanent_delete(self):
        return self._permanent_delete

    def can_invite_outside_guests(self):
        return self._invite_outside_guests


class O2SpaceSubscriptionInfo:
    _id = ''
    _oxygen_id = ''
    _display_name = ''
    _email = ''
    _space_name = ''
    _space_id = ''
    _repository_node_id = ''
    _can_write = False
    _can_manage = False
    _is_owner = False

    def __repr__(self):
        return 'O2SpaceSubscriptionInfo(' + str(self._space_name) + ' : ' + str(self._display_name) + ')'

    def get_display_name(self):
        return self._display_name

    def get_space_name(self):
        return self._space_name

    def get_space_id(self):
        return self._repository_node_id + '|' + self._space_id

    def can_write(self):
        return self._can_write

    def can_manage(self):
        return self._can_manage

    def is_owner(self):
        return self._is_owner


class O2UserInfo:
    _id = ''
    _oxygen_id = ''
    _first_name = ''
    _last_name = ''
    _display_name = ''
    _email = ''
    _external = ''
    _deleted = ''
    _disabled = ''
    _last_login_date_time = ''
    _external_id = ''

    def __repr__(self):
        return 'O2UserInfo(' + str(self._oxygen_id) + ')'

    def get_oxygen_id(self):
        return self._oxygen_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_display_name(self):
        return self._display_name

    def get_email(self):
        return self._email

    def is_external(self):
        return self._external

    def is_deleted(self):
        return self._deleted

    def is_disabled(self):
        return self._disabled

    def get_last_login_date_time(self):
        return self._last_login_date_time

    def get_external_id(self):
        return self._external_id

    def is_not_activated(self):
        return self._pending


class O2SpaceInfo:
    _id = ''
    _repository_node_id = ''
    _name = ''
    _description = ''
    _owner_oxygen_id = ''
    _storage_name = ''
    _utilized = ''
    _capacity = ''
    _listed = ''
    _writable_by_default = ''

    def __repr__(self):
        return 'O2SpaceInfo(' + str(self._name) + ')'

    def get_space_id(self):
        return self._repository_node_id + '|' + self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_owner_oxygen_id(self):
        return self._owner_oxygen_id

    def get_storage_name(self):
        return self._storage_name

    def get_utilized(self):
        return self._utilized

    def get_capacity(self):
        return self._capacity

    def is_listed(self):
        return self._listed

    def is_writable_by_default(self):
        return self._writable_by_default


class O2UserVolumeInfo:
    _owner_oxygen_id = ''
    _storage_name = ''
    _utilized = ''
    _capacity = ''

    def __repr__(self):
        return 'O2UserVolumeInfo(' + str(self._owner_oxygen_id) + ')'

    def get_owner_oxygen_id(self):
        return self._owner_oxygen_id

    def get_storage_name(self):
        return self._storage_name

    def get_utilized(self):
        return self._utilized

    def get_capacity(self):
        return self._capacity


class O2Agent:
    api_key = ''
    api_path = ''
    oxygen_api_client = 0
    session_id = 'no session'

    def __init__(self, api_key, api_path, proxy_uri = None, proxy_username = None, proxy_password = None):
        try:
            self.api_key = api_key
            self.api_path = api_path
            oxygen_api_connector = THttpClient.THttpClient(self.api_path, proxy_uri, proxy_username, proxy_password)
            oxygen_api_connector = TTransport.TBufferedTransport(oxygen_api_connector)
            oxygen_api_protocol = TBinaryProtocol.TBinaryProtocol(oxygen_api_connector)
            self.oxygen_api_client = O2Service.Client(oxygen_api_protocol)
        except BaseException as e:
            self.handle_exception(e)

    def handle_exception(self, e):
        o2exceptions.handle_exception(e)

    def convert_to_o2grouppermissions(self, group_id, tm):
        o2gp = O2GroupPermissions()
        o2gp._group_id = group_id
        o2gp._admin = tm['ADMIN']
        o2gp._create_spaces = tm['CREATE_SPACE']
        o2gp._permanent_delete = tm['PERMANENT_DELETE']
        o2gp._invite_outside_guests = tm['INVITE_OUTSIDE_GUESTS']
        return o2gp

    def convert_to_o2userinfo(self, aui):
        pending_value = '(Not Specified)'
        o2ui = O2UserInfo()
        o2ui._oid = aui.oid
        o2ui._oxygen_id = aui.oxygenId
        o2ui._first_name = aui.firstName
        o2ui._last_name = aui.lastName
        o2ui._display_name = aui.displayName
        o2ui._email = aui.email
        o2ui._external = aui.isExternal
        o2ui._deleted = aui.isDeleted
        o2ui._last_login_date_time = aui.lastLoginDateTime
        o2ui._external_id = aui.externalId
        o2ui._disabled = aui.isDisabled
        o2ui._pending = aui.isPending
        if aui.isPending:
            o2ui._oxygen_id = pending_value
        return o2ui

    def convert_to_o2userinfo_list(self, aui_list):
        return [ self.convert_to_o2userinfo(aui) for aui in aui_list ]

    def convert_to_o2uservolume(self, asi):
        o2uv = O2UserVolumeInfo()
        o2uv._owner_oxygen_id = asi.ownerOxygenId
        o2uv._storage_name = asi.storageName
        o2uv._utilized = asi.utilized
        o2uv._capacity = asi.capacity
        return o2uv

    def convert_to_o2spaceinfo(self, asi):
        o2si = O2SpaceInfo()
        o2si._id = asi.oid
        o2si._repository_node_id = asi.repositoryNodeId
        o2si._name = asi.name
        o2si._description = asi.description
        o2si._owner_oxygen_id = asi.ownerOxygenId
        o2si._storage_name = asi.storageName
        o2si._utilized = asi.utilized
        o2si._capacity = asi.capacity
        o2si._listed = asi.listed
        o2si._writable_by_default = asi.writableDefault
        return o2si

    def convert_to_o2spaceinfo_list(self, asi_list):
        return [ self.convert_to_o2spaceinfo(asi) for asi in asi_list ]

    def convert_to_o2groupinfo(self, agi):
        o2gi = O2GroupInfo()
        o2gi._id = agi.id
        o2gi._name = agi.name
        o2gi._type = agi.type

    def convert_to_o2groupinfo_list(self, agi_list):
        return [ self.convert_to_o2groupinfo(agi) for agi in agi_list ]

    def convert_to_o2spacesubscriptioninfo(self, ass):
        o2ssi = O2SpaceSubscriptionInfo()
        o2ssi._id = ass.oid
        o2ssi._oxygen_id = ass.oxygenId
        o2ssi._display_name = ass.displayName
        o2ssi._email = ass.email
        o2ssi._space_name = ass.spaceName
        o2ssi._space_id = ass.spaceOid
        o2ssi._repository_node_id = ass.repositoryNodeId
        o2ssi._can_write = ass.canWrite
        o2ssi._can_manage = ass.canManage
        o2ssi._is_owner = ass.isOwner
        return o2ssi

    def convert_to_o2spacesubscriptioninfo_list(self, ass_list):
        return [ self.convert_to_o2spacesubscriptioninfo(ass) for ass in ass_list ]

    def get_api_service_info(self):
        try:
            return self.oxygen_api_client.getInfo()
        except BaseException as e:
            self.handle_exception(e)

    def login_api_user(self, oxygen_id, password):
        try:
            retval = self.oxygen_api_client.loginAdminUser(self.api_key, oxygen_id, password)
            self.session_id = retval.id
        except BaseException as e:
            self.handle_exception(e)

    def logout(self):
        try:
            self.oxygen_api_client.logout(self.session_id)
            self.session_id = 'no session'
        except BaseException as e:
            self.handle_exception(e)

    def get_user_info(self):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.getUserInfoBySessionId(self.session_id))
        except BaseException as e:
            self.handle_exception(e)

    def create_user(self, oxygen_id, email, corporate_user_name, first_name, last_name, password):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.createUser(self.session_id, oxygen_id, email, corporate_user_name, first_name, last_name, password))
        except BaseException as e:
            self.handle_exception(e)

    def get_all_users(self):
        try:
            user_list = []
            while True:
                temp = self.convert_to_o2userinfo_list(self.oxygen_api_client.getAllUsers(self.session_id, len(user_list)))
                user_list.extend(temp)
                if len(temp) <= 0:
                    break

            return user_list
        except BaseException as e:
            self.handle_exception(e)

    def get_guest_users(self):
        try:
            return self.convert_to_o2userinfo_list(self.oxygen_api_client.getGuestUsers(self.session_id))
        except BaseException as e:
            self.handle_exception(e)

    def get_user_by_oxygen_id(self, oxygen_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.getUserByOxygenId(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def get_user_by_external_id(self, external_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.getUserByExternalId(self.session_id, external_id))
        except BaseException as e:
            self.handle_exception(e)

    def disable_user_by_oxygen_id(self, oxygen_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.disableUserByOxygenId(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def enable_user_by_oxygen_id(self, oxygen_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.enableUserByOxygenId(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def delete_user_by_oxygen_id(self, oxygen_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.deleteUserByOxygenId(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def update_user_oxygen_id(self, oxygen_id, new_oxygen_id):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.updateUserOxygenId(self.session_id, oxygen_id, new_oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def update_user_details_by_oxygen_id(self, oxygen_id, email, first_name, last_name, display_name):
        try:
            return self.convert_to_o2userinfo(self.oxygen_api_client.updateUserDetailsByOxygenId(self.session_id, oxygen_id, email, first_name, last_name, display_name))
        except BaseException as e:
            self.handle_exception(e)

    def create_space(self, name, description, owner_oxygen_id, storage_name, capacity, listed, writable_by_default):
        try:
            return self.convert_to_o2spaceinfo(self.oxygen_api_client.createSpace(self.session_id, name, description, owner_oxygen_id, storage_name, capacity, listed, writable_by_default))
        except BaseException as e:
            self.handle_exception(e)

    def modify_space_info(self, space_id, name, description, owner_oxygen_id, capacity, listed, writable_by_default):
        try:
            space_info = space_id.split('|')
            return self.convert_to_o2spaceinfo(self.oxygen_api_client.modifySpace(self.session_id, space_info[1], space_info[0], name, description, owner_oxygen_id, capacity, listed, writable_by_default))
        except BaseException as e:
            self.handle_exception(e)

    def modify_user_volume_capacity(self, oxygen_id, capacity):
        try:
            self.oxygen_api_client.modifyUserVolumeCapacityByOxygenId(self.session_id, oxygen_id, capacity)
        except BaseException as e:
            self.handle_exception(e)

    def get_user_volume_info(self, oxygen_id):
        try:
            return self.convert_to_o2uservolume(self.oxygen_api_client.getUserVolumeByOxygenId(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def get_space_by_space_id(self, space_id):
        try:
            space_info = space_id.split('|')
            return self.convert_to_o2spaceinfo(self.oxygen_api_client.getSpaceBySpaceId(self.session_id, space_info[1], space_info[0]))
        except BaseException as e:
            self.handle_exception(e)

    def get_space_by_space_name(self, space_name):
        try:
            return self.convert_to_o2spaceinfo(self.oxygen_api_client.getSpaceBySpaceName(self.session_id, space_name))
        except BaseException as e:
            self.handle_exception(e)

    def delete_space(self, space_id):
        try:
            space_info = space_id.split('|')
            self.oxygen_api_client.deleteSpace(self.session_id, space_info[1], space_info[0])
        except BaseException as e:
            self.handle_exception(e)

    def add_user_to_space(self, oxygen_id, space_id, can_write, can_manage):
        try:
            space_info = space_id.split('|')
            return self.oxygen_api_client.addUserToSpace(self.session_id, space_info[1], space_info[0], oxygen_id, can_write, can_manage)
        except BaseException as e:
            self.handle_exception(e)

    def remove_user_from_space(self, oxygen_id, space_id):
        try:
            space_info = space_id.split('|')
            return self.oxygen_api_client.removeUserFromSpace(self.session_id, space_info[1], space_info[0], oxygen_id)
        except BaseException as e:
            self.handle_exception(e)

    def add_group_to_space(self, group_id, space_id, can_write, can_manage):
        try:
            space_info = space_id.split('|')
            return self.oxygen_api_client.addGroupToSpace(self.session_id, space_info[1], space_info[0], group_id, can_write, can_manage)
        except BaseException as e:
            self.handle_exception(e)

    def remove_group_from_space(self, group_id, space_id):
        try:
            space_info = space_id.split('|')
            return self.oxygen_api_client.removeGroupFromSpace(self.session_id, space_info[1], space_info[0], group_id)
        except BaseException as e:
            self.handle_exception(e)

    def get_subscriptions_for_user(self, oxygen_id):
        try:
            return self.convert_to_o2spacesubscriptioninfo_list(self.oxygen_api_client.getSubscriptionsForUser(self.session_id, oxygen_id))
        except BaseException as e:
            self.handle_exception(e)

    def get_subscriptions_for_space(self, space_id):
        space_info = space_id.split('|')
        try:
            user_list = []
            user_list = self.convert_to_o2spacesubscriptioninfo_list(self.oxygen_api_client.getSubscriptionsForSpace(self.session_id, space_info[1], space_info[0]))
            return user_list
        except BaseException as e:
            self.handle_exception(e)

    def create_group(self, name):
        try:
            return self.convert_to_o2groupinfo(self.oxygen_api_client.createGroup(self.session_id, name))
        except BaseException as e:
            self.handle_exception(e)

    def get_all_groups(self):
        try:
            return self.convert_to_o2groupinfo_list(self.oxygen_api_client.getAllGroups(self.session_id))
        except BaseException as e:
            self.handle_exception(e)

    def get_group_permissions(self, group_id):
        try:
            return self.convert_to_o2grouppermissions(group_id, self.oxygen_api_client.getGroupPermissions(self.session_id, group_id))
        except BaseException as e:
            self.handle_exception(e)

    def modify_group_admin_permission(self, group_id, allow):
        try:
            self.oxygen_api_client.updateGroupPermissionAdmin(self.session_id, group_id, allow)
        except BaseException as e:
            self.handle_exception(e)

    def modify_group_create_space_permission(self, group_id, allow):
        try:
            self.oxygen_api_client.updateGroupPermissionCreateSpace(self.session_id, group_id, allow)
        except BaseException as e:
            self.handle_exception(e)

    def modify_group_invite_outside_guests_permission(self, group_id, allow):
        try:
            self.oxygen_api_client.updateGroupPermissionInviteOutsideGuests(self.session_id, group_id, allow)
        except BaseException as e:
            self.handle_exception(e)

    def modify_group_permanent_delete_permission(self, group_id, allow):
        try:
            self.oxygen_api_client.updateGroupPermissionPermanentDelete(self.session_id, group_id, allow)
        except BaseException as e:
            self.handle_exception(e)

    def update_group_details(self, group_id, new_name):
        try:
            return self.convert_to_o2groupinfo(group_id, self.oxygen_api_client.updateGroupDetailsByGroupId(self.session_id, group_id, new_name))
        except BaseException as e:
            self.handle_exception(e)

    def add_user_to_group(self, oxygen_id, group_id):
        try:
            return self.oxygen_api_client.addUserToGroup(self.session_id, oxygen_id, group_id)
        except BaseException as e:
            self.handle_exception(e)

    def remove_user_from_group(self, oxygen_id, group_id):
        try:
            return self.oxygen_api_client.removeUserFromGroup(self.session_id, oxygen_id, group_id)
        except BaseException as e:
            self.handle_exception(e)
