"""Testing."""
def inc(age_user):
    """Method #01"""
    return age_user + 2

def test_answer():
    """Test #01"""
    assert inc(3) == 5
