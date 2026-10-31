# L6_L7_46 — Photo Print Order

## Lab 6: Code and Branch Coverage Analysis

### About the Project

This project focuses on testing a Photo Print Order application using Python, pytest and the Coverage.py tool. The objective is to analyse code coverage and branch coverage by writing additional test cases for different conditions and edge cases.

### Application Functions

The application contains three main functions:

- **extra_print_charge()** – Calculates additional charges based on print size, number of copies, finish type and membership status.
- **order_valid()** – Checks whether an order satisfies the file size and copy limit conditions.
- **dispatch_status()** – Determines the dispatch status based on the available time, framing and international delivery.

### Technologies Used

- Python 3
- Pytest
- Coverage.py

### Test Cases

Two separate test files were created to analyse coverage:

1. `CodeCoverageTest_photo_print_order.py`
   - Tests application statements.
   - Covers valid inputs, invalid inputs and different conditions.

2. `BranchCoverageTest_photo_print_order.py`
   - Tests decision-making branches.
   - Covers True and False conditions, boundary values and different execution paths.

### Running the Tests

**1. Install dependencies**

```bash
pip install pytest coverage
```

**2. Run Code Coverage**

```bash
coverage erase
coverage run -m pytest "Lab 6/CodeCoverageTest_photo_print_order.py" "Lab 6/test_photo_print_order.py"
coverage report -m
```

**3. Run Branch Coverage**

```bash
coverage erase
coverage run --branch -m pytest "Lab 6/BranchCoverageTest_photo_print_order.py" "Lab 6/test_photo_print_order.py"
coverage report -m
```

### Coverage Results

| Coverage Type | Result |
|---|---:|
| Code Coverage | 100% |
| Branch Coverage | 100% |
| Branches Covered | 26/26 |
| Missing Statements | 0 |
| Partial Branches | 0 |

All 22 tests in the branch coverage test run passed successfully.

### Screenshots

The terminal screenshots showing the coverage reports are included in the `Lab 6` folder:

- `CodeCoverage.png`
- `BranchCoverage.png`

### Conclusion

Through this lab, code coverage and branch coverage were analysed using pytest and Coverage.py. Additional test cases were written to cover different conditions, invalid inputs and boundary cases. Both code coverage and branch coverage achieved 100%.