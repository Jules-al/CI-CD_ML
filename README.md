# 🚀 CI/CD for Machine Learning: Drug Classification Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF.svg)](https://github.com/features/actions)
[![CML](https://img.shields.io/badge/CML-Evaluation-success.svg)](https://cml.dev/)



## 📌 Description du Projet

Ce dépôt présente une architecture **MLOps complète et automatisée** de bout en bout (End-to-End). L'objectif est de démontrer comment industrialiser un modèle de Machine Learning (ici, un classificateur de médicaments) en utilisant les meilleures pratiques d'Intégration Continue (CI) et de Déploiement Continu (CD).

Plutôt que de limiter le modèle à un environnement de développement local (Jupyter Notebook), ce projet met en place un workflow où chaque modification de code ou de donnée déclenche automatiquement l'entraînement, l'évaluation et le déploiement du modèle.

## 🏗️ Architecture MLOps

Le pipeline est divisé en 4 phases automatisées via **GitHub Actions** :

1. **Préparation & Entraînement (`train.py`) :** 
   - Construction d'un pipeline de prétraitement avec `scikit-learn` (imputation, scaling, encodage).
   - Entraînement d'un modèle *Random Forest*.
   - Sérialisation sécurisée du modèle avec `skops`.

2. **Intégration Continue (CI) :**
   - Validation du formatage du code (`black`).
   - Génération automatisée des métriques de performance (Accuracy, F1-Score) et de la matrice de confusion.
   - Reporting automatique sur GitHub via **Continuous Machine Learning (CML)**.

3. **Versioning des Modèles :**
   - Sauvegarde automatique du modèle entraîné et des métriques sur une branche dédiée (`update`) pour garantir la reproductibilité.

4. **Déploiement Continu (CD) :**
   - Création d'une interface web interactive avec **Gradio**.
   - Synchronisation et déploiement via l'API Hugging Face. *(Note : L'hébergement Gradio sur Hugging Face nécessitant un compte PRO, l'architecture est conçue pour être facilement basculée vers Streamlit Cloud ou Google Cloud Run).*

## ⚙️ Technologies Utilisées

* **Langage :** Python
* **Machine Learning :** scikit-learn, pandas, numpy
* **Sérialisation :** skops
* **Orchestration & CI/CD :** GitHub Actions, Makefile, DVC / CML (Iterative)
* **Déploiement / UI :** Gradio, Hugging Face CLI

## 🚀 Comment reproduire ce projet en local ?

### 1. Cloner le dépôt
```bash
git clone [https://github.com/VOTRE_NOM_UTILISATEUR/CI-CD_ML.git](https://github.com/VOTRE_NOM_UTILISATEUR/CI-CD_ML.git)
cd CI-CD_ML
