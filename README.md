# Student Grade Calculator

A lightweight Python CLI tool to compute a student's average score, overall percentage, letter grade, and pass/fail status.

## Features
- `average(scores)`: Computes the arithmetic mean of subject marks.
- `percentage(scores, max_score_per_subject)`: Calculates overall percentage.
- `grade_letter(pct)`: Maps percentage to a letter grade (A, B, C, D, F).
- `pass_fail(pct, passing_threshold)`: Determines whether the student passed or failed.

## Grading Policy
Enhanced 6-tier honors grading scale (A+, A, B, C, D, F) with strict 0-100% input validation and a 40% passing threshold.

## Usage
```bash
python grade_calculator.py
```
