import string

def check_common(password):
    url = "https://gist.githubusercontent.com/richardkundl/b68afdcf68240dcff50a/raw/10k-common-passwords"
    try:
        response = requests.get(url)
        common_passwords = response.text.splitlines()
        return password in common_passwords
    except:
        return False
    
def calcStrength(password):
    length = len(password)
    score = 0

    upperCase = any(c.isupper() for c in password)
    lowerCase = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digit = any(c.isdigit() for c in password)

    charectersInPassword = [upperCase, lowerCase, special, digit]

    if length > 8:
        score += 1
    elif length > 12:
        score += 1
    elif length > 17:
        score += 1
    elif length > 20:
        score += 1

    score += sum(charectersInPassword) - 1

    if score < 4:
        print("Weak")
    elif score == 4:
        print("Okay")
    
    if score < 4:
        label = "Weak"
    elif score < 6:
        label = "Okay"
    elif score < 8:
        label = "Great"
    else:
        label = "Strong"

    return label, score

def feedback(password):
    if check_common(password):
        return "Password is too common. Please choose a different password."
    
    strength, score = calcStrength(password)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer (more than 8 characters). \n"
        if not any(c.isupper() for c in password):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"

    return feedback

def main():
    password = input("Enter the password: ")
    print(feedback(password))

if __name__ == "__main__":
    main()