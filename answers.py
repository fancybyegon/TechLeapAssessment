"""
TechLeap Apprenticeship — Assessment Answers
Author: Fancy Byegon
Date: October 2025
Description:
  This script contains answers to all sections of the TechLeap Apprenticeship assessment:
  1. Logic & Problem Solving
  2. Web / Software Development
  3. Debugging & Reasoning
  4. Version Control & Collaboration
"""

# ===============================================================
# SECTION 1: LOGIC & PROBLEM SOLVING (10 marks)
# ===============================================================

def second_largest(nums):
    """
    Returns the second-largest unique number in a list.
    Approach:
      - Convert list to a set to remove duplicates.
      - Sort the unique numbers.
      - Return the second largest.
    """
    unique_nums = sorted(set(nums))
    if len(unique_nums) < 2:
        raise ValueError("List must contain at least two unique numbers.")
    return unique_nums[-2]

print("Q1: Second Largest Number →", second_largest([10, 4, 8, 2, 10]))

"""
Q2: Page Optimization
Causes and Fixes:
1️⃣ Large Image Files — compress images or use WebP format.
2️⃣ Too Many HTTP Requests — minify/merge CSS & JS, enable lazy loading.
3️⃣ No Caching — enable browser caching or use a CDN.
"""

# ===============================================================
# SECTION 2: WEB / SOFTWARE DEVELOPMENT (15 marks)
# ===============================================================

import requests

def fetch_user_data():
    """Fetch user data from an API and display name & email."""
    print("\nQ3: Fetching user data...")
    try:
        print("Loading...")
        response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
        response.raise_for_status()
        user = response.json()
        print("✅ Success! User Data:")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching user data:", e)

fetch_user_data()

sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

def calculate_total_revenue(data):
    """Calculate total revenue by summing price * quantity."""
    return sum(item['price'] * item['quantity'] for item in data)

total = calculate_total_revenue(sales_data)
print("\nQ4: Total Store Revenue →", total)

# ===============================================================
# SECTION 3: DEBUGGING & REASONING (10 marks)
# ===============================================================

"""
Original buggy code:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)

Problem:
- Removes by index, not value.
- Mutates list during iteration → unexpected results.
Output: [2, 3, 5]

Fix:
Use a list comprehension to filter out even numbers.
"""

numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print("\nQ5: Corrected List (Removed Even Numbers) →", numbers)

# ===============================================================
# SECTION 4: VERSION CONTROL & COLLABORATION (5 marks)
# ===============================================================

"""
Q6: Version Control & Collaboration

1️⃣ Common Git Command:
   - git pull → fetch and merge latest changes from remote.

2️⃣ How I collaborate:
   - Each developer works on a separate branch (e.g., feature/login).
   - Commit changes regularly and open pull requests for review.
   - Merge after code review and testing.

3️⃣ Problem faced:
   - Merge conflicts during branching.
   - Solved by reviewing conflicting lines, editing, testing, and using:
     git add . && git merge --continue
"""

print("\nQ6: See explanation in comments above ✅")
print("\nAll sections completed successfully!")
