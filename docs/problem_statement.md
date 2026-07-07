# Epic 1: Define Problem and Understanding

## 🌾 Specify the Business Problem

### 1. Objective & Core Challenges
The primary objective of this phase is to clearly identify and analyze the structural challenges facing modern agriculture. Key problem areas include:
*   **Suboptimal Crop Selection:** Farmers frequently lack scientific data to match crop types with specific land traits, leading to financial losses and lower seasonal yields.
*   **Inefficient Resource Utilization:** Misjudging soil chemistry results in over-fertilization or poor nutrient management, damaging long-term soil health.
*   **Volatile Environmental Patterns:** Unpredictable fluctuations in local climate metrics complicate historical, intuition-based farming strategies.

### 2. Core Parameters Evaluated
The engine actively tracks and models seven core soil and environmental dimensions:
*   **Macronutrients:** Nitrogen (N), Phosphorus (P), and Potassium (K) values.
*   **Climate Metrics:** Real-time atmospheric temperature, humidity levels, and seasonal rainfall totals.
*   **Soil Condition:** Active pH value indicating chemical acidity or alkalinity.

### 3. Intended Outcomes
By applying predictive machine learning pipelines to these parameters, **OptiCrop** provides data-driven agricultural recommendations. This system yields actionable intelligence to empower four primary groups:
1.  **Farmers:** Minimizing risk and optimizing per-acre yield output.
2.  **Agricultural Researchers:** Mapping complex crop-to-soil performance variables.
3.  **Agribusinesses:** Streamlining seed, fertilizer, and supply chain logistics.
4.  **Policymakers:** Planning sustainable regional resource allocation strategies.

## 📋 Business Requirements

### 1. Functional Scope & Parameter Processing
*   **Predictive Analysis:** The engine must ingest and process 7 distinct parameters: Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, rainfall, and pH level alongside seasonal traits to output accurate crop suitability scores.
*   **User Interface:** Provide a simple, responsive web interface allowing end-users to input metrics dynamically and view real-time results instantly.
*   **Pipeline Integration:** Ensure direct, low-latency communication between the front-end web handler and the back-end predictive inference engine.

### 2. Analytical & Technical Frameworks
*   **Algorithmic Benchmarking:** Systematically train and compare multiple ML models: K-Nearest Neighbors (KNN), Logistic Regression, Decision Tree, Random Forest, and K-Means Clustering.
*   **Feature Lifecycle Management:** Implement reproducible data preprocessing pipelines featuring robust scaling, data transformation, validation logging, and prediction visualization components.

### 3. Structural Capabilities
*   **Resource Optimization:** Minimize fertilizer, water, and soil nutrient over-allocation through preventative algorithmic analysis.
*   **Scalability & Longevity:** Maintain modular software layers to easily hook into cloud microservices, expanded state-level datasets, or smart-iot integrations later.
EOT

# 3. Create the Literature Survey documentation
cat << 'EOT' > docs/literature_survey.md
# Epic 1: Define Problem and Understanding

## 📚 Literature Survey

### 1. Architectural Paradigms Studied
This survey examines precision agriculture models, reviewing baseline data tracking and comparative research papers focusing on automated machine learning classifiers.

### 2. Algorithmic Trade-offs Evaluated
*   **Linear & Instance Models (Logistic Regression, KNN):** Offer low-compute baselines but struggle with non-linear environmental thresholds.
*   **Tree Ensembles (Decision Trees, Random Forest):** Typically reveal top-tier accuracy bounds on multivariate tabular crop datasets due to robust feature splitting.
*   **Unsupervised Architectures (K-Means):** Excellent for grouping regional environmental profiles before classifying explicit targets.

### 3. Pipeline Synthesis
Prior literature highlights that scaling normalization (e.g., MinMax or Standard Scaling) and addressing data balance factors directly dictate model robustness against regional outliers.
EOT

# 4. Create the Social & Business Impact documentation
cat << 'EOT' > docs/social_business_impact.md
# Epic 1: Define Problem and Understanding

## 🌍 Social and Business Impact

### 1. Social & Environmental Advantages
*   **Yield Stabilization:** Mitigates immediate risks of total seasonal crop failures by steering smallholder farmers away from hostile soil placements.
*   **Precision Sustainability:** Promotes targeted resource optimization, reducing fertilizer runoff and safeguarding groundwater chemistry.

### 2. Enterprise & Governance Advantages
*   **Agribusiness Insights:** Empowers regional supply chains to align supply footprints (seed, tools, fertilizer inventory) directly with localized predictive trends.
*   **Policy Support:** Aids research planning modules to counter climate variance, bolstering macro food security goals over long horizons.

