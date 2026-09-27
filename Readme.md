# Customer Purchase Prediction using Machine Learning

## 📌 Project Overview

This project is a **Supervised Machine Learning classification task** that predicts whether a customer will purchase a product based on their **Age** and **Income**.

Two classification algorithms are implemented and compared:

- **Logistic Regression**
- **Decision Tree Classifier**

The project uses the same dataset and train-test split for both models and compares their prediction accuracy.

---

## 🎯 Problem Statement

A shopping company wants to predict whether a customer will purchase a product or not based on their **Age** and **Income**.

The model should:

1. Create the customer dataset.
2. Split the dataset into training and testing sets.
3. Train a Logistic Regression model.
4. Train a Decision Tree model.
5. Predict whether a new customer will purchase the product.
6. Compare both models using Accuracy.

---

## 📊 Dataset

The dataset contains three columns:

| Feature | Description |
|---|---|
| Age | Age of the customer |
| Income | Customer's income |
| Purchased | Purchase decision (0 = No, 1 = Yes) |

### Sample Dataset

| Age | Income | Purchased |
|---:|---:|---:|
| 20 | 15000 | 0 |
| 22 | 18000 | 0 |
| 25 | 22000 | 0 |
| 28 | 30000 | 1 |
| 30 | 35000 | 1 |
| 32 | 40000 | 1 |
| 35 | 45000 | 1 |
| 38 | 50000 | 1 |
| 40 | 55000 | 1 |
| 45 | 60000 | 1 |

### Target Values

- `0` → No Purchase
- `1` → Purchase

---

## 🤖 Machine Learning Algorithms

### 1. Logistic Regression

Logistic Regression is used as a classification algorithm to predict whether the customer will purchase the product.

**Input Features:**
- Age
- Income

**Output:**
- `0` → No Purchase
- `1` → Purchase

---

### 2. Decision Tree Classifier

The Decision Tree algorithm makes predictions by learning decision rules from the training data.

**Input Features:**
- Age
- Income

**Output:**
- `0` → No Purchase
- `1` → Purchase

---

## 🔄 Machine Learning Workflow

```text
Dataset Creation
       ↓
Data Preparation
       ↓
Feature & Target Selection
       ↓
Train-Test Split
       ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Logistic       Decision
Regression      Tree
 │               │
 ↓               ↓
Prediction      Prediction
 │               │
 └───────┬───────┘
         ↓
   Accuracy Comparison
