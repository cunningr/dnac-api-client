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

from dnac_api_client.models.template_deployment_status_dto_devices import TemplateDeploymentStatusDTODevices  # noqa: F401,E501


class TemplateDeploymentStatusDTO(object):
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
        'deployment_id': 'str',
        'deployment_name': 'str',
        'devices': 'list[TemplateDeploymentStatusDTODevices]',
        'duration': 'str',
        'end_time': 'str',
        'project_name': 'str',
        'start_time': 'str',
        'status': 'str',
        'template_name': 'str',
        'template_version': 'str'
    }

    attribute_map = {
        'deployment_id': 'deploymentId',
        'deployment_name': 'deploymentName',
        'devices': 'devices',
        'duration': 'duration',
        'end_time': 'endTime',
        'project_name': 'projectName',
        'start_time': 'startTime',
        'status': 'status',
        'template_name': 'templateName',
        'template_version': 'templateVersion'
    }

    def __init__(self, deployment_id=None, deployment_name=None, devices=None, duration=None, end_time=None, project_name=None, start_time=None, status=None, template_name=None, template_version=None):  # noqa: E501
        """TemplateDeploymentStatusDTO - a model defined in Swagger"""  # noqa: E501

        self._deployment_id = None
        self._deployment_name = None
        self._devices = None
        self._duration = None
        self._end_time = None
        self._project_name = None
        self._start_time = None
        self._status = None
        self._template_name = None
        self._template_version = None
        self.discriminator = None

        if deployment_id is not None:
            self.deployment_id = deployment_id
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if devices is not None:
            self.devices = devices
        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if project_name is not None:
            self.project_name = project_name
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if template_name is not None:
            self.template_name = template_name
        if template_version is not None:
            self.template_version = template_version

    @property
    def deployment_id(self):
        """Gets the deployment_id of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The deployment_id of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this TemplateDeploymentStatusDTO.


        :param deployment_id: The deployment_id of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._deployment_id = deployment_id

    @property
    def deployment_name(self):
        """Gets the deployment_name of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The deployment_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this TemplateDeploymentStatusDTO.


        :param deployment_name: The deployment_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._deployment_name = deployment_name

    @property
    def devices(self):
        """Gets the devices of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The devices of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: list[TemplateDeploymentStatusDTODevices]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this TemplateDeploymentStatusDTO.


        :param devices: The devices of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: list[TemplateDeploymentStatusDTODevices]
        """

        self._devices = devices

    @property
    def duration(self):
        """Gets the duration of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The duration of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TemplateDeploymentStatusDTO.


        :param duration: The duration of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The end_time of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TemplateDeploymentStatusDTO.


        :param end_time: The end_time of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def project_name(self):
        """Gets the project_name of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The project_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TemplateDeploymentStatusDTO.


        :param project_name: The project_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def start_time(self):
        """Gets the start_time of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The start_time of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TemplateDeploymentStatusDTO.


        :param start_time: The start_time of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The status of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplateDeploymentStatusDTO.


        :param status: The status of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def template_name(self):
        """Gets the template_name of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The template_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateDeploymentStatusDTO.


        :param template_name: The template_name of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def template_version(self):
        """Gets the template_version of this TemplateDeploymentStatusDTO.  # noqa: E501


        :return: The template_version of this TemplateDeploymentStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._template_version

    @template_version.setter
    def template_version(self, template_version):
        """Sets the template_version of this TemplateDeploymentStatusDTO.


        :param template_version: The template_version of this TemplateDeploymentStatusDTO.  # noqa: E501
        :type: str
        """

        self._template_version = template_version

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
        if not isinstance(other, TemplateDeploymentStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
