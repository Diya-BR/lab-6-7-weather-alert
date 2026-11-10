# Lab 7 – Fuzz Testing for Input Validation Bugs

## Overview

This lab explores fuzz testing and property-based testing using Python's **Hypothesis** library. The objective was to identify input validation bugs in a Weather Alert Classifier application, improve its robustness, and verify the fixes using automated tests.

## Application Description

The Weather Alert Classifier contains three main functions:

- `parse_reading()` – Parses temperature and humidity readings.
- `wind_category()` – Classifies wind speeds into warning, advisory, or none.
- `rainfall_spread()` – Calculates the difference between the maximum and minimum rainfall readings.

## Technologies Used

- Python 3
- Hypothesis
- pytest

## Project Structure

```text
lab7/
├── weather_alert.py
├── test_weather_alert.py
├── Lab-7_Report.pdf
└── README.md
```

## Implementation

Hypothesis was used to generate different inputs, including unexpected and invalid values, to test the application's input-handling behaviour.

The initial tests identified errors in:

- `parse_reading()` – Failed when given `None`.
- `rainfall_spread()` – Failed when given `None`.

The application was updated with input validation and appropriate error handling to prevent these unhandled exceptions.

## Running the Application

Install the required dependencies:

```bash
python -m pip install hypothesis pytest
```

Run the application:

```bash
python weather_alert.py
```

## Running the Tests

Execute the test suite using:

```bash
python -m pytest test_weather_alert.py -v
```

**Final Test Result:** 3 tests passed.

## Deliverables

- `weather_alert.py` – Updated Weather Alert Classifier application.
- `test_weather_alert.py` – Hypothesis-based fuzz testing script.
- `Lab-7_Report.pdf` – Lab report containing the experiment, observations, fixes, and execution screenshots.

## Conclusion

This experiment demonstrated how fuzz testing can help identify unexpected input-handling errors. Using Hypothesis and pytest, the application was tested with automatically generated inputs, the identified bugs were addressed, and the final test suite completed successfully.
