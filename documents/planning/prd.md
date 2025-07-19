# Product Requirements Document (PRD)

## PROJECT

Goose Setlist Prediction

## GOAL

Build a probability-based model that outputs the 25 songs most likely to be played at an upcoming
Goose show, optimized for ≥75 % recall and precision.

*For architecture, tech stack, and setup details, see [`project_context.md`](project_context.md).*

## USERS

### Primary Persona

- **Name:** Solo Developer
- **Role:** Intermediate ML learner & music fan
- **Pain Points:** Limited time to wrangle data; wants clear guidance and interpretable results
- **Goals:** Quickly build a high-quality predictive pipeline and learn ML best practices
- **Tech Comfort:** Intermediate

### Secondary Personas

- Hardcore Goose fans (Reddit/ElGoose community) interested in show predictions and post-show analysis
- Data-curious fans who explore setlist statistics

## USER STORIES

### Core User Stories

```markdown
As a Goose fan, I want to see a ranked list of likely songs so that I can set my show expectations.

Acceptance Criteria:
- [ ] User can request predictions for a future show date
- [ ] System responds with top-25 song list and probability scores
- [ ] Graceful error if date outside tour range or insufficient features
```

**Story 1:** Core workflow

- As the solo developer, I want an automated training pipeline so that I can retrain the model with fresh data quickly.
- **Priority:** Must-have
- **Effort:** [hours]

**Story 2:** Supporting feature

- As a Goose fan, I want to see a simple performance dashboard so that I can understand the model's strengths and weaknesses.
- **Priority:** Should-have
- **Effort:** [hours]

**Story 3:** Enhancement

- As a data-curious fan, I want to see a model interpretability dashboard so that I can understand why certain songs are predicted.
- **Priority:** Nice-to-have
- **Effort:** [hours]

## CORE FEATURES

### Must-Have (MVP)

- **Feature A:** Predictive model that outputs the 25 most probable songs for a given upcoming show
  - User story: Core workflow
  - Technical complexity: Medium
  - User impact: High
  - User story: [Reference to story above]
  - Technical complexity: [Low/Medium/High]
  - User impact: [High/Medium/Low]

- **Feature B:** Simple performance dashboard showing precision/recall and feature importances
  - User story: Supporting feature
  - Technical complexity: Low-Medium
  - User impact: Medium
  - User story: [Reference to story above]
  - Technical complexity: [Low/Medium/High]
  - User impact: [High/Medium/Low]

### Should-Have (Post-MVP)

- **Streamlit UI:** Lightweight web interface to input show metadata and view predictions
  - Depends on: Feature A, Feature B
  - Timeline: Week 4

- **Feature C:** Model interpretability dashboard (SHAP summary)
  - Depends on: trained XGBoost model
  - Timeline: Week 3

### Nice-to-Have (Future)

- **Setlist Sequence Generator:** RNN/Transformers to predict actual song order
  - Timeline: Post-MVP (Version 2.0)
- **Mobile App Integration** – push notifications on show day
  - Timeline: Post-MVP (Version 2.0)

## OUT OF SCOPE

### Explicitly Excluded

- Ticket resale price prediction
- Real-time setlist updates during live show
- Non-Goose bands

### Future Considerations

- Scalability concerns for future versions
- Integration with other music platforms

## ASSUMPTIONS & VALIDATIONS

### Key Assumptions

1. **User Behavior:** Fans will use the tool to inform their show expectations and engage with the community.
   - **Validation Method:** User testing and feedback
   - **Status:** Untested

2. **Technical Assumption:** The predictive model can achieve ≥75 % recall and precision with the available data.
   - **Validation Method:** Model evaluation metrics
   - **Status:** Untested

3. **Market Assumption:** There is a demand for a setlist prediction tool among Goose fans.
   - **Validation Method:** User adoption and engagement metrics
   - **Status:** Untested

## SUCCESS METRICS

### MVP Success Criteria

- **Usage Metrics:** Solo developer can generate predictions for any new show in <30 s
- **Performance Metrics:** ≥75 % precision and ≥75 % recall on held-out test data
- **User Satisfaction:** Qualitative feedback from 3+ Goose fans indicates predictions feel "mostly right" (>70 % perceived accuracy)
- **Technical Metrics:** Reproducible training pipeline, ≥80 % unit-test coverage, and CI green on main

