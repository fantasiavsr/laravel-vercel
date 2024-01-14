import spacy

nlp = spacy.load("en_core_web_sm")

def analisis_nlp(jawaban_siswa, kunci_jawaban):
    # Proses tokenisasi
    tokens_jawaban_siswa = nlp(jawaban_siswa)
    tokens_kunci_jawaban = nlp(kunci_jawaban)

    # Menghitung similarity antara jawaban siswa dan kunci jawaban
    similarity = tokens_jawaban_siswa.similarity(tokens_kunci_jawaban)

    return similarity

# Contoh penggunaan
jawaban_siswa = "Flutter adalah framework pengembangan aplikasi mobile."
kunci_jawaban = "Flutter adalah kerangka kerja pengembangan aplikasi mobile."

nilai_similarity = analisis_nlp(jawaban_siswa, kunci_jawaban)
print("Nilai Similaritas:", nilai_similarity)
