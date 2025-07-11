# Selenium Automation Framework with Pytest

This project is a test automation framework built using **Selenium WebDriver** and **Pytest**. It supports test case execution, HTML reporting, parallel execution, Excel-based data handling, and advanced reporting using Allure.

---

## 🔧 Tech Stack

- **Python**
- **Selenium**
- **Pytest**
- **Pytest-HTML**
- **Pytest-Xdist** (for parallel execution)
- **Openpyxl** (for reading/writing Excel files)
- **Allure-Pytest** (for detailed test reports)

---

## 📦 Required Dependencies

Make sure you have Python 3.7+ installed. Install all the required packages with:

```bash
pip install -r requirements.txt
````

> Example `requirements.txt`:

```text
selenium
pytest
pytest-html
pytest-xdist
openpyxl
allure-pytest
```

---

## 📁 Project Structure

```
├── bases_pages/                  
│   └── Login_Admin_page.py
├── configurations/                  
│   └── config.ini
├── logs/                  
│   └── nopcommerce.log
├── reports/                
├── screenshots/           
├── test_cases/
     └── conftest.py
     └── test_admin_login.py         
├── utillties/
    └── custom_logger.py
    └── read_property.py
└── README.md
```

---

## 🚀 How to Run Tests

### 🧪 Run All Tests

```bash
pytest
```

### 🧪 Run Tests with HTML Report

```bash
pytest --html=reports/report.html
```

### ⚡ Run Tests in Parallel

```bash
pytest -n auto
```

### 📊 Run with Allure Reporting

1. Run tests with Allure data generation:

```bash
pytest --alluredir=reports/allure-results
```

2. Generate and open the Allure report:

```bash
allure serve reports/allure-results
```

---

## 📘 Excel Data-Driven Testing

Use the `openpyxl` package to read and write test data from `.xlsx` files.
Utility functions can be added in `utils/excel_reader.py`.

---

## 🛠️ Pytest.ini (Example)

```ini
[pytest]
addopts = -v --capture=tee-sys
testpaths = tests
```

---

## 🧼 Clean Up

To clean up generated reports:

```bash
rm -rf reports/*