### Long-term Success Metrics

- Growth targets for 3-6 months
- Engagement metrics for sustained usage

## SYSTEM DIAGRAM

```ascii
+-------------+      +------------+     +------------+
| Web UI      | ---> | API Server | --> | Database   |
+-------------+      +------------+     +------------+
       |                    |                 |
       v                    v                 v
[User Actions]      [Business Logic]    [Data Storage]
```

## DATA FLOW

```ascii
[User Input] --> [Validation] --> [Processing] --> [Storage]
     |              |                  |              |
     v              v                  v              v
[Form Data]   [Error Handling]   [API Calls]   [Database]
```

## EDGE CASES & RISKS

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scraper blocked by website | Medium | High | Cache HTML, respect robots.txt, back-up CSV dump |
| Model overfits rare songs | High | Medium | Use regularization & cross-validation |
| Class imbalance | High | Medium | Class weights & threshold tuning |

### User Experience Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Fans misinterpret probabilities | Medium | Medium | Include explanation tooltip |

### Business Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Low user adoption | Medium | High | MVP validation |
| Competition launches first | Low | Medium | Focus on unique value |

## SECURITY & PRIVACY

### Data Privacy Requirements

- **PII Handling:** [What personal data is collected and how it's protected]
- **Data Retention:** [How long data is kept and deletion policies]
- **User Consent:** [What permissions are required from users]

### Security Checklist

- [ ] Input validation on all user inputs
- [ ] Authentication and authorization implemented
- [ ] HTTPS enforced for all communications
- [ ] Sensitive data encrypted at rest
- [ ] Regular security dependency updates
- [ ] Error messages don't leak sensitive information

## DEPENDENCY GRAPH

### Feature Dependencies

- **Feature A** depends on: [Database setup, User authentication]
- **Feature B** depends on: [Feature A, Third-party API integration]
- **Feature C** depends on: [Feature B, Payment processing]

### External Dependencies

- **Third-party Services:** [List APIs, services, or tools required]
- **Hardware/Infrastructure:** [Server requirements, storage needs]
- **Compliance:** [Legal requirements, industry standards]

## DECISION LOG

| Date | Decision | Alternatives | Rationale | Commit/PR | Reversible? |
|------|----------|--------------|-----------|-----------|-------------|
| YYYY-MM-DD | [Decision made] | [Other options] | [Why this choice] | [Link] | Yes/No |
| 2025-07-15 | Use React for frontend | Vue.js, Angular | Team familiarity, ecosystem | #123 | Yes |
| 2025-07-16 | PostgreSQL for database | MySQL, MongoDB | ACID compliance needed | #124 | Difficult |

## FEEDBACK & ITERATION LOG

### User Testing Results

| Date | Test Type | Participants | Key Findings | Action Items |
|------|-----------|--------------|--------------|--------------|
| YYYY-MM-DD | [Usability test] | [3 users] | [Major insights] | [Changes made] |

### Assumption Validation Results

| Date | Assumption Tested | Method | Result | Impact on Product |
|------|------------------|--------|--------|------------------|
| YYYY-MM-DD | [Assumption] | [Test method] | [Validated/Invalidated] | [Product changes] |

## VERSION HISTORY

| Version | Date | Summary of Changes | Author |
|---------|------|---------------------|--------|
| v0.1 | YYYY-MM-DD | Initial draft | [Name] |
| v0.2 | YYYY-MM-DD | Added user stories and success metrics | [Name] |
| v1.0 | YYYY-MM-DD | Complete MVP requirements | [Name] |

---

## Quick Reference

### Key Contacts

- **Product Owner:** [Name/contact]
- **Technical Lead:** [Name/contact]
- **User Research:** [Name/contact]

### Important Links

- [Design mockups/wireframes]
- [Technical architecture docs]
- [User research findings]
- [Competitive analysis]

### Next Review Date

- **Scheduled:** [YYYY-MM-DD]
- **Attendees:** [List of reviewers]
- **Agenda:** [What needs to be reviewed/updated]
