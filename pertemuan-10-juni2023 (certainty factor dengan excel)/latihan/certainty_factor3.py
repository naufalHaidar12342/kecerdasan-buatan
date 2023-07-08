def calculate_cf(evidence, rule):
    symptom, value = evidence
    symptoms = rule.split(";")
    if symptom in symptoms:
        return float(value)
    else:
        return 1.0 - float(value)


def calculate_certainty_factor(prior_cf, current_cf):
    return prior_cf + (current_cf * (1 - prior_cf))


def detect_illness(patient_data, diseases, symptoms):
    certainty_factors = {disease: 0.0 for disease in diseases}

    for symptom, value in patient_data.items():
        for disease, rule in symptoms.items():
            cf = calculate_cf((symptom, value), rule)
            certainty_factors[disease] = calculate_certainty_factor(
                certainty_factors[disease], cf
            )

    # Find the illness with the highest certainty factor
    max_cf = max(certainty_factors.values())
    illness = next(key for key, value in certainty_factors.items() if value == max_cf)

    return illness


# Define the data
diseases = {"P01": "A", "P02": "B", "P03": "C", "P04": "D"}

symptoms = {
    "P01": "G01;G03",
    "P02": "G02;G03;G06",
    "P03": "G02;G04;G01;G05",
    "P04": "G06;G05",
}

patient_data = {
    "Pusing": "0.5",
    "Batuk": "0.8",
    "Dehidrasi": "0.4",
    "Keringat Dingin": "0.3",
    "Menggigil": "0.2",
}

# Detect the illness
detected_illness = detect_illness(patient_data, diseases, symptoms)

# Print the result
print("The detected illness is:", diseases[detected_illness])
