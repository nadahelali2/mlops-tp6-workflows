
# Orchestrateur ou integration continue ? (TP06)

| Critere | Prefect (orchestrateur) | GitHub Actions (CI) |
|---|---|---|
| Ce qui declenche l'execution | Une planification chaque lundi a 6 h ou un Quick run | Un push sur GitHub |
| Ou s'execute le traitement | Sur notre ordinateur avec le worker Prefect | Sur une machine Linux de GitHub |
| Qui surveille, et ou | Prefect, dans son interface web | GitHub Actions, dans l'onglet Actions |
| Ce qui se passe en cas d'echec | La tache et le workflow passent a Failed | Le job passe au rouge |
| Type de tache adapte | Reentrainement et suivi des pipelines ML | Tests et validation automatique du code |
| Ce qui est versionne dans Git | Le code Python du workflow et sa configuration | Le fichier ci.yml et les scripts de validation |

## Conclusion (5 lignes)

Prefect permet d'organiser et de surveiller les differentes taches du pipeline MLOps.

Il permet aussi de planifier automatiquement le reentrainement du modele.

GitHub Actions execute les verifications apres chaque modification envoyee sur GitHub.

Notre test a montre que la CI detecte un modele dont le score F1 est insuffisant.

Les deux outils sont complementaires et permettent de rendre le pipeline plus fiable.
