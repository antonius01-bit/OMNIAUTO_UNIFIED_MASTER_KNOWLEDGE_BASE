---
name: automl-pipeline-optimizer
description: >-
  End-to-end Automated Machine Learning (AutoML) engineering engine fusing TPOT, AutoKeras, H2O-3, MLJAR, and Bayesian Optimization. Automates feature engineering, model selection, hyperparameter tuning, neural architecture search, and ensemble stacking.
---

# ⚙️ AutoML Pipeline Optimizer (TPOT + AutoKeras + H2O-3 + MLJAR Fusion)

Use this skill when automating end-to-end machine learning workflows on tabular, image, or text datasets: automated preprocessing, model benchmarking, neural architecture search, hyperparameter tuning, and stacked ensemble creation.

## AutoML Multi-Stage Pipeline

```mermaid
flowchart TD
    subgraph DataPrep ["1. Automated Feature Engineering"]
        D["Raw Data"] --> FE["Smart Encoding, Imputation & Scaling"]
        FE --> FT["Feature Generation & Dimensionality Reduction"]
    end

    subgraph Search ["2. Model Search & Neural Architecture Search"]
        FT --> G["Genetic Programming Optimization (TPOT)"]
        FT --> N["Neural Architecture Search (AutoKeras)"]
        FT --> B["Gradient Boosting Benchmarks (XGBoost, LightGBM, CatBoost)"]
    end

    subgraph Ensembling ["3. Multi-Layer Stacking & Blending"]
        G & N & B --> ST["Stacked Ensemble (H2O-3 SuperLearner)"]
        ST --> HP["Bayesian Hyperparameter Tuning (Optuna)"]
    end

    subgraph Explanation ["4. Explainability & Export"]
        HP --> SH["SHAP / Feature Importance Explanations"]
        SH --> PROD["Production-Ready Scikit-Learn / ONNX Pipeline Code"]
    end
```

## Core Modules
1. **Automated Feature Engineering**: Generates non-linear polynomial features, interaction terms, target encodings, and temporal aggregations.
2. **Genetic Pipeline Search (TPOT)**: Uses genetic programming to automatically assemble and optimize entire scikit-learn machine learning pipelines.
3. **Neural Architecture Search (AutoKeras)**: Efficient NAS for deep learning tasks with automatic layer sizing and learning rate schedules.
4. **Stacked Ensembles & Blending**: Combines predictions from diverse model families (Trees + Linear + Neural Nets) using a meta-learner to maximize accuracy and minimize variance.
5. **SHAP Interpretability**: Generates automated global feature importance and local instance-level SHAP force plots.

## How to Use
`Build and optimize AutoML pipeline for [dataset / target_variable] with automated feature engineering, ensemble stacking, and SHAP explanations.`
