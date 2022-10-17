from byu_pytest_utils.decorators import max_score
from test_utils import test_files, compare_files, this_folder, run_python


@max_score(2)
def test_greater_that_one_hundred_two_lines():
    input_file = test_files / "greater_than_one_hundred_two_lines.input.txt"
    observed = "greater_than_one_hundred_two_lines.observed.txt"
    run_python(this_folder / "greater_than_one_hundred.py", input_file, observed)

    expected = test_files / "greater_than_one_hundred_two_lines.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_greater_that_one_hundred_seven_lines():
    input_file = test_files / "greater_than_one_hundred_seven_lines.input.txt"
    observed = "greater_than_one_hundred_seven_lines.observed.txt"
    run_python(this_folder / "greater_than_one_hundred.py", input_file, observed)

    expected = test_files / "greater_than_one_hundred_seven_lines.expected.txt"
    compare_files(expected, observed)
