from src.retriever import _cosine

def test_cosine_identical_is_one():
    assert abs(_cosine([1, 0, 0], [1, 0, 0]) - 1.0) < 1e-6
    
def test_cosine_orthogonal_is_zero():
    assert abs(_cosine([1, 0], [0, 1])) < 1e-6
    
if __name__ == "__main__":
    test_cosine_identical_is_one()
    test_cosine_orthogonal_is_zero()
    print("All smoke tests passed. ")