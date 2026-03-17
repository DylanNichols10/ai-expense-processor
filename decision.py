def make_decision(ai_output):
    amount = ai_output["amount"]

    if amount < 500:
        decision = "auto_approve"
    elif amount < 2000:
        decision = "review"
    else:
        decision = "manual_review"

    return {
        **ai_output,
        "decision": decision
    }