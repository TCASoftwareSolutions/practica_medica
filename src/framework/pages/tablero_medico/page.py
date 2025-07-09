import time
from adapter.selenium.selenium_adapter import SeleniumAdapter as UIPort
from framework.utilities.configuration import Configuration
from framework.pages.tablero_medico.locators import TableroMedicoLocators as Locators
from framework.utilities.datagridview_helper import DataGridViewHelper
from framework.utilities.combobox_helper import ComboBoxHelper


class TableroMedicoPage:
    """Clase que contiene los metodos de la pagina Informe de Solicitudes.
    Esta clase permite interactuar con los elementos de la pagina Informe de Solicitudes
    """

    def __init__(self, ui_adapter: UIPort, test_config: Configuration):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.locators = Locators()
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

        self.data = self.ui_adapter.load_data("informe_de_solicitudes")

        self.datagrid = DataGridViewHelper(self.ui_adapter, self.test_config)
        self.combobox = ComboBoxHelper(self.ui_adapter, self.test_config)

    def onClick_Cerrar(self):
        """Hacer click en Cerrar
        Raises:
            Exception: Error al hacer click en Cerrar
        """
        try:
            self.logger.info("Haciendo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Cerrar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.app_close)
            self.ui_adapter.click(self.locators.app_close)
            self.logger.info("Se hizo click en el botón Cerrar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Cerrar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cerrar: {e}")
            raise Exception(f"Error al hacer click en Cerrar: {e}")

    def onClick_abrir_videollamada(self):
        """Hacer click en abrir videollamada
        Raises:
            Exception: Error al hacer click en abrir videollamada
        """
        try:
            self.logger.info("Haciendo click en el botón Abrir Videollamada")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Abrir Videollamada")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipAbrirLlamada)
            self.ui_adapter.click(self.locators.tipAbrirLlamada)
            self.logger.info("Se hizo click en el botón Abrir Videollamada")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Abrir Videollamada")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Abrir Videollamada: {e}")
            raise Exception(f"Error al hacer click en Abrir Videollamada: {e}")

    def onClick_Finalizar_cita(self):
        """Hacer click en finalizar cita
        Raises:
            Exception: Error al hacer click en finalizar cita
        """
        try:
            self.ui_adapter.wait_manager.wait_for_element_absent(*self.locators.notificationsDiv)
            self.logger.info("Haciendo click en el botón Finalizar Cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Finalizar Cita")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipFinalizarCita)
            self.ui_adapter.click(self.locators.tipFinalizarCita)
            self.logger.info("Se hizo click en el botón Finalizar Cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Finalizar Cita")

            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnFinCita)
            self.ui_adapter.click(self.locators.btnFinCita)
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.chkNo)
            self.ui_adapter.click(self.locators.chkNo)
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnContinuar)
            self.ui_adapter.click(self.locators.btnContinuar)
            self.ui_adapter.wait_manager.wait_for_element_absent(*self.locators.loadingBarOn)

        except Exception as e:
            self.logger.error(f"Error al hacer click en Finalizar Cita: {e}")
            raise Exception(f"Error al hacer click en Finalizar Cita: {e}")

    def onClick_Linea_de_tiempo(self):
        """Hacer click en la linea de tiempo
        Raises:
            Exception: Error al hacer click en la linea de tiempo
        """
        try:
            self.logger.info("Haciendo click en la línea de tiempo")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en la línea de tiempo")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabLineaDeTiempo)
            self.ui_adapter.click(self.locators.tabLineaDeTiempo)
            self.logger.info("Se hizo click en la línea de tiempo")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en la línea de tiempo")
        except Exception as e:
            self.logger.error(f"Error al hacer click en la línea de tiempo: {e}")
            raise Exception(f"Error al hacer click en la línea de tiempo: {e}")

    def onClick_Lista_de_problemas(self):
        """Hacer click en la lista de problemas
        Raises:
            Exception: Error al hacer click en la lista de problemas
        """
        try:
            self.logger.info("Haciendo click en la lista de problemas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en la lista de problemas")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabListaDeProblemas)
            self.ui_adapter.click(self.locators.tabListaDeProblemas)
            self.logger.info("Se hizo click en la lista de problemas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en la lista de problemas")
        except Exception as e:
            self.logger.error(f"Error al hacer click en la lista de problemas: {e}")
            raise Exception(f"Error al hacer click en la lista de problemas: {e}")

    def onClick_Antecedentes(self):
        """Hacer click en los antecedentes
        Raises:
            Exception: Error al hacer click en los antecedentes
        """
        try:
            self.logger.info("Haciendo click en los antecedentes")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en los antecedentes")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabAntecedentes)
            self.ui_adapter.click(self.locators.tabAntecedentes)
            self.logger.info("Se hizo click en los antecedentes")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en los antecedentes")
        except Exception as e:
            self.logger.error(f"Error al hacer click en los antecedentes: {e}")
            raise Exception(f"Error al hacer click en los antecedentes: {e}")

    def onClick_Alergias(self):
        """Hacer click en las alergias
        Raises:
            Exception: Error al hacer click en las alergias
        """
        try:
            self.logger.info("Haciendo click en las alergias")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en las alergias")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabAlergias)
            self.ui_adapter.click(self.locators.tabAlergias)
            self.logger.info("Se hizo click en las alergias")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en las alergias")
        except Exception as e:
            self.logger.error(f"Error al hacer click en las alergias: {e}")
            raise Exception(f"Error al hacer click en las alergias: {e}")

    def onClick_Nota_Medica(self):
        """Hacer click en la nota medica
        Raises:
            Exception: Error al hacer click en la nota medica
        """
        try:
            self.ui_adapter.wait_manager.wait_for_element_absent(*self.locators.loadingBarOn)
            self.logger.info("Haciendo click en la nota médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en la nota médica")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabNotaMedica)
            self.ui_adapter.click(self.locators.tabNotaMedica)
            self.logger.info("Se hizo click en la nota médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en la nota médica")
        except Exception as e:
            self.logger.error(f"Error al hacer click en la nota médica: {e}")
            raise Exception(f"Error al hacer click en la nota médica: {e}")

    def onClick_Estudios_complementarios(self):
        """Hacer click en los estudios complementarios
        Raises:
            Exception: Error al hacer click en los estudios complementarios
        """
        try:
            self.logger.info("Haciendo click en los estudios complementarios")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en los estudios complementarios")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabEstudiosComplementarios)
            self.ui_adapter.click(self.locators.tabEstudiosComplementarios)
            self.logger.info("Se hizo click en los estudios complementarios")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en los estudios complementarios")
        except Exception as e:
            self.logger.error(f"Error al hacer click en los estudios complementarios: {e}")
            raise Exception(f"Error al hacer click en los estudios complementarios: {e}")

    def onClick_Medicamentos_recetas(self):
        """Hacer click en los medicamentos recetas
        Raises:
            Exception: Error al hacer click en los medicamentos recetas
        """
        try:
            self.logger.info("Haciendo click en los medicamentos recetas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en los medicamentos recetas")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabMedicamentosYRecetas)
            self.ui_adapter.click(self.locators.tabMedicamentosYRecetas)
            self.logger.info("Se hizo click en los medicamentos recetas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en los medicamentos recetas")
        except Exception as e:
            self.logger.error(f"Error al hacer click en los medicamentos recetas: {e}")
            raise Exception(f"Error al hacer click en los medicamentos recetas: {e}")

    def onClick_Referencias_y_retornos(self):
        """Hacer click en las referencias y retornos
        Raises:
            Exception: Error al hacer click en las referencias y retornos
        """
        try:
            self.logger.info("Haciendo click en las referencias y retornos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en las referencias y retornos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabReferenciasYRetornos)
            self.ui_adapter.click(self.locators.tabReferenciasYRetornos)
            self.logger.info("Se hizo click en las referencias y retornos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en las referencias y retornos")
        except Exception as e:
            self.logger.error(f"Error al hacer click en las referencias y retornos: {e}")
            raise Exception(f"Error al hacer click en las referencias y retornos: {e}")

    def onClick_Incapacidad(self):
        """Hacer click en la incapacidad
        Raises:
            Exception: Error al hacer click en la incapacidad
        """
        try:
            self.logger.info("Haciendo click en la incapacidad")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en la incapacidad")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabIncapacidades)
            self.ui_adapter.click(self.locators.tabIncapacidades)
            self.logger.info("Se hizo click en la incapacidad")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en la incapacidad")
        except Exception as e:
            self.logger.error(f"Error al hacer click en la incapacidad: {e}")
            raise Exception(f"Error al hacer click en la incapacidad: {e}")

    def onClick_Califica_al_paciente(self):
        """Hacer click en califica al paciente
        Raises:
            Exception: Error al hacer click en califica al paciente
        """
        try:
            self.logger.info("Haciendo click en califica al paciente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en califica al paciente")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabCalificarAlPaciente)
            self.ui_adapter.click(self.locators.tabCalificarAlPaciente)
            self.logger.info("Se hizo click en califica al paciente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en califica al paciente")
        except Exception as e:
            self.logger.error(f"Error al hacer click en califica al paciente: {e}")
            raise Exception(f"Error al hacer click en califica al paciente: {e}")

    def onClick_Comentarios(self):
        """Hacer click en los comentarios
        Raises:
            Exception: Error al hacer click en los comentarios
        """
        try:
            self.logger.info("Haciendo click en los comentarios")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en los comentarios")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabComentarios)
            self.ui_adapter.click(self.locators.tabComentarios)
            self.logger.info("Se hizo click en los comentarios")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en los comentarios")
        except Exception as e:
            self.logger.error(f"Error al hacer click en los comentarios: {e}")
            raise Exception(f"Error al hacer click en los comentarios: {e}")

    def onClick_Signos_vitales(self):
        """Hacer click en los signos vitales
        Raises:
            Exception: Error al hacer click en los signos vitales
        """
        try:
            self.logger.info("Haciendo click en los signos vitales")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en los signos vitales")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tabSignosVitales)
            self.ui_adapter.click(self.locators.tabSignosVitales)
            self.logger.info("Se hizo click en los signos vitales")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en los signos vitales")
        except Exception as e:
            self.logger.error(f"Error al hacer click en los signos vitales: {e}")
            raise Exception(f"Error al hacer click en los signos vitales: {e}")

    def onClick_Abrir_llamada_nota_medica(self):
        """Hacer click en abrir llamada nota medica
        Raises:
            Exception: Error al hacer click en abrir llamada nota medica
        """
        try:
            self.logger.info("Haciendo click en el botón Abrir Llamada Nota Médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Abrir Llamada Nota Médica")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnAbrirLlamada)
            self.ui_adapter.click(self.locators.tipbtnAbrirLlamada)
            self.logger.info("Se hizo click en el botón Abrir Llamada Nota Médica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Abrir Llamada Nota Médica")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Abrir Llamada Nota Médica: {e}")
            raise Exception(f"Error al hacer click en Abrir Llamada Nota Médica: {e}")

    def onClick_Cita_administrativa(self):
        """Hacer click en cita administrativa
        Raises:
            Exception: Error al hacer click en cita administrativa
        """
        try:
            self.logger.info("Haciendo click en Cita Administrativa")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Cita Administrativa")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnCitaAdministrativa)
            self.ui_adapter.click(self.locators.tipbtnCitaAdministrativa)
            self.logger.info("Se hizo click en Cita Administrativa")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Cita Administrativa")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cita Administrativa: {e}")
            raise Exception(f"Error al hacer click en Cita Administrativa: {e}")

    def onClick_Referencia(self):
        """Hacer click en referencia
        Raises:
            Exception: Error al hacer click en referencia
        """
        try:
            self.logger.info("Haciendo click en Referencia")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Referencia")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnReferencia)
            self.ui_adapter.click(self.locators.tipbtnReferencia)
            self.logger.info("Se hizo click en Referencia")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Referencia")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Referencia: {e}")
            raise Exception(f"Error al hacer click en Referencia: {e}")

    def onClick_Incapacidades(self):
        """Hacer click en incapacidades
        Raises:
            Exception: Error al hacer click en incapacidades
        """
        try:
            self.logger.info("Haciendo click en Incapacidades")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Incapacidades")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnIncapacidades)
            self.ui_adapter.click(self.locators.tipbtnIncapacidades)
            self.logger.info("Se hizo click en Incapacidades")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Incapacidades")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Incapacidades: {e}")
            raise Exception(f"Error al hacer click en Incapacidades: {e}")

    def onClick_Recomendaciones(self):
        """Hacer click en recomendaciones
        Raises:
            Exception: Error al hacer click en recomendaciones
        """
        try:
            self.logger.info("Haciendo click en Recomendaciones")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Recomendaciones")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnRecomendaciones)
            self.ui_adapter.click(self.locators.tipbtnRecomendaciones)
            self.logger.info("Se hizo click en Recomendaciones")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Recomendaciones")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Recomendaciones: {e}")
            raise Exception(f"Error al hacer click en Recomendaciones: {e}")

    def onClick_Procedimientos_medicos(self):
        """Hacer click en procedimientos medicos
        Raises:
            Exception: Error al hacer click en procedimientos medicos
        """
        try:
            self.logger.info("Haciendo click en Procedimientos Médicos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Procedimientos Médicos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnProcedimientosMedicos)
            self.ui_adapter.click(self.locators.tipbtnProcedimientosMedicos)
            self.logger.info("Se hizo click en Procedimientos Médicos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Procedimientos Médicos")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Procedimientos Médicos: {e}")
            raise Exception(f"Error al hacer click en Procedimientos Médicos: {e}")

    def onClick_Imagenologia(self):
        """Hacer click en imagenologia
        Raises:
            Exception: Error al hacer click en imagenologia
        """
        try:
            self.logger.info("Haciendo click en Imagenología")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Imagenología")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnImagenologia)
            self.ui_adapter.click(self.locators.tipbtnImagenologia)
            self.logger.info("Se hizo click en Imagenología")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Imagenología")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Imagenología: {e}")
            raise Exception(f"Error al hacer click en Imagenología: {e}")

    def onClick_Laboratorio(self):
        """Hacer click en laboratorio
        Raises:
            Exception: Error al hacer click en laboratorio
        """
        try:
            self.logger.info("Haciendo click en Laboratorio")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Laboratorio")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnLaboratorio)
            self.ui_adapter.click(self.locators.tipbtnLaboratorio)
            self.logger.info("Se hizo click en Laboratorio")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Laboratorio")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Laboratorio: {e}")
            raise Exception(f"Error al hacer click en Laboratorio: {e}")

    def onClick_Recetas(self):
        """Hacer click en recetas
        Raises:
            Exception: Error al hacer click en recetas
        """
        try:
            self.logger.info("Haciendo click en Recetas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Recetas")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnReceta)
            self.ui_adapter.click(self.locators.tipbtnReceta)
            self.logger.info("Se hizo click en Recetas")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Recetas")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Recetas: {e}")
            raise Exception(f"Error al hacer click en Recetas: {e}")

    def onClick_Programar_cita(self):
        """Hacer click en programar cita
        Raises:
            Exception: Error al hacer click en programar cita
        """
        try:
            self.logger.info("Haciendo click en Programar Cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Programar Cita")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tipbtnProgramarCita)
            self.ui_adapter.click(self.locators.tipbtnProgramarCita)
            self.logger.info("Se hizo click en Programar Cita")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Programar Cita")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Programar Cita: {e}")
            raise Exception(f"Error al hacer click en Programar Cita: {e}")

    def onClick_Guardar_avance(self):
        """Hacer click en guardar avance
        Raises:
            Exception: Error al hacer click en guardar avance
        """
        try:
            self.logger.info("Haciendo click en Guardar Avance")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Guardar Avance")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGuardarAvance)
            self.ui_adapter.click(self.locators.btnGuardarAvance)
            self.logger.info("Se hizo click en Guardar Avance")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Guardar Avance")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Guardar Avance: {e}")
            raise Exception(f"Error al hacer click en Guardar Avance: {e}")

    def onClick_Finalizar(self):
        """Hacer click en finalizar
        Raises:
            Exception: Error al hacer click en finalizar
        """
        try:
            self.logger.info("Haciendo click en Finalizar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Finalizar")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnFinalizar)
            self.ui_adapter.click(self.locators.btnFinalizar)
            self.logger.info("Se hizo click en Finalizar")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Finalizar")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Finalizar: {e}")
            raise Exception(f"Error al hacer click en Finalizar: {e}")

    def set_consultar_por(self, consultar_por_data: str):
        """Seleccionar el valor de consultar por
        Args:
            consultar_por_data (str): Valor a seleccionar
        Raises:
            Exception: Error al seleccionar el valor de consultar por
        """
        try:
            consultar_por = consultar_por_data if consultar_por_data else self.data.get("consultar_por", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtConsultaPor)
            self.ui_adapter.send_keys(self.locators.txtConsultaPor, consultar_por)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Consultar Por: {e}")
            raise Exception(f"Error al configurar el campo Consultar Por: {e}")

    def set_triage(self, triage_data: str):
        """Escribir el valor de triage
        Args:
            consultar_por_data (str): Valor a seleccionar
        Raises:
            Exception: Error al seleccionar el valor de consultar por
        """
        try:
            triage = triage_data if triage_data else self.data.get("triage", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtTriage)
            self.ui_adapter.send_keys(self.locators.txtTriage, triage)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Consultar Por: {e}")
            raise Exception(f"Error al configurar el campo Consultar Por: {e}")

    def set_temperatura(self, temperatura_data: str):
        """Seleccionar el valor de temperatura
        Args:
            temperatura_data (str): Valor a seleccionar
        Raises:
            Exception: Error al seleccionar el valor de temperatura
        """
        try:
            temperatura = temperatura_data if temperatura_data else self.data.get("temperatura", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtTemp)
            self.ui_adapter.send_keys(self.locators.txtTemp, temperatura)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Temperatura: {e}")
            raise Exception(f"Error al configurar el campo Temperatura: {e}")

    def set_frecuencia_cardiaca(self, frecuencia_cardiaca_data: str):
        """Escribir el valor de frecuencia cardiaca
        Args:
            frecuencia_cardiaca_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Frecuencia Cardiaca
        """
        try:
            frecuencia_cardiaca = frecuencia_cardiaca_data if frecuencia_cardiaca_data else self.data.get("frecuencia_cardiaca", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtFC)
            self.ui_adapter.send_keys(self.locators.txtFC, frecuencia_cardiaca)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Frecuencia Cardiaca: {e}")
            raise Exception(f"Error al configurar el campo Frecuencia Cardiaca: {e}")

    def set_frecuencia_respiratoria(self, frecuencia_respiratoria_data: str):
        """Escribir el valor de frecuencia respiratoria
        Args:
            frecuencia_respiratoria_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Frecuencia Respiratoria
        """
        try:
            frecuencia_respiratoria = frecuencia_respiratoria_data if frecuencia_respiratoria_data else self.data.get("frecuencia_respiratoria", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtFR)
            self.ui_adapter.send_keys(self.locators.txtFR, frecuencia_respiratoria)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Frecuencia Respiratoria: {e}")
            raise Exception(f"Error al configurar el campo Frecuencia Respiratoria: {e}")

    def set_presion_arterial(self, presion_arterial_data: str):
        """Escribir el valor de presion arterial
        Args:
            presion_arterial_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Presion Arterial
        """
        try:
            presion_arterial = presion_arterial_data if presion_arterial_data else self.data.get("presion_arterial", "default")
            presion_arterial_sistolica, presion_arterial_diastolica = presion_arterial.split("/")

            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtPA)
            self.ui_adapter.send_keys(self.locators.txtPA, presion_arterial_sistolica)

            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.txtPA2)
            self.ui_adapter.send_keys(self.locators.txtPA2, presion_arterial_diastolica)

        except Exception as e:
            self.logger.error(f"Error al configurar el campo Presion Arterial: {e}")
            raise Exception(f"Error al configurar el campo Presion Arterial: {e}")

    def set_saturacion(self, saturacion_data: str):
        """Escribir el valor de saturacion
        Args:
            saturacion_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Saturacion
        """
        try:
            saturacion = saturacion_data if saturacion_data else self.data.get("saturacion", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtSat02)
            self.ui_adapter.send_keys(self.locators.txtSat02, saturacion)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Saturacion: {e}")
            raise Exception(f"Error al configurar el campo Saturacion: {e}")

    def set_peso(self, peso_data: str):
        """Escribir el valor de peso
        Args:
            peso_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Peso
        """
        try:
            peso = peso_data if peso_data else self.data.get("peso", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtPeso)
            self.ui_adapter.send_keys(self.locators.txtPeso, peso)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Peso: {e}")
            raise Exception(f"Error al configurar el campo Peso: {e}")

    def set_talla(self, talla_data: str):
        """Escribir el valor de talla
        Args:
            talla_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Talla
        """
        try:
            talla = talla_data if talla_data else self.data.get("talla", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtTalla)
            self.ui_adapter.send_keys(self.locators.txtTalla, talla)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Talla: {e}")
            raise Exception(f"Error al configurar el campo Talla: {e}")

    def setup_signos_vitales(self, signos_vitales_data: dict):
        """Configurar los signos vitales
        Args:
            signos_vitales_data (dict): Datos de los signos vitales
        Raises:
            Exception: Error al configurar los signos vitales
        """
        try:
            self.set_temperatura(signos_vitales_data.get("temperatura"))
            self.set_frecuencia_cardiaca(signos_vitales_data.get("frecuencia_cardiaca"))
            self.set_frecuencia_respiratoria(signos_vitales_data.get("frecuencia_respiratoria"))
            self.set_presion_arterial(signos_vitales_data.get("presion_arterial"))
            self.set_saturacion(signos_vitales_data.get("saturacion"))
            self.set_peso(signos_vitales_data.get("peso"))
            self.set_talla(signos_vitales_data.get("talla"))
        except Exception as e:
            self.logger.error(f"Error al configurar los signos vitales: {e}")
            raise Exception(f"Error al configurar los signos vitales: {e}")

    def set_presente_enfermedad(self, presente_enfermedad_data: str):
        """Escribir el valor de presente enfermedad
        Args:
            presente_enfermedad_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Presente Enfermedad
        """
        try:
            presente_enfermedad = presente_enfermedad_data if presente_enfermedad_data else self.data.get("presente_enfermedad", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtPresenteEnfermedad)
            self.ui_adapter.send_keys(self.locators.txtPresenteEnfermedad, presente_enfermedad)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Presente Enfermedad: {e}")
            raise Exception(f"Error al configurar el campo Presente Enfermedad: {e}")

    def set_apreciacion_diagnostica(self, apreciacion_diagnostica_data: str):
        """Escribir el valor de apreciacion diagnostica
        Args:
            apreciacion_diagnostica_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Apreciacion Diagnostica
        """
        try:
            apreciacion_diagnostica = apreciacion_diagnostica_data if apreciacion_diagnostica_data else self.data.get("apreciacion_diagnostica", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtApreciacionDiagnostica)
            self.ui_adapter.send_keys(self.locators.txtApreciacionDiagnostica, apreciacion_diagnostica)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Apreciacion Diagnostica: {e}")
            raise Exception(f"Error al configurar el campo Apreciacion Diagnostica: {e}")

    def onClick_Generar_apreciacion_diagnostica(self):
        """Hacer click en generar apreciacion diagnostica
        Raises:
            Exception: Error al hacer click en generar apreciacion diagnostica
        """
        try:
            self.logger.info("Haciendo click en Generar Apreciación Diagnóstica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Generar Apreciación Diagnóstica")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGenerarApreciacionDiagnostica)
            self.ui_adapter.click(self.locators.btnGenerarApreciacionDiagnostica)
            self.logger.info("Se hizo click en Generar Apreciación Diagnóstica")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Generar Apreciación Diagnóstica")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Generar Apreciación Diagnóstica: {e}")
            raise Exception(f"Error al hacer click en Generar Apreciación Diagnóstica: {e}")

    def set_diagnostico_principal(self, diagnostico_principal_data: str):
        """Escribir el valor de diagnostico principal
        Args:
            diagnostico_principal_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Diagnostico Principal
        """
        try:
            diagnostico_principal = diagnostico_principal_data if diagnostico_principal_data else self.data.get("diagnostico_principal", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtDiagnosticoPrincipal)
            self.ui_adapter.send_keys(self.locators.txtDiagnosticoPrincipal, diagnostico_principal)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Diagnostico Principal: {e}")
            raise Exception(f"Error al configurar el campo Diagnostico Principal: {e}")

    def set_button_diagnostico_principal(self, diagnostico_principal_data: str):
        """Hacer click en el boton diagnostico principal
        Raises:
            Exception: Error al hacer click en el boton Diagnostico Principal
        """
        try:
            diagnostico_principal = diagnostico_principal_data if diagnostico_principal_data else self.data.get("diagnostico_principal", "default")
            self.logger.info("Haciendo click en el botón Diagnóstico Principal")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en el botón Diagnóstico Principal")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btndgvCatalogoDiagnosticoPrincipal)
            self.datagrid.seleccionar_datagrid(self.locators.btndgvCatalogoDiagnosticoPrincipal, diagnostico_principal)
            self.logger.info("Se hizo click en el botón Diagnóstico Principal")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en el botón Diagnóstico Principal")
        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Diagnóstico Principal: {e}")
            raise Exception(f"Error al hacer click en el botón Diagnóstico Principal: {e}")

    ######################
    def set_diag_principal(self, diagnostico_principal_data: str):
        """Escribir el valor de diagnostico principal
        Args:
            diagnostico_principal_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Diagnostico Principal
        """
        try:
            diagnostico_principal = diagnostico_principal_data if diagnostico_principal_data else self.data.get("diagnostico_principal", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtDiagnosticoPrincipal)
            self.ui_adapter.send_keys_enter(self.locators.txtDiagnosticoPrincipal, diagnostico_principal)
            self.datagrid.selec_data(diagnostico_principal)
            time.sleep(2)

        except Exception as e:
            self.logger.error(f"Error al hacer click en el botón Diagnóstico Principal: {e}")
            raise Exception(f"Error al hacer click en el botón Diagnóstico Principal: {e}")

    ######################

    def onClick_generar_diagnostico_principal(self):
        """Hacer click en Generar Diagnostico Principal
        Raises:
            Exception: Error al hacer click en generar diagnostico principal
        """
        try:
            self.logger.info("Haciendo click en Generar Diagnóstico Principal")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Generar Diagnóstico Principal")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGenerarDiagnosticoPrincipal)
            self.ui_adapter.click(self.locators.btnGenerarDiagnosticoPrincipal)
            self.logger.info("Se hizo click en Generar Diagnóstico Principal")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Generar Diagnóstico Principal")
            time.sleep(5)
            self.ui_adapter.wait_manager.wait_for_element_absent(*self.locators.loadingBarOn)
        except Exception as e:
            self.logger.error(f"Error al hacer click en Generar Diagnóstico Principal: {e}")
            raise Exception(f"Error al hacer click en Generar Diagnóstico Principal: {e}")

    def onClick_Agregar_problema_activo(self, comentario_alta):
        """Hacer click en Agregar a Problemas Activos
        Raises:
            Exception: Error al hacer click en agregar diagnostico principal
        """
        try:
            self.logger.info("Haciendo click en Agregar a Problemas Activos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Agregar a Problemas Activos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAgregarProblemasActivos)
            self.ui_adapter.double_click(self.locators.btnAgregarProblemasActivos)
            self.logger.info("Se hizo click en Agregar a Problemas Activos")

            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Agregar a Problemas Activos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnSi)
            self.ui_adapter.click(self.locators.btnSi)

            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtAltaComentario)
            self.ui_adapter.clear(self.locators.txtAltaComentario)
            self.ui_adapter.send_keys_tab(self.locators.txtAltaComentario, comentario_alta)
            self.ui_adapter.click(self.locators.txtAltaComentario)
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.tbnGuardarComentario)
            self.ui_adapter.click(self.locators.tbnGuardarComentario)

        except Exception as e:
            self.logger.error(f"Error al hacer click en Agregar a Problemas Activos: {e}")
            raise Exception(f"Error al hacer click en Agregar a Problemas Activos: {e}")

    def set_diagnostico_secundario(self, diagnostico_secundario_data: str):
        """Escribir el valor de diagnostico secundario
        Args:
            diagnostico_secundario_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Diagnostico Secundario
        """
        try:
            diagnostico_secundario = diagnostico_secundario_data if diagnostico_secundario_data else self.data.get("diagnostico_secundario", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtDiagnosticoSecundario)
            self.ui_adapter.send_keys(self.locators.txtDiagnosticoSecundario, diagnostico_secundario)
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Diagnostico Secundario: {e}")
            raise Exception(f"Error al configurar el campo Diagnostico Secundario: {e}")

    def onClick_Agregar_diagnostico_secundario(self):
        """Hacer click en Agregar a Problemas Activos
        Raises:
            Exception: Error al hacer click en agregar diagnostico secundario
        """
        try:
            self.logger.info("Haciendo click en Agregar a Problemas Activos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Agregar a Problemas Activos")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnAgregarProblemaSecundario)
            self.ui_adapter.click(self.locators.btnAgregarProblemaSecundario)
            self.logger.info("Se hizo click en Agregar a Problemas Activos")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Agregar a Problemas Activos")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Agregar a Problemas Activos: {e}")
            raise Exception(f"Error al hacer click en Agregar a Problemas Activos: {e}")

    def onClick_Mostrar_plan(self):
        """Hacer click en mostrar plan
        Raises:
            Exception: Error al hacer click en mostrar plan
        """
        try:
            self.logger.info("Haciendo click en Mostrar Plan")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Mostrar Plan")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnMostrarPlan)
            self.ui_adapter.click(self.locators.btnMostrarPlan)
            self.logger.info("Se hizo click en Mostrar Plan")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Mostrar Plan")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Mostrar Plan: {e}")
            raise Exception(f"Error al hacer click en Mostrar Plan: {e}")

    def set_calificacion_paciente(self, calificacion_paciente_data: str):
        """Escribir el valor de calificacion paciente
        Args:
            calificacion_paciente_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Calificacion Paciente
        """
        try:
            calificacion_paciente = calificacion_paciente_data if calificacion_paciente_data else self.data.get("calificacion_paciente", "default")
            if calificacion_paciente not in ["1", "2", "3", "4", "5"]:
                raise ValueError("La calificación del paciente debe ser un número entre 1 y 5")

            btn_map = {
                "1": self.locators.btnCalificacion1,
                "2": self.locators.btnCalificacion2,
                "3": self.locators.btnCalificacion3,
                "4": self.locators.btnCalificacion4,
                "5": self.locators.btnCalificacion5,
            }

            btn_locator = btn_map[calificacion_paciente]
            self.ui_adapter.wait_manager.wait_for_element_clickable(*btn_locator)
            self.ui_adapter.click(btn_locator)

            self.logger.info(f"Se configuró la calificación del paciente: {calificacion_paciente}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se configuró la calificación del paciente: {calificacion_paciente}")
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Calificacion Paciente: {e}")
            raise Exception(f"Error al configurar el campo Calificacion Paciente: {e}")

    def set_motivo_de_evaluacion(self, motivo_de_evaluacion_data: str):
        """Seleccionar el motivo de evaluacion
        Args:
            motivo_de_evaluacion_data (str): Valor a seleccionar
        Raises:
            Exception: Error al seleccionar el motivo de evaluacion
        """
        try:
            motivo_de_evaluacion = motivo_de_evaluacion_data if motivo_de_evaluacion_data else self.data.get("motivo_de_evaluacion", "default")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.cmbMotivoDeEvaluacion)
            self.combobox.seleccionar_elemento_por_texto(self.locators.cmbMotivoDeEvaluacion, motivo_de_evaluacion)
            self.logger.info(f"Se configuró el motivo de evaluación: {motivo_de_evaluacion}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se configuró el motivo de evaluación: {motivo_de_evaluacion}")
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Motivo de Evaluación: {e}")
            raise Exception(f"Error al configurar el campo Motivo de Evaluación: {e}")

    def set_resena(self, resena_data: str):
        """Escribir la reseña del paciente
        Args:
            resena_data (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Reseña
        """
        try:
            resena = resena_data if resena_data else self.data.get("resena", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtResena)
            self.ui_adapter.send_keys(self.locators.txtResena, resena)
            self.logger.info(f"Se configuró la reseña del paciente: {resena}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se configuró la reseña del paciente: {resena}")
        except Exception as e:
            self.logger.error(f"Error al configurar el campo Reseña: {e}")
            raise Exception(f"Error al configurar el campo Reseña: {e}")

    def onClick_Cancelar_calificacion(self):
        """Hacer click en cancelar calificacion
        Raises:
            Exception: Error al hacer click en cancelar calificacion
        """
        try:
            self.logger.info("Haciendo click en Cancelar Calificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Cancelar Calificación")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnCancelarCalificacion)
            self.ui_adapter.click(self.locators.btnCancelarCalificacion)
            self.logger.info("Se hizo click en Cancelar Calificación")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Cancelar Calificación")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Cancelar Calificación: {e}")
            raise Exception(f"Error al hacer click en Cancelar Calificación: {e}")

    def onClick_Calificar_paciente(self):
        """Hacer click en calificar paciente
        Raises:
            Exception: Error al hacer click en calificar paciente
        """
        try:
            self.logger.info("Haciendo click en Calificar Paciente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Haciendo click en Calificar Paciente")
            self.ui_adapter.wait_manager.wait_for_element_clickable(*self.locators.btnGuardarCalificacion)
            self.ui_adapter.click(self.locators.btnGuardarCalificacion)
            self.logger.info("Se hizo click en Calificar Paciente")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, "Se hizo click en Calificar Paciente")
        except Exception as e:
            self.logger.error(f"Error al hacer click en Calificar Paciente: {e}")
            raise Exception(f"Error al hacer click en Calificar Paciente: {e}")

    def set_gridview_diagnostico_principal(self, diagnostico_principal: str):
        """Para usar el select box que se abre al salir del campo Diagnostico Principal
        Args:
            diagnostico_principal (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Diagnostico Principal
        """
        try:
            diagnostico_principal = diagnostico_principal if diagnostico_principal else self.data.get("diagnostico_principal", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtDiagnosticoPrincipal)
            self.ui_adapter.send_keys_enter(self.locators.txtDiagnosticoPrincipal, diagnostico_principal)
            self.datagrid.selec_data(diagnostico_principal)

        except Exception as e:
            self.logger.error(f"Error al iteractuar con el grid de Diagnóstico Principal: {e}")
            raise Exception(f"Error al iteractuar con el grid de Diagnóstico Principal: {e}")

    def set_gridview_diagnostico_secundario(self, diagnostico_secundario: str):
        """Para usar el select box que se abre al salir del campo Diagnostico Secundario
        Args:
            diagnostico_secundario (str): Valor a escribir
        Raises:
            Exception: Error al configurar el campo Diagnostico Secundario
        """
        try:
            diagnostico_secundario = diagnostico_secundario if diagnostico_secundario else self.data.get("diagnostico_secundario", "default")
            self.ui_adapter.wait_manager.wait_for_element_typing(*self.locators.txtDiagnosticoSecundario)
            self.ui_adapter.send_keys_enter(self.locators.txtDiagnosticoSecundario, diagnostico_secundario)
            self.datagrid.selec_data(diagnostico_secundario)
            time.sleep(2)

        except Exception as e:
            self.logger.error(f"Error al iteractuar con el grid de Diagnóstico Secundario: {e}")
            raise Exception(f"Error al iteractuar con el grid de Diagnóstico Secundario: {e}")

    def set_plan_tratamiento(self, plan_tratamiento: str):
        """LLena el campo de plan de tratamiento
        Args:
            plan_tratamiento (str): Valor a seleccionar
        Raises:
            Exception: Error al seleccionar el plan de tratamiento
        """
        try:

            self.ui_adapter.wait_manager.wait_for_element_visible(*self.locators.txtPlanTratamiento)
            self.ui_adapter.click(self.locators.txtPlanTratamiento)
            self.ui_adapter.send_keys(self.locators.txtPlanTratamiento, plan_tratamiento)
            self.logger.info(f"Se configuró el plan de tratamiento: {plan_tratamiento}")
            self.ui_adapter.take_screenshot(self.test_config.screenshot_dir, f"Se configuró el plan de tratamiento: {plan_tratamiento}")
        except Exception as e:
            self.logger.error(f"Error al configurar el campo plan de tratamiento: {e}")
            raise Exception(f"Error al configurar el campo plan de tratamiento: {e}")
