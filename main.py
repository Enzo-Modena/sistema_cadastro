# main.py
import streamlit as st
import pandas as pd
import Controllers.FuncionarioController as funcionarioController
from Models.Freelancer import Freelancer
from Models.Vendedor import Vendedor


# Interface principal
st.title('Sistema de Cadastro de Funcionários')
tipo_funcionario = st.selectbox("Selecione o tipo de funcionário", ["Freelancer", "Vendedor"])


if tipo_funcionario == "Freelancer":
    codigo = st.number_input("Digite um código: ", min_value=0)
    nome = st.text_input("Digite um nome: ")
    diasTrabalhados = st.number_input("Digite os dias trabalhados: ", min_value=0)
    valordia = st.number_input("Digite o valor do dia: ", min_value=0)


elif tipo_funcionario == "Vendedor":
    codigo = st.number_input("Digite um código: ", min_value=0)
    nome = st.text_input("Digite um nome: ")
    salariobase = st.number_input("Digite o salário base: ", min_value=0)
    comissao = st.number_input("Digite a comissão: ", min_value=0)


if st.button("Inserir funcionário"):
    if tipo_funcionario == "Freelancer":
        funcionario = Freelancer(codigo, nome, diasTrabalhados, valordia)
    elif tipo_funcionario == "Vendedor":
        funcionario = Vendedor(codigo, nome, salariobase, comissao)
   
    funcionarioController.incluirFuncionario(funcionario)
    st.success("Funcionário adicionado com sucesso")


if st.button("Consultar funcionários"):
    dados = funcionarioController.consultarFuncionario()
    if dados:
        df = pd.DataFrame(dados, columns=["Código", "Nome", "Tipo", "Dias Trabalhados",
                                        "Valor do dia", "Salario Base", "Comissão",
                                        "Salário Calculado"])
        st.header("Lista de Funcionários")
        st.table(df)
    else:
        st.info("Nenhum funcionário cadastrado!")

