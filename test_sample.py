"""Testing."""
def inc(age_user):
    """Method #01"""
    return age_user + 10

def test_answer():
    """Test #01"""
    assert inc(18) == 19
