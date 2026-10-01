"""
H2READY TOOLKIT - Tool 2.8: Dimensionamento e design tecno-economico HRS
Progetto Interreg Italia-Slovenia H2READY - APE FVG

Struttura della pagina:
  1. SCENARIO   - dai transiti alla domanda, per orizzonte 2030 / 2040 / 2050
  2. IMPIANTO   - dimensionamento di compressione, stoccaggio ed erogazione
  3. ECONOMIA   - CAPEX, OPEX e prezzo minimo alla pompa
  4. EXPORT     - trasmissione all'excelone

I risultati vivono in st.session_state: il blocco di esportazione deve
sopravvivere ai rerun, altrimenti sparisce al primo tasto premuto.
"""

import streamlit as st
import pandas as pd
import os
import requests
import json

# ==========================================
# 1. CONFIGURAZIONE PAGINA E LINGUA
# ==========================================
st.set_page_config(page_title="H2READY TOOLKIT - Tool 2.8: Dimensionamento HRS", layout="wide")

LANG_OPTIONS = {"Italiano": "it", "English": "en", "Slovenščina": "sl"}
lang_choice = st.sidebar.selectbox("🌐 Lingua / Language / Jezik", list(LANG_OPTIONS.keys()))
LANG = LANG_OPTIONS[lang_choice]

import h2ready as H

from testi_2_8 import T
_t = T.get(LANG, T["it"])


# Etichette tradotte delle chiavi dei dizionari di dati. Le chiavi restano in
# italiano: le legge il motore di calcolo e finiscono nell'excelone.
def vis(gruppo, chiave):
    return _t.get(gruppo, {}).get(chiave, chiave)

comune = H.blocco_accesso(_t["accesso"], percorso="C", avanzato=True, lingua=LANG)
if comune is None:
    st.stop()


# ==========================================
# 2. SCENARI E CONFIGURAZIONI
# ==========================================
# Quote FCEV sul circolante pesante per orizzonte. Sono scenari costruiti sui
# riferimenti citati in _t["scen_src"], non target vincolanti:
#  2030 - la riduzione richiesta dal Reg. 2024/1610 sara' coperta in prevalenza
#         dai BEV; l'idrogeno resta una nicchia sul lungo raggio
#  2040 - obbligo -90% sui nuovi immatricolati, con ricambio di flotta in corso
#  2050 - quota della Strategia Nazionale sui consumi finali nei trasporti
SCENARI = {"2030": 3.0, "2040": 15.0, "2050": 30.0}

CONFIGURAZIONI = {
    "HRS di Transito Puro (Flussi autostradali)": {
        "chiave": "transito", "pressioni": [700], "overcap": 1.9,
        "fonte_suggerita": "Carro Bombolaio (200 bar)",
    },
    "HRS Hub Intermodale Multi-Mezzo": {
        "chiave": "hub", "pressioni": [350, 700], "overcap": 2.1,
        "fonte_suggerita": "Pipeline Snam (30 bar)",
    },
    "HRS Valley Strategica Integrata": {
        "chiave": "valley", "pressioni": [350, 700], "overcap": 2.5,
        "fonte_suggerita": "Elettrolizzatore (20 bar)",
    },
}

PRESSIONI_INGRESSO = {
    "Elettrolizzatore (20 bar)": 20,
    "Pipeline Snam (30 bar)": 30,
    "Carro Bombolaio (200 bar)": 200,
}

KG_AUTO, KG_BUS, KG_CAMION = 4.5, 30.0, 50.0

# ==========================================
# 3. INTESTAZIONE
# ==========================================
st.title(_t["title"])
st.markdown(_t["credits"])
st.markdown(
    "<p style='font-size: 0.8rem; color: gray;'>"
    f"🌐 {_t['c_progetto']}: <a href='https://www.ita-slo.eu/en/h2ready' "
    "target='_blank'>Interreg H2Ready</a> | "
    f"🏠 {_t['c_ente']}: <a href='https://www.ape.fvg.it/' "
    "target='_blank'>APE FVG</a> | "
    f"📧 {_t['c_contatto']}: "
    "<a href='mailto:matteo.depiccoli@ape.fvg.it'>matteo.depiccoli@ape.fvg.it</a>"
    "</p>", unsafe_allow_html=True)
st.divider()

