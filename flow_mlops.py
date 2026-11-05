
import json
import subprocess
from prefect import flow, task

@task
def rejouer_pipeline():
    subprocess.run(["dvc", "repro"], check=True)

@task
def lire_metriques():
    with open("reports/metrics.json", encoding="utf-8") as f:
        return json.load(f)

@task
def valider(metriques):
    seuil = 0.82
    f1 = metriques["f1"]
    if f1 < seuil:
        raise ValueError(f"F1 insuffisant : {f1} < {seuil}")
    print(f"Validation OK : F1 = {f1}")

@task
def notifier(metriques):
    print(f"Pipeline terminé avec succès ! F1 = {metriques['f1']}")

@flow(name="reentrainement-fraude", log_prints=True)
def reentrainement():
    rejouer_pipeline()
    metriques = lire_metriques()
    valider(metriques)
    notifier(metriques)

if __name__ == "__main__":
    reentrainement()
