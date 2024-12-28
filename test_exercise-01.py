# test_exercise-01.py
import subprocess

def test_exercise_01():
    # Run the student's code (assuming the filename is exercise-01.py)
    result = subprocess.run(['python3', 'exercise-01.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    # Test results for each exercise based on the expected output
    assert output[0] == 'Exercise 1: 10', f"Expected 'Exercise 1: 10', but got {output[0]}"
    assert output[1] == 'Exercise 2: John Doe', f"Expected 'Exercise 2: John Doe', but got {output[1]}"
    assert output[2] == 'Exercise 3: Sum = 8, Difference = 2, Product = 15, Quotient = 1.6666666666666667', f"Unexpected result for Exercise 3: {output[2]}"
    assert output[3] == 'Exercise 4: a = 20, b = 10', f"Expected 'Exercise 4: a = 20, b = 10', but got {output[3]}"
    assert output[4] == 'Exercise 5: 7 is odd', f"Expected 'Exercise 5: 7 is odd', but got {output[4]}"
    assert output[5] == 'Exercise 6: You are 25 years old', f"Expected 'Exercise 6: You are 25 years old', but got {output[5]}"
    assert output[6] == 'Exercise 7: Length of string = 18', f"Expected 'Exercise 7: Length of string = 18', but got {output[6]}"
    assert output[7] == 'Exercise 8: a AND b = False, a OR b = True, NOT a = False', f"Unexpected result for Exercise 8: {output[7]}"
    assert output[8] == 'Exercise 9: Square of 4 = 16', f"Expected 'Exercise 9: Square of 4 = 16', but got {output[8]}"
    assert output[9] == 'Exercise 10: Hello, Alice, you are 30 years old.', f"Expected 'Exercise 10: Hello, Alice, you are 30 years old.', but got {output[9]}"

    print("Test passed!")

if __name__ == "__main__":
    test_exercise_01()
