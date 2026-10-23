# Қорытынды қорғау балын болжау (тәжірибелік жұмыс 1.8, нұсқа 3)

Зерттеу сұрағы: жобаның бастапқы кезеңіндегі көрсеткіштер бойынша қорытынды қорғау балын болжауға бола ма?

**Назар аударыңыз:** деректер жасанды (synthetic). Генерация ережесі `research_notebook.ipynb` ішінде жазылған. Нәтиже нақты магистранттарға қатысты қорытынды емес.

## Файлдар

| Файл | Мазмұны |
| --- | --- |
| `research_notebook.ipynb` | Толық зерттеу notebook-і |
| `research_model.joblib` | Pipeline + белгілер реті + ауқымдар + нұсқалар |
| `app.py` | Streamlit қосымшасы |
| `requirements.txt` | Кітапхана нұсқалары |
| `metrics.csv`, `predictions.csv` | Метрикалар мен test болжамдары |
| `data_dictionary.csv`, `project_scores_synthetic.csv` | Деректер сөздігі және жасанды деректер |

## Іске қосу

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud-та жариялау

1. Осы файлдарды GitHub репозиторийінің негізгі деңгейіне жүктеңіз (`app.py`, `research_model.joblib`, `requirements.txt` міндетті).
2. Streamlit Community Cloud-та **Create app** → GitHub-тан таңдаңыз. Repository, `main`, `app.py` көрсетіңіз.
3. **Advanced settings** ішінде Python нұсқасын notebook орындалған ортаға сәйкес таңдаңыз (`requirements.txt` нұсқалары Python 3.11+ талап етеді).
4. **Deploy** басыңыз. Үш мысалды тексеріп, сілтемені сақтаңыз.

Нақты білім алушылар деректерін Public репозиторийге жүктемеңіз.
