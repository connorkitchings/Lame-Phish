# Goose Setlist Prediction

Predict the 25 songs Goose is most likely to play at an upcoming show using a tabular
machine-learning model.

![Goose Banner](assets/goose_banner.png)

---

## Table of Contents

- [Goose Setlist Prediction](#goose-setlist-prediction)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Quick Start](#quick-start)
  - [Directory Layout](#directory-layout)
  - [Development](#development)
    - [Useful Make Targets](#useful-make-targets)
  - [Contributing](#contributing)
  - [License](#license)

## Project Overview

This repo contains everything needed to train, evaluate, and (optionally) serve a model that
outputs the top-25 probability-ranked songs for any future Goose concert date.

Core goals:

- ≥ 75 % precision / recall on held-out shows
- Human-interpretable features (e.g., last-played gap, tour tags)
- Reproducible end-to-end pipeline written **entirely in Python**

Full product requirements & architecture live in [`documents/planning`](documents/planning/).

## Quick Start

```bash
# 1. Clone & create virtualenv
$ git clone https://github.com/yourname/goose-setlist-prediction.git
$ cd goose-setlist-prediction
$ python -m venv .venv && source .venv/bin/activate

# 2. Install deps
$ pip install -r requirements.txt

# 3. Run data pipeline (Week 1)
$ python src/data/build_dataset.py  # scrapes/loads setlists → song-show matrix

# 4. Train baseline model (Week 2)
$ python src/models/train.py --model logistic_regression

# 5. Get predictions for a future date
$ python src/predict.py --date 2025-08-01 --top_k 25
```

## Directory Layout

```
documents/
  planning/          # PRD, project_context, implementation schedule
  execution/
    dev_logs/        # Daily developer logs
src/
  data/              # Scrapers & dataset builders
  features/          # Feature engineering modules
  models/            # Training scripts & model artifacts
  app/               # (Optional) Streamlit UI
assets/              # Images for README or docs
```

## Development

- **Python 3.9+**

- Code formatted with **Black**, linted by **Ruff**.
- Tests live in `/tests` and run via `pytest -q`; target ≥ 80 % coverage.

### Useful Make Targets

```makefile
make install   # pip install -r requirements.txt
make lint      # ruff check src tests
make test      # pytest --cov
make format    # black src tests
```

## Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

Before submitting a PR:

1. Ensure `make lint test` passes.
2. Follow the branch naming convention defined in
   [`documents/planning/dev_log_template.md`](documents/planning/dev_log_template.md).

## License

MIT © 2025 Goose Fan Collective
