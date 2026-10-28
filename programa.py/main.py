import csv
import json
import os
from datetime import datetime


def fazer_backup(caminho_arquivo):

  try:
    if os.path.exists(caminho_arquivo):
      timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
      nome_base, extensao = os.path.splitext(caminho_arquivo)
      caminho_backup = f"{nome_base}_backup_{timestamp}{extensao}"

      with open(caminho_arquivo, "r", encoding="utf-8") as orig, open(
          caminho_backup, "w", encoding="utf-8"
      ) as dest:
        dest.write(orig.read())

      print(f"[Backup] Cópia de segurança criada: {caminho_backup}")
  except Exception as e:
    print(f"[Aviso] Não foi possível criar o backup: {e}")


def csv_para_json(caminho_csv, caminho_json):

  try:
    fazer_backup(caminho_json)

    with open(caminho_csv, mode="r", encoding="utf-8") as f_csv:
      leitor = csv.DictReader(f_csv)
      lista_dados = list(leitor)

    with open(caminho_json, mode="w", encoding="utf-8") as f_json:
      json.dump(lista_dados, f_json, ensure_ascii=False, indent=4)

    print("Sucesso: CSV convertido para JSON com segurança!")

  except FileNotFoundError:
    print(f"Erro: O ficheiro '{caminho_csv}' não foi encontrado.")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


def json_para_csv(caminho_json, caminho_csv):

  try:
    fazer_backup(caminho_csv)

    with open(caminho_json, mode="r", encoding="utf-8") as f_json:
      dados = json.load(f_json)

    if not dados:
      print("Aviso: O ficheiro JSON está vazio.")
      return

    cabecalhos = dados[0].keys()

    with open(caminho_csv, mode="w", newline="", encoding="utf-8") as f_csv:
      escritor = csv.DictWriter(f_csv, fieldnames=cabecalhos)
      escritor.writeheader()
      escritor.writerows(dados)

    print("Sucesso: JSON convertido para CSV com segurança!")

  except FileNotFoundError:
    print(f"Erro: O ficheiro '{caminho_json}' não foi encontrado.")
  except json.JSONDecodeError:
    print("Erro: O ficheiro JSON tem uma estrutura inválida.")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
  csv_para_json("dados.csv", "dados.json")
  json_para_csv("dados.json", "dados_convertido.csv")
