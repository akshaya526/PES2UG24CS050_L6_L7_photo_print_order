# L7_46 — Photo Print Order

## Lab 7: Fuzz Testing Using Hypothesis

### About the Project

This lab focuses on fuzz testing a Photo Print Order application using Python and the Hypothesis library. The objective is to identify input-handling errors by generating different inputs, observe failures in the original application, and improve the functions through input validation.

### Application Functions

The application contains three main functions:

- **parse_order()** – Parses print size and copy count from the given input.
- **file_size_average()** – Calculates the average of comma-separated file sizes.
- **payable_amount()** – Calculates the final payable amount after applying tax and discount.

### Technologies Used

- Python 3
- Pytest
- Hypothesis

### Fuzz Testing

Three property-based tests were implemented in `test_photo_print_order.py`:

1. `test_parse_order_no_crash()`
2. `test_file_size_average_no_crash()`
3. `test_payable_amount_no_crash()`

Hypothesis generated different inputs and identified failures in the original application, including:

- Empty strings
- Missing separators
- Invalid numeric values
- None inputs

### Bug Fixes

Input validation was added to the application functions to handle:

- Invalid or missing input.
- Incorrect input formats.
- Negative numeric values.
- Invalid numeric conversions.
- Non-finite monetary values.

Invalid inputs return safe default values instead of causing unexpected exceptions.

### Running the Tests

Install the required libraries:

```bash
pip install pytest hypothesis
```

Run the fuzz tests:

```bash
python -m pytest "Lab 7/test_photo_print_order.py" -v
```

### Test Results

The initial fuzz testing identified failures in all three functions.

After modifying the application, all three Hypothesis tests passed successfully.

| Test Function | Final Result |
|---|---|
| test_parse_order_no_crash | Passed |
| test_file_size_average_no_crash | Passed |
| test_payable_amount_no_crash | Passed |

**Final Result: 3 tests passed.**

### Screenshots and Report

The Lab 7 report contains screenshots of:

- Original application execution.
- Initial Hypothesis test failures.
- Fixed application execution.
- Successful Hypothesis test execution.

The report is saved as `Lab7_Report.pdf`.

### Conclusion

Fuzz testing helped identify input-handling issues in the Photo Print Order application. The identified issues were addressed by adding input validation and appropriate error handling. After the modifications, all three property-based tests passed successfully.