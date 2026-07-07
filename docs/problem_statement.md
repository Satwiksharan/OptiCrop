# Epic 1: Problem Definition and Understanding

# 🌾 Business Problem

## 1. Project Objective

Modern agriculture faces several challenges that reduce crop productivity and resource efficiency. Farmers often rely on traditional practices and experience rather than scientific analysis, making crop selection difficult under changing environmental conditions.

**OptiCrop** aims to solve this problem by using Machine Learning to recommend the most suitable crop based on soil properties and climatic conditions.

---

## 2. Key Challenges

### 🌱 Incorrect Crop Selection
Farmers may choose crops that are not suitable for their soil or climate, resulting in poor yields and financial losses.

### 💧 Inefficient Resource Utilization
Improper understanding of soil nutrients often leads to excessive fertilizer use, nutrient imbalance, increased production costs, and long-term soil degradation.

### 🌦 Climate Variability
Changing weather conditions such as temperature, humidity, and rainfall make traditional farming decisions less reliable.

---

## 3. Parameters Used

The prediction model analyzes seven important agricultural parameters:

| Parameter | Description |
|-----------|-------------|
| Nitrogen (N) | Soil nitrogen content |
| Phosphorus (P) | Soil phosphorus level |
| Potassium (K) | Soil potassium level |
| Temperature | Atmospheric temperature (°C) |
| Humidity | Relative humidity (%) |
| Rainfall | Seasonal rainfall (mm) |
| pH | Soil acidity or alkalinity |

---

## 4. Expected Outcomes

Using these parameters, OptiCrop provides accurate crop recommendations that help improve agricultural productivity and sustainability.

### Farmers
- Select crops with higher chances of successful cultivation.
- Reduce crop failure risks.
- Improve overall yield and profitability.

### Agricultural Researchers
- Analyze relationships between soil characteristics and crop performance.
- Support research in precision agriculture.

### Agribusiness Organizations
- Improve planning for seeds, fertilizers, and agricultural supplies.
- Optimize inventory and supply chain management.

### Policymakers
- Support data-driven agricultural planning.
- Promote sustainable farming and efficient resource allocation.

---

# 📋 Business Requirements

## Functional Requirements

- Accept soil nutrient values (N, P, K), temperature, humidity, rainfall, and pH as user inputs.
- Predict the most suitable crop using trained Machine Learning models.
- Provide a responsive web interface for entering input values.
- Display prediction results instantly with minimal response time.
- Enable seamless communication between the frontend and backend prediction engine.

---

## Machine Learning Requirements

The system should train and evaluate multiple Machine Learning algorithms, including:

- K-Nearest Neighbors (KNN)
- Logistic Regression
- K-Means Clustering (for exploratory analysis)

The pipeline should include:

- Data preprocessing
- Feature scaling
- Model training
- Performance evaluation
- Prediction visualization

---

## Non-Functional Requirements

- Modular architecture for easy maintenance.
- Scalable design for future cloud deployment.
- Support integration with IoT-based smart farming systems.
- Optimize fertilizer and water usage through intelligent recommendations.
