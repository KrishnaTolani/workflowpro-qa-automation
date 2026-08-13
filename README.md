# WorkFlow Pro QA Automation

QA Automation Engineering Intern Case Study submission for Bynry Inc.

## Candidate

**Krishna Tolani**

## Role

QA Automation Engineering Intern

## Case Study

B2B SaaS Platform Testing – Multi-Platform Automation

---

## Overview

This repository contains my proposed QA automation approach for the WorkFlow Pro B2B SaaS platform.

The solution focuses on:

- Playwright UI automation
- pytest test execution and fixtures
- API testing
- Multi-tenant testing
- Tenant isolation
- Test data management
- Cross-browser testing
- Mobile testing concepts using BrowserStack
- CI/CD integration
- Flaky test prevention

---

## Repository Structure

```text
workflowpro-qa-automation/
│
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── conftest.py
│
├── case-study/
│   └── Case_Study_Solution.pdf
│
├── pages/
│   ├── login_page.py
│   └── project_page.py
│
├── api/
│   └── client.py
│
└── tests/
    ├── test_login.py
    ├── test_multi_tenant.py
    └── test_project_creation.py
