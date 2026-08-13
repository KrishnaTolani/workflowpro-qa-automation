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
├── browserstack.yml          
│
├── Case_Study_Solution.pdf
│    
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── project_page.py
│
├── api/
│   ├── __init__.py
│   └── client.py
│
└── tests/
    ├── __init__.py
    ├── test_login.py
    ├── test_multi_tenant.py
    └── test_project_creation.py


## Technology Stack
Python
pytest
Playwright
Requests
BrowserStack
GitHub Actions / CI/CD concepts
Testing Approach
UI Testing

Playwright is used for browser automation and UI validation.

Important principles include:

Use reliable locators.
Use Playwright's automatic waiting.
Avoid unnecessary time.sleep() calls.
Wait for meaningful application states.
Use isolated browser contexts.
Capture useful debugging information on failures.
API Testing

API requests are used for:

Test data creation
Backend validation
Faster setup
Tenant isolation testing
Multi-Tenant Testing

The application is treated as a multi-tenant SaaS platform.

Tests validate that:

Company 1 can access its own data.
Company 2 can access its own data.
Company 2 cannot access Company 1 resources.
Cross-tenant API requests are rejected.
Mobile Testing

BrowserStack is proposed for testing supported real mobile devices and browsers.

CI/CD

A smaller smoke suite can run on pull requests, while broader browser and mobile regression tests can run on scheduled or release pipelines.

Important Assumptions

The case study does not provide a complete executable application or API environment.

Therefore, the implementation contains assumptions regarding:

Authentication
2FA
Test credentials
Project retrieval
Project deletion
BrowserStack configuration
Expected cross-tenant HTTP status codes
UI selectors

These assumptions are documented in the case-study solution.
