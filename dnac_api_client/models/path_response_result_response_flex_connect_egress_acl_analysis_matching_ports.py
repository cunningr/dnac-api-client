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


class PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts(object):
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
        'protocol': 'str',
        'ports': 'list[PathResponseResultResponseFlexConnectEgressAclAnalysisPorts]'
    }

    attribute_map = {
        'protocol': 'protocol',
        'ports': 'ports'
    }

    def __init__(self, protocol=None, ports=None):  # noqa: E501
        """PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts - a model defined in OpenAPI"""  # noqa: E501

        self._protocol = None
        self._ports = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if ports is not None:
            self.ports = ports

    @property
    def protocol(self):
        """Gets the protocol of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501


        :return: The protocol of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.


        :param protocol: The protocol of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def ports(self):
        """Gets the ports of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501


        :return: The ports of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501
        :rtype: list[PathResponseResultResponseFlexConnectEgressAclAnalysisPorts]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.


        :param ports: The ports of this PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts.  # noqa: E501
        :type: list[PathResponseResultResponseFlexConnectEgressAclAnalysisPorts]
        """

        self._ports = ports

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
        if not isinstance(other, PathResponseResultResponseFlexConnectEgressAclAnalysisMatchingPorts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other