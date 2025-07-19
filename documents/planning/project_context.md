# Project Context – Goose Setlist Prediction

## Overview

The goal is to predict which 25 songs Goose will play at an upcoming show by training a tabular binary-classification model (one label per song per show). Deliverables include a reproducible data pipeline, interpretable ML model(s), evaluation reports, and an optional Streamlit UI for fans/developers to query predictions.

## Architecture

```ascii
+--------------+      +-----------------+      +------------------+
| Raw Setlists | -->  | Data Pipeline   | -->  | Feature Matrix   |
+--------------+      +-----------------+      +------------------+
                                   |                       |
                                   v                       v
                             +-------------+       +----------------+
                             | ML Training |  -->  | Model Artifact |
                             +-------------+       +----------------+
                                                          |
                                                          v
                                               +--------------------+
                                               | Prediction Service |
                                               +--------------------+
```

Components:

1. **Data Pipeline (`/src/data/`)** – Scraping or ingesting CSV of historical setlists, cleaning, writing parquet/CSV.
2. **Feature Engineering (`/src/features/`)** – Calculate last-played gap, song frequency, tour tags, etc.
3. **Model Training (`/src/models/`)** – Baseline Logistic Regression ➜ XGBoost with hyper-parameter tuning.
4. **Evaluation (`/notebooks/` + `/reports/`)** – Precision/Recall, PR curves, SHAP plots.
5. **Optional UI (`/app/`)** – Streamlit app to upload show metadata and view predictions.

## Technology Stack

- Python 3.9+
- pandas, numpy, scikit-learn, xgboost, lightgbm (optional), shap
- requests / BeautifulSoup (scraping) or direct CSV dumps
- Streamlit (optional UI)
- pytest & coverage for tests

## Setup Instructions

```bash
# clone repo
$ git clone <repo-url>
$ cd goose-setlist-prediction

# create virtualenv
$ python -m venv .venv
$ source .venv/bin/activate

# install deps
$ pip install -r requirements.txt

# run tests
$ pytest -q
```

## Coding Standards

- PEP 8 & Black formatting; Ruff for linting.
- Type hints on all public functions.
- snake_case for variables & functions; PascalCase for classes.

## Testing

- Unit tests under `/tests/` mirror module structure.
- Target ≥80 % coverage.
- Use `pytest` fixtures for sample setlist data.

## Business Requirements & Constraints

- All-Python stack; no external paid APIs.
- Interpretability valued over marginal accuracy gains.

## Terminology

- **Gap** – Number of shows since a song was last played.
- **Hit Rate** – Historical fraction of shows containing a song.

## Known Issues & Limitations

- Historical data may miss encore flags or sit-in guests – captured as NA.

## Contact & Ownership

- **Product/ML Lead:** @solo-dev (repo owner)
- **Community Feedback:** r/ElGoose thread after each release.

- Brief description of the project and its main goal.
- Key features or modules.

## Architecture

- High-level architecture summary (list major components/services).
- Folder structure explanation (e.g., `/src`, `/tests`, `/components`).

## Technology Stack

- Languages, frameworks, and libraries used.
- Version requirements (e.g., Node.js 18+, Python 3.11).

## Setup Instructions

- Environment setup commands.
- How to install dependencies and run the project.

## Coding Standards

- Naming conventions (e.g., snake_case for variables).
- File organization rules.
- Style guide references.

## Testing

- Testing frameworks and how to run tests.
- Required coverage or test structure.

## Business Requirements & Constraints

- Non-negotiable requirements (e.g., must use OAuth 2.0, no external cloud services).
- Performance or compliance constraints.

## Terminology

- Definitions for project-specific terms or jargon.

## Known Issues & Limitations

- Current limitations, bugs, or technical debt to be aware of.

## Contact & Ownership

- Main contributors or maintainers.
- How to get support or ask questions.
