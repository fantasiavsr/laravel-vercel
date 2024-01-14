import subprocess
import difflib
import json

def run_dart_analyze(flutter_code_path):
    try:
        process = subprocess.Popen(['dart', 'analyze', flutter_code_path],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
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

    # Menyiapkan list untuk menyimpan perbedaan antara kode siswa dan kunci jawaban
    differences = []
    for line in diff:
        if line.startswith('- ') or line.startswith('+ '):
            # Menyimpan nomor baris dan jenis perubahan
            kode = "code 1" if line.startswith('- ') else "code 2"
            differences.append({kode: line[2:].strip()})

    return {'error_count': error_count, 'differences': differences}

def evaluate_flutter_code(student_code_path, kunci_jawaban_path):
    analyze_returncode, analyze_stdout, analyze_stderr = run_dart_analyze(student_code_path)

    # Membandingkan kode siswa dengan kunci jawaban
    differences_result = compare_code(student_code_path, kunci_jawaban_path)

    # Menghitung nilai berdasarkan jumlah error dan perbedaan
    score = 100 - (analyze_returncode * 10 + differences_result['error_count'] * 5)
    score = max(0, score)  # Skor minimum adalah 0

    # Mengembalikan hasil penilaian dalam bentuk objek JSON
    result = {
        'analyze_returncode': analyze_returncode,
        'analyze_stdout': analyze_stdout,
        'analyze_stderr': analyze_stderr,
        'score': score,
        'differences': differences_result['differences'],
    }

    return json.dumps(result, indent=2)

def main():
    student_code_path = 'public/flutter_application_1/lib/main2.dart'
    kunci_jawaban_path = 'public/flutter_application_1/lib/main.dart'

    evaluation_result = evaluate_flutter_code(student_code_path, kunci_jawaban_path)

    print(evaluation_result)

if __name__ == '__main__':
    main()
