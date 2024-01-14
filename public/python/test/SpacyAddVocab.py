import spacy
from spacy.vocab import Vocab

# Tambahkan kata-kata baru ke kamus Spacy
kata_kata_baru = ["floatingActionButton", "onPressed", "backgroundColor", "Colors", "blue", "tombolchild", "Icon", "Icons", "add"]
nlp = spacy.load("en_core_web_sm")

# Ambil kamus Spacy
kamus_spacy = nlp.vocab

# Tambahkan kata-kata baru ke kamus
for kata in kata_kata_baru:
    lexeme = kamus_spacy[kata]
    if not lexeme.is_oov:
        continue
    kamus_spacy.set_vector(kata, lexeme.vector)

# Uji kata-kata yang telah ditambahkan
for kata in kata_kata_baru:
    lexeme = kamus_spacy[kata]
    print(f"Kata: {kata}, Apakah Kata OOV? {lexeme.is_oov}")
