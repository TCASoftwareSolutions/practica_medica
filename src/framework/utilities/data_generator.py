"""
# Clase: DataGenerator
# Descripción: Clase que genera datos aleatorios para las pruebas
"""

from faker import Faker


class DataGenerator:
    """Clase que genera datos aleatorios para las pruebas."""

    def __init__(self):
        """Constructor de la clase DataGenerator."""
        self.faker = Faker("es_MX")

    def generate_name(self):
        """Genera un nombre completo aleatorio.

        Returns:
            str: Nombre completo aleatorio.
        """
        return self.faker.name()

    def generate_first_name(self):
        """Genera un nombre aleatorio.

        Returns:
            str: Nombre aleatorio.
        """
        return self.faker.first_name()

    def generate_last_name(self):
        """Genera un apellido aleatorio.

        Returns:
            str: Apellido aleatorio.
        """
        return self.faker.last_name()

    def generate_date_of_birth(self):
        """Genera una fecha de nacimiento aleatoria.

        Returns:
            str: Fecha de nacimiento aleatoria.
        """
        return self.faker.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y/%m/%d")

    def generate_email(self):
        """Genera un correo electrónico aleatorio.

        Returns:
            str: Correo electrónico aleatorio.
        """
        return self.faker.email()

    def generate_phone_number(self):
        """Genera un número de teléfono aleatorio.

        Returns:
            str: Número de teléfono aleatorio.
        """
        return self.faker.phone_number()

    def generate_address(self):
        """Genera una dirección aleatoria.

        Returns:
            str: Dirección aleatoria.
        """
        return self.faker.address()

    def generate_country(self):
        """Regresa el pais actual

        Returns:
            str: Pais actual
        """
        return self.faker.current_country()

    def generate_state(self):
        """Genera un estado aleatorio.

        Returns:
            str: Estado aleatorio.
        """
        return self.faker.state()

    def generate_city(self):
        """Genera una ciudad aleatoria.

        Returns:
            str: Ciudad aleatoria.
        """
        return self.faker.city()

    def generate_street_name(self):
        """Genera un nombre de calle aleatorio.

        Returns:
            str: Nombre de calle aleatorio.
        """
        return self.faker.street_name()

    def generate_street_address(self):
        """Genera una dirección de calle aleatoria.

        Returns:
            str: Dirección de calle aleatoria.
        """
        return self.faker.street_address()

    def generate_postal_code(self):
        """Genera un código postal aleatorio.

        Returns:
            str: Código postal aleatorio.
        """
        return self.faker.postcode()

    def generate_company(self):
        """Genera un nombre de empresa aleatorio.

        Returns:
            str: Nombre de empresa aleatorio.
        """
        return self.faker.company()

    def generate_job(self):
        """Genera un trabajo aleatorio.

        Returns:
            str: Trabajo aleatorio.
        """
        return self.faker.job()

    def generate_text(self):
        """Genera un texto aleatorio.

        Returns:
            str: Texto aleatorio.
        """
        return self.faker.text()

    def generate_swift8(self):
        """Genera un código SWIFT de 8 caracteres aleatorio.

        Returns:
            _type_: Código SWIFT de 8 caracteres aleatorio.
        """
        return self.faker.swift8()
