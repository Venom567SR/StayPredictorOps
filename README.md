# StayPredictorOps 🏨🔮

StayPredictorOps is an **end-to-end MLOps project** focused on hotel reservation prediction. This project demonstrates the integration of machine learning workflows with modern MLOps tools and cloud deployment, providing a robust, automated, and reproducible pipeline for developing, tracking, and deploying predictive models.

---

## Table of Contents 📚

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation & Setup](#installation--setup)
- [ML Pipeline](#ml-pipeline)
- [Deployment](#deployment)
- [References](#references)
- [License](#license)

---

## Project Overview 🖥️

The goal of StayPredictorOps is to predict whether a hotel reservation will be honored or canceled, using historical booking data. The project illustrates:

- A full MLOps pipeline: from data ingestion and preprocessing to model deployment.
- Integration of MLflow for tracking experiments and model registry.
- Automated CI/CD using Jenkins.
- Containerization and deployment on Google Cloud Platform (GCP) using Docker and Google Cloud Run (GCR).
- Development of a Flask REST API for serving predictions.

---

## Features ✨

- **End-to-end MLOps:** Data preprocessing, model training, evaluation, experiment tracking, and cloud deployment.
- **Experiment Tracking:** All model runs, parameters, and artifacts are tracked and versioned using MLflow.
- **CI/CD Automation:** Jenkins pipelines automate testing, training, and deployment.
- **Cloud Native:** Models and APIs deployed on GCP using Docker containers and Google Cloud Run.
- **Interactive Notebooks:** Jupyter Notebooks for EDA and model prototyping.
- **Visualization:** Comprehensive analysis with matplotlib and seaborn.

---

## Tech Stack 🛠️

**Programming & Data Science:**
- Python 🐍
- Jupyter Notebook 📓
- pandas 🐼
- numpy ➗
- scikit-learn 🧠
- xgboost ⚡
- lightgbm 💡
- imbalanced-learn ⚖️
- statsmodels 📈

**Visualization:**
- matplotlib 📊
- seaborn 🌊

**MLOps & Workflow:**
- MLflow 🚀
- Jenkins 🏗️
- pyyaml 📄

**Cloud & Deployment:**
- Google Cloud Storage (GCS) ☁️
- Google Cloud Run (GCR) 🏃‍♂️
- Docker 🐳

**API Service:**
- Flask 🍶

---

## Architecture 🏗️

```
Data Source 📂
   ↓
Preprocessing & EDA (pandas, numpy, matplotlib, seaborn)
   ↓
Feature Engineering 🧩
   ↓
Model Training & Evaluation (scikit-learn, xgboost, lightgbm, imbalanced-learn, statsmodels)
   ↓
Experiment Tracking (MLflow) 📒
   ↓
CI/CD Pipeline (Jenkins) 🔁
   ↓
Containerization (Docker) 📦
   ↓
Model & API Deployment (GCR, Cloud Run, Flask) ☁️
```

---

## Installation & Setup ⚙️

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Venom567SR/StayPredictorOps.git
   cd StayPredictorOps
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Cloud Credentials**
   - Create a GCP project and service account with Storage and Cloud Run permissions.
   - Download the service account key JSON.
   - Export the credentials:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
     ```

5. **MLflow Tracking Setup**
   - Start MLflow server locally:
     ```bash
     mlflow ui
     ```
   - Or configure for remote tracking as needed.

6. **Jenkins Pipeline Setup**
   - Use the provided Jenkinsfile for configuring your Jenkins CI/CD pipeline.

---

## ML Pipeline 🧬

- **Data Ingestion & Preprocessing:** Clean and transform the raw hotel booking data using pandas and numpy.
- **EDA:** Analyze distributions and relationships using matplotlib and seaborn.
- **Feature Engineering:** Generate relevant features for model input.
- **Model Training:** Train classification models using scikit-learn, xgboost, lightgbm, and handle class imbalance with imbalanced-learn.
- **Evaluation:** Evaluate models with various metrics (accuracy, precision, recall, ROC, etc.) and visualize the results.
- **Experiment Tracking:** Log all runs, parameters, metrics, and artifacts using MLflow.
- **Model Packaging:** Containerize the trained model and API using Docker for reproducible deployment.

---

## Deployment 🚀

- **API Service:** Serve predictions via a Flask REST API.
- **Containerization:** The Flask app and model are packaged in a Docker container.
- **Cloud Deployment:** Deploy the Docker container to Google Cloud Run using Google Container Registry (GCR).
- **Jenkins Automation:** Jenkins automates building, testing, and deployment.


---


## References 🔗

- [MLflow Documentation](https://mlflow.org/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Google Cloud Platform](https://cloud.google.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [xgboost Documentation](https://xgboost.readthedocs.io/)
- [lightgbm Documentation](https://lightgbm.readthedocs.io/)
- [imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Google Cloud Run](https://cloud.google.com/run)
- [Google Cloud Storage](https://cloud.google.com/storage)

---

## License 📄

This project is licensed under the MIT License.