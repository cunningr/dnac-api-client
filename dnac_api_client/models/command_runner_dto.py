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


class CommandRunnerDTO(object):
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
        'commands': 'list[str]',
        'description': 'str',
        'device_uuids': 'list[str]',
        'name': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'commands': 'commands',
        'description': 'description',
        'device_uuids': 'deviceUuids',
        'name': 'name',
        'timeout': 'timeout'
    }

    def __init__(self, commands=None, description=None, device_uuids=None, name=None, timeout=None):  # noqa: E501
        """CommandRunnerDTO - a model defined in Swagger"""  # noqa: E501

        self._commands = None
        self._description = None
        self._device_uuids = None
        self._name = None
        self._timeout = None
        self.discriminator = None

        if commands is not None:
            self.commands = commands
        if description is not None:
            self.description = description
        if device_uuids is not None:
            self.device_uuids = device_uuids
        if name is not None:
            self.name = name
        if timeout is not None:
            self.timeout = timeout

    @property
    def commands(self):
        """Gets the commands of this CommandRunnerDTO.  # noqa: E501


        :return: The commands of this CommandRunnerDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this CommandRunnerDTO.


        :param commands: The commands of this CommandRunnerDTO.  # noqa: E501
        :type: list[str]
        """

        self._commands = commands

    @property
    def description(self):
        """Gets the description of this CommandRunnerDTO.  # noqa: E501


        :return: The description of this CommandRunnerDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CommandRunnerDTO.


        :param description: The description of this CommandRunnerDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_uuids(self):
        """Gets the device_uuids of this CommandRunnerDTO.  # noqa: E501


        :return: The device_uuids of this CommandRunnerDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_uuids

    @device_uuids.setter
    def device_uuids(self, device_uuids):
        """Sets the device_uuids of this CommandRunnerDTO.


        :param device_uuids: The device_uuids of this CommandRunnerDTO.  # noqa: E501
        :type: list[str]
        """

        self._device_uuids = device_uuids

    @property
    def name(self):
        """Gets the name of this CommandRunnerDTO.  # noqa: E501


        :return: The name of this CommandRunnerDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CommandRunnerDTO.


        :param name: The name of this CommandRunnerDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def timeout(self):
        """Gets the timeout of this CommandRunnerDTO.  # noqa: E501


        :return: The timeout of this CommandRunnerDTO.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CommandRunnerDTO.


        :param timeout: The timeout of this CommandRunnerDTO.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if not isinstance(other, CommandRunnerDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
