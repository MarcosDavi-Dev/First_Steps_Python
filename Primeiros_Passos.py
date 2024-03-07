{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWuI8/q4jt0eINAiUvxUIe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MarcosDaviDev/Primeiros-Passos/blob/main/Primeiros_Passos.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Aula Visão Geral da Linguagem Python**\n",
        "\n",
        "**Descomplica**"
      ],
      "metadata": {
        "id": "YF1DiZJdfUrA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# exemplo 1\n",
        "# entrada\n",
        "nome = input('Digite o seu nome: ')\n",
        "idade = int(input('Digite a sua idade: '))\n",
        "# saída\n",
        "print('Nome: ', nome)\n",
        "print('Idade', idade)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7jp3Kwc9ffTO",
        "outputId": "d452a5d8-0940-48b4-905f-d504d2171ec6"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome: Davi\n",
            "Digite a sua idade: 20\n",
            "Nome:  Davi\n",
            "Idade 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Solução prática 1**\n",
        "\n",
        "Programa que recebe nome, data de nascimento, endereço, peso e altura. Após exibe, nome, idade atual, endereço e IMC."
      ],
      "metadata": {
        "id": "9VZ2AJGthH2u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime\n",
        "\n",
        "def calcular_idade(data_nascimento):\n",
        "    hoje = datetime.now()\n",
        "    data_nascimento = datetime.strptime(data_nascimento, \"%Y-%m-%d\")\n",
        "    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))\n",
        "    return idade\n",
        "\n",
        "def calcular_imc(peso, altura):\n",
        "    altura_metros = altura / 100.0\n",
        "    imc = peso / (altura_metros ** 2)\n",
        "    return imc\n",
        "\n",
        "# Função principal\n",
        "def main():\n",
        "    # Solicitar informações ao usuário\n",
        "    nome = input(\"Digite seu nome: \")\n",
        "    data_nascimento = input(\"Digite sua data de nascimento (formato YYYY-MM-DD): \")\n",
        "    endereco = input(\"Digite seu endereço: \")\n",
        "    peso = float(input(\"Digite seu peso (em kg): \"))\n",
        "    altura = float(input(\"Digite sua altura (em cm): \"))\n",
        "\n",
        "    # Calcular idade\n",
        "    idade = calcular_idade(data_nascimento)\n",
        "\n",
        "    # Calcular IMC\n",
        "    imc = calcular_imc(peso, altura)\n",
        "\n",
        "    # Exibir informações\n",
        "    print(\"\\nInformações Pessoais:\")\n",
        "    print(\"Nome: \", nome)\n",
        "    print(\"Idade: \", idade, \" anos\")\n",
        "    print(\"Endereço: \", endereco)\n",
        "    print(\"IMC (Índice de Massa Corporal): {:.2f}\".format(imc))\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z5GZEyNkhh98",
        "outputId": "c499c9ab-44de-4f31-ff83-f11e5a2cba59"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome: Davi\n",
            "Digite sua data de nascimento (formato YYYY-MM-DD): 2003-03-18\n",
            "Digite seu endereço: Rua Grijalva Costa\n",
            "Digite seu peso (em kg): 82\n",
            "Digite sua altura (em cm): 180\n",
            "\n",
            "Informações Pessoais:\n",
            "Nome:  Davi\n",
            "Idade:  20  anos\n",
            "Endereço:  Rua Grijalva Costa\n",
            "IMC (Índice de Massa Corporal): 25.31\n"
          ]
        }
      ]
    }
  ]
}