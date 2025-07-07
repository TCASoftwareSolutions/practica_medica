from selenium.webdriver.common.by import By


class PanelDeEncargadoDeTurnoLocators:
    """Clase para almacenar los localizadores del programa Panel de Encargado de Turno.
    Esta clase contiene los selectores necesarios para interactuar con los elementos de la interfaz de usuario
    """

    app_name = "mp_jefedeturno"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Panel de encargado de turno']")
    tab_agenda_medica = (By.XPATH, "//span[contains(@title,'MP_JEFEDETURNO')][normalize-space()='Panel de encargado de turno']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_MP_JEFEDETURNO')]")
