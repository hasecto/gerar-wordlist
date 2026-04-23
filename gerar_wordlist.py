#!/usr/bin/env python3

import argparse

def gerar_wordlist(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = [l.strip() for l in f.readlines() if l.strip()]
        
        resultados = set()

        for linha in linhas:
            partes = linha.split()
            if len(partes) < 2:
                continue
            
            p_nome = partes[0]
            u_sobrenome = partes[-1]

            # Formatos de nomes (Logins e variações)
            # Ex: joao, silva, Joao, Silva
            formatos_base = [
                (p_nome.lower(), u_sobrenome.lower()),
                (p_nome.capitalize(), u_sobrenome.capitalize())
            ]

            for nome, sobrenome in formatos_base:
                # Estruturas comuns de AD
                estruturas = [
                    f"{nome}.{sobrenome}",     # joao.silva / Joao.Silva
                    f"{nome}{sobrenome}",      # joaosilva / JoaoSilva
                    f"{nome[0]}{sobrenome}",   # jsilva / JSilva
                    f"{nome}{sobrenome[0]}",   # joaos / JoaoS
                    f"{sobrenome}.{nome}",     # silva.joao / Silva.Joao
                ]
                
                for est in estruturas:
                    resultados.add(est)
                    # Adicionando sufixos comuns de senhas fracas
                    resultados.add(f"{est}123")
                    resultados.add(f"{est}@123")
                    resultados.add(f"{est}#123")
                    resultados.add(f"{est}123!")
                    resultados.add(f"{est}2024")
                    resultados.add(f"{est}@2024")
                    resultados.add(f"{est}#2024")
                    resultados.add(f"{est}2024!")

        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for item in sorted(resultados):
                f.write(f"{item}\n")
        
        print(f"[+] Sucesso! Arquivo '{arquivo_saida}' gerado com {len(resultados)} combinações.")

    except FileNotFoundError:
        print(f"[-] Erro: Arquivo '{arquivo_entrada}' não encontrado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de Wordlist focado em AD - Red Team")
    parser.add_argument("-l", "--lista", required=True, help="Lista de nomes (Nome Sobrenome)")
    parser.add_argument("-o", "--output", default="wordlist_ad.txt", help="Saída (padrão: wordlist_ad.txt)")
    
    args = parser.parse_args()
    gerar_wordlist(args.lista, args.output)

