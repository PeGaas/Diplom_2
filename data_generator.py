from faker import Faker


def generate_first_name():
    return Faker().first_name()


def generate_password():
    return Faker().password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)


def generate_email():
    return Faker().company_email()


