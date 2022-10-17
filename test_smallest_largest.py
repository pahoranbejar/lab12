from byu_pytest_utils.decorators import max_score
from test_utils import compare_files, test_files, this_folder, run_python


@max_score(2)
def test_smallest_largest_one_line():
    input_file = test_files / "smallest_largest_one_line.input.txt"
    observed = "smallest_largest_one_line.observed.txt"
    run_python(this_folder / "smallest_largest.py", input_file, observed)

    expected = test_files / "smallest_largest_one_line.expected.txt"
    compare_files(expected, observed)


@max_score(3)
def test_smallest_largest_multiple_lines():
    input_file = test_files / "smallest_largest_one_line.input.txt"
    observed = "smallest_largest_one_line.observed.txt"
    run_python(this_folder / "smallest_largest.py", input_file, observed)

    expected = test_files / "smallest_largest_one_line.expected.txt"
    compare_files(expected, observed)
