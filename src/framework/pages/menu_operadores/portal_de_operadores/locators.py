from selenium.webdriver.common.by import By


class PortalOperadoresLocators:
    """Clase para almacenar los localizadores del programa Portal de Operadores"""

    app_name = "mp_callcenter"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Portal de Operadores']")
    tab_portal_de_operadores = (By.XPATH, "//span[contains(@title,'MP_CALLCENTER')][normalize-space()='Portal de Operadores']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_MP_CALLCENTER')]")

    # toolbar
    tipCerrar = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_mpCallcenterTCAToolBarDesigner1ID_F99')]")

    # barra lateral izquierda
    btnRegistro = (By.XPATH, "//button[contains(@id,'btnIdMenuLate0MP_Callcenter')]")
    btnGestionDeCitas = (By.XPATH, "//button[normalize-space()='Gestión de Citas']")

    # REGISTRO
    # STEP Identificacion
    lblTituloIdentificacion = (By.XPATH, "//span[normalize-space()='Identificación del beneficiario']")
    cmbTipoDeDocumento = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_Tkdropdownlist1_wrapper')]//span[@role='listbox']")
    txtClaveDeDocumento = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_Tktextbox1')]")
    txtFechaDeNacimiento = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_MP_HOS930_TCADateTextBox1')]")
    # cmbLadaTelefono = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_Tktextbox3_wrapper')]//span[@class='k-widget k-combobox tkcombobox-input']")
    cmbLadaTelefono = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_Tktextbox3_wrapper')]")
    txtNumeroTelefono = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_MP_HOS930_TKTextBox5')]")
    cmbGenero = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosDocumento_MP_RegistroGenero_wrapper')]//span[contains(@class, 'k-widget k-dropdown tkdropdownlist-input')]")

    # STEP Verificacion
    lblTituloVerificacion = (By.XPATH, "//span[normalize-space()='Verificación de código']")
    btnEnviarPorSMS = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosPaciente_TCAPanel1_TKButton1')]")
    # msgCodigoEnviado = (By.XPATH, "//div[contains(@class, 'alertify-notifier ajs-top ajs-right')]//div[contains(@class, 'ajs-message ajs-success ajs-visible')]")
    msgCodigoEnviado = (By.XPATH, "//div[contains(@class, 'ajs-message') and starts-with(normalize-space(.), 'Se envió el código por SMS.')]")
    txtCodigo = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosPaciente_TCAPanel2_Tktextbox2')]")

    # STEP Resumen
    lblTituloResumen = (By.XPATH, "//span[normalize-space()='Resumen del registro']")
    txtCorreoElectronico = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_MPCallcenter_RegistropanelDatosResumen_Tktextbox8')]")

    # Modal Beneficiario Generado Correctamente
    modalBeneficiarioGenerado = (By.XPATH, "//div[contains(@class,'ajs-dialog')]")
    lblBeneficiarioGenerado = (By.XPATH, "//b[normalize-space()='Beneficiario generado exitosamente:Usuario:']")
    btnAceptarBeneficiarioGenerado = (By.XPATH, "//div[@class='ajs-dialog']//button[normalize-space()='OK']")
    lblYaSeEncuentraRegistrado = (By.XPATH, "//div[@class='ajs-content' and contains(., 'El beneficiario') and contains(., 'ya se encuentra registrado')]")

    btnSiguiente = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_wizard_next')]")
    btnAnterior = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_wizard_previous')]")
    btnCancelar = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterRegistroMP_MPCallcenter_RegistroWizar_wizard_cancel')]")

    # GESTION DE CITAS
    cmbCitasTipoDeDocumento = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanel_MPCallcenter_CitasGrid_TipoDocumento_wrapper')]//span[@role='listbox']")
    txtCitasClaveDeDocumento = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanel_MPCallcenter_CitasGrid_Documento')]")
    msgNoCitasProgramadas = (By.XPATH, "//div[contains(@class, 'ajs-message ajs-warning') and starts-with(normalize-space(.), 'No se encontraron citas programadas')]")
    btnLimpiar = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanel_MPCallcenter_CitasGrid_Limpiar')]")
    btnFiltrar = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanel_MPCallcenter_CitasGrid_Filtrar')]")
    btnAgendarCita = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanel_MPCallcenter_CitasGrid_Crear')]")
    btnEditar = (By.XPATH, "//a[contains(@class,'k-button k-button-icontext k-grid-edit')]")
    btnEliminar = (By.XPATH, "//a[@class='k-button k-button-icontext k-grid-DelCol']")

    # Modal envio OTP
    modalEnvioDeMensajesOTP = (By.XPATH, "//div[contains(@class,'ajs-header')][normalize-space()='Envio de mensajes OTP']")
    btnEnviarOTPporSMS = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_otpservice_panel1_otpservice_panel2_otpservice_btn_1')]")
    btnEnviarOTPporEmail = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_otpservice_panel1_otpservice_panel2_otpservice_btn_2')]")
    btnSinOTP = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_otpservice_panel1_otpservice_panel2_otpservice_btn_3')]")
    txtCodigoDeVerificacionModalOTP = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_otpservice_panel1_otpservice_panel3_otpservice_txt_campo')]")
    btnContinuarModalOTP = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_otpservice_btn_confirmar')]")
    btnCerrarModalOTP = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_otpservice_btn_close')]")

    # Modal Agendar cita
    modalAgendarCita = (By.XPATH, "//div[contains(@class,'ajs-header')][normalize-space()='Agendar cita']")
    txtFecha = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_altaFecha')]")
    cmbHoraInicio = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_editHoraIni_wrapper')]//span[@role='listbox']")
    cmbCanalDeAtencion = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_ddl_tipo_consulta_wrapper')]//span[@role='listbox']")
    btnCerrarModalAgendarCita = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_TKButton4')]")
    btnGuardarModalAgendarCita = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_TKButton5')]")

    # Modal Editar Cita
    modalEditarCita = (By.XPATH, "//div[contains(@class,'ajs-header')][normalize-space()='Editar cita']")

    # Modal motivo de editar la cita
    modalMotivoDeEditarCita = (By.XPATH, "//div[contains(@class,'ajs-header')][normalize-space()='Motivo de editar la cita']")
    btndgvMotivo = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_tMP_call_MotAut_catalogButton')]")
    txtdgvMotivo = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_tMP_call_MotAut')]")
    btnSalirModalEditarCita = (By.XPATH, "//button[contains(@id,'ctl00_nc003_MP_CALLCENTER_v10CallCenterCitasMP_MP_call_btnCancel')]")
    btnAceptarModalEditarCita = (By.XPATH, "//button[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MP_call_btnOk')]")

    # Motivo de cancelación de cita
    modalMotivoDeCancelacion = (By.XPATH, "//div[contains(@class,'ajs-header')][normalize-space()='Motivo de cancelación de cita']")

    msgLimiteDeCitas = (By.XPATH, "//div[contains(@class, 'ajs-message ajs-warning') and starts-with(normalize-space(.), 'No se puede asignar una cita, debido a que ya cuenta con una cita')]")
    msgNoHayCitas = (By.XPATH, "//div[contains(@class, 'ajs-message ajs-warning') and starts-with(normalize-space(.), 'No se encontraron citas programadas')]")
    msgCitaGeneradaConExito = (By.XPATH, "//div[contains(@class, 'ajs-message') and starts-with(normalize-space(.), 'Se ha generado la cita con el número')]")
    msgCitaReagendadaConExito = (By.XPATH, "//div[contains(@class, 'ajs-message ajs-success') and starts-with(normalize-space(.), 'Se ha actualizado el registro de la cita')]")
    msgCitaCanceladaConExito = (By.XPATH, "//div[contains(@class, 'ajs-message ajs-success') and starts-with(normalize-space(.), 'Se ha cambiado el estatus a cita cancelada')]")
    msgImposibleCancelar = (By.XPATH, "//div[contains(@class, 'ajs-message') and starts-with(normalize-space(.), 'Solo es posible cancelar citas que tienen el estatus')]")
    msgImposibleEditar = (By.XPATH, "//div[contains(@class, 'ajs-message') and starts-with(normalize-space(.), 'Solo es posible editar citas que tienen el estatus')]")

    # grid
    txtGridSearch = (By.XPATH, "//input[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanelGrid_MPCallcenter_CitasGrid_searchBox')]")
    lblNoExistenRegistros = (By.XPATH, "//div[contains(@id,'MP_CALLCENTER_v10CallCenterCitasMP_MPCallcenter_CitasPanelGrid_MPCallcenter_CitasGrid')]//div[contains(@class,'k-grid-norecords')][normalize-space()='No hay registros para mostrar']")
    lblNumeroDeCita = (By.XPATH, "//td[@id='MPCallcenter_CitasGrid_T224_CFld1_Idx1']")
