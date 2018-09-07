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


class HTTPWriteCredentialDTO(object):
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
        'comments': 'str',
        'credential_type': 'str',
        'description': 'str',
        'id': 'str',
        'instance_tenant_id': 'str',
        'instance_uuid': 'str',
        'password': 'str',
        'port': 'int',
        'secure': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'credential_type': 'credentialType',
        'description': 'description',
        'id': 'id',
        'instance_tenant_id': 'instanceTenantId',
        'instance_uuid': 'instanceUuid',
        'password': 'password',
        'port': 'port',
        'secure': 'secure',
        'username': 'username'
    }

    def __init__(self, comments=None, credential_type=None, description=None, id=None, instance_tenant_id=None, instance_uuid=None, password=None, port=None, secure=None, username=None):  # noqa: E501
        """HTTPWriteCredentialDTO - a model defined in Swagger"""  # noqa: E501

        self._comments = None
        self._credential_type = None
        self._description = None
        self._id = None
        self._instance_tenant_id = None
        self._instance_uuid = None
        self._password = None
        self._port = None
        self._secure = None
        self._username = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if credential_type is not None:
            self.credential_type = credential_type
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if instance_tenant_id is not None:
            self.instance_tenant_id = instance_tenant_id
        if instance_uuid is not None:
            self.instance_uuid = instance_uuid
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if secure is not None:
            self.secure = secure
        if username is not None:
            self.username = username

    @property
    def comments(self):
        """Gets the comments of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The comments of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this HTTPWriteCredentialDTO.


        :param comments: The comments of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def credential_type(self):
        """Gets the credential_type of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The credential_type of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """Sets the credential_type of this HTTPWriteCredentialDTO.


        :param credential_type: The credential_type of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["GLOBAL", "APP"]  # noqa: E501
        if credential_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credential_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credential_type, allowed_values)
            )

        self._credential_type = credential_type

    @property
    def description(self):
        """Gets the description of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The description of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HTTPWriteCredentialDTO.


        :param description: The description of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The id of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HTTPWriteCredentialDTO.


        :param id: The id of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance_tenant_id(self):
        """Gets the instance_tenant_id of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The instance_tenant_id of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._instance_tenant_id

    @instance_tenant_id.setter
    def instance_tenant_id(self, instance_tenant_id):
        """Sets the instance_tenant_id of this HTTPWriteCredentialDTO.


        :param instance_tenant_id: The instance_tenant_id of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._instance_tenant_id = instance_tenant_id

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The instance_uuid of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this HTTPWriteCredentialDTO.


        :param instance_uuid: The instance_uuid of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._instance_uuid = instance_uuid

    @property
    def password(self):
        """Gets the password of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The password of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this HTTPWriteCredentialDTO.


        :param password: The password of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The port of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HTTPWriteCredentialDTO.


        :param port: The port of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def secure(self):
        """Gets the secure of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The secure of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """Sets the secure of this HTTPWriteCredentialDTO.


        :param secure: The secure of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: bool
        """

        self._secure = secure

    @property
    def username(self):
        """Gets the username of this HTTPWriteCredentialDTO.  # noqa: E501


        :return: The username of this HTTPWriteCredentialDTO.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this HTTPWriteCredentialDTO.


        :param username: The username of this HTTPWriteCredentialDTO.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, HTTPWriteCredentialDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