# --- Comune e dati ereditati dal questionario 2.7 -------------------------
H.intestazione_comune(comune, _t["sottotitolo"])

_tgm = H.valore(comune, "T27_TGM_CAMION", 0) or 0
_snam = H.valore(comune, "T27_DISTANZA_SNAM_KM", None)
_voci, _avvisi = [], []

if _tgm > 0:
    _voci.append((_t["d_traffico"], f"{_tgm:,.0f} " + _t["d_mezzi_g"], _t["d_da27"]))
else:
    _avvisi.append(("warning", _t["d_no_tgm"]))
if _snam is not None:
    _voci.append((_t["d_snam"], f"{_snam:,.1f} km", _t["d_da27"]))

for _col, _k in (("T27_FLAG_AFIR_GAP", "d_afir"),
                 ("T27_FLAG_HUB_MERCI", "d_hub"),
                 ("T27_FLAG_SINERGIA_HTA", "d_hta"),
                 ("T27_FLAG_ACCORDI_FILIERA", "d_filiera"),
                 ("T27_FLAG_PUMS", "d_pums")):
    if not H.vuoto(comune.get(_col)):
        _voci.append((_t[_k], _t["d_si"] if H.vero(comune[_col]) else _t["d_no"],
                      _t["d_da27"]))

_prod_b = H.valore(comune, "T26_PRODUZIONE_H2_TON_ANNO", 0) or 0
if _prod_b > 0:
    _voci.append((_t["d_prod"], f"{_prod_b:,.1f} t/a", _t["d_da26"]))

if not H.vero(comune.get("T27_FLAG_AREE_700BAR")) and not H.vuoto(comune.get("T27_FLAG_AREE_700BAR")):
    _avvisi.append(("warning", _t["d_no_700"]))

H.scheda_dati(_t["dati_title"], _voci, _avvisi)

# --- Configurazione suggerita dai dati -----------------------------------
_modo_sugg, _perche = H.modalita_2_8(comune)
_CHIAVI = {c["chiave"]: nome for nome, c in CONFIGURAZIONI.items()}
_config_default = _CHIAVI.get(_modo_sugg, list(CONFIGURAZIONI.keys())[0])
st.info(_t["sugg"].format(c=vis("config", _config_default), p=_perche))

with st.expander(_t["instr_title"], expanded=True):
    st.markdown(_t["instructions_md"])

with st.expander(_t["logic_title"], expanded=False):
    nome_file_logica = f"logic_logistica_{LANG}.md"
    if os.path.exists(nome_file_logica):
        with open(nome_file_logica, "r", encoding="utf-8") as f:
            st.markdown(f.read())
    else:
        st.caption(_t["logic_ko"])

st.markdown("---")

# ==========================================
# 4. SIDEBAR
# ==========================================
if "prev_fonte" not in st.session_state:
    st.session_state.prev_fonte = "Elettrolizzatore (20 bar)"
    st.session_state.costo_molecola_in = 8.0

