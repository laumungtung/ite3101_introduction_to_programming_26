You are very close! Here are a few small fixes to make sure your Python code works and matches the document's instructions:

* **Question 1:**
Python variable names are case-sensitive. The instruction asks for `cucumbers` (plural), so make sure to write `cucumbers = 100`.
* **Question 2:**
Make sure to lowercase the variable name `whole_cucumbers_per_person`. To perform integer division (if you want whole cucumbers without decimals), Python uses `//`. Also, don't forget to print it!
* **Question 3:**
To get the float result (with decimals), divide `cucumbers` by `num_people` using `/` (not just setting it equal to `num_people`).

Here is the complete code:

```python
# 1. Define the variables
cucumbers = 100
num_people = 6

# 2. Divide for whole cucumbers and print
whole_cucumbers_per_person = cucumbers // num_people
print(whole_cucumbers_per_person)


float_cucumbers_per_person = cucumbers / num_people
print(float_cucumbers_per_person)

