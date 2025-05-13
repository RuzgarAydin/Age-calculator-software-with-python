import datetime

# 1
birth_year = int(input("Enter your birth year:  "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"Your age is {age} years old.")

# 2
def verify_login(username: str, password: str) -> str:
    users = {"admin": "admin123", "user": "pass456"}  # Kullanıcı veritabanı
    if username not in users:
        return "User not found"
    if users[username] != password:
        return "Wrong password"
    return "Login successful"

# Example:
print(verify_login("admin", "admin123"))  # "Login successful"
print(verify_login("user", "wrongpass"))  # "Wrong password"

# 3
def get_discount(is_vip: bool, purchase_total: float) -> float:
    if is_vip and purchase_total > 1000:
        return 0.2
    elif is_vip:
        return 0.1
    elif purchase_total > 1000:
        return 0.05
    return 0.0

# Example:
print(get_discount(True, 1200))  # 0.2
print(get_discount(False, 1500))  # 0.05

# 4
def is_eligible(age: int, is_member: bool) -> bool:
    if age < 18 or age > 60:
        return False
    if is_member:
        return False
    return True

# Example:
print(is_eligible(25, False))  # True
print(is_eligible(17, False))  # False
print(is_eligible(25, True))   # False

# 5
def is_eligible_for_insurance(age: int, country: str, has_condition: bool, high_risk_zone: bool) -> bool:
    if not (18 <= age <= 70):
        return False
    if country not in ["USA", "UK", "Canada", "Germany"]:
        return False
    if has_condition and high_risk_zone:
        return False
    return True

# Example:
print(is_eligible_for_insurance(30, "USA", False, False))  # True
print(is_eligible_for_insurance(80, "USA", False, False))  # False
