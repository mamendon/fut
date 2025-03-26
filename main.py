from core.test_case import TestCase
from core.test_runner import run_validator
from pathlib import Path

def main():
    # Caminhos dos arquivos
    input_path = "tests/suite1/test1.json"
    expected_path = "tests/suite1/test1_expected.json"
    validator_path = "validator_cli.jar"  

    # Criar instância do teste
    test_case = TestCase(name="test1", input_path=input_path, expected_path=expected_path)

    # Rodar o validador
    print(f"Executando o teste: {test_case.name}")
    result_path = run_validator(test_case, validator_path)

    if result_path:
        print(f"Validação concluída. Resultado salvo em: {result_path}")
    else:
        print("Falha na execução do validador.")

if __name__ == "__main__":
    main()
