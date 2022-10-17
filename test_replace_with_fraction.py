from byu_pytest_utils.decorators import max_score
from test_utils import test_files, compare_files, this_folder, run_python


@max_score(2)
def test_replace_with_fraction_one_line():
    input_file = test_files / "replace_with_fraction_one_line.input.txt"
    observed = "replace_with_fraction_one_line.observed.txt"
    run_python(this_folder / "replace_with_fraction.py", input_file, observed)

    expected = test_files / "replace_with_fraction_one_line.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_replace_with_fraction_multiple_lines():
    input_file = test_files / "replace_with_fraction_multiple_lines.input.txt"
    observed = "replace_with_fraction_multiple_lines.observed.txt"
    run_python(this_folder / "replace_with_fraction.py", input_file, observed)

    expected = test_files / "replace_with_fraction_multiple_lines.expected.txt"
    compare_files(expected, observed)
