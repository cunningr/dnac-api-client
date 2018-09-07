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

from dnac_api_client.models.topology_result_response_links import TopologyResultResponseLinks  # noqa: F401,E501
from dnac_api_client.models.topology_result_response_nodes import TopologyResultResponseNodes  # noqa: F401,E501


class TopologyResultResponse(object):
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
        'id': 'str',
        'links': 'list[TopologyResultResponseLinks]',
        'nodes': 'list[TopologyResultResponseNodes]'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, links=None, nodes=None):  # noqa: E501
        """TopologyResultResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._links = None
        self._nodes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if nodes is not None:
            self.nodes = nodes

    @property
    def id(self):
        """Gets the id of this TopologyResultResponse.  # noqa: E501


        :return: The id of this TopologyResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopologyResultResponse.


        :param id: The id of this TopologyResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this TopologyResultResponse.  # noqa: E501


        :return: The links of this TopologyResultResponse.  # noqa: E501
        :rtype: list[TopologyResultResponseLinks]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TopologyResultResponse.


        :param links: The links of this TopologyResultResponse.  # noqa: E501
        :type: list[TopologyResultResponseLinks]
        """

        self._links = links

    @property
    def nodes(self):
        """Gets the nodes of this TopologyResultResponse.  # noqa: E501


        :return: The nodes of this TopologyResultResponse.  # noqa: E501
        :rtype: list[TopologyResultResponseNodes]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this TopologyResultResponse.


        :param nodes: The nodes of this TopologyResultResponse.  # noqa: E501
        :type: list[TopologyResultResponseNodes]
        """

        self._nodes = nodes

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
        if not isinstance(other, TopologyResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
