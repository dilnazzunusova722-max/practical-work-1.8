# -*- coding: utf-8 -*-
"""Қорытынды қорғау балын болжау: Streamlit қосымшасы (тәжірибелік жұмыс 1.8, нұсқа 3)."""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Қорғау балын болжау", page_icon="📊")


@st.cache_resource
def load_bundle():
    return joblib.load(Path(__file__).parent / "research_model.joblib")


bundle = load_bundle()
features = bundle["features"]
ranges = bundle["input_ranges"]
lo_out, hi_out = bundle["output_range"]

st.title("Қорытынды қорғау балын болжау")
st.write(
    "Жобаның бастапқы кезеңіндегі көрсеткіштер бойынша кейінгі қорытынды қорғаудың "
    "рубрика балын болжайтын оқу демонстрациясы."
)
st.warning(
    "Модель **жасанды (synthetic) деректермен** оқытылған. Нәтиже нақты магистранттарға "
    "қатысты қорытынды болып саналмайды. Болжам баға қоюға немесе автоматты шешім "
    "қабылдауға негіз емес, тек әдістемелік кеңес бағытын жоспарлауға көмектеседі."
)

labels = {
    "plan_score": "Зерттеу жоспарының рубрика балы (0–100)",
    "prototype_score": "Алғашқы прототип балы (0–100)",
    "ontime_share": "Мерзімінде орындалған кезеңдер үлесі (0–1)",
    "method_task_score": "Бастапқы әдістемелік тапсырма нәтижесі (0–100)",
}

values = {}
for name in features:
    lo, hi = ranges[name]
    if name == "ontime_share":
        values[name] = st.number_input(labels[name], value=0.7, step=0.05, format="%.2f")
    else:
        values[name] = st.number_input(labels[name], value=65.0, step=1.0, format="%.1f")

if st.button("Болжам жасау"):
    errors = [
        f"«{labels[n]}» мәні {ranges[n][0]}–{ranges[n][1]} ауқымында болуы керек."
        for n in features
        if not (ranges[n][0] <= values[n] <= ranges[n][1])
    ]
    if errors:
        for e in errors:
            st.error(e)
    else:
        row = pd.DataFrame([[values[n] for n in features]], columns=features)
        pred = float(bundle["pipeline"].predict(row)[0])
        pred = min(max(pred, lo_out), hi_out)  # 0–100 ауқымына шектеу
        st.success(f"Болжамды қорғау балы: **{pred:.1f}** / 100")
        st.caption(
            f"Модель: {bundle['model_name']}. Test MAE ≈ {bundle['metrics']['MAE_test']} балл "
            f"(базалық модельде {bundle['metrics']['MAE_baseline']}). Рубрика нұсқасы: {bundle['rubric_version']}."
        )

with st.expander("Модель туралы"):
    st.write(f"Кітапхана нұсқалары: {bundle['versions']}")
