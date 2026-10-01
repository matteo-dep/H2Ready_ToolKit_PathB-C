# -*- coding: utf-8 -*-
"""
H2READY - Tool 2.8 · testi dell'interfaccia in italiano, inglese e sloveno.

CHIAVI DEI DATI, NON TRADOTTE
"config", "fonti", "routing" e "taglie" traducono solo l'ETICHETTA a schermo.
Le chiavi dei dizionari del tool restano in italiano perche':
  - CONFIGURAZIONI e PRESSIONI_INGRESSO finiscono in T28_CONFIGURAZIONE e
    T28_STRATEGIA_SUPPLY, cioe' nell'excelone e poi nell'Action Plan;
  - routing_logic viene letto con 'if "Cascata" in routing';
  - la taglia finisce in T28_TAGLIA_HRS.
Tradurre le chiavi significherebbe spaccare il motore di calcolo e l'export.
"""

T = {

    # ======================================================================
    # ITALIANO
    # ======================================================================
    "it": {
        "title": "🚀 H2READY TOOLKIT - Tool 2.8: Dimensionamento e design tecno-economico HRS",
        "credits": "Sviluppato all'interno del progetto [INTERREG H2Ready]"
                   "(https://www.ita-slo.eu/en/h2ready) da **Matteo De Piccoli - "
                   "[APE FVG](https://www.ape.fvg.it/)**",
        "accesso": "H2READY TOOLKIT - Tool 2.8: Dimensionamento HRS",
        "sottotitolo": "Tool 2.8 · Dimensionamento della stazione di rifornimento",
        "c_progetto": "Progetto", "c_ente": "Sito dell'Ente", "c_contatto": "Contatto",
        "instr_title": "📖 Guida operativa (leggi prima di iniziare)",
        "logic_title": "🧠 Analisi metodologica e standard di progettazione",
        "logic_ko": "ℹ️ File di analisi metodologica estesa caricato esternamente.",
        "instructions_md": """
### 🎯 Qual è il tuo obiettivo?
Dimensionare l'architettura tecnica e stimare l'impatto economico di una
**stazione di rifornimento a idrogeno (HRS)** per mezzi pesanti.

**Istruzioni:**
1. Scegli la **configurazione obiettivo**: determina quali pressioni la stazione deve
   erogare e quanto margine di stoccaggio serve.
2. Imposta la domanda. Puoi inserire i mezzi a mano, oppure derivarli da uno
   **scenario di penetrazione** partendo dal traffico che transita sul nodo.
3. Clicca su **Avvia dimensionamento**: il report resta a schermo e in fondo puoi
   esportarlo nel database centrale.
        """,

        # --- dati ereditati ---
        "dati_title": "📥 Dati ereditati dai questionari precedenti",
        "d_traffico": "Traffico pesante",
        "d_mezzi_g": "mezzi/giorno",
        "d_snam": "Distanza dalla dorsale H₂",
        "d_afir": "Colma un vuoto della rete AFIR",
        "d_hub": "Hub merci o interporti entro 5 km",
        "d_hta": "Distretto Hard-to-Abate confinante",
        "d_filiera": "Accordi di filiera già attivi",
        "d_pums": "Idrogeno già nel PUMS",
        "d_prod": "Produzione locale prevista",
        "d_si": "Sì",
        "d_no": "No",
        "d_da27": "questionario 2.7",
        "d_da26": "tool 2.6",
        "d_no_tgm": "Il questionario 2.7 non riporta un traffico pesante: il valore va "
                    "inserito a mano nella barra laterale.",
        "d_no_700": "Dal 2.7 non risultano aree a piano regolatore compatibili con lo "
                    "stoccaggio a 700 bar: verificare con l'ufficio urbanistica prima di "
                    "dimensionare la stazione.",
        "sugg": "**Configurazione suggerita: {c}**\n\n{p}",

        # --- sidebar ---
        "sb_scen": "🎯 Scenario di penetrazione",
        "sb_config": "🏗️ Configurazione strategica",
        "sb_tech": "⚡ Parametri tecnici HRS",
        "sb_econ": "💸 Parametri economici",
        "lbl_conf_type": "Configurazione dell'impianto obiettivo",
        "scen_on": "Deriva i camion da uno scenario di penetrazione",
        "scen_help": "Invece di indicare quanti camion servi, parti dal traffico che passa "
                     "sul nodo e applica una quota di mezzi a idrogeno e una quota di "
                     "cattura della stazione.",
        "scen_year": "Orizzonte temporale",
        "scen_tgm": "TGM camion a lungo raggio (mezzi/giorno)",
        "scen_tgm_help": "Traffico giornaliero medio di mezzi pesanti sul nodo. "
                         "È il dato raccolto dal tool 2.7.",
        "scen_share": "Quota FCEV sul circolante pesante (%)",
        "scen_capture": "Quota di cattura della stazione (%)",
        "scen_capture_help": "Dei mezzi a idrogeno che transitano, quanti si riforniscono "
                             "proprio qui. Dipende da quante altre stazioni ci sono "
                             "sulla tratta.",
        "scen_result": "**{tgm:,.0f}** camion/giorno × **{s:.1f}%** FCEV × **{c:.0f}%** "
                       "cattura = **{n}** camion serviti al giorno",
        "scen_zero": "⚠️ Con questi parametri la stazione non servirebbe nessun camion. "
                     "Alza la quota di cattura o il traffico.",
        "scen_traj": "📈 Traiettoria a parametri costanti",
        "scen_traj_note": "Stessa quota di cattura, quota FCEV secondo lo scenario di "
                          "riferimento di ciascun orizzonte. Serve al cronoprogramma "
                          "dell'action plan: dice quando la stazione va ampliata.",
        "scen_src": "**Riferimenti.** Reg. UE 2024/1610: −45% CO₂ sui veicoli pesanti "
                    "nuovi entro il 2030, −65% entro il 2035, −90% entro il 2040 (base "
                    "2019); bus urbani nuovi a zero emissioni dal 2030. Roland Berger, "
                    "*Camion a idrogeno* (2021): nel 2023 il parco pesante europeo è "
                    "diesel al 99,5%, FCEV allo 0,4%; ricambio di flotta 10-15 anni. "
                    "Strategia Nazionale Idrogeno (2024), orizzonte 2040-2050: l'idrogeno "
                    "può coprire il 30% dei consumi finali nei trasporti. Le quote "
                    "predefinite sono scenari, non obiettivi vincolanti: vanno discusse, "
                    "non prese per buone.",
        "lbl_cars": "Auto private e flotta leggera (4,5 kg/pieno)",
        "lbl_buses": "Autobus TPL e mezzi speciali (30 kg/pieno)",
        "lbl_trucks": "Camion pesanti a lungo raggio (50 kg/pieno)",
        "trucks_scen": "🎯 {l}: **{n}** (dallo scenario {o})",
        "lbl_window": "Finestra di rifornimento (ore/giorno)",
        "lbl_cf": "Fattore di carico della stazione (capacity factor %)",
        "lbl_source": "Sorgente e pressione di ingresso dell'H₂",
        "help_source": "Suggerita per questa configurazione: {f}",
        "lbl_routing": "Architettura di compressione e stoccaggio",
        "lbl_dispenser": "Pressione di erogazione finale",
        "disp_info": "**{l}:** {p}\n\nDeterminata dalla configurazione.",
        "lbl_energia": "Costo dell'elettricità (€/kWh)",
        "lbl_molecola": "Costo di acquisto o produzione dell'H₂ (€/kg)",
        "lbl_wacc": "Costo del capitale (WACC %)",
        "lbl_anni": "Vita utile dell'impianto (anni)",
        "btn_calc": "🚀 Avvia il dimensionamento impiantistico della HRS",
        "no_veicoli": "Inserisci almeno un veicolo per effettuare il dimensionamento.",

        # --- report ---
        "r_config": "**Configurazione:** {c}",
        "r_scen": "🎯 Scenario {o}",
        "r_tgm": "TGM camion",
        "r_giorno": "/giorno",
        "r_fcev": "Quota FCEV",
        "r_cattura": "Quota di cattura",
        "r_serviti": "Camion serviti",
        "tr_orizzonte": "Orizzonte",
        "tr_fcev": "Quota FCEV",
        "tr_camion": "Camion/giorno",
        "tr_domanda": "Domanda [kg/giorno]",
        "tr_taglia": "Taglia AFIR",
        "tr_colonnine": "Colonnine",
        "tr_capex": "CAPEX [€]",
        "tr_prezzo": "Prezzo minimo [€/kg]",
        "i_title": "⚙️ Dimensionamento dell'impianto",
        "i_domanda": "Domanda nominale",
        "i_stoccaggio": "Stoccaggio fisico",
        "i_potenza": "Potenza del compressore",
        "i_punti": "Punti di erogazione",
        "i_compressione": "{v} kWh/kg di compressione",
        "i_linee": "Linee di erogazione",
        "i_linea": "- **{p} bar** — {kg} kg/giorno · **{n} punti di erogazione** · "
                   "stoccaggio {s} kg · compressore {kw} kW · CAPEX {cx} €",
        "i_sae": "⏱️ **Standard SAE J2601 — linea {p} bar:** velocità limitata a **{v} g/s**. "
                 "Un pieno medio da {kg} kg richiede **{m} minuti** manovra compresa, quindi "
                 "un dispenser serve al massimo **{d} mezzi** nella finestra di apertura. "
                 "Per {e} rifornimenti al giorno servono **{n} colonnine**.",
        "f_title": "💶 Analisi finanziaria",
        "f_capex": "CAPEX totale (chiavi in mano)",
        "f_opex_f": "OPEX fisso (O&M, 4% del CAPEX)",
        "f_opex_e": "OPEX elettrico",
        "f_anno": "/ anno",
        "be_title": "🎯 Break-even point (prezzo minimo alla pompa)",
        "be_txt": "Per coprire il rientro dell'investimento e i costi operativi, il prezzo "
                  "minimo di vendita alla pompa deve essere di **{v} €/kg**.",
        "be_molecola": "Costo della molecola in ingresso",
        "be_sovra": "Sovrapprezzo HRS",
        "be_minimo": "Prezzo minimo di vendita",
        "be_nota": "ℹ️ Il *sovrapprezzo HRS* è il margine necessario alla stazione per "
                   "ripagare compressori, manutenzione ed energia. Se la domanda è troppo "
                   "bassa il sovrapprezzo schizza, rendendo il carburante fuori mercato.",
        "sp_title": "📐 Vincoli spaziali",
        "sp_txt": "**Vincolo DM 23/10/2018:** per garantire le distanze di sicurezza, il "
                  "lotto deve avere una superficie minima di **{a} m²**.",

        # --- export ---
        "e_title": "💾 Esportazione",
        "e_assoc": "I dati verranno associati a {c} (ID {id}).",
        "e_btn": "💾 Esporta il report nel database centrale",
        "e_ok": "✅ Dati del design impiantistico trasmessi con successo.",
        "e_resp": "Risposta del server: {r}",
        "e_err": "Errore di sincronizzazione (codice {c})",
        "e_timeout": "⏳ Il server non ha risposto entro il tempo massimo. Quasi sempre "
                     "significa che i dati **sono stati scritti** e solo la conferma è "
                     "andata persa: controlla la riga del Comune sul foglio prima di "
                     "ripetere l'invio.",
        "e_conn": "Errore di connessione: {e}",

        # --- etichette delle chiavi di dato ---
        "config": {
            "HRS di Transito Puro (Flussi autostradali)": "HRS di solo transito (flussi autostradali)",
            "HRS Hub Intermodale Multi-Mezzo": "HRS hub intermodale multi-mezzo",
            "HRS Valley Strategica Integrata": "HRS valley strategica integrata",
        },
        "config_nota": {
            "HRS di Transito Puro (Flussi autostradali)":
                "Erogazione a 700 bar per il solo trasporto pesante a lungo raggio. "
                "Autobus e mezzi di piazzale non sono serviti da questa configurazione.",
            "HRS Hub Intermodale Multi-Mezzo":
                "Due linee di erogazione: 350 bar per autobus e mezzi di piazzale, "
                "700 bar per camion e auto. Raddoppia dispenser e chiller.",
            "HRS Valley Strategica Integrata":
                "Stazione integrata con produzione locale. Lo stoccaggio assorbe la "
                "variabilità della fonte rinnovabile: margine più ampio.",
        },
        "fonti": {"Elettrolizzatore (20 bar)": "Elettrolizzatore (20 bar)",
                  "Pipeline Snam (30 bar)": "Dorsale Snam (30 bar)",
                  "Carro Bombolaio (200 bar)": "Carro bombolaio (200 bar)"},
        "routing": {"Magazzino a Cascata (3 banchi)": "Stoccaggio a cascata (3 banchi)",
                    "Booster Compressor (Diretta)": "Compressore booster (diretta)"},
        "taglie": {"Large (≥ 1 t/giorno, conforme AFIR)": "Large (≥ 1 t/giorno, conforme AFIR)",
                   "Medium (0,5 - 1 t/giorno)": "Medium (0,5 - 1 t/giorno)",
                   "Small (< 0,5 t/giorno)": "Small (< 0,5 t/giorno)"},
    },

    # ======================================================================
    # ENGLISH
    # ======================================================================
    "en": {
        "title": "🚀 H2READY TOOLKIT - Tool 2.8: HRS sizing and techno-economic design",
        "credits": "Developed within the [INTERREG H2Ready]"
                   "(https://www.ita-slo.eu/en/h2ready) project by **Matteo De Piccoli - "
                   "[APE FVG](https://www.ape.fvg.it/)**",
        "accesso": "H2READY TOOLKIT - Tool 2.8: HRS sizing",
        "sottotitolo": "Tool 2.8 · Sizing of the refuelling station",
        "c_progetto": "Project", "c_ente": "Organisation website", "c_contatto": "Contact",
        "instr_title": "📖 Operational guide (read before starting)",
        "logic_title": "🧠 Methodology and design standards",
        "logic_ko": "ℹ️ The extended methodology file is loaded externally.",
        "instructions_md": """
### 🎯 What is your goal?
To size the technical architecture and estimate the economic impact of a
**hydrogen refuelling station (HRS)** for heavy vehicles.

**Instructions:**
1. Choose the **target configuration**: it determines which pressures the station must
   dispense and how much storage margin is needed.
2. Set the demand. You can enter the vehicles by hand, or derive them from a
   **penetration scenario** starting from the traffic crossing the node.
3. Click **Run the sizing**: the report stays on screen and at the bottom you can
   export it to the central database.
        """,

        "dati_title": "📥 Data inherited from the previous questionnaires",
        "d_traffico": "Heavy traffic",
        "d_mezzi_g": "vehicles/day",
        "d_snam": "Distance from the H₂ backbone",
        "d_afir": "Fills a gap in the AFIR network",
        "d_hub": "Freight hubs or terminals within 5 km",
        "d_hta": "Adjacent hard-to-abate district",
        "d_filiera": "Supply chain agreements already active",
        "d_pums": "Hydrogen already in the mobility plan",
        "d_prod": "Local production planned",
        "d_si": "Yes",
        "d_no": "No",
        "d_da27": "questionnaire 2.7",
        "d_da26": "tool 2.6",
        "d_no_tgm": "Questionnaire 2.7 reports no heavy traffic: the value must be entered "
                    "by hand in the sidebar.",
        "d_no_700": "Questionnaire 2.7 shows no zoned areas compatible with 700 bar storage: "
                    "check with the planning office before sizing the station.",
        "sugg": "**Suggested configuration: {c}**\n\n{p}",

        "sb_scen": "🎯 Penetration scenario",
        "sb_config": "🏗️ Strategic configuration",
        "sb_tech": "⚡ HRS technical parameters",
        "sb_econ": "💸 Economic parameters",
        "lbl_conf_type": "Target plant configuration",
        "scen_on": "Derive the trucks from a penetration scenario",
        "scen_help": "Instead of stating how many trucks you serve, start from the traffic "
                     "crossing the node and apply a share of hydrogen vehicles and a "
                     "capture rate for the station.",
        "scen_year": "Time horizon",
        "scen_tgm": "Long-haul truck AADT (vehicles/day)",
        "scen_tgm_help": "Average daily traffic of heavy vehicles at the node. "
                         "It is the figure collected by tool 2.7.",
        "scen_share": "FCEV share of the heavy fleet (%)",
        "scen_capture": "Station capture rate (%)",
        "scen_capture_help": "Of the hydrogen vehicles passing through, how many refuel "
                             "here. It depends on how many other stations sit on the "
                             "same route.",
        "scen_result": "**{tgm:,.0f}** trucks/day × **{s:.1f}%** FCEV × **{c:.0f}%** "
                       "capture = **{n}** trucks served per day",
        "scen_zero": "⚠️ With these parameters the station would serve no trucks. "
                     "Raise the capture rate or the traffic.",
        "scen_traj": "📈 Trajectory at constant parameters",
        "scen_traj_note": "Same capture rate, FCEV share following the reference scenario "
                          "for each horizon. It feeds the action plan's timeline: it says "
                          "when the station must be expanded.",
        "scen_src": "**References.** EU Reg. 2024/1610: −45% CO₂ on new heavy vehicles by "
                    "2030, −65% by 2035, −90% by 2040 (2019 baseline); new urban buses "
                    "zero-emission from 2030. Roland Berger, *Hydrogen trucks* (2021): in "
                    "2023 the European heavy fleet was 99.5% diesel and 0.4% FCEV; fleet "
                    "renewal takes 10-15 years. Italian National Hydrogen Strategy (2024), "
                    "2040-2050 horizon: hydrogen may cover 30% of final transport "
                    "consumption. The default shares are scenarios, not binding targets: "
                    "they are to be discussed, not taken as given.",
        "lbl_cars": "Private cars and light fleet (4.5 kg/fill)",
        "lbl_buses": "Public transport buses and special vehicles (30 kg/fill)",
        "lbl_trucks": "Long-haul heavy trucks (50 kg/fill)",
        "trucks_scen": "🎯 {l}: **{n}** (from the {o} scenario)",
        "lbl_window": "Refuelling window (hours/day)",
        "lbl_cf": "Station capacity factor (%)",
        "lbl_source": "H₂ source and inlet pressure",
        "help_source": "Suggested for this configuration: {f}",
        "lbl_routing": "Compression and storage architecture",
        "lbl_dispenser": "Final dispensing pressure",
        "disp_info": "**{l}:** {p}\n\nSet by the configuration.",
        "lbl_energia": "Electricity cost (€/kWh)",
        "lbl_molecola": "H₂ purchase or production cost (€/kg)",
        "lbl_wacc": "Cost of capital (WACC %)",
        "lbl_anni": "Plant service life (years)",
        "btn_calc": "🚀 Run the HRS plant sizing",
        "no_veicoli": "Enter at least one vehicle to run the sizing.",

        "r_config": "**Configuration:** {c}",
        "r_scen": "🎯 {o} scenario",
        "r_tgm": "Truck AADT",
        "r_giorno": "/day",
        "r_fcev": "FCEV share",
        "r_cattura": "Capture rate",
        "r_serviti": "Trucks served",
        "tr_orizzonte": "Horizon",
        "tr_fcev": "FCEV share",
        "tr_camion": "Trucks/day",
        "tr_domanda": "Demand [kg/day]",
        "tr_taglia": "AFIR size",
        "tr_colonnine": "Dispensers",
        "tr_capex": "CAPEX [€]",
        "tr_prezzo": "Minimum price [€/kg]",
        "i_title": "⚙️ Plant sizing",
        "i_domanda": "Nominal demand",
        "i_stoccaggio": "Physical storage",
        "i_potenza": "Compressor power",
        "i_punti": "Dispensing points",
        "i_compressione": "{v} kWh/kg of compression",
        "i_linee": "Dispensing lines",
        "i_linea": "- **{p} bar** — {kg} kg/day · **{n} dispensing points** · "
                   "storage {s} kg · compressor {kw} kW · CAPEX {cx} €",
        "i_sae": "⏱️ **SAE J2601 standard — {p} bar line:** rate limited to **{v} g/s**. "
                 "An average {kg} kg fill takes **{m} minutes** including manoeuvring, so "
                 "one dispenser serves at most **{d} vehicles** within the opening window. "
                 "For {e} refuellings per day, **{n} dispensers** are needed.",
        "f_title": "💶 Financial analysis",
        "f_capex": "Total CAPEX (turnkey)",
        "f_opex_f": "Fixed OPEX (O&M, 4% of CAPEX)",
        "f_opex_e": "Electricity OPEX",
        "f_anno": "/ year",
        "be_title": "🎯 Break-even point (minimum price at the pump)",
        "be_txt": "To cover the return on investment and the operating costs, the minimum "
                  "selling price at the pump must be **{v} €/kg**.",
        "be_molecola": "Inlet molecule cost",
        "be_sovra": "HRS surcharge",
        "be_minimo": "Minimum selling price",
        "be_nota": "ℹ️ The *HRS surcharge* is the margin the station needs to pay back "
                   "compressors, maintenance and energy. If demand is too low the surcharge "
                   "soars, pricing the fuel out of the market.",
        "sp_title": "📐 Spatial constraints",
        "sp_txt": "**Italian DM 23/10/2018 constraint:** to guarantee safety distances, "
                  "the plot must have a minimum area of **{a} m²**.",

        "e_title": "💾 Export",
        "e_assoc": "The data will be linked to {c} (ID {id}).",
        "e_btn": "💾 Export the report to the central database",
        "e_ok": "✅ Plant design data transmitted successfully.",
        "e_resp": "Server response: {r}",
        "e_err": "Synchronisation error (code {c})",
        "e_timeout": "⏳ The server did not answer within the time limit. This almost always "
                     "means the data **was written** and only the confirmation was lost: "
                     "check the municipality's row in the sheet before sending again.",
        "e_conn": "Connection error: {e}",

        "config": {
            "HRS di Transito Puro (Flussi autostradali)": "Pure transit HRS (motorway flows)",
            "HRS Hub Intermodale Multi-Mezzo": "Intermodal multi-vehicle hub HRS",
            "HRS Valley Strategica Integrata": "Integrated strategic valley HRS",
        },
        "config_nota": {
            "HRS di Transito Puro (Flussi autostradali)":
                "700 bar dispensing for long-haul heavy transport only. Buses and yard "
                "vehicles are not served by this configuration.",
            "HRS Hub Intermodale Multi-Mezzo":
                "Two dispensing lines: 350 bar for buses and yard vehicles, 700 bar for "
                "trucks and cars. It doubles dispensers and chillers.",
            "HRS Valley Strategica Integrata":
                "Station integrated with local production. Storage absorbs the variability "
                "of the renewable source: a wider margin.",
        },
        "fonti": {"Elettrolizzatore (20 bar)": "Electrolyser (20 bar)",
                  "Pipeline Snam (30 bar)": "Snam backbone (30 bar)",
                  "Carro Bombolaio (200 bar)": "Tube trailer (200 bar)"},
        "routing": {"Magazzino a Cascata (3 banchi)": "Cascade storage (3 banks)",
                    "Booster Compressor (Diretta)": "Booster compressor (direct)"},
        "taglie": {"Large (≥ 1 t/giorno, conforme AFIR)": "Large (≥ 1 t/day, AFIR compliant)",
                   "Medium (0,5 - 1 t/giorno)": "Medium (0.5 - 1 t/day)",
                   "Small (< 0,5 t/giorno)": "Small (< 0.5 t/day)"},
    },

    # ======================================================================
    # SLOVENŠČINA
    # ======================================================================
    "sl": {
        "title": "🚀 H2READY TOOLKIT - Orodje 2.8: Dimenzioniranje in tehnično-ekonomsko "
                 "načrtovanje HRS",
        "credits": "Razvito v okviru projekta [INTERREG H2Ready]"
                   "(https://www.ita-slo.eu/en/h2ready), avtor **Matteo De Piccoli - "
                   "[APE FVG](https://www.ape.fvg.it/)**",
        "accesso": "H2READY TOOLKIT - Orodje 2.8: Dimenzioniranje HRS",
        "sottotitolo": "Orodje 2.8 · Dimenzioniranje polnilne postaje",
        "c_progetto": "Projekt", "c_ente": "Spletna stran ustanove", "c_contatto": "Kontakt",
        "instr_title": "📖 Operativni vodnik (preberite pred začetkom)",
        "logic_title": "🧠 Metodologija in projektni standardi",
        "logic_ko": "ℹ️ Razširjena metodološka datoteka je naložena zunaj aplikacije.",
        "instructions_md": """
### 🎯 Kakšen je vaš cilj?
Dimenzionirati tehnično zasnovo in oceniti gospodarski učinek **vodikove polnilne
postaje (HRS)** za težka vozila.

**Navodila:**
1. Izberite **ciljno konfiguracijo**: določa, katere tlake mora postaja zagotavljati
   in kolikšna rezerva skladiščenja je potrebna.
2. Nastavite povpraševanje. Vozila lahko vnesete ročno ali jih izpeljete iz
   **scenarija prodora** na podlagi prometa, ki prečka vozlišče.
3. Kliknite **Zaženi dimenzioniranje**: poročilo ostane na zaslonu, na dnu pa ga
   lahko izvozite v osrednjo bazo.
        """,

        "dati_title": "📥 Podatki, prevzeti iz prejšnjih vprašalnikov",
        "d_traffico": "Težki promet",
        "d_mezzi_g": "vozil/dan",
        "d_snam": "Razdalja do vodikovega hrbtenice",
        "d_afir": "Zapolnjuje vrzel v omrežju AFIR",
        "d_hub": "Tovorna vozlišča ali terminali v 5 km",
        "d_hta": "Sosednje energetsko intenzivno območje",
        "d_filiera": "Sporazumi v dobavni verigi že sklenjeni",
        "d_pums": "Vodik je že v prometni strategiji",
        "d_prod": "Načrtovana lokalna proizvodnja",
        "d_si": "Da",
        "d_no": "Ne",
        "d_da27": "vprašalnik 2.7",
        "d_da26": "orodje 2.6",
        "d_no_tgm": "Vprašalnik 2.7 ne navaja težkega prometa: vrednost je treba ročno "
                    "vnesti v stranski vrstici.",
        "d_no_700": "Iz vprašalnika 2.7 ni razvidno, da bi prostorski akti predvidevali "
                    "območja, primerna za shranjevanje pri 700 bar: pred dimenzioniranjem "
                    "postaje preverite pri službi za prostor.",
        "sugg": "**Predlagana konfiguracija: {c}**\n\n{p}",

        "sb_scen": "🎯 Scenarij prodora",
        "sb_config": "🏗️ Strateška konfiguracija",
        "sb_tech": "⚡ Tehnični parametri HRS",
        "sb_econ": "💸 Ekonomski parametri",
        "lbl_conf_type": "Ciljna konfiguracija naprave",
        "scen_on": "Število tovornjakov izpelji iz scenarija prodora",
        "scen_help": "Namesto da navedete, koliko tovornjakov oskrbujete, izhajajte iz "
                     "prometa skozi vozlišče ter uporabite delež vodikovih vozil in delež, "
                     "ki ga postaja zajame.",
        "scen_year": "Časovni horizont",
        "scen_tgm": "PLDP tovornjakov na dolge razdalje (vozil/dan)",
        "scen_tgm_help": "Povprečni dnevni promet težkih vozil na vozlišču. To je podatek, "
                         "zbran z orodjem 2.7.",
        "scen_share": "Delež FCEV v voznem parku težkih vozil (%)",
        "scen_capture": "Delež, ki ga postaja zajame (%)",
        "scen_capture_help": "Koliko vodikovih vozil, ki vozijo mimo, se oskrbi prav tukaj. "
                             "Odvisno je od tega, koliko drugih postaj je na isti trasi.",
        "scen_result": "**{tgm:,.0f}** tovornjakov/dan × **{s:.1f} %** FCEV × "
                       "**{c:.0f} %** zajem = **{n}** oskrbljenih tovornjakov na dan",
        "scen_zero": "⚠️ S temi parametri postaja ne bi oskrbela nobenega tovornjaka. "
                     "Povečajte delež zajema ali promet.",
        "scen_traj": "📈 Trajektorija pri nespremenjenih parametrih",
        "scen_traj_note": "Enak delež zajema, delež FCEV po referenčnem scenariju za vsak "
                          "horizont. Služi časovnici akcijskega načrta: pove, kdaj je treba "
                          "postajo razširiti.",
        "scen_src": "**Viri.** Uredba EU 2024/1610: −45 % CO₂ pri novih težkih vozilih do "
                    "leta 2030, −65 % do 2035, −90 % do 2040 (izhodišče 2019); novi mestni "
                    "avtobusi brez emisij od leta 2030. Roland Berger, *Vodikovi tovornjaki* "
                    "(2021): leta 2023 je bil evropski park težkih vozil 99,5 % dizelski in "
                    "0,4 % FCEV; obnova voznega parka traja 10-15 let. Italijanska nacionalna "
                    "vodikova strategija (2024), horizont 2040-2050: vodik lahko pokrije 30 % "
                    "končne porabe v prometu. Privzeti deleži so scenariji, ne zavezujoči "
                    "cilji: o njih je treba razpravljati, ne jemati jih za dane.",
        "lbl_cars": "Osebna vozila in lahki vozni park (4,5 kg/polnjenje)",
        "lbl_buses": "Avtobusi JPP in posebna vozila (30 kg/polnjenje)",
        "lbl_trucks": "Težki tovornjaki na dolge razdalje (50 kg/polnjenje)",
        "trucks_scen": "🎯 {l}: **{n}** (iz scenarija {o})",
        "lbl_window": "Okno za oskrbo (ure/dan)",
        "lbl_cf": "Faktor obremenitve postaje (capacity factor %)",
        "lbl_source": "Vir in vstopni tlak H₂",
        "help_source": "Predlagano za to konfiguracijo: {f}",
        "lbl_routing": "Zasnova stiskanja in skladiščenja",
        "lbl_dispenser": "Končni tlak oddaje",
        "disp_info": "**{l}:** {p}\n\nDoloča ga konfiguracija.",
        "lbl_energia": "Strošek elektrike (€/kWh)",
        "lbl_molecola": "Strošek nakupa ali proizvodnje H₂ (€/kg)",
        "lbl_wacc": "Strošek kapitala (WACC %)",
        "lbl_anni": "Življenjska doba naprave (leta)",
        "btn_calc": "🚀 Zaženi dimenzioniranje naprave HRS",
        "no_veicoli": "Za dimenzioniranje vnesite vsaj eno vozilo.",

        "r_config": "**Konfiguracija:** {c}",
        "r_scen": "🎯 Scenarij {o}",
        "r_tgm": "PLDP tovornjakov",
        "r_giorno": "/dan",
        "r_fcev": "Delež FCEV",
        "r_cattura": "Delež zajema",
        "r_serviti": "Oskrbljeni tovornjaki",
        "tr_orizzonte": "Horizont",
        "tr_fcev": "Delež FCEV",
        "tr_camion": "Tovornjakov/dan",
        "tr_domanda": "Povpraševanje [kg/dan]",
        "tr_taglia": "Velikost AFIR",
        "tr_colonnine": "Polnilna mesta",
        "tr_capex": "CAPEX [€]",
        "tr_prezzo": "Najnižja cena [€/kg]",
        "i_title": "⚙️ Dimenzioniranje naprave",
        "i_domanda": "Nazivno povpraševanje",
        "i_stoccaggio": "Fizično skladiščenje",
        "i_potenza": "Moč kompresorja",
        "i_punti": "Polnilna mesta",
        "i_compressione": "{v} kWh/kg stiskanja",
        "i_linee": "Linije oddaje",
        "i_linea": "- **{p} bar** — {kg} kg/dan · **{n} polnilnih mest** · "
                   "skladiščenje {s} kg · kompresor {kw} kW · CAPEX {cx} €",
        "i_sae": "⏱️ **Standard SAE J2601 — linija {p} bar:** hitrost omejena na **{v} g/s**. "
                 "Povprečno polnjenje {kg} kg traja **{m} minut** z manevriranjem vred, zato "
                 "eno polnilno mesto v odpiralnem oknu oskrbi največ **{d} vozil**. "
                 "Za {e} polnjenj na dan je potrebnih **{n} polnilnih mest**.",
        "f_title": "💶 Finančna analiza",
        "f_capex": "Skupni CAPEX (na ključ)",
        "f_opex_f": "Fiksni OPEX (O&M, 4 % CAPEX)",
        "f_opex_e": "OPEX za elektriko",
        "f_anno": "/ leto",
        "be_title": "🎯 Prag rentabilnosti (najnižja cena na polnilnici)",
        "be_txt": "Za pokritje povračila naložbe in obratovalnih stroškov mora najnižja "
                  "prodajna cena na polnilnici znašati **{v} €/kg**.",
        "be_molecola": "Strošek vstopne molekule",
        "be_sovra": "Pribitek HRS",
        "be_minimo": "Najnižja prodajna cena",
        "be_nota": "ℹ️ *Pribitek HRS* je marža, ki jo postaja potrebuje za povrnitev "
                   "kompresorjev, vzdrževanja in energije. Če je povpraševanje prenizko, "
                   "pribitek poskoči in gorivo postane tržno nezanimivo.",
        "sp_title": "📐 Prostorske omejitve",
        "sp_txt": "**Omejitev it. DM 23/10/2018:** za zagotovitev varnostnih odmikov mora "
                  "imeti parcela najmanjšo površino **{a} m²**.",

        "e_title": "💾 Izvoz",
        "e_assoc": "Podatki bodo povezani z {c} (ID {id}).",
        "e_btn": "💾 Izvozi poročilo v osrednjo bazo",
        "e_ok": "✅ Podatki o zasnovi naprave so bili uspešno poslani.",
        "e_resp": "Odgovor strežnika: {r}",
        "e_err": "Napaka sinhronizacije (koda {c})",
        "e_timeout": "⏳ Strežnik ni odgovoril v najdaljšem času. Skoraj vedno to pomeni, da "
                     "so bili podatki **zapisani** in da se je izgubila le potrditev: pred "
                     "ponovnim pošiljanjem preverite vrstico občine v preglednici.",
        "e_conn": "Napaka povezave: {e}",

        "config": {
            "HRS di Transito Puro (Flussi autostradali)": "HRS za čisti tranzit (avtocestni tokovi)",
            "HRS Hub Intermodale Multi-Mezzo": "HRS intermodalno vozlišče za več vrst vozil",
            "HRS Valley Strategica Integrata": "Integrirana strateška dolinska HRS",
        },
        "config_nota": {
            "HRS di Transito Puro (Flussi autostradali)":
                "Oddaja pri 700 bar samo za težki promet na dolge razdalje. Avtobusi in "
                "vozila na dvorišču s to konfiguracijo niso oskrbovani.",
            "HRS Hub Intermodale Multi-Mezzo":
                "Dve liniji oddaje: 350 bar za avtobuse in vozila na dvorišču, 700 bar za "
                "tovornjake in osebna vozila. Podvoji polnilna mesta in hladilnike.",
            "HRS Valley Strategica Integrata":
                "Postaja, povezana z lokalno proizvodnjo. Skladiščenje absorbira "
                "spremenljivost obnovljivega vira: širša rezerva.",
        },
        "fonti": {"Elettrolizzatore (20 bar)": "Elektrolizer (20 bar)",
                  "Pipeline Snam (30 bar)": "Hrbtenica Snam (30 bar)",
                  "Carro Bombolaio (200 bar)": "Jeklenkarski prikoličar (200 bar)"},
        "routing": {"Magazzino a Cascata (3 banchi)": "Kaskadno skladiščenje (3 bloki)",
                    "Booster Compressor (Diretta)": "Pospeševalni kompresor (neposredno)"},
        "taglie": {"Large (≥ 1 t/giorno, conforme AFIR)": "Large (≥ 1 t/dan, skladno z AFIR)",
                   "Medium (0,5 - 1 t/giorno)": "Medium (0,5 - 1 t/dan)",
                   "Small (< 0,5 t/giorno)": "Small (< 0,5 t/dan)"},
    },
}
