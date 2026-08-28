"""
H2READY - 1.3 Il tuo percorso
Pagina di smistamento dopo il questionario 1.2.

E' l'unico indirizzo da distribuire insieme al 1.1: mostra quali percorsi si sono
aperti, quali strumenti compilare e a che punto e' il lavoro.
"""

import streamlit as st

import h2ready as H

st.set_page_config(page_title="H2READY TOOLKIT: Tool 1.3 - Il tuo percorso", page_icon="🧭",
                   layout="centered")

st.markdown(
    '<div style="background:linear-gradient(90deg,#003399,#0057c2);padding:20px;'
    'border-radius:12px;text-align:center">'
    '<h2 style="color:white;margin:0;letter-spacing:1px">H2READY TOOLKIT</h2>'
    '<p style="color:#cddafc;margin:4px 0 0">Tool 1.3: Il percorso del tuo Comune</p></div>',
    unsafe_allow_html=True)
st.write("")

comune = H.blocco_accesso("Tool 1.3 - Il tuo percorso")
if comune is None:
    st.stop()

liv = H.livello(comune)
H.intestazione_comune(comune)

st.subheader("A che punto sei")
H.mostra_avanzamento(comune)

st.subheader("I tuoi percorsi")
st.info(H.REGOLE_LIVELLO[liv]["descrizione"])

stato = H.percorsi_disponibili(comune)
for lettera, s in stato.items():
    nome = H.NOMI_PERCORSO[lettera]
    if s["aperto"]:
        st.success(f"**Percorso {lettera} — {nome}**  ·  punteggio {s['punteggio']:g}")
    else:
        st.markdown(
            f"<div style='padding:10px 14px;margin-bottom:8px;border-radius:8px;"
            f"background:#F2F3F5;color:#8A94A0;border:1px solid #E3E6EA'>"
            f"<b>Percorso {lettera} — {nome}</b><br>"
            f"<span style='font-size:.85rem'>{s['motivo']}</span></div>",
            unsafe_allow_html=True)

if not any(s["aperto"] for s in stato.values()):
    st.warning("Nessun percorso risulta attivo. Verifica di aver completato il "
               "questionario 1.2: se i punteggi ci sono e restano sotto soglia, "
               "l'idrogeno non è la priorità per questo territorio, e conviene "
               "concentrarsi su elettrificazione ed efficienza energetica.")

st.subheader("Strumenti da compilare")
H.mostra_prossimi_tool(comune, lingua="it")

note = []
if H.accesso_strumento(comune, "avanzato") == "richiesta":
    note.append("gli strumenti di dimensionamento (2.6 e 2.8)")
if H.accesso_strumento(comune, "fast") == "richiesta":
    note.append("gli strumenti H2 FAST")
if note:
    st.caption("Per " + " e ".join(note) + f" l'accesso avviene su richiesta al gruppo "
               f"di progetto: scrivi a {H.CONTATTO_PROGETTO} indicando il codice del "
               "Comune.")
