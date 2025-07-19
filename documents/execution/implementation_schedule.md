<!-- markdownlint-disable MD013 MD033 MD055 MD056 -->
# Implementation Schedule – Goose Setlist Prediction

| Week | Focus | Key Deliverables |
|------|-------|------------------|
| 1 | Data discovery & extraction | • Scrape/collect historical setlists<br>• Clean & normalize into tabular song-show matrix (CSV/parquet)<br>• Commit raw + processed data artifacts |
| 2 | Feature engineering & baseline model | • Engineer song-level features (last played gap, tour/venue tags, play frequency)<br>• Train baseline logistic-regression classifier<br>• Track metrics (precision, recall, PR curve) |
| 3 | Model improvement & evaluation | • Iterate with XGBoost / LightGBM<br>• Handle class imbalance, tune hyper-params<br>• Produce evaluation report + confusion matrix<br>• Generate feature-importance visual (e.g., SHAP) |
| 4 | Polish & optional Streamlit UI | • Finalize reproducible training script & README<br>• Build simple Streamlit app to upload upcoming show metadata and return top-25 predictions<br>• Prepare project write-up & shareable notebook |

## Dependencies

- **Data Access:** Stable scraping endpoint or exported CSV from ElGoose / setlist.fm.
- **Libraries:** `pandas`, `scikit-learn`, `xgboost`, `streamlit` (optional), `shap`.
- **Environment:** Python ≥3.9, Git with branch naming conventions from dev_log.

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Site structure changes / scraping blocks | Med | High | Cache raw HTML responses; fall back to manual CSV dump |
| Class imbalance hurts recall | High | Med | Use class-weighting, threshold tuning, ensemble methods |
| Incomplete metadata (encores, guests) | Med | Low | Treat unknowns as NA; include boolean flags |

## Rollback Plans

- If feature engineering slows progress → fall back to last-played-gap + frequency only.
- If XGBoost underperforms → stick with regularized logistic regression.
- If Streamlit UI scope creep → deliver CLI notebook for predictions instead.

## Sprint Overview

- **Sprint Duration:** 1 week
- **Start Date:** [YYYY-MM-DD]
- **End Date:** [YYYY-MM-DD]
- **Sprint Goal:** [Brief description of what this sprint aims to achieve]

## Task Tracking

| ID | Deliverable | Owner | Est (h) | Dependencies | Risk | Start | End | Status | Definition of
Done | Rollback Plan |
|----|-------------|-------|---------|--------------|------|-------|-----|--------|-------------------|---------------|
| 1  | MVP endpoint | @dev | 4 | - | L | 2025-07-15 | 2025-07-15 | ⬜ Todo | Tests pass, API docs updated, error handling complete | Use mock data response |
| 2  | UI stub      | @dev | 6 | ID:1 | M | 2025-07-15 | 2025-07-16 | ⬜ Todo | Components render, basic interactions work, responsive design | Static mockup with placeholder data |
| 3  | User test 1  | @dev | 2 | ID:2 | L | 2025-07-16 | 2025-07-16 | ⬜ Todo | 3 users test core flow, feedback documented, critical issues identified | Skip if timeline tight, use internal testing |
| 4  | Database setup | @dev | 3 | - | H | 2025-07-17 | 2025-07-17 | ⬜ Todo | Schema created, migrations work, backup strategy defined | Use in-memory storage temporarily |
| 5  | Authentication | @dev | 8 | ID:4 | H | 2025-07-18 | 2025-07-19 | ⬜ Todo | Login/logout works, sessions secure, password reset functional | Skip auth, use hardcoded user |

## User Testing Schedule

| ID | Test Type | Participants | Success Criteria | Scheduled Date | Status |
|----|-----------|--------------|------------------|----------------|---------|
| UT1 | Core flow usability | 3 users | Users complete signup→action in <2 min | 2025-07-16 | ⬜
Todo |
| UT2 | Feature validation | 5 users | 80% prefer new UI layout | 2025-07-20 | ⬜ Todo |
| UT3 | Pre-launch test | 5 users | <1 critical bug per user session | 2025-07-25 | ⬜ Todo |

## Legend

- **Status:** ⬜ Todo · 🔄 In-Progress · ✅ Done · ⏸ Blocked
- **Risk:** H(igh) · M(edium) · L(ow)
- **Dependencies:** Use ID:X format to reference other tasks

## Global Definition of Done

Every task must meet these criteria:

- [ ] Tests pass (unit + integration)
- [ ] Linter clean (no warnings)
- [ ] Documentation updated if needed
- [ ] Security checklist reviewed
- [ ] Code reviewed (AI-assisted for solo projects)
- [ ] User impact considered

## Sprint Retrospective

*(Fill out at end of sprint)*

**What Went Well:**
-

**What Didn't Go Well:**
-

**Action Items for Next Sprint:**
-

**Velocity:** [Completed story points / Planned story points]

---

## Backlog (Future Sprints)

| Priority | Feature | Estimated Effort | Notes |
|----------|---------|------------------|-------|
| High | User profiles | 12h | Depends on auth completion |
| Medium | Email notifications | 6h | Nice to have for MVP |
| Low | Advanced search | 20h | Post-MVP feature |

## Risk Management

| Risk | Probability | Impact | Mitigation Strategy | Owner |
|------|-------------|--------|-------------------|-------|
| Third-party API changes | Medium | High | Implement fallback, monitor changelog | @dev |
| User adoption lower than expected | High | Medium | Pivot to simpler use case, gather more feedback | @dev |
| Technical debt accumulation | High | Medium | Allocate 20% of sprint to refactoring | @dev |
