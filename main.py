from core.test_case import TestCase
from core.test_runner import run_validator
from pathlib import Path
import shutil

def main():
    # Caminhos
    input_path = "tests/suite1/test1.json"
    expected_path = "tests/suite1/test1_expected.json"
    validator_path = "validator_cli.jar"

    # Criar o teste
    test_case = TestCase(name="test1", input_path=input_path, expected_path=expected_path)

    # Rodar o validador
    print(f"Executando o teste: {test_case.name}")
    result_path = run_validator(test_case, validator_path)

    if result_path:
        print(f"Resultado salvo em: {result_path}")

        # Se o expected ainda não existir, vamos criá-lo com base na primeira saída
        if not Path(expected_path).exists():
            shutil.copy(result_path, expected_path)
            print(f"[INFO] Arquivo esperado criado automaticamente: {expected_path}")
        else:
            print(f"[INFO] Arquivo esperado já existe.")
    else:
        print("Erro ao rodar o validador.")

if __name__ == "__main__":
    main()
