import spacy
import difflib

nlp = spacy.load("en_core_web_sm")

def analisis_nlp(jawaban_siswa, kunci_jawaban):
    # Proses tokenisasi
    tokens_jawaban_siswa = nlp(jawaban_siswa)
    tokens_kunci_jawaban = nlp(kunci_jawaban)

    # Menghitung similarity antara jawaban siswa dan kunci jawaban
    similarity = tokens_jawaban_siswa.similarity(tokens_kunci_jawaban)

    # Mendapatkan perbandingan kata menggunakan difflib
    differ = difflib.Differ()
    diff = differ.compare(jawaban_siswa.split(), kunci_jawaban.split())

    # Menampilkan kata-kata yang berbeda
    kata_berbeda = [word[2:] for word in diff if word.startswith('- ')]
    print("Kata-kata yang Berbeda:", kata_berbeda)

    return similarity

# Contoh penggunaan
jawaban_siswa = "floatingActionButton: FloatingActionButton(onPressed: () {}, backgroundColor: Colors.blue, tombolchild: Icon(Icons.add), ),"
kunci_jawaban = "floatingActionButton: FloatingActionButton(onPressed: () {}, backgroundColor: Colors.red, tombolchild: Icon(Icons.add), ),"

nilai_similarity = analisis_nlp(jawaban_siswa, kunci_jawaban)
print("Nilai Similaritas:", nilai_similarity)
