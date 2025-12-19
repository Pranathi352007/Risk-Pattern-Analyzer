import pandas as pd
# 1. Sample Dataset
data = {
    "transaction_id": [101, 102, 103, 104],
    "amount": [500, 12000, 300, 15000],
    "country": ["India", "India", "Unknown", "Nigeria"],
    "message": [
        "Payment for groceries",
        "Urgent transfer required",
        "Click this link to win prize",
        "Immediate action needed, verify account"
    ]
}
df = pd.DataFrame(data)
# 2. Risk Keywords
risk_keywords = [
    "urgent", "click", "win", "verify", "immediate", "prize"
]
# 3. Risk Scoring Function
def calculate_risk(row):
    score = 0
    reasons = []
    # Rule 1: High transaction amount
    if row["amount"] > 10000:
        score += 40
        reasons.append("High transaction amount")
    # Rule 2: Suspicious country
    if row["country"] in ["Unknown", "Nigeria"]:
        score += 30
        reasons.append("Transaction from high-risk country")
    # Rule 3: Risky message content
    message_lower = row["message"].lower()
    for word in risk_keywords:
        if word in message_lower:
            score += 10
            reasons.append(f"Contains risky keyword: '{word}'")
    return score, reasons
# 4. Apply Risk Analysis
risk_scores = []
risk_reasons = []

for _, row in df.iterrows():
    score, reasons = calculate_risk(row)
    risk_scores.append(score)
    risk_reasons.append(", ".join(reasons))

df["risk_score"] = risk_scores
df["risk_reason"] = risk_reasons
# 5. GenAI-style Risk Labeling
def generate_risk_label(score):
    if score >= 70:
        return "HIGH RISK"
    elif score >= 40:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

df["risk_label"] = df["risk_score"].apply(generate_risk_label)
# 6. Final Output
print("\nGenAI Risk Analysis Report\n")
print(df)
def genai_explanation(row):
    return (
        f"Transaction {row['transaction_id']} is labeled as {row['risk_label']} "
        f"because the risk score is {row['risk_score']} due to: {row['risk_reason']}."
    )

df["genai_explanation"] = df.apply(genai_explanation, axis=1)

print("\nGenAI Explanations:\n")
for exp in df["genai_explanation"]:
    print("-", exp)

