import subprocess
import difflib

def run_dart_analyze(flutter_code_path):
    try:
        process = subprocess.Popen(['dart', 'analyze', flutter_code_path],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr
    except Exception as e:
        return -1, str(e), str(e)

def compare_code(student_code_path, kunci_jawaban_path):
    with open(student_code_path, 'r') as student_file:
        student_code = student_file.readlines()

    with open(kunci_jawaban_path, 'r') as kunci_jawaban_file:
        kunci_jawaban_code = kunci_jawaban_file.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(student_code, kunci_jawaban_code))

    error_count = 0
    for line in diff:
        if line.startswith('? '):  # Karakter ? menunjukkan perbedaan yang tidak dapat dihitung
            error_count += 1

    # Menampilkan perbedaan antara kode siswa dan kunci jawaban
    print("Perbedaan antara Kode Siswa dan Kunci Jawaban:")
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            # Menampilkan nomor baris dan jenis perubahan
            kode = "code 1" if line.startswith('- ') else "code 2"
            print(f"{kode}: {line[2:].strip()}")

    return error_count

def evaluate_flutter_code(student_code_path, kunci_jawaban_path):
    analyze_returncode, analyze_stdout, analyze_stderr = run_dart_analyze(student_code_path)

    # Membandingkan kode siswa dengan kunci jawaban
    differences_count = compare_code(student_code_path, kunci_jawaban_path)

    # Menghitung nilai berdasarkan jumlah error dan perbedaan
    score = 100 - (analyze_returncode * 10 + differences_count * 5)
    score = max(0, score)  # Skor minimum adalah 0

    # Mengembalikan hasil penilaian
    return {
        'analyze_returncode': analyze_returncode,
        'analyze_stdout': analyze_stdout,
        'analyze_stderr': analyze_stderr,
        'score': score,
    }

def main():
    student_code_path = 'public/flutter_application/lib/main2.dart'
    kunci_jawaban_path = 'public/flutter_application/lib/kunci_jawaban.dart'

    evaluation_result = evaluate_flutter_code(student_code_path, kunci_jawaban_path)

    print("Dart Analyze Return Code:", evaluation_result['analyze_returncode'])
    print("Dart Analyze Output:")
    print(evaluation_result['analyze_stdout'])
    print("Skor:", evaluation_result['score'])

if __name__ == '__main__':
    main()
