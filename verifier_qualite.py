
import json
import sys
import yaml

with open("reports/metrics.json", encoding="utf-8") as f:
    metriques = json.load(f)

with open("params.yaml", encoding="utf-8") as f:
    params = yaml.safe_load(f)

f1 = metriques["f1"]
seuil = params["validation"]["seuil_f1"]

print(f"Score F1 : {f1}")
print(f"Seuil minimum : {seuil}")

if f1 < seuil:
    print("ECHEC : score F1 insuffisant")
    sys.exit(1)

print("SUCCES : qualite du modele validee")
