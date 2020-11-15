# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CollisionObj(object):
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
        'embedded': 'object',
        'front': 'CollisionObjFront',
        'id': 'str',
        'lateral': 'CollisionObjFront',
        'pedestrian': 'bool',
        'rear': 'CollisionObjFront',
        'roll_over': 'bool',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'embedded': '_embedded',
        'front': 'front',
        'id': 'id',
        'lateral': 'lateral',
        'pedestrian': 'pedestrian',
        'rear': 'rear',
        'roll_over': 'rollOver',
        'updated_at': 'updatedAt'
    }

    def __init__(self, embedded=None, front=None, id=None, lateral=None, pedestrian=None, rear=None, roll_over=None, updated_at=None):  # noqa: E501
        """CollisionObj - a model defined in Swagger"""  # noqa: E501

        self._embedded = None
        self._front = None
        self._id = None
        self._lateral = None
        self._pedestrian = None
        self._rear = None
        self._roll_over = None
        self._updated_at = None
        self.discriminator = None

        if embedded is not None:
            self.embedded = embedded
        if front is not None:
            self.front = front
        if id is not None:
            self.id = id
        if lateral is not None:
            self.lateral = lateral
        if pedestrian is not None:
            self.pedestrian = pedestrian
        if rear is not None:
            self.rear = rear
        if roll_over is not None:
            self.roll_over = roll_over
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def embedded(self):
        """Gets the embedded of this CollisionObj.  # noqa: E501


        :return: The embedded of this CollisionObj.  # noqa: E501
        :rtype: object
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this CollisionObj.


        :param embedded: The embedded of this CollisionObj.  # noqa: E501
        :type: object
        """

        self._embedded = embedded

    @property
    def front(self):
        """Gets the front of this CollisionObj.  # noqa: E501


        :return: The front of this CollisionObj.  # noqa: E501
        :rtype: CollisionObjFront
        """
        return self._front

    @front.setter
    def front(self, front):
        """Sets the front of this CollisionObj.


        :param front: The front of this CollisionObj.  # noqa: E501
        :type: CollisionObjFront
        """

        self._front = front

    @property
    def id(self):
        """Gets the id of this CollisionObj.  # noqa: E501


        :return: The id of this CollisionObj.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollisionObj.


        :param id: The id of this CollisionObj.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lateral(self):
        """Gets the lateral of this CollisionObj.  # noqa: E501


        :return: The lateral of this CollisionObj.  # noqa: E501
        :rtype: CollisionObjFront
        """
        return self._lateral

    @lateral.setter
    def lateral(self, lateral):
        """Sets the lateral of this CollisionObj.


        :param lateral: The lateral of this CollisionObj.  # noqa: E501
        :type: CollisionObjFront
        """

        self._lateral = lateral

    @property
    def pedestrian(self):
        """Gets the pedestrian of this CollisionObj.  # noqa: E501


        :return: The pedestrian of this CollisionObj.  # noqa: E501
        :rtype: bool
        """
        return self._pedestrian

    @pedestrian.setter
    def pedestrian(self, pedestrian):
        """Sets the pedestrian of this CollisionObj.


        :param pedestrian: The pedestrian of this CollisionObj.  # noqa: E501
        :type: bool
        """

        self._pedestrian = pedestrian

    @property
    def rear(self):
        """Gets the rear of this CollisionObj.  # noqa: E501


        :return: The rear of this CollisionObj.  # noqa: E501
        :rtype: CollisionObjFront
        """
        return self._rear

    @rear.setter
    def rear(self, rear):
        """Sets the rear of this CollisionObj.


        :param rear: The rear of this CollisionObj.  # noqa: E501
        :type: CollisionObjFront
        """

        self._rear = rear

    @property
    def roll_over(self):
        """Gets the roll_over of this CollisionObj.  # noqa: E501


        :return: The roll_over of this CollisionObj.  # noqa: E501
        :rtype: bool
        """
        return self._roll_over

    @roll_over.setter
    def roll_over(self, roll_over):
        """Sets the roll_over of this CollisionObj.


        :param roll_over: The roll_over of this CollisionObj.  # noqa: E501
        :type: bool
        """

        self._roll_over = roll_over

    @property
    def updated_at(self):
        """Gets the updated_at of this CollisionObj.  # noqa: E501


        :return: The updated_at of this CollisionObj.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CollisionObj.


        :param updated_at: The updated_at of this CollisionObj.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(CollisionObj, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollisionObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
