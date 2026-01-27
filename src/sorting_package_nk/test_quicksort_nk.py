import pytest
from module1 import sorting_class_nk

def test_quicksort_sorts_general_case():
    # Includes positives, negatives, and duplicates
    data = [3, -1, 2, 2, 10, 0, -5, 3]
    expected = sorted(data)

    result = sorting_class_nk.quicksort_nk(data, 0, len(data) - 1)

    # Should sort in-place and the returned list should be sorted as well
    assert result == expected
    assert data == expected  # in-place behavior

    print("both tests passed")


@pytest.mark.parametrize(
    "data",
    [
        [],          # empty list
        [42],        # single element
    ],
)


def test_quicksort_edge_cases(data):
    # For empty list, high becomes -1; function should no-op and return []
    # For single element, low == high; function should no-op and return [elem]
    expected = sorted(data)
    result = sorting_class_nk.quicksort_nk(data, 0, len(data) - 1 if data else -1)

    assert result == expected
    assert data == expected  # in-place behavior preserved
