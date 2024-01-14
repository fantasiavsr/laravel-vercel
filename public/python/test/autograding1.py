import subprocess

def run_dart_analyze(flutter_code_path):
    try:
        process = subprocess.Popen(['dart', 'analyze', flutter_code_path],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr
    except Exception as e:
        return -1, str(e), str(e)

def evaluate_flutter_code(student_code_path):
    analyze_returncode, analyze_stdout, analyze_stderr = run_dart_analyze(student_code_path)

    # Mengembalikan hasil penilaian
    return {
        'analyze_returncode': analyze_returncode,
        'analyze_stdout': analyze_stdout,
        'analyze_stderr': analyze_stderr,
    }

def main():
    # Lokasi file kode Flutter siswa
    student_code_path = 'app/Http/Controllers/student_code.dart'

    # Menilai kode Flutter siswa
    evaluation_result = evaluate_flutter_code(student_code_path)

    # Menampilkan hasil penilaian
    print("Dart Analyze Return Code:", evaluation_result['analyze_returncode'])
    print("Dart Analyze Output:")
    print(evaluation_result['analyze_stdout'])
    print("Dart Analyze Error:")
    print(evaluation_result['analyze_stderr'])

if __name__ == '__main__':
    main()
