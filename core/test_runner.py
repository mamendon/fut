import subprocess
from pathlib import Path

def run_validator(test_case, validator_path, fhir_version="4.0.1", output_dir="outputs"):
    """
    Executa o validador FHIR usando o validator_cli.jar.

    Parâmetros:
    - test_case: objeto TestCase
    - validator_path: caminho para o arquivo validator_cli.jar
    - fhir_version: versão FHIR usada na validação
    - output_dir: diretório onde o resultado será salvo

    Retorna:
    - Caminho do arquivo de resultado (output.json)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{test_case.name}_result.json"
    command = [
        "java",
        "-jar", str(validator_path),
        "-version", fhir_version,
        "-output", str(output_path),
        str(test_case.input_path)
    ]

    try:
        subprocess.run(command, check=True)
        test_case.result_path = output_path
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o validador para {test_case.name}: {e}")
        return None
