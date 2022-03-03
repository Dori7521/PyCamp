from powtorki import my_sum

def test_my_sum():
    score=my_sum(2,2)
    assert score == 4

def test_add_3_and_2():
    score=my_sum(3,4)
    assert score == 7