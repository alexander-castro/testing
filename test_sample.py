"""Testing."""
def inc(ageUser):
    """Method #01"""
    return ageUser + 1

def test_answer():
    """Test #01"""
    assert inc(3) == 5
