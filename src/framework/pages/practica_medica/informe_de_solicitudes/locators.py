from selenium.webdriver.common.by import By


class InformeDeSolicitudesLocators:
    """Clase para almacenar los localizadores del programa Informe de Solicitudes.
    Esta clase contiene los selectores necesarios para interactuar con los elementos de la interfaz de usuario
    """

    app_name = "mp_informesolicitudes"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Informe de Solicitudes']")
    tab_informe_de_solicitudes = (By.XPATH, "//span[contains(@title,'mp_informesolicitudes')][normalize-space()='Informe de Solicitudes']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_MP_INFORMESOLICITUDES')]")

    cmb_tipo_de_informe = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt1_wrapper')]/descendant::span[contains(@aria-owns,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt1_listbox')]")
    txt_id = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt2_wrapper')]/descendant::input[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt2')]")
    cmb_tipo_de_documento = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt3_wrapper')]/descendant::span[contains(@aria-owns,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt3_listbox')]")
    txt_clave_de_documento = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt4_wrapper')]/descendant::input[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt4')]")

    btn_limpiar = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt7_wrapper')]/descendant::button[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt7')]")
    btn_filtrar = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt8_wrapper')]/descendant::button[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_filtros_mpinf_txt8')]")

    btn_medicamentos = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_listview_KendoListSelectTabHorTemplate')]/descendant::button[contains(@id,'btnSelectComboId0')]")
    btn_laboratorio = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_listview_KendoListSelectTabHorTemplate')]/descendant::button[contains(@id,'btnSelectComboId1')]")
    btn_imagenes = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_listview_KendoListSelectTabHorTemplate')]/descendant::button[contains(@id,'btnSelectComboId2')]")

    btn_exportar_pdf = (By.XPATH, "//div[contains(@id,'mpinf_pnl_grid3_mpinf_grid3_buttonsZone')]/descendant::a[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_grid3_mpinf_grid3_toolbar_exportpdf')]")
    btn_exportar_excel = (By.XPATH, "//div[contains(@id,'mpinf_pnl_grid3_mpinf_grid3_buttonsZone')]/descendant::a[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_grid3_mpinf_grid3_toolbar_exportexcel')]")
    btn_exportar_csv = (By.XPATH, "//div[contains(@id,'mpinf_pnl_grid3_mpinf_grid3_buttonsZone')]/descendant::a[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_grid3_mpinf_grid3_toolbar_exportcsv')]")

    lbl_no_data = (By.XPATH, "//div[contains(@id,'MP_INFORMESOLICITUDES_mpinf_pnl_contenido_mpinf_pnl_grid1_mpinf_grid1')]/descendant::div[@class='k-grid-norecords'][contains(text(),'No hay información')]")
