# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SettingsSavaMappingList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'virtual_account_id': 'str',
        'auto_sync_period': 'int',
        'sync_result_str': 'str',
        'cco_user': 'str',
        'profile': 'SAVAMappingProfile',
        'sync_result': 'SAVAMappingSyncResult',
        'token': 'str',
        'sync_start_time': 'int',
        'last_sync': 'int',
        'tenant_id': 'str',
        'smart_account_id': 'str',
        'expiry': 'int',
        'sync_status': 'str'
    }

    attribute_map = {
        'virtual_account_id': 'virtualAccountId',
        'auto_sync_period': 'autoSyncPeriod',
        'sync_result_str': 'syncResultStr',
        'cco_user': 'ccoUser',
        'profile': 'profile',
        'sync_result': 'syncResult',
        'token': 'token',
        'sync_start_time': 'syncStartTime',
        'last_sync': 'lastSync',
        'tenant_id': 'tenantId',
        'smart_account_id': 'smartAccountId',
        'expiry': 'expiry',
        'sync_status': 'syncStatus'
    }

    def __init__(self, virtual_account_id=None, auto_sync_period=None, sync_result_str=None, cco_user=None, profile=None, sync_result=None, token=None, sync_start_time=None, last_sync=None, tenant_id=None, smart_account_id=None, expiry=None, sync_status=None):  # noqa: E501
        """SettingsSavaMappingList - a model defined in OpenAPI"""  # noqa: E501

        self._virtual_account_id = None
        self._auto_sync_period = None
        self._sync_result_str = None
        self._cco_user = None
        self._profile = None
        self._sync_result = None
        self._token = None
        self._sync_start_time = None
        self._last_sync = None
        self._tenant_id = None
        self._smart_account_id = None
        self._expiry = None
        self._sync_status = None
        self.discriminator = None

        if virtual_account_id is not None:
            self.virtual_account_id = virtual_account_id
        if auto_sync_period is not None:
            self.auto_sync_period = auto_sync_period
        if sync_result_str is not None:
            self.sync_result_str = sync_result_str
        if cco_user is not None:
            self.cco_user = cco_user
        if profile is not None:
            self.profile = profile
        if sync_result is not None:
            self.sync_result = sync_result
        if token is not None:
            self.token = token
        if sync_start_time is not None:
            self.sync_start_time = sync_start_time
        if last_sync is not None:
            self.last_sync = last_sync
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if smart_account_id is not None:
            self.smart_account_id = smart_account_id
        if expiry is not None:
            self.expiry = expiry
        if sync_status is not None:
            self.sync_status = sync_status

    @property
    def virtual_account_id(self):
        """Gets the virtual_account_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The virtual_account_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._virtual_account_id

    @virtual_account_id.setter
    def virtual_account_id(self, virtual_account_id):
        """Sets the virtual_account_id of this SettingsSavaMappingList.


        :param virtual_account_id: The virtual_account_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._virtual_account_id = virtual_account_id

    @property
    def auto_sync_period(self):
        """Gets the auto_sync_period of this SettingsSavaMappingList.  # noqa: E501


        :return: The auto_sync_period of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._auto_sync_period

    @auto_sync_period.setter
    def auto_sync_period(self, auto_sync_period):
        """Sets the auto_sync_period of this SettingsSavaMappingList.


        :param auto_sync_period: The auto_sync_period of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._auto_sync_period = auto_sync_period

    @property
    def sync_result_str(self):
        """Gets the sync_result_str of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_result_str of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._sync_result_str

    @sync_result_str.setter
    def sync_result_str(self, sync_result_str):
        """Sets the sync_result_str of this SettingsSavaMappingList.


        :param sync_result_str: The sync_result_str of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._sync_result_str = sync_result_str

    @property
    def cco_user(self):
        """Gets the cco_user of this SettingsSavaMappingList.  # noqa: E501


        :return: The cco_user of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._cco_user

    @cco_user.setter
    def cco_user(self, cco_user):
        """Sets the cco_user of this SettingsSavaMappingList.


        :param cco_user: The cco_user of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._cco_user = cco_user

    @property
    def profile(self):
        """Gets the profile of this SettingsSavaMappingList.  # noqa: E501


        :return: The profile of this SettingsSavaMappingList.  # noqa: E501
        :rtype: SAVAMappingProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SettingsSavaMappingList.


        :param profile: The profile of this SettingsSavaMappingList.  # noqa: E501
        :type: SAVAMappingProfile
        """

        self._profile = profile

    @property
    def sync_result(self):
        """Gets the sync_result of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_result of this SettingsSavaMappingList.  # noqa: E501
        :rtype: SAVAMappingSyncResult
        """
        return self._sync_result

    @sync_result.setter
    def sync_result(self, sync_result):
        """Sets the sync_result of this SettingsSavaMappingList.


        :param sync_result: The sync_result of this SettingsSavaMappingList.  # noqa: E501
        :type: SAVAMappingSyncResult
        """

        self._sync_result = sync_result

    @property
    def token(self):
        """Gets the token of this SettingsSavaMappingList.  # noqa: E501


        :return: The token of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SettingsSavaMappingList.


        :param token: The token of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def sync_start_time(self):
        """Gets the sync_start_time of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_start_time of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._sync_start_time

    @sync_start_time.setter
    def sync_start_time(self, sync_start_time):
        """Sets the sync_start_time of this SettingsSavaMappingList.


        :param sync_start_time: The sync_start_time of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._sync_start_time = sync_start_time

    @property
    def last_sync(self):
        """Gets the last_sync of this SettingsSavaMappingList.  # noqa: E501


        :return: The last_sync of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this SettingsSavaMappingList.


        :param last_sync: The last_sync of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._last_sync = last_sync

    @property
    def tenant_id(self):
        """Gets the tenant_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The tenant_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this SettingsSavaMappingList.


        :param tenant_id: The tenant_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def smart_account_id(self):
        """Gets the smart_account_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The smart_account_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._smart_account_id

    @smart_account_id.setter
    def smart_account_id(self, smart_account_id):
        """Sets the smart_account_id of this SettingsSavaMappingList.


        :param smart_account_id: The smart_account_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._smart_account_id = smart_account_id

    @property
    def expiry(self):
        """Gets the expiry of this SettingsSavaMappingList.  # noqa: E501


        :return: The expiry of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SettingsSavaMappingList.


        :param expiry: The expiry of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def sync_status(self):
        """Gets the sync_status of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_status of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this SettingsSavaMappingList.


        :param sync_status: The sync_status of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_SYNCED", "SYNCING", "SUCCESS", "FAILURE"]  # noqa: E501
        if sync_status not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_status` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_status, allowed_values)
            )

        self._sync_status = sync_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsSavaMappingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
