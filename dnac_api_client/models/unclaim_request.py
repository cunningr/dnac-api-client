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


class UnclaimRequest(object):
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
        'device_id_list': 'list[str]'
    }

    attribute_map = {
        'device_id_list': 'deviceIdList'
    }

    def __init__(self, device_id_list=None):  # noqa: E501
        """UnclaimRequest - a model defined in Swagger"""  # noqa: E501

        self._device_id_list = None
        self.discriminator = None

        if device_id_list is not None:
            self.device_id_list = device_id_list

    @property
    def device_id_list(self):
        """Gets the device_id_list of this UnclaimRequest.  # noqa: E501


        :return: The device_id_list of this UnclaimRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_id_list

    @device_id_list.setter
    def device_id_list(self, device_id_list):
        """Sets the device_id_list of this UnclaimRequest.


        :param device_id_list: The device_id_list of this UnclaimRequest.  # noqa: E501
        :type: list[str]
        """

        self._device_id_list = device_id_list

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
        if not isinstance(other, UnclaimRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
