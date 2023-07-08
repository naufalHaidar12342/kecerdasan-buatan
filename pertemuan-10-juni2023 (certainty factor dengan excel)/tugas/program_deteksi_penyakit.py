# deteksi penyakit dengan certainty factor
symptoms = {
    "P01": "G01;G03",
    "P02": "G02;G03;G06",
    "P03": "G02;G04;G01;G05",
    "P04": "G06;G05",
}
diseases = {
    "P01": "A",
    "P02": "B",
    "P03": "C",
    "P04": "D",
}

patient_data = {
    "Pusing": "0.50",
    "Batuk": "0.80",
    "Dehidrasi": "0.40",
    "Keringat dingin": "0.30",
    "Menggigil": "0.20",
}


# fungsi calculate_cf untuk menghitung nilai certainty factor
def calculate_cf(evidence, rule):
    symptom, value = evidence
    symptoms = rule.split(";")
    if symptom in symptoms:
        return float(value)
    else:
        return 1.0 - float(value)


# menghitung certainty factor terkini dan certainty factor sebelumnya
def delta_cf(prior_cf, current_cf):
    return prior_cf + (current_cf * (1 - prior_cf))


# melakukan deteksi penyakit
def detect_illness(patient_data, diseases, symptoms):
    cf = {disease: 0.0 for disease in diseases}

    for symptom, value in patient_data.items():
        for disease, rule in symptoms.items():
            perform_cf = calculate_cf((symptom, value), rule)
            cf[disease] = delta_cf(cf[disease], perform_cf)

    # mencari nilai certainty factor tertinggi
    max_cf = max(cf.values())
    illness = next(key for key, value in cf.items() if value == max_cf)

    return illness


""" 
dictionary bernama patient_data, diseases, dan symptoms sudah di definisikan/deklarasikan (lihat baris 2, 8, dan 15)
"""
test_program_deteksi = detect_illness(patient_data, diseases, symptoms)

# print/cetak hasil deteksi penyakit
print("Hasil deteksi penyakit adalah:", diseases[test_program_deteksi])
