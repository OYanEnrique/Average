# Average
A simple Python script that calculates the average of two scores and determines the student's status: failed, needs a retake, or passed.

# 📊 Grade Average Calculator

This is a command-line program written in Python that calculates the average of two test scores and provides the student's academic status based on the result.

The script prompts the user to enter two scores. It then computes the average and uses conditional logic to determine if the student has passed, failed, or needs to take a retake test. 

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `Average.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python Average.py
    ```
5.  Enter the first score when prompted and press Enter.
6.  Enter the second score and press Enter to see the final average and status.

## Grading Logic

The program classifies the student's status based on the calculated average:

* **Failed:** If the average is less than `5.0`.
* **Needs Retake:** If the average is between `5.0` and `6.9` (inclusive).
* **Passed:** If the average is `7.0` or greater.
