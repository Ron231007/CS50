from project import is_float, create_expense,calculate_budget_status

def test_is_float_valid():
    assert(is_float(10) == True)
    assert(is_float(10.5) == True)

def test_is_float_invalid():
    assert(is_float('a') == False)
    assert(is_float([1,2,3,5]) == False)
    assert(is_float(['1','2','3','5']) == False)


def test_budget_within():
    status, amt = calculate_budget_status(100, 60)
    assert status == "within"
    assert amt == 40

def test_budget_over():
    status, amt = calculate_budget_status(100, 150)
    assert status == "over"
    assert amt == 50

def test_create_expense_valid():
    exp = create_expense("food", "10.5", 1)
    assert exp.name == "Food"
    assert exp.cost == 10.5

def test_create_expense_invalid():
    import pytest
    with pytest.raises(ValueError):
        create_expense("food", "abc", 1)