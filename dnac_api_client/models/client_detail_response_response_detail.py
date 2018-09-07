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

from dnac_api_client.models.client_detail_response_response_detail_health_score import ClientDetailResponseResponseDetailHealthScore  # noqa: F401,E501
from dnac_api_client.models.client_detail_response_response_detail_onboarding import ClientDetailResponseResponseDetailOnboarding  # noqa: F401,E501


class ClientDetailResponseResponseDetail(object):
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
        'ap_group': 'str',
        'auth_type': 'str',
        'avg_rssi': 'str',
        'avg_snr': 'str',
        'channel': 'str',
        'client_connection': 'str',
        'connected_device': 'list[str]',
        'connection_status': 'str',
        'data_rate': 'str',
        'dns_failure': 'str',
        'dns_success': 'str',
        'frequency': 'str',
        'health_score': 'list[ClientDetailResponseResponseDetailHealthScore]',
        'host_ip_v4': 'str',
        'host_ip_v6': 'list[str]',
        'host_mac': 'str',
        'host_name': 'str',
        'host_os': 'str',
        'host_type': 'str',
        'host_version': 'str',
        'id': 'str',
        'issue_count': 'str',
        'last_updated': 'str',
        'location': 'str',
        'onboarding': 'ClientDetailResponseResponseDetailOnboarding',
        'onboarding_time': 'str',
        'port': 'str',
        'rssi': 'str',
        'rx_bytes': 'str',
        'snr': 'str',
        'ssid': 'str',
        'sub_type': 'str',
        'tx_bytes': 'str',
        'user_id': 'str',
        'vlan_id': 'str'
    }

    attribute_map = {
        'ap_group': 'apGroup',
        'auth_type': 'authType',
        'avg_rssi': 'avgRssi',
        'avg_snr': 'avgSnr',
        'channel': 'channel',
        'client_connection': 'clientConnection',
        'connected_device': 'connectedDevice',
        'connection_status': 'connectionStatus',
        'data_rate': 'dataRate',
        'dns_failure': 'dnsFailure',
        'dns_success': 'dnsSuccess',
        'frequency': 'frequency',
        'health_score': 'healthScore',
        'host_ip_v4': 'hostIpV4',
        'host_ip_v6': 'hostIpV6',
        'host_mac': 'hostMac',
        'host_name': 'hostName',
        'host_os': 'hostOs',
        'host_type': 'hostType',
        'host_version': 'hostVersion',
        'id': 'id',
        'issue_count': 'issueCount',
        'last_updated': 'lastUpdated',
        'location': 'location',
        'onboarding': 'onboarding',
        'onboarding_time': 'onboardingTime',
        'port': 'port',
        'rssi': 'rssi',
        'rx_bytes': 'rxBytes',
        'snr': 'snr',
        'ssid': 'ssid',
        'sub_type': 'subType',
        'tx_bytes': 'txBytes',
        'user_id': 'userId',
        'vlan_id': 'vlanId'
    }

    def __init__(self, ap_group=None, auth_type=None, avg_rssi=None, avg_snr=None, channel=None, client_connection=None, connected_device=None, connection_status=None, data_rate=None, dns_failure=None, dns_success=None, frequency=None, health_score=None, host_ip_v4=None, host_ip_v6=None, host_mac=None, host_name=None, host_os=None, host_type=None, host_version=None, id=None, issue_count=None, last_updated=None, location=None, onboarding=None, onboarding_time=None, port=None, rssi=None, rx_bytes=None, snr=None, ssid=None, sub_type=None, tx_bytes=None, user_id=None, vlan_id=None):  # noqa: E501
        """ClientDetailResponseResponseDetail - a model defined in Swagger"""  # noqa: E501

        self._ap_group = None
        self._auth_type = None
        self._avg_rssi = None
        self._avg_snr = None
        self._channel = None
        self._client_connection = None
        self._connected_device = None
        self._connection_status = None
        self._data_rate = None
        self._dns_failure = None
        self._dns_success = None
        self._frequency = None
        self._health_score = None
        self._host_ip_v4 = None
        self._host_ip_v6 = None
        self._host_mac = None
        self._host_name = None
        self._host_os = None
        self._host_type = None
        self._host_version = None
        self._id = None
        self._issue_count = None
        self._last_updated = None
        self._location = None
        self._onboarding = None
        self._onboarding_time = None
        self._port = None
        self._rssi = None
        self._rx_bytes = None
        self._snr = None
        self._ssid = None
        self._sub_type = None
        self._tx_bytes = None
        self._user_id = None
        self._vlan_id = None
        self.discriminator = None

        if ap_group is not None:
            self.ap_group = ap_group
        if auth_type is not None:
            self.auth_type = auth_type
        if avg_rssi is not None:
            self.avg_rssi = avg_rssi
        if avg_snr is not None:
            self.avg_snr = avg_snr
        if channel is not None:
            self.channel = channel
        if client_connection is not None:
            self.client_connection = client_connection
        if connected_device is not None:
            self.connected_device = connected_device
        if connection_status is not None:
            self.connection_status = connection_status
        if data_rate is not None:
            self.data_rate = data_rate
        if dns_failure is not None:
            self.dns_failure = dns_failure
        if dns_success is not None:
            self.dns_success = dns_success
        if frequency is not None:
            self.frequency = frequency
        if health_score is not None:
            self.health_score = health_score
        if host_ip_v4 is not None:
            self.host_ip_v4 = host_ip_v4
        if host_ip_v6 is not None:
            self.host_ip_v6 = host_ip_v6
        if host_mac is not None:
            self.host_mac = host_mac
        if host_name is not None:
            self.host_name = host_name
        if host_os is not None:
            self.host_os = host_os
        if host_type is not None:
            self.host_type = host_type
        if host_version is not None:
            self.host_version = host_version
        if id is not None:
            self.id = id
        if issue_count is not None:
            self.issue_count = issue_count
        if last_updated is not None:
            self.last_updated = last_updated
        if location is not None:
            self.location = location
        if onboarding is not None:
            self.onboarding = onboarding
        if onboarding_time is not None:
            self.onboarding_time = onboarding_time
        if port is not None:
            self.port = port
        if rssi is not None:
            self.rssi = rssi
        if rx_bytes is not None:
            self.rx_bytes = rx_bytes
        if snr is not None:
            self.snr = snr
        if ssid is not None:
            self.ssid = ssid
        if sub_type is not None:
            self.sub_type = sub_type
        if tx_bytes is not None:
            self.tx_bytes = tx_bytes
        if user_id is not None:
            self.user_id = user_id
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def ap_group(self):
        """Gets the ap_group of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The ap_group of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._ap_group

    @ap_group.setter
    def ap_group(self, ap_group):
        """Sets the ap_group of this ClientDetailResponseResponseDetail.


        :param ap_group: The ap_group of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._ap_group = ap_group

    @property
    def auth_type(self):
        """Gets the auth_type of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The auth_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ClientDetailResponseResponseDetail.


        :param auth_type: The auth_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._auth_type = auth_type

    @property
    def avg_rssi(self):
        """Gets the avg_rssi of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The avg_rssi of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._avg_rssi

    @avg_rssi.setter
    def avg_rssi(self, avg_rssi):
        """Sets the avg_rssi of this ClientDetailResponseResponseDetail.


        :param avg_rssi: The avg_rssi of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._avg_rssi = avg_rssi

    @property
    def avg_snr(self):
        """Gets the avg_snr of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The avg_snr of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._avg_snr

    @avg_snr.setter
    def avg_snr(self, avg_snr):
        """Sets the avg_snr of this ClientDetailResponseResponseDetail.


        :param avg_snr: The avg_snr of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._avg_snr = avg_snr

    @property
    def channel(self):
        """Gets the channel of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The channel of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ClientDetailResponseResponseDetail.


        :param channel: The channel of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def client_connection(self):
        """Gets the client_connection of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The client_connection of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._client_connection

    @client_connection.setter
    def client_connection(self, client_connection):
        """Sets the client_connection of this ClientDetailResponseResponseDetail.


        :param client_connection: The client_connection of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._client_connection = client_connection

    @property
    def connected_device(self):
        """Gets the connected_device of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The connected_device of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._connected_device

    @connected_device.setter
    def connected_device(self, connected_device):
        """Sets the connected_device of this ClientDetailResponseResponseDetail.


        :param connected_device: The connected_device of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: list[str]
        """

        self._connected_device = connected_device

    @property
    def connection_status(self):
        """Gets the connection_status of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The connection_status of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this ClientDetailResponseResponseDetail.


        :param connection_status: The connection_status of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._connection_status = connection_status

    @property
    def data_rate(self):
        """Gets the data_rate of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The data_rate of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._data_rate

    @data_rate.setter
    def data_rate(self, data_rate):
        """Sets the data_rate of this ClientDetailResponseResponseDetail.


        :param data_rate: The data_rate of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._data_rate = data_rate

    @property
    def dns_failure(self):
        """Gets the dns_failure of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The dns_failure of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._dns_failure

    @dns_failure.setter
    def dns_failure(self, dns_failure):
        """Sets the dns_failure of this ClientDetailResponseResponseDetail.


        :param dns_failure: The dns_failure of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._dns_failure = dns_failure

    @property
    def dns_success(self):
        """Gets the dns_success of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The dns_success of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._dns_success

    @dns_success.setter
    def dns_success(self, dns_success):
        """Sets the dns_success of this ClientDetailResponseResponseDetail.


        :param dns_success: The dns_success of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._dns_success = dns_success

    @property
    def frequency(self):
        """Gets the frequency of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The frequency of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ClientDetailResponseResponseDetail.


        :param frequency: The frequency of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def health_score(self):
        """Gets the health_score of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The health_score of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: list[ClientDetailResponseResponseDetailHealthScore]
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        """Sets the health_score of this ClientDetailResponseResponseDetail.


        :param health_score: The health_score of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: list[ClientDetailResponseResponseDetailHealthScore]
        """

        self._health_score = health_score

    @property
    def host_ip_v4(self):
        """Gets the host_ip_v4 of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_ip_v4 of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_ip_v4

    @host_ip_v4.setter
    def host_ip_v4(self, host_ip_v4):
        """Sets the host_ip_v4 of this ClientDetailResponseResponseDetail.


        :param host_ip_v4: The host_ip_v4 of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_ip_v4 = host_ip_v4

    @property
    def host_ip_v6(self):
        """Gets the host_ip_v6 of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_ip_v6 of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_ip_v6

    @host_ip_v6.setter
    def host_ip_v6(self, host_ip_v6):
        """Sets the host_ip_v6 of this ClientDetailResponseResponseDetail.


        :param host_ip_v6: The host_ip_v6 of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: list[str]
        """

        self._host_ip_v6 = host_ip_v6

    @property
    def host_mac(self):
        """Gets the host_mac of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_mac of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_mac

    @host_mac.setter
    def host_mac(self, host_mac):
        """Sets the host_mac of this ClientDetailResponseResponseDetail.


        :param host_mac: The host_mac of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_mac = host_mac

    @property
    def host_name(self):
        """Gets the host_name of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_name of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ClientDetailResponseResponseDetail.


        :param host_name: The host_name of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def host_os(self):
        """Gets the host_os of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_os of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_os

    @host_os.setter
    def host_os(self, host_os):
        """Sets the host_os of this ClientDetailResponseResponseDetail.


        :param host_os: The host_os of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_os = host_os

    @property
    def host_type(self):
        """Gets the host_type of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this ClientDetailResponseResponseDetail.


        :param host_type: The host_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_type = host_type

    @property
    def host_version(self):
        """Gets the host_version of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The host_version of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._host_version

    @host_version.setter
    def host_version(self, host_version):
        """Sets the host_version of this ClientDetailResponseResponseDetail.


        :param host_version: The host_version of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._host_version = host_version

    @property
    def id(self):
        """Gets the id of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientDetailResponseResponseDetail.


        :param id: The id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issue_count(self):
        """Gets the issue_count of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The issue_count of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._issue_count

    @issue_count.setter
    def issue_count(self, issue_count):
        """Sets the issue_count of this ClientDetailResponseResponseDetail.


        :param issue_count: The issue_count of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._issue_count = issue_count

    @property
    def last_updated(self):
        """Gets the last_updated of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The last_updated of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ClientDetailResponseResponseDetail.


        :param last_updated: The last_updated of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def location(self):
        """Gets the location of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The location of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClientDetailResponseResponseDetail.


        :param location: The location of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def onboarding(self):
        """Gets the onboarding of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The onboarding of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: ClientDetailResponseResponseDetailOnboarding
        """
        return self._onboarding

    @onboarding.setter
    def onboarding(self, onboarding):
        """Sets the onboarding of this ClientDetailResponseResponseDetail.


        :param onboarding: The onboarding of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: ClientDetailResponseResponseDetailOnboarding
        """

        self._onboarding = onboarding

    @property
    def onboarding_time(self):
        """Gets the onboarding_time of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The onboarding_time of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._onboarding_time

    @onboarding_time.setter
    def onboarding_time(self, onboarding_time):
        """Sets the onboarding_time of this ClientDetailResponseResponseDetail.


        :param onboarding_time: The onboarding_time of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._onboarding_time = onboarding_time

    @property
    def port(self):
        """Gets the port of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The port of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ClientDetailResponseResponseDetail.


        :param port: The port of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def rssi(self):
        """Gets the rssi of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The rssi of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """Sets the rssi of this ClientDetailResponseResponseDetail.


        :param rssi: The rssi of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._rssi = rssi

    @property
    def rx_bytes(self):
        """Gets the rx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The rx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._rx_bytes

    @rx_bytes.setter
    def rx_bytes(self, rx_bytes):
        """Sets the rx_bytes of this ClientDetailResponseResponseDetail.


        :param rx_bytes: The rx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._rx_bytes = rx_bytes

    @property
    def snr(self):
        """Gets the snr of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The snr of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this ClientDetailResponseResponseDetail.


        :param snr: The snr of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._snr = snr

    @property
    def ssid(self):
        """Gets the ssid of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The ssid of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this ClientDetailResponseResponseDetail.


        :param ssid: The ssid of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def sub_type(self):
        """Gets the sub_type of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The sub_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this ClientDetailResponseResponseDetail.


        :param sub_type: The sub_type of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def tx_bytes(self):
        """Gets the tx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The tx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._tx_bytes

    @tx_bytes.setter
    def tx_bytes(self, tx_bytes):
        """Sets the tx_bytes of this ClientDetailResponseResponseDetail.


        :param tx_bytes: The tx_bytes of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._tx_bytes = tx_bytes

    @property
    def user_id(self):
        """Gets the user_id of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The user_id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ClientDetailResponseResponseDetail.


        :param user_id: The user_id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this ClientDetailResponseResponseDetail.  # noqa: E501


        :return: The vlan_id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this ClientDetailResponseResponseDetail.


        :param vlan_id: The vlan_id of this ClientDetailResponseResponseDetail.  # noqa: E501
        :type: str
        """

        self._vlan_id = vlan_id

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
        if not isinstance(other, ClientDetailResponseResponseDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other