# 🚀 Automated Data Pipeline with Apache Airflow

![Airflow Logo](https://airflow.apache.org/images/feature-image.png)

A simple yet powerful automated data pipeline using Apache Airflow to process CSV data daily.

## 📋 Table of Contents
- [Features](#✨-features)
- [Prerequisites](#📋-prerequisites)
- [Setup](#⚙️-setup)
- [Project Structure](#📂-project-structure)
- [How It Works](#🤖-how-it-works)
- [Accessing Airflow UI](#🌐-accessing-airflow-ui)
- [Customizing](#🎨-customizing)
- [Troubleshooting](#🐛-troubleshooting)
- [License](#📜-license)

## ✨ Features

- **🔄 Automated Processing**: Runs daily to process your data
- **📊 CSV Handling**: Processes input CSV files
- **⏱️ Timestamping**: Adds processing timestamps to your data
- **📅 Date Calculations**: Computes days since joining
- **🐳 Dockerized**: Easy setup with Docker Compose
- **📈 Scalable**: Ready to add more processing steps

## 📋 Prerequisites

Before you begin, ensure you have installed:

- [Docker](https://www.docker.com/) (v20.10.0+)
- [Docker Compose](https://docs.docker.com/compose/) (v1.29.0+)

## ⚙️ Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/airflow-data-pipeline.git
   cd airflow-data-pipeline