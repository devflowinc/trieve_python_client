# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateDatasetRequest(BaseModel):
    """
    CreateDatasetRequest
    """ # noqa: E501
    client_configuration: Optional[Any] = Field(description="Client configuration for the dataset, can be arbitrary JSON. We recommend setting to `{}` to start. See docs.trieve.ai for more information or adjust with the admin dashboard.")
    dataset_name: StrictStr = Field(description="Name of the dataset. Must be unique within the organization.")
    organization_id: StrictStr = Field(description="Organization ID that the dataset will belong to.")
    server_configuration: Optional[Any] = Field(description="Server configuration for the dataset, can be arbitrary JSON. We recommend setting to `{}` to start. See docs.trieve.ai for more information or adjust with the admin dashboard.")
    __properties: ClassVar[List[str]] = ["client_configuration", "dataset_name", "organization_id", "server_configuration"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateDatasetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if client_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.client_configuration is None and "client_configuration" in self.model_fields_set:
            _dict['client_configuration'] = None

        # set to None if server_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.server_configuration is None and "server_configuration" in self.model_fields_set:
            _dict['server_configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateDatasetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_configuration": obj.get("client_configuration"),
            "dataset_name": obj.get("dataset_name"),
            "organization_id": obj.get("organization_id"),
            "server_configuration": obj.get("server_configuration")
        })
        return _obj


