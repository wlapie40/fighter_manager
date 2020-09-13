from datetime import date
from marshmallow import EXCLUDE, Schema, fields, validate
from pprint import pprint


def validate_account_type(n):
    if n not in ["fighter", "manger", "federation"]:
        raise ValidationError("Wrong data")


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class AddUserInputSchema(Schema):
    pass


class GetUserSchemaOut(Schema):
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"), allow_none=False)
    username = fields.Str(required=True, allow_none=False, validate=validate.Length(min=4))
    account_type = fields.Str(required=True, allow_none=False, validate=validate_account_type)


class GetUserSchemaIn(Schema):
    id = fields.UUID(required=True, allow_none=False)


# class UserOutSchema(Schema):
#     email = fields.Str(required=True, validate=validate.email, allow_none=False)
#     username = fields.Str(required=True, allow_none=False)
#     id = fields.UUID(required=True, allow_none=False)


# class AddUserSchemaIn(Schema):
#     email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"), allow_none=False)
#     username = fields.Str(required=True, allow_none=False, validate=validate.Length(min=4))
#     password = fields.Str(required=True, allow_none=False)
#     account_type = fields.Str(required=True, allow_none=False, validate=validate_account_type)


get_user_schema_out = GetUserSchemaOut()
get_user_schema_in = GetUserSchemaIn()
