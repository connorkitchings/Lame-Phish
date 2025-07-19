<!-- markdownlint-disable MD013 MD033 MD055 MD056 -->
# Implementation Schedule – Goose Setlist Prediction

This document outlines the development sprints for the Goose Setlist Selector project.

---

## Sprint 1: Data Acquisition and Initial Setup

**Goal:** Fetch and store historical setlist, show, and song data from the elgoose.net API, and set up the basic project structure.

**Timeline:** 2025-07-19 - TBD

| Task ID  | Description                                                                                                                              | Status      | Assignee | PR Link |
| :------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------- | :------- | :------ |
| `TASK-01` | **Setup Project Structure:** Create the necessary directories (`src`, `data/raw`, `notebooks`, `scripts`, `tests`).                         | `DONE`      | Co-Pilot |         |
| `TASK-02` | **Develop API Client:** Create a Python module (`src/data/api_client.py`) to interact with the elgoose.net API.                           | `DONE`      | Co-Pilot |         |
| `TASK-03` | **Create Data Fetching Script:** Implement a script (`scripts/fetch_data.py`) to download all historical show, setlist, and song data.      | `DONE`      | Co-Pilot |         |

---
