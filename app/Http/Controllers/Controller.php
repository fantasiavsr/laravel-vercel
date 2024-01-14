<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Symfony\Component\Process\Process;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;

    public function test()
    {

        return view('test', [
            'title' => "test",
        ]);
    }

    public function executePythonScript()
    {
        $pythonScriptPath = 'python/code2.py';
        $command = 'python ' . $pythonScriptPath;

        // Eksekusi skrip Python menggunakan exec
        exec($command . ' 2>&1', $output, $returnCode);

        // $output berisi hasil eksekusi (output skrip Python)
        // $returnCode berisi kode keluaran dari skrip Python

        // Mengonsumsi output sebagai JSON
        $jsonOutput = implode("\n", $output);
        $outputData = json_decode($jsonOutput, true);

        // Memeriksa apakah penguraian JSON berhasil
        if (json_last_error() !== JSON_ERROR_NONE) {
            return response()->json([
                'error' => 'Error decoding JSON: ' . json_last_error_msg(),
                'output' => $jsonOutput,
                'return_code' => $returnCode,
            ]);
        }

        return response()->json([
            'output' => $outputData,
            'return_code' => $returnCode,
        ]);


    }
}
