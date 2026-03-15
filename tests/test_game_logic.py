from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" with correct message "Go LOWER!"
    result = check_guess(60, 50)
    assert result == ("Too High", "📈 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" with correct message "Go HIGHER!"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📉 Go HIGHER!")

def test_get_range_easy():
    # Easy difficulty should return 1-20
    result = get_range_for_difficulty("Easy")
    assert result == (1, 20)

def test_get_range_normal():
    # Normal difficulty should return 1-50
    result = get_range_for_difficulty("Normal")
    assert result == (1, 50)

def test_get_range_hard():
    # Hard difficulty should return 1-100, making it harder than Normal
    result = get_range_for_difficulty("Hard")
    assert result == (1, 100)

def test_get_range_default():
    # Unknown difficulty defaults to 1-100
    result = get_range_for_difficulty("Unknown")
    assert result == (1, 100)
