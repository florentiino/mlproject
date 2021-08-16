from mlproject.distance import haversine


def test_length_distance():
    assert type(haversine(12.1231, 32.2132, 33.2123, 12.22)) == float
