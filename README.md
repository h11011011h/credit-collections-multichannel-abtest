# 📬 Multichannel Collections A/B Testing & Unit Economics Optimization Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Consumer%20Credit%20Risk-orange.svg)]()

An end-to-end experimental framework designed to evaluate and optimize collections outreach strategies across the credit lifecycle. Specifically, this repository models the decision to introduce physical **Direct Mail** alongside digital-first channels (SMS, Email, Dialer) for consumer loans entering early-stage delinquency (**30–60 Days Past Due / DPD**)[cite: 1].

---

## 📌 Executive Summary & Business Impact

In digital-first consumer lending, engagement rates on SMS and email often decay rapidly as accounts slip into deeper delinquency. This project builds a rigorous A/B testing pipeline ($N = 20,000$) to evaluate whether the physical mailer's marginal cost (~$0.75) is justified by incremental cure rates and net dollar recovery.

### Key Results Summary:
* **Baseline (Control - Digital Only):** 21.76% Cure Rate
* **Treatment (+ Direct Mail):** 24.82% Cure Rate
* **Relative Lift:** **+14.04%** ($p = 0.000$, $p < 0.05$)
* **Outcome:** Adding direct mail produced a statistically significant boost in cured accounts, recovering substantial principal that far outweighs the $0.75/unit mailing cost.

---

## 🛠️ Repository Architecture

```text
credit-collections-multichannel-abtest/
├── config/
│   └── config.yaml               # Experiment configuration & cost parameters
├── data/
│   ├── raw/                      # Synthetic delinquent account cohort
│   └── processed/                # Processed feature & variant data
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Synthetic dataset generator
│   └── evaluation.py             # Two-proportion Z-test engine
├── main.py                       # CLI execution entry point
├── requirements.txt              # Environment dependencies
└── README.md