with st.sidebar:
    with st.expander(_t["sb_config"], expanded=True):
        _opz = list(CONFIGURAZIONI.keys())
        config_scelta = st.selectbox(_t["lbl_conf_type"], _opz,
                                     index=_opz.index(_config_default),
                                     format_func=lambda k: vis("config", k))
        CFG = CONFIGURAZIONI[config_scelta]
        st.caption(vis("config_nota", config_scelta))

    with st.expander(_t["sb_scen"], expanded=True):
        scen_on = st.checkbox(_t["scen_on"], value=_tgm > 0, help=_t["scen_help"])
        if scen_on:
            orizzonte = st.selectbox(_t["scen_year"], list(SCENARI.keys()))
            tgm_camion = st.number_input(_t["scen_tgm"], 0, 50000,
                                         int(min(_tgm, 50000)) if _tgm > 0 else 5000,
                                         step=100, help=_t["scen_tgm_help"])
            quota_fcev = st.slider(_t["scen_share"], 0.0, 60.0, SCENARI[orizzonte], step=0.5)
            # con un hub merci o accordi di filiera i mezzi rientrano in deposito:
            # la stazione ne cattura una quota molto più alta che sul solo transito
            _cattura_def = 25 if (H.vero(comune.get("T27_FLAG_HUB_MERCI")) or
                                  H.vero(comune.get("T27_FLAG_ACCORDI_FILIERA"))) else 10
            quota_cattura = st.slider(_t["scen_capture"], 1, 100, _cattura_def,
                                      help=_t["scen_capture_help"])
            n_camion = int(round(tgm_camion * quota_fcev / 100.0 * quota_cattura / 100.0))
            st.markdown(_t["scen_result"].format(tgm=tgm_camion, s=quota_fcev,
                                                 c=quota_cattura, n=n_camion))
            if n_camion == 0:
                st.warning(_t["scen_zero"])
        else:
            orizzonte, tgm_camion, quota_fcev, quota_cattura = "-", 0, 0.0, 0
            n_camion = None

    with st.expander(_t["sb_tech"], expanded=True):
        n_auto = st.slider(_t["lbl_cars"], 0, 100, 10, step=5)
        n_bus = st.slider(_t["lbl_buses"], 0, 50, 5, step=1)
        if n_camion is None:
            n_camion = st.slider(_t["lbl_trucks"], 0, 150, 30, step=5)
        else:
            st.caption(_t["trucks_scen"].format(l=_t["lbl_trucks"], n=n_camion,
                                                o=orizzonte))
        finestra_ore = st.slider(_t["lbl_window"], 1, 24, 8)
        capacity_factor = st.slider(_t["lbl_cf"], 10, 100, 75) / 100.0

        fonte_h2 = st.selectbox(
            _t["lbl_source"], list(PRESSIONI_INGRESSO.keys()),
            index=list(PRESSIONI_INGRESSO.keys()).index(CFG["fonte_suggerita"]),
            format_func=lambda k: vis("fonti", k),
            help=_t["help_source"].format(f=vis("fonti", CFG["fonte_suggerita"])))

        if st.session_state.prev_fonte != fonte_h2:
            if "Pipeline" in fonte_h2:
                st.session_state.costo_molecola_in = 6.0
            elif "Carro" in fonte_h2:
                st.session_state.costo_molecola_in = 10.0
            else:
                st.session_state.costo_molecola_in = 8.0
            st.session_state.prev_fonte = fonte_h2

        routing_logic = st.selectbox(
            _t["lbl_routing"], ["Magazzino a Cascata (3 banchi)", "Booster Compressor (Diretta)"],
            format_func=lambda k: vis("routing", k))

        etichette = " + ".join(f"{p} bar" for p in CFG["pressioni"])
        st.info(_t["disp_info"].format(l=_t["lbl_dispenser"], p=etichette))

    with st.expander(_t["sb_econ"], expanded=True):
        costo_energia = st.number_input(_t["lbl_energia"], 0.05, 0.50, 0.15, step=0.01)
        costo_molecola_in = st.number_input(_t["lbl_molecola"],
                                            1.0, 20.0, step=0.5, key="costo_molecola_in")
        wacc = st.slider(_t["lbl_wacc"], 1, 15, 6) / 100.0
        anni_vita = st.slider(_t["lbl_anni"], 5, 30, 15)


# ==========================================
# 5. MOTORE DI CALCOLO
# ==========================================
MINUTI_MANOVRA = 6.0   # accosto, aggancio, pagamento, ripartenza


