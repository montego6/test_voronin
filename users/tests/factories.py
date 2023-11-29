import factory


class UserFactory(factory.Factory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
