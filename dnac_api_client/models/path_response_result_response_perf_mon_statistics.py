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


class PathResponseResultResponsePerfMonStatistics(object):
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
        'byte_rate': 'int',
        'dest_ip_address': 'str',
        'dest_port': 'str',
        'input_interface': 'str',
        'ipv4_dscp': 'str',
        'ipv4_ttl': 'int',
        'output_interface': 'str',
        'packet_bytes': 'int',
        'packet_count': 'int',
        'packet_loss': 'int',
        'packet_loss_percentage': 'float',
        'protocol': 'str',
        'refreshed_at': 'int',
        'rtp_jitter_max': 'int',
        'rtp_jitter_mean': 'int',
        'rtp_jitter_min': 'int',
        'source_ip_address': 'str',
        'source_port': 'str'
    }

    attribute_map = {
        'byte_rate': 'byteRate',
        'dest_ip_address': 'destIpAddress',
        'dest_port': 'destPort',
        'input_interface': 'inputInterface',
        'ipv4_dscp': 'ipv4DSCP',
        'ipv4_ttl': 'ipv4TTL',
        'output_interface': 'outputInterface',
        'packet_bytes': 'packetBytes',
        'packet_count': 'packetCount',
        'packet_loss': 'packetLoss',
        'packet_loss_percentage': 'packetLossPercentage',
        'protocol': 'protocol',
        'refreshed_at': 'refreshedAt',
        'rtp_jitter_max': 'rtpJitterMax',
        'rtp_jitter_mean': 'rtpJitterMean',
        'rtp_jitter_min': 'rtpJitterMin',
        'source_ip_address': 'sourceIpAddress',
        'source_port': 'sourcePort'
    }

    def __init__(self, byte_rate=None, dest_ip_address=None, dest_port=None, input_interface=None, ipv4_dscp=None, ipv4_ttl=None, output_interface=None, packet_bytes=None, packet_count=None, packet_loss=None, packet_loss_percentage=None, protocol=None, refreshed_at=None, rtp_jitter_max=None, rtp_jitter_mean=None, rtp_jitter_min=None, source_ip_address=None, source_port=None):  # noqa: E501
        """PathResponseResultResponsePerfMonStatistics - a model defined in Swagger"""  # noqa: E501

        self._byte_rate = None
        self._dest_ip_address = None
        self._dest_port = None
        self._input_interface = None
        self._ipv4_dscp = None
        self._ipv4_ttl = None
        self._output_interface = None
        self._packet_bytes = None
        self._packet_count = None
        self._packet_loss = None
        self._packet_loss_percentage = None
        self._protocol = None
        self._refreshed_at = None
        self._rtp_jitter_max = None
        self._rtp_jitter_mean = None
        self._rtp_jitter_min = None
        self._source_ip_address = None
        self._source_port = None
        self.discriminator = None

        if byte_rate is not None:
            self.byte_rate = byte_rate
        if dest_ip_address is not None:
            self.dest_ip_address = dest_ip_address
        if dest_port is not None:
            self.dest_port = dest_port
        if input_interface is not None:
            self.input_interface = input_interface
        if ipv4_dscp is not None:
            self.ipv4_dscp = ipv4_dscp
        if ipv4_ttl is not None:
            self.ipv4_ttl = ipv4_ttl
        if output_interface is not None:
            self.output_interface = output_interface
        if packet_bytes is not None:
            self.packet_bytes = packet_bytes
        if packet_count is not None:
            self.packet_count = packet_count
        if packet_loss is not None:
            self.packet_loss = packet_loss
        if packet_loss_percentage is not None:
            self.packet_loss_percentage = packet_loss_percentage
        if protocol is not None:
            self.protocol = protocol
        if refreshed_at is not None:
            self.refreshed_at = refreshed_at
        if rtp_jitter_max is not None:
            self.rtp_jitter_max = rtp_jitter_max
        if rtp_jitter_mean is not None:
            self.rtp_jitter_mean = rtp_jitter_mean
        if rtp_jitter_min is not None:
            self.rtp_jitter_min = rtp_jitter_min
        if source_ip_address is not None:
            self.source_ip_address = source_ip_address
        if source_port is not None:
            self.source_port = source_port

    @property
    def byte_rate(self):
        """Gets the byte_rate of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The byte_rate of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._byte_rate

    @byte_rate.setter
    def byte_rate(self, byte_rate):
        """Sets the byte_rate of this PathResponseResultResponsePerfMonStatistics.


        :param byte_rate: The byte_rate of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._byte_rate = byte_rate

    @property
    def dest_ip_address(self):
        """Gets the dest_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The dest_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._dest_ip_address

    @dest_ip_address.setter
    def dest_ip_address(self, dest_ip_address):
        """Sets the dest_ip_address of this PathResponseResultResponsePerfMonStatistics.


        :param dest_ip_address: The dest_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._dest_ip_address = dest_ip_address

    @property
    def dest_port(self):
        """Gets the dest_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The dest_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this PathResponseResultResponsePerfMonStatistics.


        :param dest_port: The dest_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._dest_port = dest_port

    @property
    def input_interface(self):
        """Gets the input_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The input_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._input_interface

    @input_interface.setter
    def input_interface(self, input_interface):
        """Sets the input_interface of this PathResponseResultResponsePerfMonStatistics.


        :param input_interface: The input_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._input_interface = input_interface

    @property
    def ipv4_dscp(self):
        """Gets the ipv4_dscp of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The ipv4_dscp of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_dscp

    @ipv4_dscp.setter
    def ipv4_dscp(self, ipv4_dscp):
        """Sets the ipv4_dscp of this PathResponseResultResponsePerfMonStatistics.


        :param ipv4_dscp: The ipv4_dscp of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._ipv4_dscp = ipv4_dscp

    @property
    def ipv4_ttl(self):
        """Gets the ipv4_ttl of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The ipv4_ttl of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._ipv4_ttl

    @ipv4_ttl.setter
    def ipv4_ttl(self, ipv4_ttl):
        """Sets the ipv4_ttl of this PathResponseResultResponsePerfMonStatistics.


        :param ipv4_ttl: The ipv4_ttl of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._ipv4_ttl = ipv4_ttl

    @property
    def output_interface(self):
        """Gets the output_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The output_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._output_interface

    @output_interface.setter
    def output_interface(self, output_interface):
        """Sets the output_interface of this PathResponseResultResponsePerfMonStatistics.


        :param output_interface: The output_interface of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._output_interface = output_interface

    @property
    def packet_bytes(self):
        """Gets the packet_bytes of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The packet_bytes of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._packet_bytes

    @packet_bytes.setter
    def packet_bytes(self, packet_bytes):
        """Sets the packet_bytes of this PathResponseResultResponsePerfMonStatistics.


        :param packet_bytes: The packet_bytes of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._packet_bytes = packet_bytes

    @property
    def packet_count(self):
        """Gets the packet_count of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The packet_count of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._packet_count

    @packet_count.setter
    def packet_count(self, packet_count):
        """Sets the packet_count of this PathResponseResultResponsePerfMonStatistics.


        :param packet_count: The packet_count of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._packet_count = packet_count

    @property
    def packet_loss(self):
        """Gets the packet_loss of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The packet_loss of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._packet_loss

    @packet_loss.setter
    def packet_loss(self, packet_loss):
        """Sets the packet_loss of this PathResponseResultResponsePerfMonStatistics.


        :param packet_loss: The packet_loss of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._packet_loss = packet_loss

    @property
    def packet_loss_percentage(self):
        """Gets the packet_loss_percentage of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The packet_loss_percentage of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: float
        """
        return self._packet_loss_percentage

    @packet_loss_percentage.setter
    def packet_loss_percentage(self, packet_loss_percentage):
        """Sets the packet_loss_percentage of this PathResponseResultResponsePerfMonStatistics.


        :param packet_loss_percentage: The packet_loss_percentage of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: float
        """

        self._packet_loss_percentage = packet_loss_percentage

    @property
    def protocol(self):
        """Gets the protocol of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The protocol of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PathResponseResultResponsePerfMonStatistics.


        :param protocol: The protocol of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def refreshed_at(self):
        """Gets the refreshed_at of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The refreshed_at of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._refreshed_at

    @refreshed_at.setter
    def refreshed_at(self, refreshed_at):
        """Sets the refreshed_at of this PathResponseResultResponsePerfMonStatistics.


        :param refreshed_at: The refreshed_at of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._refreshed_at = refreshed_at

    @property
    def rtp_jitter_max(self):
        """Gets the rtp_jitter_max of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The rtp_jitter_max of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._rtp_jitter_max

    @rtp_jitter_max.setter
    def rtp_jitter_max(self, rtp_jitter_max):
        """Sets the rtp_jitter_max of this PathResponseResultResponsePerfMonStatistics.


        :param rtp_jitter_max: The rtp_jitter_max of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._rtp_jitter_max = rtp_jitter_max

    @property
    def rtp_jitter_mean(self):
        """Gets the rtp_jitter_mean of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The rtp_jitter_mean of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._rtp_jitter_mean

    @rtp_jitter_mean.setter
    def rtp_jitter_mean(self, rtp_jitter_mean):
        """Sets the rtp_jitter_mean of this PathResponseResultResponsePerfMonStatistics.


        :param rtp_jitter_mean: The rtp_jitter_mean of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._rtp_jitter_mean = rtp_jitter_mean

    @property
    def rtp_jitter_min(self):
        """Gets the rtp_jitter_min of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The rtp_jitter_min of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: int
        """
        return self._rtp_jitter_min

    @rtp_jitter_min.setter
    def rtp_jitter_min(self, rtp_jitter_min):
        """Sets the rtp_jitter_min of this PathResponseResultResponsePerfMonStatistics.


        :param rtp_jitter_min: The rtp_jitter_min of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: int
        """

        self._rtp_jitter_min = rtp_jitter_min

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The source_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this PathResponseResultResponsePerfMonStatistics.


        :param source_ip_address: The source_ip_address of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501


        :return: The source_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this PathResponseResultResponsePerfMonStatistics.


        :param source_port: The source_port of this PathResponseResultResponsePerfMonStatistics.  # noqa: E501
        :type: str
        """

        self._source_port = source_port

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
        if not isinstance(other, PathResponseResultResponsePerfMonStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
