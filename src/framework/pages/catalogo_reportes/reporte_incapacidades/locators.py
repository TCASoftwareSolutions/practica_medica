from selenium.webdriver.common.by import By


class ReporteDeIncapacidadesLocators:
    """Clase para almacenar los localizadores del programa de Reporte de incapacidades.
    Esta clase contiene los selectores necesarios para interactuar con los elementos de la interfaz de usuario
    """

    app_name = "repReportPreview594"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Reporte de incapacidades']")
    tab_reporte_incapacidades = (By.XPATH, "//span[contains(@title , 'repReportPreview594(DB)')] [normalize-space()='Reporte de incapacidades']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_repReportPreview594')]")

    # toolbar
    loadingBarOn = (By.XPATH, "//div[@class='line-loader']")
    notificationsDiv = (By.XPATH, "//div[contains(@class, 'alertify-notifier')]/descendant::div")

    # Inputs
    btnModificarParam = (By.XPATH, "//button[contains(@id, 'repReportPreview594_ReportSplitter_TCAButton2')]")
    fchInicail = (By.XPATH, " //span[contains(@class, 'riContentWrapper')]/input[contains(@tabindex, '3')]")
    fchFinal = (By.XPATH, " //span[contains(@class, 'riContentWrapper')]/input[contains(@tabindex, '4')] ")
    Documento = (By.XPATH, " //span[contains(@class, 'riContentWrapper')]/input[contains(@tabindex, '5')] ")
    btnActualizar = (By.XPATH, "//span[contains(@id, 'repReportPreview594_ReportSplitter_GetReportBtn')]")

    # table
    tableInfo = (By.XPATH, "//span[contains(@class, 'k-pager-info')]")
    tableRow = (By.XPATH, "//table[contains(@class, 'k-selectable')]/descendant::tr[contains(@role, 'row')]")
