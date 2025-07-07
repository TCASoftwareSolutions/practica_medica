import time
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.menu_operadores.portal_de_operadores.locators import PortalOperadoresLocators as Locators
from framework.utilities.combobox_helper import ComboBoxHelper
from framework.utilities.datagridview_helper import DataGridViewHelper


class PortalDeOperadoresPage:
    """Clase que contiene los metodos de la pagina Portal de Operadores"""

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.data = self.ui_adapter.load_data("portal_operadores")

        self.combobox = ComboBoxHelper(self.ui_adapter, self.test_config)
        self.datagrid = DataGridViewHelper(self.ui_adapter, self.test_config)
        self.numero_de_cita = None

    def onClick_Cerrar(self):
        """Hacer click en Cerrar
        Raises:
            Exception: Error al hacer click en Cerrar
        """
        try:
            self.logger.info("Haciendo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Cerrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipCerrar)
            self.ui_adapter.click(self.locators.tipCerrar)
            self.logger.info("Se hizo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Cerrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cerrar: {e}")
            raise Exception(f"Error al hacer click en Cerrar: {e}")

    def verificar_paso_identificacion(self):
        """Verifica estar posicionado en el paso de Idetificación
        Returns:
            bool: True si se esta posicionado el paso de Idetificación, False de lo contrario.
        """
        try:
            self.logger.info("Verificando estar localizado en el paso de Identificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando estar localizado en el paso de Identificación")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.lblTituloIdentificacion)
            self.logger.info("Se verificó estar localizado en el paso de Identificacón")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó estar localizado en el paso de Identificacón")
            return True
        except Exception:
            return False

    def set_tipo_de_documento(self, tipo_de_documento: str = ""):
        """Configura el tipo de documento
        Args:
            tipo_de_documento (str): tipo de documento a seleccionar
        Raises:
            Exception: Error al configurar el tipo de documento
        """
        try:
            self.logger.info("Configurando el tipo de documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el tipo de documento")
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbTipoDeDocumento, tipo_de_documento, "k-item")
            self.logger.info("Se configuró el tipo de Documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró el tipo de Documento")
        except Exception as e:
            self.logger.error(f"Error al configurar el tipo de documento: {str(e)}")
            raise Exception(f"Error al configurar el tipo de documento: {str(e)}")

    def set_clave_de_documento(self, clave_de_documento: str = ""):
        """Configurar clave de Documento
        Args:
            clave_de_documento (str): La clave del documento del beneficiario
        Raises:
            Exception: Error al configurar la clave del documento
        """
        try:
            self.logger.info("Configurando clave del documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando clave del documento")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtClaveDeDocumento)
            self.ui_adapter.send_keys_tab(self.locators.txtClaveDeDocumento, clave_de_documento)
            self.logger.info("Se configuró la clave del documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la clave del documento")
        except Exception as e:
            self.logger.error(f"Error al configurar la clave del documento: {str(e)}")
            raise Exception(f"Error al configurar la clave del documento: {str(e)}")

    def set_fecha_nacimiento(self, fecha: str = ""):
        """Configura la fecha de Nacimiento
        Args:
            fecha (str): La fecha de nacimiento del beneficiario
        Raises:
            Exception: Error al configurar la fecha de nacimiento
        """
        try:
            self.logger.info("Configurando la fecha de nacimiento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando la fecha de nacimiento")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtFechaDeNacimiento)
            self.ui_adapter.send_keys_tab(self.locators.txtFechaDeNacimiento, fecha)
            self.logger.info("Se configuró la fecha de nacimiento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la fecha de nacimiento")
        except Exception as e:
            self.logger.error(f"Error al configurar la fecha de nacimiento: {str(e)}")
            raise Exception(f"Error al configurar la fecha de nacimiento: {str(e)}")

    def set_lada_telefono(self, lada: str = ""):
        """Configura la lada de marcación telefónica
        Args:
            lada (str): Lada del pais del beneficiario
        Raises:
            Exception: Error al configurar la lada del teléfono
        """
        try:
            self.logger.info("Configurando lada de marcación telefónica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando Lada telefónica")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.cmbLadaTelefono)
            self.logger.info(f"lada: {lada}")
            self.combobox.seleccionar_elemento_por_texto_open(lada, "k-item")
            self.logger.info("Se configuró la lada de marcación telefónica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la lada de marcación telefónica")
        except Exception as e:
            self.logger.error(f"Error al configurar la lada del teléfono: {str(e)}")
            raise Exception(f"Error al configurar la lada del teléfono: {str(e)}")

    def set_numero_telefono(self, numero: str = ""):
        """Configura el número del Teléfono
        Args:
            numero (str): Número de teléfono del beneficiario
        Raises:
            Exception: Error al configurar el número del teléfono
        """
        try:
            self.logger.info("Configurando el el número del teléfono")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el número del teléfono")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtNumeroTelefono)
            self.ui_adapter.click(self.locators.txtNumeroTelefono)
            self.ui_adapter.send_keys_tab(self.locators.txtNumeroTelefono, numero)
            self.logger.info("Se ha configurado el número del teléfono")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha configurado el número del teléfono")
        except Exception as e:
            self.logger.error(f"Error al configurar el número del teléfono: {str(e)}")
            raise Exception(f"Error al configurar el número del teléfono: {str(e)}")

    def set_genero(self, genero: str = ""):
        """Configura el Genero
        Args:
            genero (str): Genero del beneficiario
        Raises:
            Exception: Error al configurar el genero del beneficiario
        """
        try:
            self.logger.info("Configurando el genero del beneficiario")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el genero del beneficiario")
            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.cmbGenero)
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbGenero, genero, "k-item")
            self.logger.info("Se ha configurado el genero del beneficiario")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha configurado el genero del beneficiario")
        except Exception as e:
            self.logger.error(f"Error al configurar el genero del beneficiario: {str(e)}")
            raise Exception(f"Error al configurar el genero del beneficiario: {str(e)}")

    def onClick_Siguiente(self):
        """Hace Click en el botón Siguiente
        Raises:
            Exception: Error al hacer click en el botón Siguiente
        """
        try:
            self.logger.info("Haciendo click en el botón Siguiente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Siguiente")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnSiguiente)
            self.ui_adapter.click(self.locators.btnSiguiente)
            self.logger.info("Se hizo click en el botón Siguiente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Siguiente")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Siguiente: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Siguiente: {str(e)}")

    def set_identificacion_del_beneficiario(self, identificacion_data: dict = None):
        """Configura la identificación del beneficiario
        Args:
            identificacion_data (dict): Datos del beneficiario
        Raises:
            Exception: Error al configurar identificación del beneficiario
        """
        try:
            assert self.verificar_paso_identificacion()
            time.sleep(2)
            self.set_tipo_de_documento_y_clave_para_registro(identificacion_data.get("tipo_de_documento"), identificacion_data.get("clave_de_documento"))
            time.sleep(2)
            self.set_fecha_nacimiento(identificacion_data.get("fecha_de_nacimiento"))
            assert self.verificar_usuario_ya_registrado()
            time.sleep(1)
            self.set_lada_telefono(identificacion_data.get("lada_telefono"))
            time.sleep(1)
            self.set_numero_telefono(identificacion_data.get("numero_telefono"))
            time.sleep(1)
            self.set_genero(identificacion_data.get("genero"))
            time.sleep(1)
            self.onClick_Siguiente()
        except Exception as e:
            self.logger.error(f"Error al configurar identificación del beneficiario: {str(e)}")
            raise Exception(f"Error al configurar identificación del beneficiario: {str(e)}")

    def verificar_paso_verificacion(self):
        """Verifica estar posicionado en el paso de Verificación
        Returns:
            bool: True si se esta posicionado el paso de Verificación, False de lo contrario.
        """
        try:
            self.logger.info("Verificando estar localizado en el paso de Verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando estar localizado en el paso de Verificación")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.lblTituloVerificacion)
            self.logger.info("Se verificó estar localizado en el paso de Verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó estar localizado en el paso de Verificación")
            return True
        except Exception:
            return False

    def onClick_EnviarPorSMS(self):
        """Hace click en el botón Enviar por SMS
        Raises:
            Exception: Error al hacer click en el botón Enviar por SMS
        """
        try:
            self.logger.info("Haciendo click en el botón Enviar por SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Enviar por SMS")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnEnviarPorSMS)
            self.ui_adapter.click(self.locators.btnEnviarPorSMS)
            self.logger.info("Se hizo click en el botón Enviar por SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Enviar por SMS")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Enviar por SMS: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Enviar por SMS: {str(e)}")

    def validar_SMS_enviado(self):
        """Confirma que el SMS se envio
        Returns:
            bool: True si el SMS se envió, False de lo contrario
        """
        try:
            self.logger.info("Confirmando el envio del SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando el envio del SMS")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgCodigoEnviado)
            self.ui_adapter.click(self.locators.msgCodigoEnviado)
            self.logger.info("Se confirmó el envio del SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó el envio del SMS")
            return True
        except Exception:
            return False

    def set_codigo(self, codigo: str = ""):
        """Configura el códido de verificación recibido
        Args:
            codigo (str): Código de verificación recibido
        Raises:
            Exception: Error al configurar código de verificación
        """
        try:
            self.logger.info("Configurando el código de verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el código de verificación")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtCodigo)
            self.ui_adapter.click(self.locators.txtCodigo)
            self.ui_adapter.send_keys_enter(self.locators.txtCodigo, codigo)
            self.logger.info("Se ha configurado el código de verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha configurado el código de verificación")
        except Exception as e:
            self.logger.error(f"Error al configurar código de verificación: {str(e)}")
            raise Exception(f"Error al configurar código de verificación: {str(e)}")

    def set_verificacion_de_codigo(self, codigo_OTP: str = ""):
        """Configura la verficiacion del codigó
        Args:
            identificacion_data (dict): Datos del beneficiario
        Raises:
            Exception: Error al configurar identificación del beneficiario
        """
        try:
            assert self.verificar_paso_verificacion()
            time.sleep(2)
            self.onClick_EnviarPorSMS()
            time.sleep(5)
            assert self.validar_SMS_enviado()
            time.sleep(2)
            self.set_codigo(codigo_OTP)
            time.sleep(2)
            self.onClick_Siguiente()
        except Exception as e:
            raise Exception(f"Error al configurar identificación del beneficiario: {str(e)}")

    def set_correo(self, correo: str = ""):
        """Configura el Correo electrónico
        Args:
            correo (str): Correo electrónico del beneficiario
        Raises:
            Exception: Error al configurar el Correo electrónico
        """
        try:
            self.logger.info("Configurando el Correo electrónico")
            self.ui_adapter.take_screenshot(self.test_config.logger_dir, "Configurando el Correo electrónico")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtCorreoElectronico)
            self.ui_adapter.click(self.locators.txtCorreoElectronico)
            self.ui_adapter.send_keys_enter(self.locators.txtCorreoElectronico, correo)
            self.logger.info("Se configuró el Correo electrónico")
            self.ui_adapter.take_screenshot(self.test_config.logger_dir, "Se configuró el Correo electrónico")
        except Exception as e:
            self.logger.error(f"Error al configurar el Correo electrónico: {str(e)}")
            raise Exception(f"Error al configurar el Correo electrónico: {str(e)}")

    def verificar_paso_resumen(self):
        """Verifica estar posicionado en el paso de Resumen
        Returns:
            bool: True si se esta posicionado el paso de Resumen, False de lo contrario.
        """
        try:
            self.logger.info("Verificando estar localizado en el paso de Resumen")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando estar localizado en el paso de Resumen")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.lblTituloResumen)
            self.logger.info("Se verificó estar localizado en el paso de Resumen")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó estar localizado en el paso de Resumen")
            return True
        except Exception:
            return False

    def verficar_beneficiario_registrado_correctamente(self):
        """Confirma que el beneficiario se registró correctamente
        Returns:
            bool: True si el beneficiario se registró correctamente, False de lo contrario
        """
        try:
            self.logger.info("Confirmando que el beneficiario se haya registrado correctamente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando que el beneficiario se haya registrado correctamente")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.lblBeneficiarioGenerado)
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAceptarBeneficiarioGenerado)
            self.ui_adapter.click(self.locators.btnAceptarBeneficiarioGenerado)
            self.logger.info("Se confirmó que el beneficiario se ha registrado correctamente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó que el beneficiario se ha registrado correctamente")
            return True
        except Exception as e:
            self.logger.error(f"Error al confirmar que el beneficiario se registró correctamente {str(e)}")
            raise Exception(f"Error al confirmar que el beneficiario se registró correctamente {str(e)}")

    def verificar_usuario_ya_registrado(self):
        try:
            if self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.lblYaSeEncuentraRegistrado):
                self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAceptarBeneficiarioGenerado)
                self.logger.error("El beneficiario ya se encontrabá registrado")
                self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "El beneficiario ya se encontrabá registrado")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Error al confirmar que el beneficiario se registró correctamente {str(e)}")
            raise Exception(f"Error al confirmar que el beneficiario se registró correctamente {str(e)}")

    def set_resumen_del_registro(self, resumen_data: dict = None):
        """Configura el resumen del registro
        Args:
            resumen_data (dict): Datos del beneficiario
        Raises:
            Exception: Error al configurar el resumen del registro
        """
        try:
            assert self.verificar_paso_resumen()
            time.sleep(3)
            self.set_correo(resumen_data.get("correo"))
            time.sleep(2)
            self.onClick_Siguiente()
        except Exception as e:
            self.logger.error(f"Error al configurar el resumen del registro: {str(e)}")
            raise Exception(f"Error al configurar el resumen del registro: {str(e)}")

    def onClick_MenuGestionDeCitas(self):
        try:
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGestionDeCitas)
            self.ui_adapter.click(self.locators.btnGestionDeCitas)
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Gestion de Citas: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Gestion de Citas: {str(e)}")

    def set_tipo_de_documento_para_cita(self, tipo_de_documento: str = ""):
        """Configura el tipo de documento
        Args:
            tipo_de_documento (str): tipo de documento a seleccionar
        Raises:
            Exception: Error al configurar el tipo de documento
        """
        try:
            self.logger.info("Configurando el tipo de documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el tipo de documento")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.cmbCitasTipoDeDocumento)
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbCitasTipoDeDocumento, tipo_de_documento, "k-item")
            self.logger.info("Se configuró el tipo de Documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró el tipo de Documento")
        except Exception as e:
            self.logger.error(f"Error al configurar el tipo de documento: {str(e)}")
            raise Exception(f"Error al configurar el tipo de documento: {str(e)}")

    def set_clave_de_documento_para_cita(self, clave_de_documento: str = ""):
        """Configurar clave de Documento
        Args:
            clave_de_documento (str): La clave del documento del beneficiario
        Raises:
            Exception: Error al configurar la clave del documento
        """
        try:
            self.logger.info("Configurando clave del documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando clave del documento")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtCitasClaveDeDocumento)
            self.ui_adapter.send_keys_tab(self.locators.txtCitasClaveDeDocumento, clave_de_documento)
            self.logger.info("Se configuró la clave del documento")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la clave del documento")
        except Exception as e:
            self.logger.error(f"Error al configurar la clave del documento: {str(e)}")
            raise Exception(f"Error al configurar la clave del documento: {str(e)}")

    def onClick_AgendarCita(self):
        """Hace click en el botón Agendar cita
        Raises:
            Exception: Error al hacer click en el botón Agendar cita
        """
        try:
            self.logger.info("Haciendo click en el botón Agendar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Agendar cita")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAgendarCita)
            self.ui_adapter.click(self.locators.btnAgendarCita)
            self.logger.info("Se hizo click en el botón Agendar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Agendar cita")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Agendar cita: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Agendar cita: {str(e)}")

    def validar_limite_de_citas(self):
        """Válida el limite de citas
        Returns:
            bool: True si la cita se generó exitosamente, False de lo contrario
        """
        try:
            self.logger.info("Validando el limite de citas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Validando el limite de citas")
            if self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgLimiteDeCitas):
                self.logger.error("Limite de citas superado!")
                self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Limite de citas superado")
                self.ui_adapter.click(self.locators.msgLimiteDeCitas)
                return False
            self.logger.info("Se ha validado el limite de citas superado")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha validado el limite de citas superado")
            return True
        except Exception as e:
            self.logger.error(f"Error al validar el limite de citas: {str(e)}")
            raise Exception(f"Error al validar el limite de citas: {str(e)}")

    def verificar_modal_Envio_de_Mensajes_OTP(self):
        """Verifica la apertura del modal Envio de mensajes OTP
        Returns:
            bool: True si abrió, False de lo contrario.
        """
        try:
            self.logger.info("Verificando la apertura del modal Envio de mensajes OTP")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando la apertura del modal Envio de mensajes OTP")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalEnvioDeMensajesOTP)
            self.logger.info("Se verificó la apertura del modal Envio de mensajes OTP")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó la apertura del modal Envio de mensajes OTP")
            return True
        except Exception as e:
            self.logger.error(f"Error al verificar la apertura del modal Envio de mensajes OTP: {str(e)}")
            raise Exception(f"Error al verificar la apertura del modal Envio de mensajes OTP: {str(e)}")

    def onClick_EnviarOTPporSMS(self):
        """Hace click en el botón Enviar por SMS
        Raises:
            Exception: Error al hacer click en el botón Enviar por SMS
        """
        try:
            self.logger.info("Haciendo click en el botón Enviar por SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Enviar por SMS")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnEnviarOTPporSMS)
            self.ui_adapter.click(self.locators.btnEnviarOTPporSMS)
            self.logger.info("Se hizo click en el botón Enviar por SMS")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Enviar por SMS")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Enviar por SMS: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Enviar por SMS: {str(e)}")

    def set_codigo_OTP(self, codigo: str = ""):
        """Configura el códido de verificación recibido
        Args:
            codigo (str): Código de verificación recibido
        Raises:
            Exception: Error al configurar código de verificación
        """
        try:
            self.logger.info("Configurando el código de verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el código de verificación")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtCodigoDeVerificacionModalOTP)
            self.ui_adapter.click(self.locators.txtCodigoDeVerificacionModalOTP)
            self.ui_adapter.send_keys_enter(self.locators.txtCodigoDeVerificacionModalOTP, codigo)
            self.logger.info("Se ha configurado el código de verificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha configurado el código de verificación")
        except Exception as e:
            self.logger.error(f"Error al configurar código de verificación: {str(e)}")
            raise Exception(f"Error al configurar código de verificación: {str(e)}")

    def onClick_Continuar(self):
        """Hace click en el botón Continuar
        Raises:
            Exception: Error al hacer click en el botón Continuar
        """
        try:
            self.logger.info("Haciendo click en el botón Continuar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Continuar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnContinuarModalOTP)
            self.ui_adapter.click(self.locators.btnContinuarModalOTP)
            self.logger.info("Se hizo click en el botón Continuar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Continuar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Continuar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Continuar: {str(e)}")

    def verificar_modal_agendar_cita(self):
        """Verifica la apertura del modal Agendar cita
        Returns:
            bool: True si abrió, False de lo contrario.
        """
        try:
            self.logger.info("Verificando la apertura del modal Agendar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando la apertura del modal Agendar cita")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalEnvioDeMensajesOTP)
            self.logger.info("Se verificó la apertura del modal Agendar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó la apertura del modal Agendar cita")
            return True
        except Exception as e:
            self.logger.error(f"Error al validar la apertura del modal Agendar cita: {str(e)}")
            return False

    def set_fecha_de_cita(self, fecha: str = ""):
        """Configura la fecha de la cita médica
        Args:
            fecha (str): La fecha de la cita médica del beneficiario
        Raises:
            Exception: Error al configurar la fecha de la cita médica
        """
        try:
            self.logger.info("Configurando la fecha de la cita médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando la fecha de la cita médica")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtFecha)
            self.ui_adapter.click(self.locators.txtFecha)
            self.ui_adapter.send_keys_tab(self.locators.txtFecha, fecha)
            self.logger.info("Se configuró la fecha de la cita médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la fecha de la cita médica")
        except Exception as e:
            self.logger.error(f"Error al configurar la fecha de la cita médica: {str(e)}")
            raise Exception(f"Error al configurar la fecha de la cita médica: {str(e)}")

    def set_hora_de_inicio(self, hora_de_inicio: str = ""):
        """Configura la hora de inicio de la cita médica
        Args:
            hora_de_inicio (str): La fecha de la cita médica del beneficiario
        Raises:
            Exception: Error al configurar la hora de la cita médica
        """
        try:
            self.logger.info("Configurando la hora de la cita médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando la hora de la cita médica")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.cmbHoraInicio)
            self.combobox.seleccionar_elemento_por_texto_open(hora_de_inicio, "k-item")
            self.logger.info("Se configuró la hora de la cita médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró la hora de la cita médica")
        except Exception as e:
            self.logger.error(f"Error al configurar la hora de la cita médica: {str(e)}")
            raise Exception(f"Error al configurar la hora de la cita médica: {str(e)}")

    def set_canal_de_atencion(self, canal_de_atencion: str = ""):
        """Configura el canal de atención para la cita médica
        Args:
            canal_de_atencion (str): canal de atención del beneficiario
        Raises:
            Exception: Error al configurar el canal de atención del beneficiario
        """
        try:
            self.logger.info("Configurando el canal de atención del beneficiario")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el canal de atención del beneficiario")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.cmbCanalDeAtencion)
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbCanalDeAtencion, canal_de_atencion, "k-item")
            self.logger.info("Se ha configurado el canal de atención del beneficiario")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se ha configurado el canal de atención del beneficiario")
        except Exception as e:
            self.logger.error(f"Error al configurar el canal de atención del beneficiario: {str(e)}")
            raise Exception(f"Error al configurar el canal de atención del beneficiario: {str(e)}")

    def onClick_Guardar(self):
        """Hace click en el botón Guardar
        Raises:
            Exception: Error al hacer click en el botón Guardar
        """
        try:
            self.logger.info("Haciendo click en el botón Guardar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Guardar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGuardarModalAgendarCita)
            self.ui_adapter.click(self.locators.btnGuardarModalAgendarCita)
            self.logger.info("Se hizo click en el botón Guardar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Guardar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Guardar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Guardar: {str(e)}")

    def validar_cita_generada_con_exito(self):
        """Válida que la cita se agendó con éxito
        Returns:
            bool: True si la cita se generó exitosamente, False de lo contrario
        """
        try:
            self.logger.info("Confirmando la cita se agendó con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando la cita se agendó con éxito")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgCitaGeneradaConExito)

            mensaje = self.ui_adapter.get_text(self.locators.msgCitaGeneradaConExito)
            self.numero_de_cita = mensaje.split("[")[1].split("]")[0].strip()

            self.ui_adapter.click(self.locators.msgCitaGeneradaConExito)
            self.logger.info("Se confirmó la cita se agendó con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó la cita se agendó con éxito")
            return True
        except Exception:
            return False

    def validar_existencia_de_cita_medica(self, numero_de_cita: str = ""):
        """Valida la existencia de la cita médica
        Args:
            numero_de_cita (str): número de cita a buscar
        Raises:
            Exception: Error al validar la existencia de la cita médica
        """
        try:
            self.logger.info(f"Validando la existencia de la cita médica: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Validando la existencia de la cita médica: {numero_de_cita}")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.txtGridSearch)
            self.ui_adapter.send_keys_enter(self.locators.txtGridSearch, numero_de_cita)

            # if numero_de_cita != self.ui_adapter.get_text(self.locators.lblNumeroDeCita):
            # time.sleep(5)
            if self.ui_adapter.find_element_is_exist(self.locators.lblNoExistenRegistros):
                return False
            self.logger.info(f"Se confirmó la existencia de la cita medica: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se confirmó la existencia de la cita medica: {numero_de_cita}")
            return True
        except Exception as e:
            self.logger.error(f"Error al validar la existencia de la cita médica: {str(e)}")
            raise Exception(f"Error al validar la existencia de la cita médica: {str(e)}")

    def set_tipo_de_documento_y_clave_para_registro(self, tipo: str = "", clave: str = ""):
        """Establece el tipo de documento y clave

        Args:
            tipo (str): tipo de documento.
            clave (str): clave del documento.

        Raises:
            Exception: Error al establecer tipo de documento y clave.
        """
        try:
            self.set_tipo_de_documento(tipo)
            time.sleep(2)
            self.set_clave_de_documento(clave)
        except Exception as e:
            self.logger.error(f"Error al establecer tipo de documento y clave: {str(e)}")
            raise Exception(f"Error al establecer tipo de documento y clave: {str(e)}")

    def set_tipo_de_documento_y_clave_para_cita(self, tipo: str = "", clave: str = ""):
        """Establece el tipo de documento y clave

        Args:
            tipo (str): tipo de documento.
            clave (str): clave del documento.

        Raises:
            Exception: Error al establecer tipo de documento y clave.
        """
        try:
            self.set_tipo_de_documento_para_cita(tipo)
            time.sleep(2)
            self.set_clave_de_documento_para_cita(clave)
        except Exception as e:
            self.logger.error(f"Error al establecer tipo de documento y clave: {str(e)}")
            raise Exception(f"Error al establecer tipo de documento y clave: {str(e)}")

    def agendar_cita(self, cita_data: dict = None, codigo_OTP: str = ""):
        """Hace el proceso de agendar cita
        Args:
            cita_data (dict, optional): datos de la cita
            codigo_OTP (str, optional): codigo de verificación
        Raises:
            Exception: Error al agendar cita
        """
        try:
            self.onClick_MenuGestionDeCitas()
            time.sleep(2)
            self.set_tipo_de_documento_y_clave_para_cita(cita_data.get("tipo_de_documento"), cita_data.get("clave_de_documento"))
            time.sleep(2)
            self.onClick_AgendarCita()
            assert self.validar_limite_de_citas()
            assert self.verificar_modal_Envio_de_Mensajes_OTP()
            self.onClick_EnviarOTPporSMS()
            time.sleep(2)
            self.set_codigo_OTP(codigo_OTP)
            time.sleep(2)
            self.onClick_Continuar()
            assert self.verificar_modal_agendar_cita()
            self.set_fecha_de_cita(cita_data.get("fecha_de_cita_medica"))
            time.sleep(2)
            self.set_hora_de_inicio(cita_data.get("hora_de_inicio_cita_medica"))
            time.sleep(1)
            self.set_canal_de_atencion(cita_data.get("canal_de_atencion"))
            time.sleep(2)
            self.onClick_Guardar()
            time.sleep(5)
            assert self.validar_cita_generada_con_exito()
            time.sleep(2)
            assert self.validar_existencia_de_cita_medica(self.numero_de_cita)
        except Exception as e:
            self.logger.error(f"Error al agendar cita: {str(e)}")
            raise Exception(f"Error al agendar cita: {str(e)}")

    def onClick_editar_cita(self):
        """Hace click en el botón Editar cita
        Raises:
            Exception: Error al hacer click en el botón Editar
        """
        try:
            self.logger.info("Haciendo click en el botón Editar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Editar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnEditar)
            self.ui_adapter.click(self.locators.btnEditar)
            self.logger.info("Se hizo click en el botón Editar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Editar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Editar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Editar: {str(e)}")

    def verificar_modal_editar_cita(self):
        """Verifica la apertura del modal Editar cita
        Returns:
            bool: True si abrió, False de lo contrario.
        """
        try:
            self.logger.info("Verificando la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando la apertura del modal Editar cita")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalEditarCita)
            self.logger.info("Se verificó la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó la apertura del modal Editar cita")
            return True
        except Exception:
            return False

    def validar_modal_editar_cita(self):
        """Valida la apertura del modal Editar cita
        Returns:
            bool: True si existe, False de lo contrario.
        """
        try:
            self.logger.info("Validando la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Validando la apertura del modal Editar cita")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalEditarCita)
            self.logger.info("Se confirmó la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó la apertura del modal Editar cita")
            return True
        except Exception:
            return False

    def validar_modal_motivo_editar_cita(self):
        """Valida la apertura del modal Editar cita
        Returns:
            bool: True si existe, False de lo contrario.
        """
        try:
            self.logger.info("Validando la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Validando la apertura del modal Editar cita")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalMotivoDeEditarCita)
            self.logger.info("Se confirmó la apertura del modal Editar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó la apertura del modal Editar cita")
            return True
        except Exception:
            return False

    def set_motivo_de_reprogramacion(self, motivo: str = ""):
        """Configura el motivo de reprogramación
        Args:
            motivo (str): motivo de reprogramación
        Raises:
            Exception: Error al configurar el motivo de reprogramación
        """
        try:
            self.logger.info("Configurando el motivo de reprogramación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el motivo de reprogramación")
            self.datagrid.seleccionar_datagrid(self.locators.btndgvMotivo, motivo)
            self.logger.info("Se configuró el motivo de reprogramación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró el motivo de reprogramación")
        except Exception as e:
            self.logger.error(f"Error al configurar el motivo de reprogramación: {str(e)}")
            raise Exception(f"Error al configurar el motivo de reprogramación: {str(e)}")

    def onClick_Aceptar(self):
        """Hace click en el botón Aceptar
        Raises:
            Exception: Error al hacer click en el botón Aceptar
        """
        try:
            self.logger.info("Haciendo click en el botón Aceptar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Aceptar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAceptarModalEditarCita)
            self.ui_adapter.click(self.locators.btnAceptarModalEditarCita)
            self.logger.info("Se hizo click en el botón Aceptar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Aceptar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Aceptar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Aceptar: {str(e)}")

    def validar_cita_reprogramada_con_exito(self):
        """Válida que la cita se reprogramó con éxito
        Returns:
            bool: True si la cita se reprogramó exitosamente, False de lo contrario
        """
        try:
            self.logger.info("Confirmando la cita se reprogramó con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando la cita se reprogramó con éxito")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgCitaReagendadaConExito)
            self.ui_adapter.click(self.locators.msgCitaReagendadaConExito)
            self.logger.info("Se confirmó la cita se reprogramó con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó la cita se reprogramó con éxito")
            return True
        except Exception:
            return False

    def buscar_cita(self, numero_de_cita: str = ""):
        """Busca la cita médica
        Args:
            numero_de_cita (str): número de cita a buscar
        Raises:
            Exception: Error al buscar la cita médica
        """
        try:
            self.logger.info(f"Buscando la cita médica: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Buscando la cita médica: {numero_de_cita}")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.txtGridSearch)
            self.ui_adapter.send_keys_enter(self.locators.txtGridSearch, numero_de_cita)
            self.logger.info("Se encontró la cita médica: {numero_de_cita}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se encontró la cita médica")
        except Exception as e:
            self.logger.error(f"Error al buscar la cita médica: {numero_de_cita}: {str(e)}")
            raise Exception(f"Error al buscar la cita médica: {numero_de_cita}: {str(e)}")

    def reprogramar_cita(self, cita_data: dict = None, codigo_OTP: str = "", numero_de_cita: str = None):
        """Reprograma la cita médica
        Args:
            cita_data (dict): datos de la cita
            codigo_OTP (str): código de verificación
            numero_de_cita (str): número de cita a buscar
        Raises:
            Exception: Error al reprogramar la cita médica
        """
        try:
            self.onClick_MenuGestionDeCitas()
            time.sleep(2)
            self.set_tipo_de_documento_y_clave_para_cita(cita_data.get("tipo_de_documento"), cita_data.get("clave_de_documento"))
            time.sleep(2)
            self.buscar_cita(numero_de_cita if numero_de_cita else cita_data.get("numero_de_cita"))
            time.sleep(2)
            self.onClick_editar_cita()
            assert self.validar_cita_reprogramable()
            assert self.verificar_modal_Envio_de_Mensajes_OTP()
            self.onClick_EnviarOTPporSMS()
            time.sleep(2)
            self.set_codigo_OTP(codigo_OTP)
            time.sleep(2)
            self.onClick_Continuar()
            assert self.verificar_modal_editar_cita()
            self.set_fecha_de_cita(cita_data.get("fecha_de_cita_medica"))
            time.sleep(2)
            self.set_hora_de_inicio(cita_data.get("hora_de_inicio_cita_medica"))
            time.sleep(2)
            # self.set_canal_de_atencion(cita_data.get("canal_de_atencion"))
            # time.sleep(2)
            self.onClick_Guardar()
            assert self.validar_modal_motivo_editar_cita()
            self.set_motivo_de_reprogramacion(cita_data.get("motivo_de_reprogramacion"))
            time.sleep(2)
            self.onClick_Aceptar()
            time.sleep(6)
            assert self.validar_cita_reprogramada_con_exito()
        except Exception as e:
            self.logger.error(f"Error al reprogramar cita: {str(e)}")
            raise Exception(f"Error al reprogramar cita: {str(e)}")

    def onClick_CancelarCita(self):
        """Hace click en el botón Cancelar cita
        Raises:
            Exception: Error al hacer click en el botón Cancelar
        """
        try:
            self.logger.info("Haciendo click en el botón Cancelar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Cancelar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnEliminar)
            self.ui_adapter.click(self.locators.btnEliminar)
            self.logger.info("Se hizo click en el botón Cancelar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Cancelar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Cancelar: {str(e)}")
            raise Exception(f"Error al hacer click en el botón Cancelar: {str(e)}")

    def verificar_modal_cancelar_cita(self):
        """Verifica la apertura del modal Cancelar cita
        Returns:
            bool: True si abrió, False de lo contrario.
        """
        try:
            self.logger.info("Verificando la apertura del modal Cancelar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Verificando la apertura del modal Cancelar cita")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.modalMotivoDeCancelacion)
            self.logger.info("Se verificó la apertura del modal Cancelar cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se verificó la apertura del modal Cancelar cita")
            return True
        except Exception:
            return False

    def set_motivo_de_cancelacion(self, motivo: str = ""):
        """Configura el motivo de cancelación
        Args:
            motivo (str): motivo de cancelación
        Raises:
            Exception: Error al configurar el motivo de cancelación
        """
        try:
            self.logger.info("Configurando el motivo de cancelación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Configurando el motivo de cancelación")
            self.datagrid.seleccionar_datagrid(self.locators.btndgvMotivo, motivo)
            self.logger.info("Se configuró el motivo de cancelación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se configuró el motivo de cancelación")
        except Exception as e:
            self.logger.error(f"Error al configurar el motivo de cancelación: {str(e)}")
            raise Exception(f"Error al configurar el motivo de cancelación: {str(e)}")

    def validar_cita_cancelada_con_exito(self):
        """Válida que la cita se canceló con éxito
        Returns:
            bool: True si la cita se canceló exitosamente, False de lo contrario
        """
        try:
            self.logger.info("Confirmando la cita se canceló con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando la cita se canceló con éxito")
            assert self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgCitaCanceladaConExito)
            self.ui_adapter.click(self.locators.msgCitaCanceladaConExito)
            self.logger.info("Se confirmó la cita se canceló con éxito")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó la cita se canceló con éxito")
            return True
        except Exception:
            return False

    def validar_cita_cancelable(self):
        """Válida que la cita no tenga estatus de Cancelada
        Returns:
            bool: True si la cita es cancelable, False de lo contrario
        """
        try:
            self.logger.info("Confirmando que la cita sea cancelable")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando que la cita sea cancelable")
            if self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgImposibleCancelar):
                self.logger.error("Solo es posible cancelar citas que tienen el estatus 'Programado'")
                self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Imposible cancelar citas con estatus 'Cancelada'")
                return False
            self.logger.info("Se confirmó que la cita es cancelable")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó que la cita es cancelable")
            return True
        except Exception as e:
            self.logger.info(f"Error al confirmar si la cita es cancelable: {str(e)}")
            raise Exception(f"Error al confirmar si la cita es cancelable: {str(e)}")

    def validar_cita_reprogramable(self):
        """Válida que la cita no tenga estatus de Cancelada
        Returns:
            bool: True si la cita es reprogramable, False de lo contrario
        """
        try:
            self.logger.info("Confirmando que la cita sea reprogramable")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Confirmando que la cita sea reprogramable")
            if self.ui_adapter.wait_manager.wait_for_element_exists(*self.locators.msgImposibleEditar):
                self.logger.error("Solo es posible reprogramar citas que tienen el estatus 'Programado'")
                self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Imposible reprogramar citas con estatus 'Cancelada'")
                return False
            self.logger.info("Se confirmó que la cita es reprogramable")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se confirmó que la cita es reprogramable")
            return True
        except Exception as e:
            self.logger.info(f"Error al confirmar si la cita es reprogramable: {str(e)}")
            raise Exception(f"Error al confirmar si la cita es reprogramable: {str(e)}")

    def cancelar_cita(self, cita_data: dict = None, codigo_OTP: str = "", numero_de_cita: str = None):
        """Cancela la cita médica
        Args:
            cita_data (dict): datos de la cita
            codigo_OTP (str): código de verificación
            numero_de_cita (str): número de cita a buscar
        Raises:
            Exception: Error al cancelar la cita médica
        """
        try:
            self.onClick_MenuGestionDeCitas()
            self.set_tipo_de_documento_y_clave_para_cita(cita_data.get("tipo_de_documento"), cita_data.get("clave_de_documento"))
            time.sleep(2)
            self.buscar_cita(numero_de_cita if numero_de_cita else cita_data.get("numero_de_cita"))
            time.sleep(2)
            self.onClick_CancelarCita()
            assert self.validar_cita_cancelable()
            assert self.verificar_modal_Envio_de_Mensajes_OTP()
            self.onClick_EnviarOTPporSMS()
            time.sleep(2)
            self.set_codigo_OTP(codigo_OTP)
            time.sleep(2)
            self.onClick_Continuar()
            assert self.verificar_modal_cancelar_cita()
            time.sleep(2)
            self.set_motivo_de_cancelacion(cita_data.get("motivo_de_cancelacion"))
            time.sleep(2)
            self.onClick_Aceptar()
            time.sleep(6)
            assert self.validar_cita_cancelada_con_exito()
        except Exception as e:
            self.logger.error(f"Error al cancelar cita: {str(e)}")
            raise Exception(f"Error al cancelar cita: {str(e)}")
