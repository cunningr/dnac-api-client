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


class PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics(object):
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
        'input_queue_max_depth': 'int',
        'operational_status': 'str',
        'output_queue_count': 'int',
        'output_packets': 'int',
        'input_queue_flushes': 'int',
        'input_queue_count': 'int',
        'input_queue_drops': 'int',
        'output_ratebps': 'int',
        'input_packets': 'int',
        'input_ratebps': 'int',
        'output_queue_depth': 'int',
        'admin_status': 'str',
        'refreshed_at': 'int',
        'output_drop': 'int'
    }

    attribute_map = {
        'input_queue_max_depth': 'inputQueueMaxDepth',
        'operational_status': 'operationalStatus',
        'output_queue_count': 'outputQueueCount',
        'output_packets': 'outputPackets',
        'input_queue_flushes': 'inputQueueFlushes',
        'input_queue_count': 'inputQueueCount',
        'input_queue_drops': 'inputQueueDrops',
        'output_ratebps': 'outputRatebps',
        'input_packets': 'inputPackets',
        'input_ratebps': 'inputRatebps',
        'output_queue_depth': 'outputQueueDepth',
        'admin_status': 'adminStatus',
        'refreshed_at': 'refreshedAt',
        'output_drop': 'outputDrop'
    }

    def __init__(self, input_queue_max_depth=None, operational_status=None, output_queue_count=None, output_packets=None, input_queue_flushes=None, input_queue_count=None, input_queue_drops=None, output_ratebps=None, input_packets=None, input_ratebps=None, output_queue_depth=None, admin_status=None, refreshed_at=None, output_drop=None):  # noqa: E501
        """PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics - a model defined in OpenAPI"""  # noqa: E501

        self._input_queue_max_depth = None
        self._operational_status = None
        self._output_queue_count = None
        self._output_packets = None
        self._input_queue_flushes = None
        self._input_queue_count = None
        self._input_queue_drops = None
        self._output_ratebps = None
        self._input_packets = None
        self._input_ratebps = None
        self._output_queue_depth = None
        self._admin_status = None
        self._refreshed_at = None
        self._output_drop = None
        self.discriminator = None

        if input_queue_max_depth is not None:
            self.input_queue_max_depth = input_queue_max_depth
        if operational_status is not None:
            self.operational_status = operational_status
        if output_queue_count is not None:
            self.output_queue_count = output_queue_count
        if output_packets is not None:
            self.output_packets = output_packets
        if input_queue_flushes is not None:
            self.input_queue_flushes = input_queue_flushes
        if input_queue_count is not None:
            self.input_queue_count = input_queue_count
        if input_queue_drops is not None:
            self.input_queue_drops = input_queue_drops
        if output_ratebps is not None:
            self.output_ratebps = output_ratebps
        if input_packets is not None:
            self.input_packets = input_packets
        if input_ratebps is not None:
            self.input_ratebps = input_ratebps
        if output_queue_depth is not None:
            self.output_queue_depth = output_queue_depth
        if admin_status is not None:
            self.admin_status = admin_status
        if refreshed_at is not None:
            self.refreshed_at = refreshed_at
        if output_drop is not None:
            self.output_drop = output_drop

    @property
    def input_queue_max_depth(self):
        """Gets the input_queue_max_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_queue_max_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_queue_max_depth

    @input_queue_max_depth.setter
    def input_queue_max_depth(self, input_queue_max_depth):
        """Sets the input_queue_max_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_queue_max_depth: The input_queue_max_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_queue_max_depth = input_queue_max_depth

    @property
    def operational_status(self):
        """Gets the operational_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The operational_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param operational_status: The operational_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

    @property
    def output_queue_count(self):
        """Gets the output_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The output_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._output_queue_count

    @output_queue_count.setter
    def output_queue_count(self, output_queue_count):
        """Sets the output_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param output_queue_count: The output_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._output_queue_count = output_queue_count

    @property
    def output_packets(self):
        """Gets the output_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The output_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._output_packets

    @output_packets.setter
    def output_packets(self, output_packets):
        """Sets the output_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param output_packets: The output_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._output_packets = output_packets

    @property
    def input_queue_flushes(self):
        """Gets the input_queue_flushes of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_queue_flushes of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_queue_flushes

    @input_queue_flushes.setter
    def input_queue_flushes(self, input_queue_flushes):
        """Sets the input_queue_flushes of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_queue_flushes: The input_queue_flushes of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_queue_flushes = input_queue_flushes

    @property
    def input_queue_count(self):
        """Gets the input_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_queue_count

    @input_queue_count.setter
    def input_queue_count(self, input_queue_count):
        """Sets the input_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_queue_count: The input_queue_count of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_queue_count = input_queue_count

    @property
    def input_queue_drops(self):
        """Gets the input_queue_drops of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_queue_drops of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_queue_drops

    @input_queue_drops.setter
    def input_queue_drops(self, input_queue_drops):
        """Sets the input_queue_drops of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_queue_drops: The input_queue_drops of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_queue_drops = input_queue_drops

    @property
    def output_ratebps(self):
        """Gets the output_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The output_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._output_ratebps

    @output_ratebps.setter
    def output_ratebps(self, output_ratebps):
        """Sets the output_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param output_ratebps: The output_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._output_ratebps = output_ratebps

    @property
    def input_packets(self):
        """Gets the input_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_packets

    @input_packets.setter
    def input_packets(self, input_packets):
        """Sets the input_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_packets: The input_packets of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_packets = input_packets

    @property
    def input_ratebps(self):
        """Gets the input_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The input_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._input_ratebps

    @input_ratebps.setter
    def input_ratebps(self, input_ratebps):
        """Sets the input_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param input_ratebps: The input_ratebps of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._input_ratebps = input_ratebps

    @property
    def output_queue_depth(self):
        """Gets the output_queue_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The output_queue_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._output_queue_depth

    @output_queue_depth.setter
    def output_queue_depth(self, output_queue_depth):
        """Sets the output_queue_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param output_queue_depth: The output_queue_depth of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._output_queue_depth = output_queue_depth

    @property
    def admin_status(self):
        """Gets the admin_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The admin_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: str
        """
        return self._admin_status

    @admin_status.setter
    def admin_status(self, admin_status):
        """Sets the admin_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param admin_status: The admin_status of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: str
        """

        self._admin_status = admin_status

    @property
    def refreshed_at(self):
        """Gets the refreshed_at of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The refreshed_at of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._refreshed_at

    @refreshed_at.setter
    def refreshed_at(self, refreshed_at):
        """Sets the refreshed_at of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param refreshed_at: The refreshed_at of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._refreshed_at = refreshed_at

    @property
    def output_drop(self):
        """Gets the output_drop of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501


        :return: The output_drop of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :rtype: int
        """
        return self._output_drop

    @output_drop.setter
    def output_drop(self, output_drop):
        """Sets the output_drop of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.


        :param output_drop: The output_drop of this PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics.  # noqa: E501
        :type: int
        """

        self._output_drop = output_drop

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
        if not isinstance(other, PathResponseResultResponseEgressVirtualInterfaceInterfaceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other