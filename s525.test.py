def test_main():
    # Test case where both inputs are valid floats
    input_data = "3.5 4.2\n"
    expected_output = Point(3.5, 4.2)
    with patch("builtins.input", side_effect=input_data):
        main()
        assert pt._x == expected_output._x
        assert pt._y == expected_output._y

    # Test case where one input is not a valid float
    input_data = "3.5 a\n"
    expected_output = Point()
    with patch("builtins.input", side_effect=input_data):
        main()
        assert pt._x == expected_output._x
        assert pt._y == expected_output._y

    # Test case where both inputs are not valid floats
    input_data = "a b\n"
    expected_output = Point()
    with patch("builtins.input", side_effect=input_data):
        main()
        assert pt._x == expected_output._x
        assert pt._y == expected_output._y
