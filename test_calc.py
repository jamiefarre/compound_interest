from calc import monthly_compounding


def test_zeros():
    # Arrange
    initial = 0
    apr = 0
    monthly = 0
    years = 0
    expected_output = 0

    # Act
    actual_output = monthly_compounding(initial, apr, monthly, years)

    # Assert
    assert actual_output == expected_output


def test_one_year_zero_interest():
    # Arrange
    initial = 100
    apr = 0
    monthly = 0
    years = 1
    expected_output = 100

    # Act
    actual_output = monthly_compounding(initial, apr, monthly, years)

    # Assert
    assert actual_output == expected_output
