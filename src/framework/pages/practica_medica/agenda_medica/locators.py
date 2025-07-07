from selenium.webdriver.common.by import By


class AgendaMedicaLocators:
    """Clase para almacenar los localizadores del programa Agenda Medica."""

    app_name = "mp_hos930"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Agenda médica']")
    tab_agenda_medica = (By.XPATH, "//span[contains(@title,'MP_HOS930')][normalize-space()='Agenda médica']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_MP_HOS930')]")
    app_loading = (By.XPATH, "//div[@id='loading-zone']")

    # toolbar
    tipCerrar = (By.XPATH, "//div[contains(@id,'MP_HOS930_MP_HOS930_TCAToolBarDesigner1ID_F99')]")
    tipActualizar = (By.XPATH, "//div[contains(@id,'MP_HOS930_MP_HOS930_TCAToolBarDesigner1ID_F5')]")
    tipLimpiar = (By.XPATH, "//div[contains(@id,'MP_HOS930_MP_HOS930_TCAToolBarDesigner1ID_F3')]")

    cmbEspecialidad = (By.XPATH, "//select[contains(@id,'MP_HOS930_MP_HOS930_TCAToolBarDesigner1ID_F2')]")
    btnFiltrar = (By.XPATH, "//div[contains(@id,'MP_HOS930_btnFiltrar_wrapper')]/descendant::button[contains(@id,'MP_HOS930_btnFiltrar')]")
    cmbEscalas = (By.XPATH, "//div[contains(@id,'MP_HOS930_Escalas_wrapper')]/descendant::span[contains(@aria-owns, 'MP_HOS930_Escalas_listbox')]")
    btnDescansa = (By.XPATH, "//div[contains(@id,'MP_HOS930_PanelFiltros_TkbutonPause_wrapper')]/descendant::button[contains(@id,'MP_HOS930_PanelFiltros_TkbutonPause')]")
    btnTerminarDescanso = (By.XPATH, "//div[contains(@id,'MP_HOS930_PanelFiltros_TkbutonPauseD')]/descendant::button[contains(@id,'MP_HOS930_PanelFiltros_TkbutonPause')]")

    divNuevaCitaAsignada = (By.XPATH, "//div[contains(@class,'MP_infopaciente-card-standard')]")
    btnAbrirModulo_card = (By.XPATH, "//div[contains(@class,'MP_infopaciente-card-standard')]/descendant::button[contains(@class,'MP_infopaciente-action-button')]")

    btnModulo = (By.XPATH, "//button[contains(@onclick, 'TKScheduler_ButtonClickTooltip')][contains(text(),'Módulo')]")
    lblHorario = (By.XPATH, "//div[contains(@id,'MP_HOS930_Scheduler1_wrapper')]//tr/th[@class='k-slot-cell']")
    # //tr/th[@class='k-slot-cell'][span[text()='11:00'] and span[text()='AM']]
    # //div[@class='k-scheduler-content']//tr[1]/td[@class='k-today' and @role='gridcell']
    # //div[contains(@role,'gridcell')][contains(@class,'tcakschedulerGray2')]
    citasInasistencias = (By.XPATH, "//div[contains(@role,'gridcell')][contains(@class,'tcakschedulerRed')]")
    citasFinalizadas = (By.XPATH, "//div[contains(@role,'gridcell')][contains(@class,'tcakschedulerViolet')]")
    citasProgramadas = (By.XPATH, "//div[contains(@role,'gridcell')][contains(@class,'tcakschedulerGray2')]")

    ### CREACION DE CITAS
    txtClaveDocumento = (By.XPATH, "//div[contains(@id,'MP_HOS930_altaclavedoc_wrapper')]/descendant::input[contains(@id,'MP_HOS930_altaclavedoc')]")
    cmbReferido = (By.XPATH, "//div[contains(@id,'MP_HOS930_altaReferido_wrapper')]/descendant::span[contains(@aria-owns,'MP_HOS930_altaReferido_listbox')]")
    btnGuardarNuevaCita = (By.XPATH, "//div[contains(@id,'MP_HOS930_altaBtnGuardar_wrapper')]/descendant::button")
    btnCerrarNuevaCita = (By.XPATH, "//div[contains(@id,'MP_HOS930_altaBtnCerrar_wrapper')]/descendant::button")
