def calculate_risk(findings):
    score = 0

    score += len(findings["xss"]) * 5
    score += len(findings["sqli"]) * 7
    score += len(findings["sensitive"]) * 4

    if findings["clickjacking"]:
        score += 3

    return score