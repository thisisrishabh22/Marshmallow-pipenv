from marshmallow import Schema, fields, post_load, ValidationError, validates


class Person:
    def __init__(self, name, age, email, location):
        self.name = name
        self.age = age
        self.email = email
        self.location = location

    def __repr__(self):
        return f'{self.name} is {self.age} years old has email {self.email} lives at {self.location}'

# Using custom function
# def validate_age(age):
#     if age < 18 :
#         raise ValidationError("The age is too young")


class PersonSchema(Schema):
    name = fields.String()

    # using custom fucntion
    # age = fields.Integer(validate=validate_age)

    # using decorator
    age = fields.Integer()
    email = fields.Email()
    location = fields.String(required=True)

    # Using decorator
    @validates("age")
    def validate_age(self, age):
        if age < 18:
            raise ValidationError("The age is too young")
        elif age > 150:
            raise ValidationError("The age is too old")

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {}

try:
    input_data["name"] = input("What is your name? ")
    input_data["age"] = input("What is your age? ")
    input_data["email"] = input("What is your email? ")
    input_data["location"] = input("What is your location? ")

    schema = PersonSchema()
    person = schema.load(input_data)

    # person = Person(name=input_data["name"], age=input_data["age"])
    print(person)

    result = schema.dump(person)

    print(result)
except ValidationError as err:
    print(err)
    print(err.valid_data)