def dimensiona_linea(kg_giorno, n_erogazioni, p_inlet, p_disp, routing, finestra, overcap):
    """Dimensiona una singola linea di compressione, stoccaggio ed erogazione.

    n_erogazioni serve a contare i punti di erogazione necessari: un dispenser
    non e' illimitato. Lo standard SAE J2601 fissa la velocita' massima di
    riempimento, quindi il numero di mezzi che una colonnina serve in un giorno
    dipende solo dalla finestra di apertura e dal tempo del singolo pieno."""
    Cp, k_ad, eta_is, T_in, stadi = 14.5, 1.41, 0.60, 293.15, 3

    if "Cascata" in routing:
        eta_el, fat_usabilita, costo_storage_kg, ore_lavoro = 0.88, 0.91, 1092, 20
    else:
        eta_el, fat_usabilita, costo_storage_kg, ore_lavoro = 0.92, 0.95, 968, finestra

    p_stoccaggio = p_disp + 150
    portata_kg_s = kg_giorno / (ore_lavoro * 3600) if kg_giorno > 0 else 0.0
    stoccaggio_kg = (kg_giorno * overcap) / fat_usabilita

    beta_st = (p_stoccaggio / p_inlet) ** (1 / stadi)
    T_out = T_in * (beta_st ** ((k_ad - 1) / k_ad))
    lav_reale = (Cp * (T_out - T_in) / eta_is) * stadi

    potenza_kW = (lav_reale * portata_kg_s) / eta_el
    consumo_kwh_kg = lav_reale / 3600 / eta_el

    # --- Punti di erogazione necessari ---
    velocita = 60 if p_disp == 700 else 120          # g/s, limite SAE J2601
    kg_medio = kg_giorno / n_erogazioni if n_erogazioni > 0 else 0.0
    minuti_pieno = (kg_medio * 1000 / velocita) / 60 + MINUTI_MANOVRA
    per_dispenser = (finestra * 60) / minuti_pieno if minuti_pieno > 0 else 0.0
    n_disp = max(1, int(-(-n_erogazioni // per_dispenser))) if per_dispenser > 0 else 1

    costo_disp = 200000 * (1.3 if p_disp == 700 else 1.0)
    costo_chiller = 120000 if p_disp == 700 else 60000
    capex = (stoccaggio_kg * costo_storage_kg
             + potenza_kW * 2500
             + n_disp * (costo_disp + costo_chiller))

    return {"p_disp": p_disp, "kg_giorno": kg_giorno, "stoccaggio_kg": stoccaggio_kg,
            "potenza_kW": potenza_kW, "consumo_kwh_kg": consumo_kwh_kg, "capex": capex,
            "velocita_g_s": velocita, "n_disp": n_disp, "kg_medio": kg_medio,
            "minuti_pieno": minuti_pieno, "per_dispenser": per_dispenser,
            "n_erogazioni": n_erogazioni}


def dimensiona(camion, auto, bus):
    """Dimensionamento completo per un dato numero di mezzi.
    Restituisce None se la domanda e' nulla."""
    kg_auto = auto * KG_AUTO * capacity_factor
    kg_bus = bus * KG_BUS * capacity_factor
    kg_camion = camion * KG_CAMION * capacity_factor
    kg_totale = kg_auto + kg_bus + kg_camion
    if kg_totale <= 0:
        return None

    p_inlet = PRESSIONI_INGRESSO[fonte_h2]
    # Per ogni linea servono i kg e il numero di rifornimenti: il primo
    # dimensiona compressione e stoccaggio, il secondo i punti di erogazione.
    if CFG["pressioni"] == [700]:
        domanda = {700: (kg_totale, camion + auto + bus)}
    else:
        # 350 bar: autobus e mezzi di piazzale. 700 bar: camion e auto.
        domanda = {350: (kg_bus, bus), 700: (kg_camion + kg_auto, camion + auto)}

    linee = [dimensiona_linea(kg, n_erog, p_inlet, p, routing_logic, finestra_ore, CFG["overcap"])
             for p, (kg, n_erog) in domanda.items() if kg > 0]

    capex_tot = sum(l["capex"] for l in linee) * 1.25          # +25% opere civili
    potenza_tot = sum(l["potenza_kW"] for l in linee)
    stoccaggio_tot = sum(l["stoccaggio_kg"] for l in linee)

    energia_giorno = sum(l["consumo_kwh_kg"] * l["kg_giorno"] for l in linee)
    consumo_medio = energia_giorno / kg_totale

    opex_fisso = capex_tot * 0.04
    opex_energia = energia_giorno * 365 * costo_energia
    opex_totale = opex_fisso + opex_energia

    crf = (wacc * (1 + wacc) ** anni_vita) / (((1 + wacc) ** anni_vita) - 1)
    costo_specifico_hrs = (capex_tot * crf + opex_totale) / (kg_totale * 365)
    break_even = st.session_state.costo_molecola_in + costo_specifico_hrs

    area_netta = (stoccaggio_tot * 0.15) + (potenza_tot * 0.5)

    if kg_totale >= 1000:
        taglia = "Large (≥ 1 t/giorno, conforme AFIR)"
    elif kg_totale >= 500:
        taglia = "Medium (0,5 - 1 t/giorno)"
    else:
        taglia = "Small (< 0,5 t/giorno)"

    return {"config": config_scelta, "linee": linee, "kg_totale": kg_totale,
            "stoccaggio_tot": stoccaggio_tot, "potenza_tot": potenza_tot,
            "consumo_medio": consumo_medio, "capex_tot": capex_tot,
            "opex_fisso": opex_fisso, "opex_energia": opex_energia, "opex_totale": opex_totale,
            "costo_specifico_hrs": costo_specifico_hrs, "break_even": break_even,
            "area_minima": area_netta * 9.5, "taglia": taglia, "fonte": fonte_h2,
            "costo_molecola": st.session_state.costo_molecola_in,
            "n_disp_tot": sum(l["n_disp"] for l in linee),
            "n_camion": camion, "n_auto": auto, "n_bus": bus}


def calcola():
    R = dimensiona(n_camion, n_auto, n_bus)
    if R is None:
        return None
    R.update(scen_on=scen_on, orizzonte=orizzonte, tgm=tgm_camion,
             quota_fcev=quota_fcev, quota_cattura=quota_cattura)

    # Traiettoria: stessa stazione, stessi parametri, quota FCEV che cresce.
    # Dice quando la capacita' andra' ampliata, che e' cio' che serve al
    # cronoprogramma dell'action plan.
    if scen_on and tgm_camion > 0:
        traj = []
        for anno, quota in SCENARI.items():
            n = int(round(tgm_camion * quota / 100.0 * quota_cattura / 100.0))
            r = dimensiona(n, n_auto, n_bus)
            traj.append({"anno": anno, "quota": quota, "camion": n,
                         "kg": r["kg_totale"] if r else 0.0,
                         "taglia": r["taglia"] if r else "-",
                         "capex": r["capex_tot"] if r else 0.0,
                         "disp": r["n_disp_tot"] if r else 0,
                         "be": r["break_even"] if r else 0.0})
        R["traiettoria"] = traj
    return R


if st.button(_t["btn_calc"], type="primary", use_container_width=True):
    R = calcola()
    if R is None:
        st.error(_t["no_veicoli"])
        st.session_state.pop("hrs", None)
    else:
        st.session_state["hrs"] = R

# ==========================================
# 6. REPORT
# ==========================================
if "hrs" in st.session_state:
    R = st.session_state["hrs"]

    st.success(_t["r_config"].format(c=vis("config", R["config"])))

    if R.get("scen_on"):
        st.header(_t["r_scen"].format(o=R["orizzonte"]))
        s1, s2, s3, s4 = st.columns(4)
        s1.metric(_t["r_tgm"], f"{R['tgm']:,.0f} " + _t["r_giorno"])
        s2.metric(_t["r_fcev"], f"{R['quota_fcev']:.1f}%")
        s3.metric(_t["r_cattura"], f"{R['quota_cattura']}%")
        s4.metric(_t["r_serviti"], f"{R['n_camion']} " + _t["r_giorno"])

        if R.get("traiettoria"):
            st.subheader(_t["scen_traj"])
            st.caption(_t["scen_traj_note"])
            st.table(pd.DataFrame([{
                _t["tr_orizzonte"]: r["anno"],
                _t["tr_fcev"]: f"{r['quota']:.0f}%",
                _t["tr_camion"]: r["camion"],
                _t["tr_domanda"]: f"{r['kg']:,.0f}",
                _t["tr_taglia"]: vis("taglie", r["taglia"]),
                _t["tr_colonnine"]: r["disp"],
                _t["tr_capex"]: f"{r['capex']:,.0f}",
                _t["tr_prezzo"]: f"{r['be']:.2f}",
            } for r in R["traiettoria"]]))
        st.caption(_t["scen_src"])
        st.divider()

    st.header(_t["i_title"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(_t["i_domanda"], f"{R['kg_totale']:,.1f} kg" + _t["r_giorno"],
              vis("taglie", R["taglia"]))
    c2.metric(_t["i_stoccaggio"], f"{R['stoccaggio_tot']:,.0f} kg")
    c3.metric(_t["i_potenza"], f"{R['potenza_tot']:,.1f} kW")
    c4.metric(_t["i_punti"], f"{R['n_disp_tot']}",
              _t["i_compressione"].format(v=f"{R['consumo_medio']:,.2f}"))

    st.subheader(_t["i_linee"])
    for l in R["linee"]:
        st.markdown(_t["i_linea"].format(
            p=l["p_disp"], kg=f"{l['kg_giorno']:,.1f}", n=l["n_disp"],
            s=f"{l['stoccaggio_kg']:,.0f}", kw=f"{l['potenza_kW']:,.1f}",
            cx=f"{l['capex']:,.0f}"))

    for l in R["linee"]:
        st.info(_t["i_sae"].format(
            p=l["p_disp"], v=l["velocita_g_s"], kg=f"{l['kg_medio']:,.1f}",
            m=f"{l['minuti_pieno']:.1f}", d=f"{l['per_dispenser']:.0f}",
            e=f"{l['n_erogazioni']:,.0f}", n=l["n_disp"]))

    st.header(_t["f_title"])
    co1, co2, co3 = st.columns(3)
    co1.metric(_t["f_capex"], f"€ {R['capex_tot']:,.0f}")
    co2.metric(_t["f_opex_f"], f"€ {R['opex_fisso']:,.0f} " + _t["f_anno"])
    co3.metric(_t["f_opex_e"], f"€ {R['opex_energia']:,.0f} " + _t["f_anno"])

    st.header(_t["be_title"])
    st.success(_t["be_txt"].format(v=f"{R['break_even']:.2f}"))

    b1, b2, b3 = st.columns(3)
    b1.metric(_t["be_molecola"], f"€ {R['costo_molecola']:.2f} / kg")
    b2.metric(_t["be_sovra"], f"+ € {R['costo_specifico_hrs']:.2f} / kg")
    b3.metric(_t["be_minimo"], f"€ {R['break_even']:.2f} / kg")

    st.caption(_t["be_nota"])

    st.header(_t["sp_title"])
    st.warning(_t["sp_txt"].format(a=f"{R['area_minima']:,.0f}"))

    # ==========================================
    # 7. ESPORTAZIONE
    # ==========================================
    st.divider()
    st.subheader(_t["e_title"])

    GOOGLE_URL = "https://script.google.com/macros/s/AKfycbwpP0x0hBnhOadXA43IieWg9EusAuhaafpyeXpyaStssDd7Qo-jwnuOttAllzz8r5JS/exec"

    id_comune = H.testo(comune, H.COL_ID)
    st.caption(_t["e_assoc"].format(c=H.testo(comune, H.COL_NOME), id=id_comune))

    if st.button(_t["e_btn"]):
        if True:
            payload = {
                "ID_ISTAT": id_comune,
                "T28_CONFIGURAZIONE": R["config"],
                "T28_CAPACITA_KG_GIORNO": round(R["kg_totale"], 1),
                "T28_TAGLIA_HRS": R["taglia"],
                "T28_STRATEGIA_SUPPLY": R["fonte"],
                "T28_POTENZA_COMPRESSORE_KW": round(R["potenza_tot"], 1),
                "T28_N_DISPENSER": R["n_disp_tot"],
                "T28_AREA_MINIMA_MQ": round(R["area_minima"], 0),
                "T28_CAPEX_COMPLESSIVO_EURO": round(R["capex_tot"], 0),
                "T28_BREAK_EVEN_EURO_KG": round(R["break_even"], 2),
            }
            # l'orizzonte serve al cronoprogramma dell'action plan: si esporta
            # sempre, anche quando i mezzi sono stati inseriti a mano
            payload["T28_ORIZZONTE"] = R["orizzonte"] if R.get("scen_on") else "attuale"
            payload["T28_QUOTA_FCEV_PERC"] = round(R["quota_fcev"], 1) if R.get("scen_on") else 0.0

            salvato = False
            try:
                resp = requests.post(GOOGLE_URL, data=json.dumps(payload),
                                     headers={"Content-Type": "application/json"},
                                     allow_redirects=True, timeout=60)
                if resp.status_code in (200, 201):
                    st.success(_t["e_ok"])
                    st.caption(_t["e_resp"].format(r=resp.text))
                    st.balloons()
                    salvato = True
                else:
                    st.error(_t["e_err"].format(c=resp.status_code))
            except requests.exceptions.ReadTimeout:
                st.warning(_t["e_timeout"])
                salvato = True
            except Exception as e:
                st.error(_t["e_conn"].format(e=e))

            if salvato:
                H.dopo_salvataggio(comune, lingua=LANG)


# Tendina "Prosegui cosi" + rientro al menu H2READY, in fondo alla pagina.
# Dopo un salvataggio riuscito e' gia' stata mostrata da dopo_salvataggio()
# e questa chiamata non fa nulla.
H.prosegui(comune, lingua=LANG)
