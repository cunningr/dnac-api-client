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


class NetworkDeviceListResultResponse(object):
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
        'ap_manager_interface_ip': 'str',
        'associated_wlc_ip': 'str',
        'boot_date_time': 'str',
        'collection_interval': 'str',
        'collection_status': 'str',
        'error_code': 'str',
        'error_description': 'str',
        'family': 'str',
        'hostname': 'str',
        'id': 'str',
        'instance_tenant_id': 'str',
        'instance_uuid': 'str',
        'interface_count': 'str',
        'inventory_status_detail': 'str',
        'last_update_time': 'str',
        'last_updated': 'str',
        'line_card_count': 'str',
        'line_card_id': 'str',
        'location': 'str',
        'location_name': 'str',
        'mac_address': 'str',
        'management_ip_address': 'str',
        'memory_size': 'str',
        'platform_id': 'str',
        'reachability_failure_reason': 'str',
        'reachability_status': 'str',
        'role': 'str',
        'role_source': 'str',
        'serial_number': 'str',
        'series': 'str',
        'snmp_contact': 'str',
        'snmp_location': 'str',
        'software_type': 'str',
        'software_version': 'str',
        'tag_count': 'str',
        'tunnel_udp_port': 'str',
        'type': 'str',
        'up_time': 'str',
        'waas_device_mode': 'str'
    }

    attribute_map = {
        'ap_manager_interface_ip': 'apManagerInterfaceIp',
        'associated_wlc_ip': 'associatedWlcIp',
        'boot_date_time': 'bootDateTime',
        'collection_interval': 'collectionInterval',
        'collection_status': 'collectionStatus',
        'error_code': 'errorCode',
        'error_description': 'errorDescription',
        'family': 'family',
        'hostname': 'hostname',
        'id': 'id',
        'instance_tenant_id': 'instanceTenantId',
        'instance_uuid': 'instanceUuid',
        'interface_count': 'interfaceCount',
        'inventory_status_detail': 'inventoryStatusDetail',
        'last_update_time': 'lastUpdateTime',
        'last_updated': 'lastUpdated',
        'line_card_count': 'lineCardCount',
        'line_card_id': 'lineCardId',
        'location': 'location',
        'location_name': 'locationName',
        'mac_address': 'macAddress',
        'management_ip_address': 'managementIpAddress',
        'memory_size': 'memorySize',
        'platform_id': 'platformId',
        'reachability_failure_reason': 'reachabilityFailureReason',
        'reachability_status': 'reachabilityStatus',
        'role': 'role',
        'role_source': 'roleSource',
        'serial_number': 'serialNumber',
        'series': 'series',
        'snmp_contact': 'snmpContact',
        'snmp_location': 'snmpLocation',
        'software_type': 'softwareType',
        'software_version': 'softwareVersion',
        'tag_count': 'tagCount',
        'tunnel_udp_port': 'tunnelUdpPort',
        'type': 'type',
        'up_time': 'upTime',
        'waas_device_mode': 'waasDeviceMode'
    }

    def __init__(self, ap_manager_interface_ip=None, associated_wlc_ip=None, boot_date_time=None, collection_interval=None, collection_status=None, error_code=None, error_description=None, family=None, hostname=None, id=None, instance_tenant_id=None, instance_uuid=None, interface_count=None, inventory_status_detail=None, last_update_time=None, last_updated=None, line_card_count=None, line_card_id=None, location=None, location_name=None, mac_address=None, management_ip_address=None, memory_size=None, platform_id=None, reachability_failure_reason=None, reachability_status=None, role=None, role_source=None, serial_number=None, series=None, snmp_contact=None, snmp_location=None, software_type=None, software_version=None, tag_count=None, tunnel_udp_port=None, type=None, up_time=None, waas_device_mode=None):  # noqa: E501
        """NetworkDeviceListResultResponse - a model defined in Swagger"""  # noqa: E501

        self._ap_manager_interface_ip = None
        self._associated_wlc_ip = None
        self._boot_date_time = None
        self._collection_interval = None
        self._collection_status = None
        self._error_code = None
        self._error_description = None
        self._family = None
        self._hostname = None
        self._id = None
        self._instance_tenant_id = None
        self._instance_uuid = None
        self._interface_count = None
        self._inventory_status_detail = None
        self._last_update_time = None
        self._last_updated = None
        self._line_card_count = None
        self._line_card_id = None
        self._location = None
        self._location_name = None
        self._mac_address = None
        self._management_ip_address = None
        self._memory_size = None
        self._platform_id = None
        self._reachability_failure_reason = None
        self._reachability_status = None
        self._role = None
        self._role_source = None
        self._serial_number = None
        self._series = None
        self._snmp_contact = None
        self._snmp_location = None
        self._software_type = None
        self._software_version = None
        self._tag_count = None
        self._tunnel_udp_port = None
        self._type = None
        self._up_time = None
        self._waas_device_mode = None
        self.discriminator = None

        if ap_manager_interface_ip is not None:
            self.ap_manager_interface_ip = ap_manager_interface_ip
        if associated_wlc_ip is not None:
            self.associated_wlc_ip = associated_wlc_ip
        if boot_date_time is not None:
            self.boot_date_time = boot_date_time
        if collection_interval is not None:
            self.collection_interval = collection_interval
        if collection_status is not None:
            self.collection_status = collection_status
        if error_code is not None:
            self.error_code = error_code
        if error_description is not None:
            self.error_description = error_description
        if family is not None:
            self.family = family
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if instance_tenant_id is not None:
            self.instance_tenant_id = instance_tenant_id
        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if interface_count is not None:
            self.interface_count = interface_count
        if inventory_status_detail is not None:
            self.inventory_status_detail = inventory_status_detail
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if last_updated is not None:
            self.last_updated = last_updated
        if line_card_count is not None:
            self.line_card_count = line_card_count
        if line_card_id is not None:
            self.line_card_id = line_card_id
        if location is not None:
            self.location = location
        if location_name is not None:
            self.location_name = location_name
        if mac_address is not None:
            self.mac_address = mac_address
        if management_ip_address is not None:
            self.management_ip_address = management_ip_address
        if memory_size is not None:
            self.memory_size = memory_size
        if platform_id is not None:
            self.platform_id = platform_id
        if reachability_failure_reason is not None:
            self.reachability_failure_reason = reachability_failure_reason
        if reachability_status is not None:
            self.reachability_status = reachability_status
        if role is not None:
            self.role = role
        if role_source is not None:
            self.role_source = role_source
        if serial_number is not None:
            self.serial_number = serial_number
        if series is not None:
            self.series = series
        if snmp_contact is not None:
            self.snmp_contact = snmp_contact
        if snmp_location is not None:
            self.snmp_location = snmp_location
        if software_type is not None:
            self.software_type = software_type
        if software_version is not None:
            self.software_version = software_version
        if tag_count is not None:
            self.tag_count = tag_count
        if tunnel_udp_port is not None:
            self.tunnel_udp_port = tunnel_udp_port
        if type is not None:
            self.type = type
        if up_time is not None:
            self.up_time = up_time
        if waas_device_mode is not None:
            self.waas_device_mode = waas_device_mode

    @property
    def ap_manager_interface_ip(self):
        """Gets the ap_manager_interface_ip of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The ap_manager_interface_ip of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._ap_manager_interface_ip

    @ap_manager_interface_ip.setter
    def ap_manager_interface_ip(self, ap_manager_interface_ip):
        """Sets the ap_manager_interface_ip of this NetworkDeviceListResultResponse.


        :param ap_manager_interface_ip: The ap_manager_interface_ip of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._ap_manager_interface_ip = ap_manager_interface_ip

    @property
    def associated_wlc_ip(self):
        """Gets the associated_wlc_ip of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The associated_wlc_ip of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._associated_wlc_ip

    @associated_wlc_ip.setter
    def associated_wlc_ip(self, associated_wlc_ip):
        """Sets the associated_wlc_ip of this NetworkDeviceListResultResponse.


        :param associated_wlc_ip: The associated_wlc_ip of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._associated_wlc_ip = associated_wlc_ip

    @property
    def boot_date_time(self):
        """Gets the boot_date_time of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The boot_date_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._boot_date_time

    @boot_date_time.setter
    def boot_date_time(self, boot_date_time):
        """Sets the boot_date_time of this NetworkDeviceListResultResponse.


        :param boot_date_time: The boot_date_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._boot_date_time = boot_date_time

    @property
    def collection_interval(self):
        """Gets the collection_interval of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The collection_interval of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._collection_interval

    @collection_interval.setter
    def collection_interval(self, collection_interval):
        """Sets the collection_interval of this NetworkDeviceListResultResponse.


        :param collection_interval: The collection_interval of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._collection_interval = collection_interval

    @property
    def collection_status(self):
        """Gets the collection_status of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The collection_status of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._collection_status

    @collection_status.setter
    def collection_status(self, collection_status):
        """Sets the collection_status of this NetworkDeviceListResultResponse.


        :param collection_status: The collection_status of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._collection_status = collection_status

    @property
    def error_code(self):
        """Gets the error_code of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The error_code of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this NetworkDeviceListResultResponse.


        :param error_code: The error_code of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_description(self):
        """Gets the error_description of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The error_description of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this NetworkDeviceListResultResponse.


        :param error_description: The error_description of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def family(self):
        """Gets the family of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The family of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this NetworkDeviceListResultResponse.


        :param family: The family of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def hostname(self):
        """Gets the hostname of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The hostname of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this NetworkDeviceListResultResponse.


        :param hostname: The hostname of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The id of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkDeviceListResultResponse.


        :param id: The id of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance_tenant_id(self):
        """Gets the instance_tenant_id of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The instance_tenant_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_tenant_id

    @instance_tenant_id.setter
    def instance_tenant_id(self, instance_tenant_id):
        """Sets the instance_tenant_id of this NetworkDeviceListResultResponse.


        :param instance_tenant_id: The instance_tenant_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._instance_tenant_id = instance_tenant_id

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The instance_uuid of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this NetworkDeviceListResultResponse.


        :param instance_uuid: The instance_uuid of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._instance_uuid = instance_uuid

    @property
    def interface_count(self):
        """Gets the interface_count of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The interface_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._interface_count

    @interface_count.setter
    def interface_count(self, interface_count):
        """Sets the interface_count of this NetworkDeviceListResultResponse.


        :param interface_count: The interface_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._interface_count = interface_count

    @property
    def inventory_status_detail(self):
        """Gets the inventory_status_detail of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The inventory_status_detail of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._inventory_status_detail

    @inventory_status_detail.setter
    def inventory_status_detail(self, inventory_status_detail):
        """Sets the inventory_status_detail of this NetworkDeviceListResultResponse.


        :param inventory_status_detail: The inventory_status_detail of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._inventory_status_detail = inventory_status_detail

    @property
    def last_update_time(self):
        """Gets the last_update_time of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The last_update_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this NetworkDeviceListResultResponse.


        :param last_update_time: The last_update_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._last_update_time = last_update_time

    @property
    def last_updated(self):
        """Gets the last_updated of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The last_updated of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this NetworkDeviceListResultResponse.


        :param last_updated: The last_updated of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def line_card_count(self):
        """Gets the line_card_count of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The line_card_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._line_card_count

    @line_card_count.setter
    def line_card_count(self, line_card_count):
        """Sets the line_card_count of this NetworkDeviceListResultResponse.


        :param line_card_count: The line_card_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._line_card_count = line_card_count

    @property
    def line_card_id(self):
        """Gets the line_card_id of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The line_card_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._line_card_id

    @line_card_id.setter
    def line_card_id(self, line_card_id):
        """Sets the line_card_id of this NetworkDeviceListResultResponse.


        :param line_card_id: The line_card_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._line_card_id = line_card_id

    @property
    def location(self):
        """Gets the location of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The location of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this NetworkDeviceListResultResponse.


        :param location: The location of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def location_name(self):
        """Gets the location_name of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The location_name of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this NetworkDeviceListResultResponse.


        :param location_name: The location_name of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def mac_address(self):
        """Gets the mac_address of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The mac_address of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetworkDeviceListResultResponse.


        :param mac_address: The mac_address of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def management_ip_address(self):
        """Gets the management_ip_address of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The management_ip_address of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._management_ip_address

    @management_ip_address.setter
    def management_ip_address(self, management_ip_address):
        """Sets the management_ip_address of this NetworkDeviceListResultResponse.


        :param management_ip_address: The management_ip_address of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._management_ip_address = management_ip_address

    @property
    def memory_size(self):
        """Gets the memory_size of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The memory_size of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this NetworkDeviceListResultResponse.


        :param memory_size: The memory_size of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._memory_size = memory_size

    @property
    def platform_id(self):
        """Gets the platform_id of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The platform_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this NetworkDeviceListResultResponse.


        :param platform_id: The platform_id of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._platform_id = platform_id

    @property
    def reachability_failure_reason(self):
        """Gets the reachability_failure_reason of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The reachability_failure_reason of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._reachability_failure_reason

    @reachability_failure_reason.setter
    def reachability_failure_reason(self, reachability_failure_reason):
        """Sets the reachability_failure_reason of this NetworkDeviceListResultResponse.


        :param reachability_failure_reason: The reachability_failure_reason of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._reachability_failure_reason = reachability_failure_reason

    @property
    def reachability_status(self):
        """Gets the reachability_status of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The reachability_status of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._reachability_status

    @reachability_status.setter
    def reachability_status(self, reachability_status):
        """Sets the reachability_status of this NetworkDeviceListResultResponse.


        :param reachability_status: The reachability_status of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._reachability_status = reachability_status

    @property
    def role(self):
        """Gets the role of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The role of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NetworkDeviceListResultResponse.


        :param role: The role of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def role_source(self):
        """Gets the role_source of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The role_source of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._role_source

    @role_source.setter
    def role_source(self, role_source):
        """Sets the role_source of this NetworkDeviceListResultResponse.


        :param role_source: The role_source of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._role_source = role_source

    @property
    def serial_number(self):
        """Gets the serial_number of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The serial_number of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NetworkDeviceListResultResponse.


        :param serial_number: The serial_number of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def series(self):
        """Gets the series of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The series of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this NetworkDeviceListResultResponse.


        :param series: The series of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._series = series

    @property
    def snmp_contact(self):
        """Gets the snmp_contact of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The snmp_contact of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._snmp_contact

    @snmp_contact.setter
    def snmp_contact(self, snmp_contact):
        """Sets the snmp_contact of this NetworkDeviceListResultResponse.


        :param snmp_contact: The snmp_contact of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._snmp_contact = snmp_contact

    @property
    def snmp_location(self):
        """Gets the snmp_location of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The snmp_location of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._snmp_location

    @snmp_location.setter
    def snmp_location(self, snmp_location):
        """Sets the snmp_location of this NetworkDeviceListResultResponse.


        :param snmp_location: The snmp_location of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._snmp_location = snmp_location

    @property
    def software_type(self):
        """Gets the software_type of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The software_type of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._software_type

    @software_type.setter
    def software_type(self, software_type):
        """Sets the software_type of this NetworkDeviceListResultResponse.


        :param software_type: The software_type of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._software_type = software_type

    @property
    def software_version(self):
        """Gets the software_version of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The software_version of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this NetworkDeviceListResultResponse.


        :param software_version: The software_version of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def tag_count(self):
        """Gets the tag_count of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The tag_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag_count

    @tag_count.setter
    def tag_count(self, tag_count):
        """Sets the tag_count of this NetworkDeviceListResultResponse.


        :param tag_count: The tag_count of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._tag_count = tag_count

    @property
    def tunnel_udp_port(self):
        """Gets the tunnel_udp_port of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The tunnel_udp_port of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_udp_port

    @tunnel_udp_port.setter
    def tunnel_udp_port(self, tunnel_udp_port):
        """Sets the tunnel_udp_port of this NetworkDeviceListResultResponse.


        :param tunnel_udp_port: The tunnel_udp_port of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._tunnel_udp_port = tunnel_udp_port

    @property
    def type(self):
        """Gets the type of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The type of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkDeviceListResultResponse.


        :param type: The type of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def up_time(self):
        """Gets the up_time of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The up_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._up_time

    @up_time.setter
    def up_time(self, up_time):
        """Sets the up_time of this NetworkDeviceListResultResponse.


        :param up_time: The up_time of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._up_time = up_time

    @property
    def waas_device_mode(self):
        """Gets the waas_device_mode of this NetworkDeviceListResultResponse.  # noqa: E501


        :return: The waas_device_mode of this NetworkDeviceListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._waas_device_mode

    @waas_device_mode.setter
    def waas_device_mode(self, waas_device_mode):
        """Sets the waas_device_mode of this NetworkDeviceListResultResponse.


        :param waas_device_mode: The waas_device_mode of this NetworkDeviceListResultResponse.  # noqa: E501
        :type: str
        """

        self._waas_device_mode = waas_device_mode

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
        if not isinstance(other, NetworkDeviceListResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other