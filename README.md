# EDA Heart Diseases Project 🫀💻

<p align="center">
  <img src="data/Cure-for-cardiovascular-diseases-1200x675.jpg" width="500"/>
</p>


This project analyzes the [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) to explore cardiovascular risk patterns based on clinical features. Cardiovascular diseases (CVDs) are the leading cause of death globally, responsible for 17.9 million deaths annually. Early detection through data-driven methods is crucial to manage risk and save lives.

Using 11 clinical attributes (such as age, blood pressure, cholesterol, chest pain type, ECG results, and more), this project identifies trends, visualizes relationships, and prepares the ground for further classification and predictive modeling.

The analysis is structured into modular sections, each focused on a specific medical factor. All code is implemented using Python libraries such as **pandas**, **NumPy**, and **matplotlib**, with clean tabular summaries and expressive visualizations to convey insights.

> 🚧 **Note:** Some sections and visualizations are still in progress and will be completed soon.


## Section One – Cardiovascular Patient Classification by Sex

This section analyzes the **distribution of cardiovascular patients** based on **sex** (Male and Female). It involves calculating the number and percentage of male and female patients, along with comparing them to the total population.

### 🔍 Analysis Performed
- Filtered cardiovascular patients (`HeartDisease == 1`)
- Counted male (`M`) and female (`F`) patients
- Calculated:
  - Number and percentage of patients by sex
  - Total percentage of cardiovascular patients in the dataset

### 📊 Visualizations
1. **Bar Chart 1** – Number of male vs. female cardiovascular patients
2. **Bar Chart 2** – Cardiovascular patients vs. total population
3. **Pie Chart 1** – Gender distribution of cardiovascular patients (percentage)
4. **Pie Chart 2** – Cardiovascular patients as a percentage of entire dataset

### 💾 Output
- A DataFrame named `df_of_patients_num` storing all calculated values
- Visuals saved or displayed using `matplotlib`


## Section Two – Age Distribution of Cardiovascular Patients

This section focuses on analyzing the **age range and distribution** of patients diagnosed with cardiovascular disease.

### 🔍 Analysis Performed
- Filtered the dataset to only include patients with `HeartDisease == 1`
- Extracted and calculated:
  - Minimum age
  - Maximum age
  - Mean (average) age

### 📊 Visualizations
1. **Histogram** showing the distribution of patients’ ages:
    - X-axis: Age range
    - Y-axis: Number of patients
    - Vertical dashed line marking the **mean age**
    - Annotations for bin counts
    - Highlighted text showing total patient count

### 💾 Output
- A DataFrame named `age_df` containing:
  - Minimum age of patients
  - Maximum age of patients
  - Mean age of patients
- You can export this table to a CSV using:
  ```python
  age_df().to_csv("../outputs/section2_age_analysis.csv", index=False)


## Section Three – Distribution of Chest Pain Types in Patients and Non-Patients

This section analyzes the types of chest pain experienced by individuals in the dataset and compares their distribution between cardiovascular patients and non-patients.

### 🔍 Analysis Performed
- Filtered dataset by `HeartDisease` to identify:
  - Count of each chest pain type among patients
  - Count of each chest pain type among non-patients
- Chest pain types considered:
  - ASY (Asymptomatic)
  - NAP (Non-Anginal Pain)
  - ATA (Atypical Angina)
  - TA (Typical Angina)

### 📊 Visualizations
1. **Stacked Bar Chart**:
   - Shows counts of each chest pain type for both patients and non-patients
   - Individual counts are labeled along with total bar counts
2. **Donut Charts**:
   - One for cardiovascular patients
   - One for non-patients
   - Each showing percentage share of chest pain types

### 💾 Output
- A DataFrame called `chest_p_t_df` showing:
  - Count of each chest pain type for patients and non-patients side-by-side
- You can export this table using:
  ```python
  chest_p_t_df(patients, non_patients).to_csv("../outputs/section3_chestpain_analysis.csv", index=False)


## Section Four – Lab Measurement-Based Classification

This section analyzes key **clinical laboratory measurements** related to cardiovascular health and classifies their distributions among patients and non-patients.

### 🔍 Factors Analyzed
- **Resting Blood Pressure (RestingBP)**
  - Mean, min, max
  - Count of values above and below 120 mmHg
- **Cholesterol**
  - Mean, min, max
  - High (>240), Borderline (200–239), Desirable (<200)
- **Fasting Blood Sugar (FastingBS)**
  - Counts of individuals above (1) or below (0) the standard threshold

### 💾 Outputs
Each factor is stored in its own DataFrame:
- `resting_bp_data_df`
- `cholesterol_data_df`
- `fasting_bs_data_df`

> ✅ These tables can easily be saved as CSVs for reporting purposes.

### 📊 Visualizations
This section is under development. Visualizations for these measurements will be included in the upcoming update.

---

