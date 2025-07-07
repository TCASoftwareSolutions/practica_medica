import random
from threading import Lock

from framework.utilities.configuration import Configuration

from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
import requests


class PortalDeOperadoresLoadData:
    """Generador de datos para pruebas de carga en el portal de operadores.
    Esta clase se encarga de generar y gestionar los datos necesarios para las pruebas de carga,
    asegurando que los DUIs generados sean únicos y válidos según el formato del El Salvador."""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        # Inicializa el generador de datos con la configuración del adaptador de UI
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.data = ui_adapter.load_write_data("portal_operadores_load")
        self.generated_duis = set()

        self.lock = Lock()
        # if 'user_pool' not in self.data or 'duis' not in self.data['user_pool']:
        #    raise ValueError("Configuración inválida: falta 'user_pool' o 'duis'.")

    def _generate_valid_dui(self):
        """Genera un DUI válido según formato del El Salvador."""
        while True:
            # Parte numérica (8 dígitos)
            first_part = "".join([str(random.randint(0, 9)) for _ in range(8)])

            # Dígito verificador (1 dígito)
            second_part = str(random.randint(0, 9))

            dui = f"{first_part}-{second_part}"

            # Validar que no se haya generado antes
            with self._lock:
                if dui not in self.generated_duis:
                    self.generated_duis.add(dui)
                    return dui

    def get_valid_dui(self, list_of_duis):
        """Obtiene un DUI válido de una lista, asegurando que no se repita."""
        for dui in list_of_duis:
            numero = dui.get("numero")
            if numero not in self.generated_duis:
                self.generated_duis.add(numero)
                return dui
        self.ui_adapter.logger.error("No hay DUIs disponibles que no hayan sido usados.")
        raise RuntimeError("No hay DUIs disponibles que no hayan sido usados.")

    def reset_generated_duis(self):
        """Limpia el set de DUIs generados (útil para pruebas)."""
        with self.lock:
            self.generated_duis.clear()

    def get_next_user_data(self):
        """Devuelve los datos del siguiente usuario disponible para pruebas de carga."""
        try:
            self.ui_adapter.logger.info("Solicitando DUI único desde el servicio API.")
            with self.lock:
                response = requests.get(f"{self.ui_adapter.config.get("api_url", "http://localhost:8000")}/dui", timeout=10)
                if response.status_code == 404:
                    self.test_config.logger.error("No hay más DUIs disponibles.")
                    raise RuntimeError("No hay más DUIs disponibles.")
                response.raise_for_status()

                data_json = response.json()
                dui = data_json.get("dui")
                if not dui:
                    self.test_config.logger.error("Respuesta de API sin campo 'dui'.")
                    raise RuntimeError("Respuesta de API sin campo 'dui'.")

                numero_dui = dui.get("numero")
                if not numero_dui:
                    self.test_config.logger.error("El campo 'numero' no está presente en el DUI recibido.")
                    raise RuntimeError("El campo 'numero' no está presente en el DUI recibido.")

                if numero_dui in self.generated_duis:
                    self.test_config.logger.warning(f"DUI repetido recibido: {numero_dui}. Generando un nuevo DUI.")
                    raise RuntimeError("DUI repetido recibido del servicio.")

                self.generated_duis.add(numero_dui)
                user_id = len(self.generated_duis)
                self.test_config.logger.info(f"DUI obtenido: {dui}")

            # Validación de campos requeridos en self.data
            try:
                tipo_doc = self.data["test_scenarios"]["registro"]["tipo_de_documento"]
                lada = self.data["user_pool"]["phone"]["lada"]
                prefix = self.data["user_pool"]["phone"]["prefix"]
                email_domain = self.data["user_pool"]["email_domain"]
                fecha_cita = self.data["test_scenarios"]["gestion_de_citas"]["fecha_de_cita_medica"]
                hora_cita = self.data["test_scenarios"]["gestion_de_citas"]["hora_de_inicio_cita_medica"]
                canal = self.data["test_scenarios"]["gestion_de_citas"]["canal_de_atencion"]
            except KeyError as ke:
                self.ui_adapter.logger.error(f"Falta configuración requerida: {ke}")
                raise RuntimeError(f"Falta configuración requerida: {ke}")

            return {
                "codigo_OTP": self.data.get("codigo_OTP"),
                "registro": {
                    "identificacion": {"tipo_de_documento": tipo_doc, "clave_de_documento": numero_dui, "fecha_de_nacimiento": dui.get("fecha_de_nacimiento"), "lada_telefono": lada, "numero_telefono": prefix, "genero": dui.get("genero")},
                    "resumen": {"correo": f"user_{numero_dui.replace('-', '')}{email_domain}"},
                },
                "gestion_de_citas": {"tipo_de_documento": tipo_doc, "clave_de_documento": numero_dui, "fecha_de_cita_medica": fecha_cita, "hora_de_inicio_cita_medica": hora_cita, "canal_de_atencion": canal},
            }
        except (requests.RequestException, ValueError) as e:
            self.ui_adapter.logger.error(f"Error al obtener DUI único: {str(e)}")
            raise RuntimeError(f"Error al obtener DUI único: {str(e)}")
