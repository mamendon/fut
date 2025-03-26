# FHIRUT - Conjunto de Testes Unitários FHIR

**FHIRUT**  é uma ferramenta desenvolvida para automatizar testes de validação de recursos FHIR, com o objetivo de simplificar e agilizar o processo de verificação de conformidade com o padrão HL7 FHIR.

## 💡 Objetivo

Automatizar a execução do validador FHIR oficial (`validator_cli.jar`) para múltiplos recursos FHIR, comparando os resultados com as expectativas definidas pelo usuário.

## 🧩 Componentes

- **Casos de Teste**: cada caso define um recurso FHIR a ser validado (`input.json`) e o resultado esperado (`expected.json`).
- **Conjuntos de Testes (Suites)**: agrupamentos de casos relacionados.
- **Test Runner**: executa os testes usando o `validator_cli.jar`.
- **Comparador de Resultados**: verifica se o resultado gerado está de acordo com o esperado.
- **Gerador de Relatórios**: gera relatórios claros e organizados com os resultados de todos os testes executados.
- **Interface Gráfica (opcional)**: permite que o usuário interaja com a ferramenta de forma visual.

## ▶️ Exemplo de uso do validador

## 🚧 Estrutura de Diretórios

fhirut/
├── tests/                  # Casos e conjuntos de testes
│   └── suite1/
│       ├── test1.json
│       ├── test1_expected.json
├── core/                   # Código principal da ferramenta
│   ├── test_case.py
│   ├── test_runner.py
│   ├── result_comparator.py
│   ├── report_generator.py
│   └── config.py
├── gui/                    # Interface gráfica
├── main.py                 # Ponto de entrada principal
└── README.md               # Este arquivo
🔧 Requisitos
Python 3.7+

Java 8 ou superior

validator_cli.jar 

📌 Status
🚧 Em desenvolvimento para a disciplina de Construção de Software.