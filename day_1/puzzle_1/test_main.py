"""
Test script for Day 1, Puzzle 1
Tests that the sample.txt file produces the expected result.
"""

import sys

# Import functions from main.py
from main import parse_input_file, calculate_password

def test_sample_file():
    """
    Test that processing sample.txt produces the expected result.
    """
    # Parse sample.txt
    file_instructions = parse_input_file('day_1/sample.txt')
    
    # Initialize dial
    dial = list(range(100))
    
    # Apply rotations
    counter = calculate_password(dial, file_instructions)
    
    # Expected result
    expected = 3
    
    # Verify result
    assert counter == expected, f"Test failed: Expected {expected}, got {counter}"
    print(f"✓ Test passed: sample.txt produces {counter} (expected {expected})")
    return True

if __name__ == "__main__":
    print("Running tests for Day 1, Puzzle 1...")
    print("-" * 50)
    
    try:
        test_sample_file()
        print("-" * 50)
        print("All tests passed! ✓")
    except AssertionError as e:
        print(f"✗ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error running tests: {e}")
        sys.exit(1)
