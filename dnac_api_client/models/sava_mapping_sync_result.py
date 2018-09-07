# coding: utf-8

"""
    Cisco DNA Center Platform v. 1.2.x (EFT)

    REST API (EFT)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dnac_api_client.models.sava_mapping_sync_result_sync_list import SAVAMappingSyncResultSyncList  # noqa: F401,E501


class SAVAMappingSyncResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sync_list': 'list[SAVAMappingSyncResultSyncList]',
        'sync_msg': 'str'
    }

    attribute_map = {
        'sync_list': 'syncList',
        'sync_msg': 'syncMsg'
    }

    def __init__(self, sync_list=None, sync_msg=None):  # noqa: E501
        """SAVAMappingSyncResult - a model defined in Swagger"""  # noqa: E501

        self._sync_list = None
        self._sync_msg = None
        self.discriminator = None

        if sync_list is not None:
            self.sync_list = sync_list
        if sync_msg is not None:
            self.sync_msg = sync_msg

    @property
    def sync_list(self):
        """Gets the sync_list of this SAVAMappingSyncResult.  # noqa: E501


        :return: The sync_list of this SAVAMappingSyncResult.  # noqa: E501
        :rtype: list[SAVAMappingSyncResultSyncList]
        """
        return self._sync_list

    @sync_list.setter
    def sync_list(self, sync_list):
        """Sets the sync_list of this SAVAMappingSyncResult.


        :param sync_list: The sync_list of this SAVAMappingSyncResult.  # noqa: E501
        :type: list[SAVAMappingSyncResultSyncList]
        """

        self._sync_list = sync_list

    @property
    def sync_msg(self):
        """Gets the sync_msg of this SAVAMappingSyncResult.  # noqa: E501


        :return: The sync_msg of this SAVAMappingSyncResult.  # noqa: E501
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        """Sets the sync_msg of this SAVAMappingSyncResult.


        :param sync_msg: The sync_msg of this SAVAMappingSyncResult.  # noqa: E501
        :type: str
        """

        self._sync_msg = sync_msg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, SAVAMappingSyncResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other