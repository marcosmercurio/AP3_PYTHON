import random


def sortWords():
    words = [
        ["LASANHA", "COMIDA"],
        ["PATO", "ANIMAL"],
        ["OVELHA", "ANIMAL"],
        ["GALO", "ANIMAL"],
        ["UVA", "FRUTA"],
        ["SORVETE", "DOCE"],
        ["HAMSTER", "ANIMAL"],
        ["COBRA", "ANIMAL"],
        ["TIGRE", "ANIMAL"],
        ["ELEFANTE", "ANIMAL"],
        ["AVESTRUZ", "ANIMAL"],
        ["ELEFANTE", "ANIMAL"],
        ["CARANGUEJO", "ANIMAL"],
        ["LEBRE", "ANIMAL"],
        ["GANSO", "ANIMAL"],
        ["GAFANHOTO", "ANIMAL"],
        ["CROCODILO", "ANIMAL"],
        ["MINHOCA", "ANIMAL"],
        ["CABRA", "ANIMAL"],
        ["POMBA", "ANIMAL"],
        ["CARACOL", "ANIMAL"],
        ["COBAIA", "ANIMAL"],
        ["BOI", "ANIMAL"],

        ["VERMELHO", "CORES"],
        ["PRETO", "CORES"],
        ["CINZA", "CORES"],
        ["AMARELO", "CORES"],
        ["BRANCO", "CORES"],
        ["ROXO", "CORES"],
        ["LARANJA", "CORES"],
        ["CASTANHO", "CORES"],
        ["VERDE", "CORES"],

        ["ESPINHA", "CORPO HUMANO"],
        ["DEDO", "CORPO HUMANO"],
        ["CABELO", "CORPO HUMANO"],
        ["PERNA", "CORPO HUMANO"],
        ["CINTURA", "CORPO HUMANO"],
        ["BOCA", "CORPO HUMANO"],
        ["BIGODE", "CORPO HUMANO"],
        ["SANGUE", "CORPO HUMANO"],

        ["ENFERMEIRA", "PROFISSÃO"],
        ["PILOTO", "PROFISSÃO"],
        ["TAXISTA", "PROFISSÃO"],
        ["BOMBEIRO", "PROFISSÃO"],
        ["DENTISTA", "PROFISSÃO"],
        ["ENGENHEIRO", "PROFISSÃO"],
        ["PROFESSOR", "PROFISSÃO"],
        ["ATOR", "PROFISSÃO"],
        ["MOTORISTA", "PROFISSÃO"],

        ["PARAPENTE", "TRANSPORTE"],
        ["FERROVIA", "TRANSPORTE"],
        ["PLANADOR", "TRANSPORTE"],
        ["CAIAQUE", "TRANSPORTE"],
        ["TRICICLO", "TRANSPORTE"],
        ["SUBMARINO", "TRANSPORTE"],
    ]

    selected_option = random.choice(words)
    print(selected_option)
    return selected_option
