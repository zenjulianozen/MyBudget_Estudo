import pandas as pd
import os

if("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())

else:
    data_structure = {
        "Valor": [],
        "Efetuado": [],
        "Fixo": [],
        "Data": [],
        "Categoria": [],
        "Descrição": []
    }

    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv")
    df_despesas.to_csv("df_despesas.csv")


if("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0, parse_dates=True)
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0, parse_dates=True)
    cat_despesa = df_cat_despesa["Categoria"].tolist()
    cat_receita = df_cat_receita["Categoria"].tolist()

else:
    cat_receita = {
        "Categoria": ["Salario", "13º", "Dividendos", "Investimentos"]
    }
    cat_despesa = {
        "Categoria": ["Alimentação", "Aluguel", "Água", "Eletricidade", "Saúde", "Lazer", "Transporte", "Compras Cartão", "Empréstimos", "Doações"]
    }

    df_cat_despesa = pd.DataFrame(cat_despesa)
    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")

    cat_receita = df_cat_receita["Categoria"].tolist()
    cat_despesa = df_cat_despesa["Categoria"].tolist()