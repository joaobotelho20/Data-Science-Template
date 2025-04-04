#Bibliotecas
import os
import pandas as pd

#Funções
def unir_xlsx_em_df(pasta):
    """
    Lê todos os arquivos .xlsx de uma pasta e os une em um único DataFrame,
    mantendo apenas o cabeçalho do primeiro arquivo.

    Parâmetros:
    - pasta (str): Caminho da pasta com os arquivos .xlsx.

    Retorna:
    - df_final (pd.DataFrame): DataFrame unificado.
    """
    arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(".xlsx")])
    
    if not arquivos:
        print("Nenhum arquivo .xlsx encontrado.")
        return pd.DataFrame()

    lista_dfs = []

    for i, arquivo in enumerate(arquivos):
        caminho_arquivo = os.path.join(pasta, arquivo)

        if i == 0:
            # Primeiro arquivo: lê com cabeçalho
            df = pd.read_excel(caminho_arquivo)
        else:
            # Restante: ignora o cabeçalho
            df = pd.read_excel(caminho_arquivo, header=None, skiprows=1)
            df.columns = lista_dfs[0].columns  # aplica o cabeçalho do primeiro

        lista_dfs.append(df)

    df_final = pd.concat(lista_dfs, ignore_index=True)
    return df_final