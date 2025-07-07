from selenium.webdriver.common.by import By


class TableroMedicoLocators:
    """Clase para almacenar los localizadores del programa de Tablero Médico.
    Esta clase contiene los selectores necesarios para interactuar con los elementos de la interfaz de usuario
    """

    app_name = "mp_tableromedico"
    app_title = (By.XPATH, "//div[@class='title'][normalize-space()='Tablero Médico']")
    tab_tablero_medico = (By.XPATH, "//span[contains(@title,'MP_TableroMedico')][normalize-space()='Tablero Médico']")
    app_close = (By.XPATH, "//input[contains(@onclick,'tab_MP_TableroMedico')]")

    # Información del paciente
    imgPaciente = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXImgUser_wrapper')]/descendant::button[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXImgUser')]")
    lblNombreDelPaciente = (By.XPATH, "//span[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXtcaNombre')]")
    lblExpediente = (By.XPATH, "//span[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXlblExpedientetxt')]")
    lblEdad = (By.XPATH, "//span[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXlblEdadtxt')]")
    lblFechaDeNacimiento = (By.XPATH, "//span[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXlblFechaNcText')]")
    lblSexo = (By.XPATH, "//span[contains(@id,'MP_TableroMedico_v10HeaderCEX_ctl00_CEXlblSexoText')]")

    # toolbar
    tipMoverAEspera = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_mpTabMedTCAToolBarDesigner1_wrapper')]/descendant::div[contains(@id,'mpTabMedTCAToolBarDesigner1ID_F4')]")
    tipAbrirLlamada = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_mpTabMedTCAToolBarDesigner1_wrapper')]/descendant::div[contains(@id,'mpTabMedTCAToolBarDesigner1ID_F2')]")
    tipFinalizarCita = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_mpTabMedTCAToolBarDesigner1_wrapper')]/descendant::div[contains(@id,'mpTabMedTCAToolBarDesigner1ID_F1')]")
    tipSalir = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_mpTabMedTCAToolBarDesigner1_wrapper')]/descendant::div[contains(@id,'mpTabMedTCAToolBarDesigner1ID_F99')]")

    tabLineaDeTiempo = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate0MP_TableroMedico')]")
    tabListaDeProblemas = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate2MP_TableroMedico')]")
    tabAntecedentes = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate3MP_TableroMedico')]")
    tabAlergias = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate4MP_TableroMedico')]")
    tabNotaMedica = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate5MP_TableroMedico')]")
    tabEstudiosComplementarios = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate6MP_TableroMedico')]")
    tabMedicamentosYRecetas = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate7MP_TableroMedico')]")
    tabReferenciasYRetornos = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate8MP_TableroMedico')]")
    tabIncapacidades = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate9MP_TableroMedico')]")
    tabCalificarAlPaciente = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate10MP_TableroMedico')]")
    tabComentarios = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate11MP_TableroMedico')]")
    tabSignosVitales = (By.XPATH, "//div[contains(@id,'MP_TableroMedico_ctl00_KendoListSelectTabMedTemplate_wrapper')]/descendant::button[contains(@id,'btnIdMenuLate12MP_TableroMedico')]")

    # Información del paciente - Línea de tiempo
    txtFechaInicio = (By.XPATH, "//div[contains(@id,'MPTableroMedico_FilRngFec1_wrapper')]/descendant::input[contains(@id,'MP_TableroMedico_v10InicioMP_MPTableroMedicoInicio_pnlFiltros_MPTableroMedico_FilRngFec1')]")
    txtFechaFin = (By.XPATH, "//div[contains(@id,'MPTableroMedico_FilRngFec2_wrapper')]/descendant::input[contains(@id,'MP_TableroMedico_v10InicioMP_MPTableroMedicoInicio_pnlFiltros_MPTableroMedico_FilRngFec2')]")
    txtFiltro = (By.XPATH, "//div[contains(@id,'MPTableroMedico_Filtro_wrapper')]/descendant::input[contains(@id,'MPTableroMedicoInicio_pnlFiltros_MPTableroMedico_Filtro')]")
    btnFiltrar = (By.XPATH, "//div[contains(@id,'MPTableroMedico_BtnFiltrar_wrapper')]/descendant::button[contains(@id,'MPTableroMedicoInicio_pnlFiltros_MPTableroMedico_BtnFiltrar')]")
    btnLimpiar = (By.XPATH, "//div[contains(@id,'MPTableroMedico_BtnLimpiar_wrapper')]/descendant::button[contains(@id,'MPTableroMedicoInicio_pnlFiltros_MPTableroMedico_BtnLimpiar')]")

    # Información del paciente - Lista de problemas
    cmbEstado = (By.XPATH, "//div[contains(@id,'MPTableroMedico_pnlProblemas_mpTabMed_Estado1_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_pnlProblemas_mpTabMed_Estado1_listbox')]")

    # Información del paciente - Antecedentes
    # Discapacidad certificada
    chkDiscapacidadCertificadaAfirmativo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10002_Si')]")
    chkDiscapacidadCertificadaNegativo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10002_No')]")
    chkDiscapacidadCertificadaNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10002_NA')]")
    txtDiscapacidadCual = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_ant_ddl_3513')]")

    # Discapacidad limita actividades
    chkDiscapacidadLimitaSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10004_Si')]")
    chkDiscapacidadLimitaNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10004_No')]")
    chkDiscapacidadLimitaNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10004_NA')]")
    txtDiscapacidadActividad = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_ant_ddl_3515')]")

    # Cuidador
    chkCuidadorSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10006_Si')]")
    chkCuidadorNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10006_No')]")
    chkCuidadorNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10006_NA')]")

    # Dificultad para caminar
    chkDificultadCaminarSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10007_Si')]")
    chkDificultadCaminarNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10007_No')]")
    chkDificultadCaminarNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10007_NA')]")
    txtDificultadCaminarCual = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_ant_ddl_3518')]")

    # Cintura
    txtCintura = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TKSwitch4')]")

    # Presión arterial
    txtPresionSistolica = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TkNumericBox1')]")
    txtPresionDiastolica = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TkNumericBox2')]")

    # Fuma
    chkFumaSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10012_Si')]")
    chkFumaNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10012_No')]")
    chkFumaNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10012_NA')]")
    txtFumaTiempo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_ant_ddl_3621')]")
    txtFumaCantidad = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_ant_ddl_3520')]")

    # Control colesterol
    chkColesterolSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10015_Si')]")
    chkColesterolNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10015_No')]")
    chkColesterolNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10015_NA')]")
    txtColesterolFecha = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_Tkdatetimepicker1')]")
    txtColesterolValor = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TKDropDownList1')]")

    # Test Framingham
    chkFraminghamSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10018_Si')]")
    chkFraminghamNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10018_No')]")
    chkFraminghamNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10018_NA')]")
    txtFraminghamFecha = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_Tkdatetimepicker2')]")

    # Verduras
    chkVerdurasSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10021_Si')]")
    chkVerdurasNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10021_No')]")
    chkVerdurasNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10021_NA')]")
    txtVerdurasPorciones = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TKDropDownList2')]")

    # Frutas
    chkFrutasSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10023_Si')]")
    chkFrutasNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10023_No')]")
    chkFrutasNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10023_NA')]")
    txtFrutasPorciones = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TKDropDownList3')]")

    # Análisis de orina
    chkOrinaSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10025_Si')]")
    chkOrinaNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10025_No')]")
    chkOrinaNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10025_NA')]")
    txtOrinaFecha = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_Tkdatetimepicker3')]")

    # 12. Consulta de inscripción por médico general, pediatra y/o neonatólogo
    chkConsultaInscripcionSi = (By.XPATH, "//input[contains(@id,'mp_10027_Si')]")
    chkConsultaInscripcionNo = (By.XPATH, "//input[contains(@id,'mp_10027_No')]")
    chkConsultaInscripcionNA = (By.XPATH, "//input[contains(@id,'mp_10027_NA')]")
    txtUltimoControlMedico = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker4')]")

    # 13. Vacunado contra Tuberculosis y Hepatitis B
    chkVacunaTubHepBSi = (By.XPATH, "//input[contains(@id,'mp_10029_Si')]")
    chkVacunaTubHepBNo = (By.XPATH, "//input[contains(@id,'mp_10029_No')]")
    chkVacunaTubHepBNA = (By.XPATH, "//input[contains(@id,'mp_10029_NA')]")

    # 14. Lactancia materna
    chkLactanciaMaternaSi = (By.XPATH, "//input[contains(@id,'mp_10030_Si')]")
    chkLactanciaMaternaNo = (By.XPATH, "//input[contains(@id,'mp_10030_No')]")
    chkLactanciaMaternaNA = (By.XPATH, "//input[contains(@id,'mp_10030_NA')]")

    # 15. Consulta de inscripción por médico general, pediatra y/o neonatólogo (otra vez)
    chkConsultaInscripcion2Si = (By.XPATH, "//input[contains(@id,'mp_10031_Si')]")
    chkConsultaInscripcion2No = (By.XPATH, "//input[contains(@id,'mp_10031_No')]")
    chkConsultaInscripcion2NA = (By.XPATH, "//input[contains(@id,'mp_10031_NA')]")
    txtUltimoControlMedico2 = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker5')]")

    # 16. Controles de niño sano
    chkControlNinoSanoSi = (By.XPATH, "//input[contains(@id,'mp_10033_Si')]")
    chkControlNinoSanoNo = (By.XPATH, "//input[contains(@id,'mp_10033_No')]")
    chkControlNinoSanoNA = (By.XPATH, "//input[contains(@id,'mp_10033_NA')]")

    # 17. ¿Qué vacunas tiene aplicadas?
    cmbVacunasAplicadas1 = (By.XPATH, "//input[contains(@id,'TKDropDownList10')]")

    # 18. Controles de niño sano (otra vez)
    chkControlNinoSano2Si = (By.XPATH, "//input[contains(@id,'mp_10035_Si')]")
    chkControlNinoSano2No = (By.XPATH, "//input[contains(@id,'mp_10035_No')]")
    chkControlNinoSano2NA = (By.XPATH, "//input[contains(@id,'mp_10035_NA')]")

    # 19. ¿Qué vacunas tiene aplicadas?
    cmbVacunasAplicadas2 = (By.XPATH, "//input[contains(@id,'TKDropDownList12')]")

    # 20. Consejería
    chkConsejeriaSi = (By.XPATH, "//input[contains(@id,'mp_10037_Si')]")
    chkConsejeriaNo = (By.XPATH, "//input[contains(@id,'mp_10037_No')]")
    chkConsejeriaNA = (By.XPATH, "//input[contains(@id,'mp_10037_NA')]")

    # 21. ¿Qué vacunas tiene aplicadas?
    cmbVacunasAplicadas3 = (By.XPATH, "//input[contains(@id,'TKCombobox1')]")

    # 22. Controles de niño sano (otra vez)
    chkControlNinoSano3Si = (By.XPATH, "//input[contains(@id,'mp_10039_Si')]")
    chkControlNinoSano3No = (By.XPATH, "//input[contains(@id,'mp_10039_No')]")
    chkControlNinoSano3NA = (By.XPATH, "//input[contains(@id,'mp_10039_NA')]")

    # 23. ¿Se hizo evaluación Oftalmológica?
    chkEvalOftalmoSi = (By.XPATH, "//input[contains(@id,'mp_10040_Si')]")
    chkEvalOftalmoNo = (By.XPATH, "//input[contains(@id,'mp_10040_No')]")
    chkEvalOftalmoNA = (By.XPATH, "//input[contains(@id,'mp_10040_NA')]")
    txtEvalOftalmoCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker6')]")

    # 24. Visita domiciliar para control del niño/a
    chkVisitaDomiciliarSi = (By.XPATH, "//input[contains(@id,'mp_10042_Si')]")
    chkVisitaDomiciliarNo = (By.XPATH, "//input[contains(@id,'mp_10042_No')]")
    chkVisitaDomiciliarNA = (By.XPATH, "//input[contains(@id,'mp_10042_NA')]")
    txtVisitaDomiciliarCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker7')]")

    # 25. Análisis de sangre y orina
    chkAnalisisSangreOrinaSi = (By.XPATH, "//input[contains(@id,'mp_10044_Si')]")
    chkAnalisisSangreOrinaNo = (By.XPATH, "//input[contains(@id,'mp_10044_No')]")
    chkAnalisisSangreOrinaNA = (By.XPATH, "//input[contains(@id,'mp_10044_NA')]")
    txtAnalisisSangreOrinaCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker8')]")

    # 26. Vacuna VPH
    chkVacunaVPHSI = (By.XPATH, "//input[contains(@id,'mp_10046_Si')]")
    chkVacunaVPHNo = (By.XPATH, "//input[contains(@id,'mp_10046_No')]")
    chkVacunaVPHNA = (By.XPATH, "//input[contains(@id,'mp_10046_NA')]")
    txtVacunaVPHCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker9')]")

    # 27. Consulta inscripción por médico general o pediatra
    chkConsultaInscripcion3Si = (By.XPATH, "//input[contains(@id,'mp_10048_Si')]")
    chkConsultaInscripcion3No = (By.XPATH, "//input[contains(@id,'mp_10048_No')]")
    chkConsultaInscripcion3NA = (By.XPATH, "//input[contains(@id,'mp_10048_NA')]")

    # 28. Controles de niño sano (otra vez)
    chkControlNinoSano4Si = (By.XPATH, "//input[contains(@id,'mp_10049_Si')]")
    chkControlNinoSano4No = (By.XPATH, "//input[contains(@id,'mp_10049_No')]")
    chkControlNinoSano4NA = (By.XPATH, "//input[contains(@id,'mp_10049_NA')]")

    # 29. Consulta Odontológica
    chkConsultaOdontoSi = (By.XPATH, "//input[contains(@id,'mp_10050_Si')]")
    chkConsultaOdontoNo = (By.XPATH, "//input[contains(@id,'mp_10050_No')]")
    chkConsultaOdontoNA = (By.XPATH, "//input[contains(@id,'mp_10050_NA')]")
    txtConsultaOdontoCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker10')]")

    # 30. Análisis de sangre y orina (otra vez)
    chkAnalisisSangreOrina2Si = (By.XPATH, "//input[contains(@id,'mp_10052_Si')]")
    chkAnalisisSangreOrina2No = (By.XPATH, "//input[contains(@id,'mp_10052_No')]")
    chkAnalisisSangreOrina2NA = (By.XPATH, "//input[contains(@id,'mp_10052_NA')]")
    txtAnalisisSangreOrina2Cuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker11')]")

    # 31. Consejería
    chkConsejeria2Si = (By.XPATH, "//input[contains(@id,'mp_10054_Si')]")
    chkConsejeria2No = (By.XPATH, "//input[contains(@id,'mp_10054_No')]")
    chkConsejeria2NA = (By.XPATH, "//input[contains(@id,'mp_10054_NA')]")

    # 32. ¿Puede estar siendo víctima de violencia?
    chkVictimaViolenciaSi = (By.XPATH, "//input[contains(@id,'mp_10055_Si')]")
    chkVictimaViolenciaNo = (By.XPATH, "//input[contains(@id,'mp_10055_No')]")
    chkVictimaViolenciaNA = (By.XPATH, "//input[contains(@id,'mp_10055_NA')]")

    # 33. ¿Enfermedades?
    cmbEnfermedades = (By.XPATH, "//input[contains(@id,'TKCombobox2')]")

    # 34. Mamografía
    chkMamografiaSi = (By.XPATH, "//input[contains(@id,'mp_10057_Si')]")
    chkMamografiaNo = (By.XPATH, "//input[contains(@id,'mp_10057_No')]")
    chkMamografiaNA = (By.XPATH, "//input[contains(@id,'mp_10057_NA')]")
    txtMamografiaCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker12')]")
    txtMamografiaValores = (By.XPATH, "//input[contains(@id,'TKTextBox2')]")

    # 35. Papanicolau
    chkPapanicolauSi = (By.XPATH, "//input[contains(@id,'mp_10059_Si')]")
    chkPapanicolauNo = (By.XPATH, "//input[contains(@id,'mp_10059_No')]")
    chkPapanicolauNA = (By.XPATH, "//input[contains(@id,'mp_10059_NA')]")
    txtPapanicolauCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker13')]")
    txtPapanicolauValores = (By.XPATH, "//input[contains(@id,'TkNumericBox6')]")

    # 36. Vacuna VPH (otra vez)
    chkVacunaVPH2Si = (By.XPATH, "//input[contains(@id,'mp_10061_Si')]")
    chkVacunaVPH2No = (By.XPATH, "//input[contains(@id,'mp_10061_No')]")
    chkVacunaVPH2NA = (By.XPATH, "//input[contains(@id,'mp_10061_NA')]")
    txtVacunaVPH2Cuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker14')]")

    # 37. Antecedente de cáncer de mama familiar
    chkCancerMamaFamiliarSi = (By.XPATH, "//input[contains(@id,'mp_10094_Si')]")
    chkCancerMamaFamiliarNo = (By.XPATH, "//input[contains(@id,'mp_10094_No')]")
    chkCancerMamaFamiliarNA = (By.XPATH, "//input[contains(@id,'mp_10094_NA')]")
    swUSGMama = (By.XPATH, "//input[contains(@id,'TKSwitch70')]")
    txtUSGMamaCuando = (By.XPATH, "//input[contains(@id,'TKTextbox4')]")

    # 38. Mamografía o USG de mama
    chkMamografiaUSGSi = (By.XPATH, "//input[contains(@id,'mp_10063_Si')]")
    chkMamografiaUSGNo = (By.XPATH, "//input[contains(@id,'mp_10063_No')]")
    chkMamografiaUSGNA = (By.XPATH, "//input[contains(@id,'mp_10063_NA')]")
    txtMamografiaUSGCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker15')]")

    # 39. Examen de Papanicolau
    chkExamenPapanicolauSi = (By.XPATH, "//input[contains(@id,'mp_10065_Si')]")
    chkExamenPapanicolauNo = (By.XPATH, "//input[contains(@id,'mp_10065_No')]")
    chkExamenPapanicolauNA = (By.XPATH, "//input[contains(@id,'mp_10065_NA')]")
    txtExamenPapanicolauCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker16')]")
    txtExamenPapanicolauValores = (By.XPATH, "//input[contains(@id,'TkNumericBox6')]")

    # 40. Prueba de detección de VPH
    chkPruebaVPHSi = (By.XPATH, "//input[contains(@id,'mp_10097_Si')]")
    chkPruebaVPHNo = (By.XPATH, "//input[contains(@id,'mp_10097_No')]")
    chkPruebaVPHNA = (By.XPATH, "//input[contains(@id,'mp_10097_NA')]")
    txtPruebaVPHDesdeCuando = (By.XPATH, "//input[contains(@id,'TKTextbox5')]")

    # 41. ¿Cuántas Gestaciones tuvo?
    txtGestaciones = (By.XPATH, "//input[contains(@id,'TkNumericBox3')]")

    # 42. ¿Cuántos partos tuvo?
    txtPartos = (By.XPATH, "//input[contains(@id,'TkNumericBox4')]")
    txtUltimoParto = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker17')]")

    # 43. ¿Cuantos Prematuros?
    txtPrematuros = (By.XPATH, "//input[contains(@id,'TkNumericBox7')]")

    # 44. ¿Cuantos Abortos?
    txtAbortos = (By.XPATH, "//input[contains(@id,'TkNumericBox8')]")

    # 45. ¿Cuantos vivos actualmente?
    txtVivos = (By.XPATH, "//input[contains(@id,'TkNumericBox9')]")

    # 46. Fecha de última menstruación
    txtUltimaMenstruacion = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker18')]")

    # 47. ¿Estás embarazada?
    chkEmbarazadaSi = (By.XPATH, "//input[contains(@id,'mp_10071_Si')]")
    chkEmbarazadaNo = (By.XPATH, "//input[contains(@id,'mp_10071_No')]")
    chkEmbarazadaNA = (By.XPATH, "//input[contains(@id,'mp_10071_NA')]")

    # 48. ¿Estás en período de posparto?
    chkPospartoSi = (By.XPATH, "//input[contains(@id,'mp_10073_Si')]")
    chkPospartoNo = (By.XPATH, "//input[contains(@id,'mp_10073_No')]")
    chkPospartoNA = (By.XPATH, "//input[contains(@id,'mp_10073_NA')]")
    txtSemanasPosparto = (By.XPATH, "//input[contains(@id,'TkNumericBox5')]")

    # 49. Métodos anticonceptivos (mujer)
    chkAnticonceptivosSi = (By.XPATH, "//input[contains(@id,'mp_10075_Si')]")
    chkAnticonceptivosNo = (By.XPATH, "//input[contains(@id,'mp_10075_No')]")
    chkAnticonceptivosNA = (By.XPATH, "//input[contains(@id,'mp_10075_NA')]")
    cmbAnticonceptivoCual = (By.XPATH, "//input[contains(@id,'TKDropDownList4')]")

    # Lactancia
    chkLactanciaSi = (By.XPATH, "//input[contains(@id,'TCACheckBox1')]")
    chkLactanciaNo = (By.XPATH, "//input[contains(@id,'TCACheckBox2')]")
    chkLactanciaNA = (By.XPATH, "//input[contains(@id,'TCACheckBox3')]")

    # 49. Métodos anticonceptivos (hombre)
    chkAnticonceptivosHombreSi = (By.XPATH, "//input[contains(@id,'mp_10105_Si')]")
    chkAnticonceptivosHombreNo = (By.XPATH, "//input[contains(@id,'mp_10105_No')]")
    chkAnticonceptivosHombreNA = (By.XPATH, "//input[contains(@id,'mp_10105_NA')]")
    cmbAnticonceptivoHombreCual = (By.XPATH, "//input[contains(@id,'TKCombobox16')]")

    # 50. Análisis para detectar Cáncer de próstata
    chkAnalisisProstataSi = (By.XPATH, "//input[contains(@id,'mp_10077_Si')]")
    chkAnalisisProstataNo = (By.XPATH, "//input[contains(@id,'mp_10077_No')]")
    chkAnalisisProstataNA = (By.XPATH, "//input[contains(@id,'mp_10077_NA')]")

    # 51. Análisis de sangre oculta en heces
    chkSangreHecesSi = (By.XPATH, "//input[contains(@id,'mp_10078_Si')]")
    chkSangreHecesNo = (By.XPATH, "//input[contains(@id,'mp_10078_No')]")
    chkSangreHecesNA = (By.XPATH, "//input[contains(@id,'mp_10078_NA')]")

    # 52. Consulta de inscripción por médico general
    chkConsultaInscripcion4Si = (By.XPATH, "//input[contains(@id,'mp_10079_Si')]")
    chkConsultaInscripcion4No = (By.XPATH, "//input[contains(@id,'mp_10079_No')]")
    chkConsultaInscripcion4NA = (By.XPATH, "//input[contains(@id,'mp_10079_NA')]")

    # 53. Control anual adolescentes
    chkControlAnualAdolescentesSi = (By.XPATH, "//input[contains(@id,'mp_10080_Si')]")
    chkControlAnualAdolescentesNo = (By.XPATH, "//input[contains(@id,'mp_10080_No')]")
    chkControlAnualAdolescentesNA = (By.XPATH, "//input[contains(@id,'mp_10080_NA')]")
    txtControlAnualAdolescentesCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker19')]")

    # 54. Análisis de sangre y orina (otra vez)
    chkAnalisisSangreOrina3Si = (By.XPATH, "//input[contains(@id,'mp_10082_Si')]")
    chkAnalisisSangreOrina3No = (By.XPATH, "//input[contains(@id,'mp_10082_No')]")
    chkAnalisisSangreOrina3NA = (By.XPATH, "//input[contains(@id,'mp_10082_NA')]")
    txtAnalisisSangreOrina3Cuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker20')]")

    # 55. Consejería
    chkConsejeria3Si = (By.XPATH, "//input[contains(@id,'mp_10084_Si')]")
    chkConsejeria3No = (By.XPATH, "//input[contains(@id,'mp_10084_No')]")
    chkConsejeria3NA = (By.XPATH, "//input[contains(@id,'mp_10084_NA')]")

    # 56. Conductas anormales para la edad
    chkConductasAnormalesSi = (By.XPATH, "//input[contains(@id,'mp_10085_Si')]")
    chkConductasAnormalesNo = (By.XPATH, "//input[contains(@id,'mp_10085_No')]")
    chkConductasAnormalesNA = (By.XPATH, "//input[contains(@id,'mp_10085_NA')]")

    # 57. Violencia en hijos
    chkViolenciaHijosSi = (By.XPATH, "//input[contains(@id,'mp_10086_Si')]")
    chkViolenciaHijosNo = (By.XPATH, "//input[contains(@id,'mp_10086_No')]")
    chkViolenciaHijosNA = (By.XPATH, "//input[contains(@id,'mp_10086_NA')]")

    # 58. Adicciones en hijos
    chkAdiccionesHijosSi = (By.XPATH, "//input[contains(@id,'mp_10087_Si')]")
    chkAdiccionesHijosNo = (By.XPATH, "//input[contains(@id,'mp_10087_No')]")
    chkAdiccionesHijosNA = (By.XPATH, "//input[contains(@id,'mp_10087_NA')]")

    # 59. Trastornos cognitivos
    chkTrastornosCognitivosSi = (By.XPATH, "//input[contains(@id,'mp_10088_Si')]")
    chkTrastornosCognitivosNo = (By.XPATH, "//input[contains(@id,'mp_10088_No')]")
    chkTrastornosCognitivosNA = (By.XPATH, "//input[contains(@id,'mp_10088_NA')]")
    txtTrastornosCognitivosDesdeCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker21')]")

    # Dificultad para escuchar
    chkDificultadEscucharSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10090_Si')]")
    chkDificultadEscucharNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10090_No')]")
    chkDificultadEscucharNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10090_NA')]")
    txtDificultadEscucharDesdeCuando = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_Tkdatetimepicker22')]")

    # Vacuna de influenza
    chkVacunaInfluenzaSi = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10102_Si')]")
    chkVacunaInfluenzaNo = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10102_No')]")
    chkVacunaInfluenzaNA = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_mp_10102_NA')]")
    txtVacunaInfluenzaFecha = (By.XPATH, "//input[contains(@id,'MPTableroMedico_Antecedentes_TKTextbox6')]")

    # Antecedentes - Antecedentes familiares
    # 1. ¿Sabe si alguien de su familia tiene actualmente o ha tenido alguna de estas condiciones?
    chkCondicionesFamiliaSi = (By.XPATH, "//input[contains(@id,'mp_10152_Si')]")
    chkCondicionesFamiliaNo = (By.XPATH, "//input[contains(@id,'mp_10152_No')]")
    chkCondicionesFamiliaNA = (By.XPATH, "//input[contains(@id,'mp_10152_NA')]")

    # 2. Diabetes
    chkDiabetesSi = (By.XPATH, "//input[contains(@id,'mp_10153_Si')]")
    chkDiabetesNo = (By.XPATH, "//input[contains(@id,'mp_10153_No')]")
    chkDiabetesNA = (By.XPATH, "//input[contains(@id,'mp_10153_NA')]")
    cmbDiabetesFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10154')]")

    # 3. Muerte por causa cardiovascular antes de los 60 años
    chkMuerteCardioSi = (By.XPATH, "//input[contains(@id,'mp_10155_Si')]")
    chkMuerteCardioNo = (By.XPATH, "//input[contains(@id,'mp_10155_No')]")
    chkMuerteCardioNA = (By.XPATH, "//input[contains(@id,'mp_10155_NA')]")
    cmbMuerteCardioFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10156')]")

    # 4. Hipercolesterolemia Familiar
    chkHipercolesterolemiaSi = (By.XPATH, "//input[contains(@id,'mp_10157_Si')]")
    chkHipercolesterolemiaNo = (By.XPATH, "//input[contains(@id,'mp_10157_No')]")
    chkHipercolesterolemiaNA = (By.XPATH, "//input[contains(@id,'mp_10157_NA')]")
    cmbHipercolesterolemiaFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10158')]")

    # 5. Cáncer de mama
    chkCancerMamaSi = (By.XPATH, "//input[contains(@id,'mp_10159_Si')]")
    chkCancerMamaNo = (By.XPATH, "//input[contains(@id,'mp_10159_No')]")
    chkCancerMamaNA = (By.XPATH, "//input[contains(@id,'mp_10159_NA')]")
    cmbCancerMamaFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10160')]")

    # 6. Cáncer de Colon o Recto
    chkCancerColonSi = (By.XPATH, "//input[contains(@id,'mp_10161_Si')]")
    chkCancerColonNo = (By.XPATH, "//input[contains(@id,'mp_10161_No')]")
    chkCancerColonNA = (By.XPATH, "//input[contains(@id,'mp_10161_NA')]")
    cmbCancerColonFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10162')]")

    # 7. Enf de Alzheimer
    chkAlzheimerSi = (By.XPATH, "//input[contains(@id,'mp_10163_Si')]")
    chkAlzheimerNo = (By.XPATH, "//input[contains(@id,'mp_10163_No')]")
    chkAlzheimerNA = (By.XPATH, "//input[contains(@id,'mp_10163_NA')]")
    cmbAlzheimerFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10164')]")

    # 8. Enf de Parkinson
    chkParkinsonSi = (By.XPATH, "//input[contains(@id,'mp_10165_Si')]")
    chkParkinsonNo = (By.XPATH, "//input[contains(@id,'mp_10165_No')]")
    chkParkinsonNA = (By.XPATH, "//input[contains(@id,'mp_10165_NA')]")
    cmbParkinsonFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10166')]")

    # 9. Hemofilia
    chkHemofiliaSi = (By.XPATH, "//input[contains(@id,'mp_10167_Si')]")
    chkHemofiliaNo = (By.XPATH, "//input[contains(@id,'mp_10167_No')]")
    chkHemofiliaNA = (By.XPATH, "//input[contains(@id,'mp_10167_NA')]")
    cmbHemofiliaFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10168')]")

    # 10. Fibrosis Quística
    chkFibrosisSi = (By.XPATH, "//input[contains(@id,'mp_10169_Si')]")
    chkFibrosisNo = (By.XPATH, "//input[contains(@id,'mp_10169_No')]")
    chkFibrosisNA = (By.XPATH, "//input[contains(@id,'mp_10169_NA')]")
    cmbFibrosisFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10170')]")

    # 11. Talasemia
    chkTalasemiaSi = (By.XPATH, "//input[contains(@id,'mp_10171_Si')]")
    chkTalasemiaNo = (By.XPATH, "//input[contains(@id,'mp_10171_No')]")
    chkTalasemiaNA = (By.XPATH, "//input[contains(@id,'mp_10171_NA')]")
    cmbTalasemiaFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10172')]")

    # 12. Trastornos del Espectro Autista (TEA)
    chkTEASi = (By.XPATH, "//input[contains(@id,'mp_10173_Si')]")
    chkTEANo = (By.XPATH, "//input[contains(@id,'mp_10173_No')]")
    chkTEANA = (By.XPATH, "//input[contains(@id,'mp_10173_NA')]")
    cmbTEAFamiliar = (By.XPATH, "//input[contains(@id,'mp_ant_sw_10174')]")

    # 13. Hipertensión
    chkHipertensionSi = (By.XPATH, "//input[contains(@id,'mp_10175_Si')]")
    chkHipertensionNo = (By.XPATH, "//input[contains(@id,'mp_10175_No')]")
    chkHipertensionNA = (By.XPATH, "//input[contains(@id,'mp_10175_NA')]")
    cmbHipertensionFamiliar = (By.XPATH, "//input[contains(@id,'TKCombobox14')]")

    # 14. Enfermedad Renal Crónica
    chkEnfRenalSi = (By.XPATH, "//input[contains(@id,'mp_10177_Si')]")
    chkEnfRenalNo = (By.XPATH, "//input[contains(@id,'mp_10177_No')]")
    chkEnfRenalNA = (By.XPATH, "//input[contains(@id,'mp_10177_NA')]")
    cmbEnfRenalFamiliar = (By.XPATH, "//input[contains(@id,'TKCombobox15')]")

    # Botón Guardar
    btnGuardarFamiliares = (By.XPATH, "//button[contains(@id,'Tkbutton2')]")

    # Antecedentes - Patologicos Personales
    # 4. ¿Tienes diabetes? (azucar en sangre)
    chkDiabetesSi = (By.XPATH, "//input[contains(@id,'mp_10302_Si')]")
    chkDiabetesNo = (By.XPATH, "//input[contains(@id,'mp_10302_No')]")
    chkDiabetesNA = (By.XPATH, "//input[contains(@id,'mp_10302_NA')]")
    txtDiabetesTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist5')]")
    txtDiabetesTiempo = (By.XPATH, "//input[contains(@id,'mp_ant_ddl_3611')]")
    txtDiabetesUltimoControl = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3613')]")

    # ¿Está en tratamiento? (diabetes)
    chkDiabetesTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10305_Si')]")
    chkDiabetesTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10305_No')]")
    chkDiabetesTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10305_NA')]")
    cmbDiabetesMedicamento = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3614')]")

    # 5. ¿Padeces de presión arterial?
    chkPresionSi = (By.XPATH, "//input[contains(@id,'mp_10308_Si')]")
    chkPresionNo = (By.XPATH, "//input[contains(@id,'mp_10308_No')]")
    chkPresionNA = (By.XPATH, "//input[contains(@id,'mp_10308_NA')]")

    # ¿Está en tratamiento? (presión arterial)
    chkPresionTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10309_Si')]")
    chkPresionTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10309_No')]")
    chkPresionTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10309_NA')]")
    txtPresionMedicamento = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3617')]")

    # 6. ¿Tiene alguna enfermedad del corazón?
    chkCorazonSi = (By.XPATH, "//input[contains(@id,'mp_10311_Si')]")
    chkCorazonNo = (By.XPATH, "//input[contains(@id,'mp_10311_No')]")
    chkCorazonNA = (By.XPATH, "//input[contains(@id,'mp_10311_NA')]")
    txtCorazonTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist6')]")

    # ¿Está en tratamiento? (corazón)
    chkCorazonTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10313_Si')]")
    chkCorazonTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10313_No')]")
    chkCorazonTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10313_NA')]")
    txtCorazonMedicamento = (By.XPATH, "//input[contains(@id,'Tkdropdownlist7')]")

    # 7. ¿Tiene alguna enfermedad de los pulmones?
    chkPulmonesSi = (By.XPATH, "//input[contains(@id,'mp_10315_Si')]")
    chkPulmonesNo = (By.XPATH, "//input[contains(@id,'mp_10315_No')]")
    chkPulmonesNA = (By.XPATH, "//input[contains(@id,'mp_10315_NA')]")
    txtPulmonesTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist8')]")

    # ¿Está en tratamiento? (pulmones)
    chkPulmonesTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10317_Si')]")
    chkPulmonesTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10317_No')]")
    chkPulmonesTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10317_NA')]")
    txtPulmonesMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox3')]")

    # 8. ¿Tienes alguna enfermedad de los riñones?
    chkRinonesSi = (By.XPATH, "//input[contains(@id,'mp_10319_Si')]")
    chkRinonesNo = (By.XPATH, "//input[contains(@id,'mp_10319_No')]")
    chkRinonesNA = (By.XPATH, "//input[contains(@id,'mp_10319_NA')]")
    txtRinonesTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist9')]")

    # ¿Está en tratamiento? (riñones)
    chkRinonesTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10321_Si')]")
    chkRinonesTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10321_No')]")
    chkRinonesTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10321_NA')]")
    txtRinonesMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox4')]")

    # ¿Está en programa de diálisis?
    chkDialisisSi = (By.XPATH, "//input[contains(@id,'mp_10363_Si')]")
    chkDialisisNo = (By.XPATH, "//input[contains(@id,'mp_10363_No')]")
    chkDialisisNA = (By.XPATH, "//input[contains(@id,'mp_10363_NA')]")

    # 9. ¿Tienes alguna enfermedad del hígado?
    chkHigadoSi = (By.XPATH, "//input[contains(@id,'mp_10323_Si')]")
    chkHigadoNo = (By.XPATH, "//input[contains(@id,'mp_10323_No')]")
    chkHigadoNA = (By.XPATH, "//input[contains(@id,'mp_10323_NA')]")
    txtHigadoTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist11')]")

    # ¿Está en tratamiento? (hígado)
    chkHigadoTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10325_Si')]")
    chkHigadoTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10325_No')]")
    chkHigadoTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10325_NA')]")
    txtHigadoMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox5')]")

    # 10. ¿Ha padecido un Accidente Vascular Cerebral?
    chkAVCSi = (By.XPATH, "//input[contains(@id,'mp_10327_Si')]")
    chkAVCNo = (By.XPATH, "//input[contains(@id,'mp_10327_No')]")
    chkAVCNA = (By.XPATH, "//input[contains(@id,'mp_10327_NA')]")

    # ¿Está en tratamiento? (AVC)
    chkAVCTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10328_Si')]")
    chkAVCTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10328_No')]")
    chkAVCTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10328_NA')]")
    txtAVCMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox6')]")

    # 11. ¿Tienes o has tenido algún tipo de Cáncer?
    chkCancerSi = (By.XPATH, "//input[contains(@id,'mp_10330_Si')]")
    chkCancerNo = (By.XPATH, "//input[contains(@id,'mp_10330_No')]")
    chkCancerNA = (By.XPATH, "//input[contains(@id,'mp_10330_NA')]")
    txtCancerTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist13')]")

    # ¿Está en tratamiento? (Cáncer)
    chkCancerTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10332_Si')]")
    chkCancerTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10332_No')]")
    chkCancerTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10332_NA')]")
    txtCancerMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox7')]")
    txtCancerTratamientoFin = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker23')]")

    # 12. ¿Tiene artritis?
    chkArtritisSi = (By.XPATH, "//input[contains(@id,'mp_10335_Si')]")
    chkArtritisNo = (By.XPATH, "//input[contains(@id,'mp_10335_No')]")
    chkArtritisNA = (By.XPATH, "//input[contains(@id,'mp_10335_NA')]")
    txtArtritisTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist14')]")

    # ¿Está en tratamiento? (artritis)
    chkArtritisTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10337_Si')]")
    chkArtritisTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10337_No')]")
    chkArtritisTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10337_NA')]")
    txtArtritisMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox8')]")

    # 13. ¿Ha tenido algún traumatismo múltiple?
    chkTraumatismoSi = (By.XPATH, "//input[contains(@id,'mp_10340_Si')]")
    chkTraumatismoNo = (By.XPATH, "//input[contains(@id,'mp_10340_No')]")
    chkTraumatismoNA = (By.XPATH, "//input[contains(@id,'mp_10340_NA')]")
    txtTraumatismoAnio = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker26')]")

    # ¿Está en tratamiento? (traumatismo)
    chkTraumatismoTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10342_Si')]")
    chkTraumatismoTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10342_No')]")
    chkTraumatismoTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10342_NA')]")
    cmbTraumatismoTratamiento = (By.XPATH, "//input[contains(@id,'Tkcombobox9')]")

    # 14. ¿Tiene antecedentes de operaciones quirúrgicas con anestesia?
    chkOperacionSi = (By.XPATH, "//input[contains(@id,'mp_10344_Si')]")
    chkOperacionNo = (By.XPATH, "//input[contains(@id,'mp_10344_No')]")
    chkOperacionNA = (By.XPATH, "//input[contains(@id,'mp_10344_NA')]")
    txtOperacionTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist15')]")
    txtOperacionAnio = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker25')]")

    # 15. ¿Tiene enfermedad de la tiroides?
    chkTiroidesSi = (By.XPATH, "//input[contains(@id,'mp_10347_Si')]")
    chkTiroidesNo = (By.XPATH, "//input[contains(@id,'mp_10347_No')]")
    chkTiroidesNA = (By.XPATH, "//input[contains(@id,'mp_10347_NA')]")
    txtTiroidesTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist16')]")

    # ¿Está en tratamiento? (tiroides)
    chkTiroidesTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10349_Si')]")
    chkTiroidesTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10349_No')]")
    chkTiroidesTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10349_NA')]")
    txtTiroidesMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox10')]")

    # 16. ¿Tiene actualmente o ha tenido alguna de estas enfermedades?
    cmbOtrasEnfermedades = (By.XPATH, "//input[contains(@id,'Tkdropdownlist17')]")

    # ¿Está en tratamiento? (otras enfermedades)
    chkOtrasEnfermedadesTratamientoSi = (By.XPATH, "//input[contains(@id,'mp_10352_Si')]")
    chkOtrasEnfermedadesTratamientoNo = (By.XPATH, "//input[contains(@id,'mp_10352_No')]")
    chkOtrasEnfermedadesTratamientoNA = (By.XPATH, "//input[contains(@id,'mp_10352_NA')]")
    txtOtrasEnfermedadesMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox11')]")

    # 17. ¿Ha estado ingresado en un establecimiento de salud alguna vez?
    chkIngresoSaludSi = (By.XPATH, "//input[contains(@id,'mp_10354_Si')]")
    chkIngresoSaludNo = (By.XPATH, "//input[contains(@id,'mp_10354_No')]")
    chkIngresoSaludNA = (By.XPATH, "//input[contains(@id,'mp_10354_NA')]")
    txtIngresoSaludMotivo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist18')]")
    txtIngresoSaludCuando = (By.XPATH, "//input[contains(@id,'Tkdatetimepicker27')]")

    # 18. ¿Está actualmente en tratamiento para alguna otra enfermedad o condición?
    chkTratamientoOtraEnfSi = (By.XPATH, "//input[contains(@id,'mp_10357_Si')]")
    chkTratamientoOtraEnfNo = (By.XPATH, "//input[contains(@id,'mp_10357_No')]")
    chkTratamientoOtraEnfNA = (By.XPATH, "//input[contains(@id,'mp_10357_NA')]")
    txtTratamientoOtraEnfTipo = (By.XPATH, "//input[contains(@id,'Tkdropdownlist19')]")
    txtTratamientoOtraEnfMedicamento = (By.XPATH, "//input[contains(@id,'Tkcombobox12')]")

    # 19. ¿Ha tenido alguna otra enfermedad crónica o grave que ud considere importante?
    chkOtraEnfGraveSi = (By.XPATH, "//input[contains(@id,'mp_10360_Si')]")
    chkOtraEnfGraveNo = (By.XPATH, "//input[contains(@id,'mp_10360_No')]")
    chkOtraEnfGraveNA = (By.XPATH, "//input[contains(@id,'mp_10360_NA')]")
    txtOtraEnfGraveCual = (By.XPATH, "//input[contains(@id,'Tktextbox1')]")

    # ¿Se considera curado?
    chkCuradoSi = (By.XPATH, "//input[contains(@id,'mp_10362_Si')]")
    chkCuradoNo = (By.XPATH, "//input[contains(@id,'mp_10362_No')]")
    chkCuradoNA = (By.XPATH, "//input[contains(@id,'mp_10362_NA')]")

    # Botón Guardar
    btnGuardarPatologias = (By.XPATH, "//button[contains(@id,'Tkbutton3')]")

    # Antecedentes - Determinantes Sociales
    # Actividad habitual (Ocupación)
    cmbActividadHabitual = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3700')]")

    # ¿Fue a la escuela?
    chkEscuelaSi = (By.XPATH, "//input[contains(@id,'mp_10453_Si')]")
    chkEscuelaNo = (By.XPATH, "//input[contains(@id,'mp_10453_No')]")
    chkEscuelaNA = (By.XPATH, "//input[contains(@id,'mp_10453_NA')]")

    # ¿Qué nivel de educación alcanzó?
    cmbNivelEducacion = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3702')]")

    # ¿El Jefe de familia tiene trabajo estable?
    chkJefeTrabajoSi = (By.XPATH, "//input[contains(@id,'mp_10455_Si')]")
    chkJefeTrabajoNo = (By.XPATH, "//input[contains(@id,'mp_10455_No')]")
    chkJefeTrabajoNA = (By.XPATH, "//input[contains(@id,'mp_10455_NA')]")

    # Cantidad de habitantes en la vivienda
    txtHabitantesVivienda = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3704')]")

    # ¿Quién cuida a los niños en edad preescolar?
    cmbCuidaNinios = (By.XPATH, "//input[contains(@id,'mp_ant_ddl_3705')]")

    # No. de habitaciones
    txtNumHabitaciones = (By.XPATH, "//input[contains(@id,'mp_ant_sw_3706')]")

    # ¿Cuenta con servicio sanitario?
    chkSanitarioSi = (By.XPATH, "//input[contains(@id,'mp_10459_Si')]")
    chkSanitarioNo = (By.XPATH, "//input[contains(@id,'mp_10459_No')]")
    chkSanitarioNA = (By.XPATH, "//input[contains(@id,'mp_10459_NA')]")

    # ¿Cuenta con agua potable?
    chkAguaSi = (By.XPATH, "//input[contains(@id,'mp_10460_Si')]")
    chkAguaNo = (By.XPATH, "//input[contains(@id,'mp_10460_No')]")
    chkAguaNA = (By.XPATH, "//input[contains(@id,'mp_10460_NA')]")

    # ¿Cuenta con electricidad?
    chkElectricidadSi = (By.XPATH, "//input[contains(@id,'mp_10461_Si')]")
    chkElectricidadNo = (By.XPATH, "//input[contains(@id,'mp_10461_No')]")
    chkElectricidadNA = (By.XPATH, "//input[contains(@id,'mp_10461_NA')]")

    # ¿Tiene cocina a leña?
    chkCocinaLeniaSi = (By.XPATH, "//input[contains(@id,'mp_10462_Si')]")
    chkCocinaLeniaNo = (By.XPATH, "//input[contains(@id,'mp_10462_No')]")
    chkCocinaLeniaNA = (By.XPATH, "//input[contains(@id,'mp_10462_NA')]")

    # ¿Tiene servicio de recolección de basura?
    chkBasuraSi = (By.XPATH, "//input[contains(@id,'mp_10463_Si')]")
    chkBasuraNo = (By.XPATH, "//input[contains(@id,'mp_10463_No')]")
    chkBasuraNA = (By.XPATH, "//input[contains(@id,'mp_10463_NA')]")

    # ¿Trabaja en la agricultura y tiene exposición a plaguicidas?
    chkPlaguicidasSi = (By.XPATH, "//input[contains(@id,'mp_10464_Si')]")
    chkPlaguicidasNo = (By.XPATH, "//input[contains(@id,'mp_10464_No')]")
    chkPlaguicidasNA = (By.XPATH, "//input[contains(@id,'mp_10464_NA')]")

    # ¿Cuánto tiempo demora en llegar al Centro de Salud más cercano?
    txtTiempoCentroSalud = (By.XPATH, "//input[contains(@id,'TKSwitch67')]")

    # Tipo de centro de salud
    cmbTipoCentroSalud = (By.XPATH, "//input[contains(@id,'Tktextbox3')]")

    # Acceso desde su vivienda al Centro de Salud
    cmbAccesoCentroSalud = (By.XPATH, "//input[contains(@id,'Tkcombobox13')]")

    # Botón Guardar
    btnGuardarDeterminantes = (By.XPATH, "//button[contains(@id,'Tkbutton4')]")

    # Información del paciente - Alergias
    cmbTipoDeAlergia = (By.XPATH, "//div[contains(@id,'MPTableroMedico_FiltroTipoAlergia_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_FiltroTipoAlergia_listbox')]")
    btnNoRefiere = (By.XPATH, "//div[contains(@id,'MPTableroMedico_BtnNorefiere_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_BtnNorefiere')]")
    btnAgregarNuevaAlergia = (By.XPATH, "//div[contains(@id,'MPTableroMedico_BtnAgregaralergia_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_BtnAgregaralergia')]")

    # Información del paciente - Nota Medica - Toolbar
    tipbtnAbrirLlamada = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnVideo')]")
    tipbtnCitaAdministrativa = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnAdministrativa')]")
    tipbtnReferencia = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnReferencia')]")
    tipbtnIncapacidades = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnIncapacidad')]")
    tipbtnRecomendaciones = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnRecomendaciones')]")
    tipbtnProcedimientosMedicos = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnProcMedicos')]")
    tipbtnImagenologia = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnSolIma')]")
    tipbtnLaboratorio = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnSolEst')]")
    tipbtnReceta = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnSolRec')]")
    tipbtnProgramarCita = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnProgCita')]")
    tipbtnGuardarAvance = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnGuardar')]")
    tipbtnFinalizar = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed_mpTabMed_btnResolver')]")

    # Información del paciente - Nota Medica
    txtConsultaPor = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed2_mp_nm_txtMot_wrapper')]/descendant::textarea[contains(@id,'MPTableroMedico_panelNotaMed2_mp_nm_txtMot')]")
    txtTriage = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed3_mp_nm_txtSS_wrapper')]/descendant::textarea[contains(@id,'MPTableroMedico_panelNotaMed3_mp_nm_txtSS')]")

    # Información del paciente - Nota Medica - Signos Vitales
    btnVerSignosVitales = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_btnSVApp_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed4_btnSVApp')]")
    txtTemp = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtTemp_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtTemp')]/preceding-sibling::input")
    txtFC = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtFC_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtFC')]/preceding-sibling::input")
    txtFR = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtFR_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtFR')]/preceding-sibling::input")
    txtPA = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtPA_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtPA')]/preceding-sibling::input")
    txtPA2 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_lblPA2_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_lblPA2')]/preceding-sibling::input")
    txtSat02 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtSat_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtSat')]/preceding-sibling::input")
    txtPeso = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtPeso_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtPeso')]/preceding-sibling::input")
    txtTalla = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtTalla_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed4_mp_nm_txtTalla')]/preceding-sibling::input")

    # Información del paciente - Nota Medica - Presente enfermedad
    txtPresenteEnfermedad = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed5_mp_nm_txtApreciativo_wrapper')]/descendant::textarea[contains(@id,'MPTableroMedico_panelNotaMed5_mp_nm_txtApreciativo')]")

    # Información del paciente - Nota Medica - Apreciacion Diagnostica
    txtApreciacionDiagnostica = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed9_mp_nm_txtApreciativo2_wrapper')]/descendant::textarea[contains(@id,'MPTableroMedico_panelNotaMed9_mp_nm_txtApreciativo2')]")
    btnGenerarApreciacionDiagnostica = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed9_mp_nm_btnEnviarIA_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed9_mp_nm_btnEnviarIA')]")

    txtDiagnosticoPrincipal = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_DiagP_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_DiagP')]")
    btndgvCatalogoDiagnosticoPrincipal = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_DiagP_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_DiagP_catalogButton')]")
    btnGenerarDiagnosticoPrincipal = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_btnEnviarIA2_wrapper')]/descendant::button[contains(@id,'panelNotaMed6_mp_nm_btnEnviarIA2')]")
    btnAgregarProblemasActivos = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_btnAgregarProblema_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_btnAgregarProblema')]")

    txtDiagnosticoSecundario = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_Diag1_wrapper')]/descendant::input[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_Diag1')]")
    btndgvCatalogoDiagnosticoSecundario = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_Diag1_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_Diag1_catalogButton')]")
    btnAgregarProblemaSecundario = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_btnAgregarDco_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed6_mp_nm_btnAgregarDco')]")

    # Información del paciente - Nota Medica - Tratamiento
    btnMostrarPlan = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelNotaMed7_mp_nm_btnMostrarPlan_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelNotaMed7_mp_nm_btnMostrarPlan')]")

    # Información del paciente - Estudios complementarios
    cmbTipoDeEstudio = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelEstudios_mpTabMed_tipoEstudio_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_panelEstudios_mpTabMed_tipoEstudio_listbox')]")
    cmbEstadoEstudio = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelEstudios_mpTabMed_Estado2_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_panelEstudios_mpTabMed_Estado2_listbox')]")

    # Información del paciente - Medicamentos y Recetas
    cmbEstadoRecetas = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelMed_mpTabMed_Estado3_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_panelMed_mpTabMed_Estado3_listbox')]")

    # Información del paciente - Referencias
    btnGenerarReferencia = (By.XPATH, "//div[contains(@id,'MPTableroMedico_btnGenerarRef_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_btnGenerarRef')]")

    # Informacion del paciente - Incapacidades
    cmbEstadoIncapacidad = (By.XPATH, "//div[contains(@id,'MP_incapacidadesEstado_wrapper')]/descendant::span[contains(@aria-owns,'MP_incapacidadesEstado_listbox')]")
    btnGenerarIncapacidad = (By.XPATH, "//div[contains(@id,'MP_incapacidadesGenerar_wrapper')]/descendant::button[contains(@id,'MP_incapacidadesGenerar')]")

    # Califica al paciente
    btnCalificacion1 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_KendoListViewMPTableroMedicoCalificar')]/descendant::div[@class='stars']/*[1]")
    btnCalificacion2 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_KendoListViewMPTableroMedicoCalificar')]/descendant::div[@class='stars']/*[2]")
    btnCalificacion3 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_KendoListViewMPTableroMedicoCalificar')]/descendant::div[@class='stars']/*[3]")
    btnCalificacion4 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_KendoListViewMPTableroMedicoCalificar')]/descendant::div[@class='stars']/*[4]")
    btnCalificacion5 = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_KendoListViewMPTableroMedicoCalificar')]/descendant::div[@class='stars']/*[5]")
    cmbMotivoDeEvaluacion = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_TKDrop_CalfPaciente_1_wrapper')]/descendant::span[contains(@aria-owns,'MPTableroMedico_panelResumen_TKDrop_CalfPaciente_1_listbox')]")
    txtResena = (By.XPATH, "//div[contains(@id,'MPTableroMedicoReseña_wrapper')]/descendant::textarea[contains(@id,'MPTableroMedico_panelResumen_MPTableroMedicoReseña')]")
    btnCancelarCalificacion = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_TKButton1_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelResumen_TKButton1')]")
    btnGuardarCalificacion = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelResumen_TKButton2_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelResumen_TKButton2')]")

    # Información del paciente - Comentarios
    txtFechaInicialComentarios = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelComentarios_MPTableroMedico_FilRngFec1_validator')]/descendant::input[contains(@id,'MPTableroMedico_panelComentarios_MPTableroMedico_FilRngFec1')]")
    txtFechaFinalComentarios = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelComentarios_MPTableroMedico_FilRngFec2_validator')]/descendant::input[contains(@id,'MPTableroMedico_panelComentarios_MPTableroMedico_FilRngFec2')]")
    txtFiltrarComentarios = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelComentarios_mpTabCom_btnFiltrar_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelComentarios_mpTabCom_btnFiltrar')]")

    # Información del paciente - Signos Vitales
    btnRefrescarSignosVitales = (By.XPATH, "//div[contains(@id,'MPTableroMedico_panelSignosVitales1_btnActualizarGridSV_wrapper')]/descendant::button[contains(@id,'MPTableroMedico_panelSignosVitales1_btnActualizarGridSV')]")
