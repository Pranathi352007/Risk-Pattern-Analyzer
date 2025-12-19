# Explainable Risk Pattern Analyzer

## Overview
This project implements a GenAI-inspired, explainable risk analysis system using Python and Pandas.  
It analyzes transaction data to identify potentially risky activities based on amount, country, and message content, and generates **human-readable explanations** for each decision.
The goal is to demonstrate **Explainable AI (XAI)** concepts using simple, interpretable rules instead of black-box models.

## Problem Statement
Manual inspection of financial transactions is time-consuming and error-prone.  
This project automates risk detection and provides transparent explanations to support faster and more reliable decision-making.

## Features
- Rule-based risk scoring engine
- NLP-style keyword detection from transaction messages
- Explainable AI (GenAI-style natural language explanations)
- Risk classification: **Low / Medium / High**
- Structured risk reports using Pandas DataFrames
- Easily extensible for ML-based models

## Risk Scoring Logic
| Rule | Condition | Score |
|-----|----------|-------|
| High Amount | Amount > 10,000 | +40 |
| Risky Country | Unknown / Nigeria | +30 |
| Risky Keywords | urgent, click, win, verify, prize | +10 per keyword |

## Technologies Used
- Python
- Pandas
- Basic NLP techniques
- Explainable AI (XAI) concepts

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas
