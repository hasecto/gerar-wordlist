# AD Name Wordlist Generator 🛡️

Este é um script em Python 3 desenvolvido para auxiliar profissionais de **Red Team** e **Pentest** na criação de wordlists personalizadas durante auditorias de **Active Directory**. 

O script transforma uma lista de nomes e sobrenomes em diversos formatos comuns de login e senhas utilizados em ambientes corporativos.

## 🚀 Funcionalidades

- **Múltiplos Formatos:** Gera padrões como `nome.sobrenome`, `nsobrenome`, `sobrenome.n`, entre outros.
- **Variações de Case:** Cria entradas em minúsculas e com a primeira letra maiúscula (Capitalize).
- **Sufixos Comuns:** Adiciona terminações frequentes como `123`, `@123`, `2024`, etc.
- **Saída Limpa:** Remove duplicatas automaticamente e ordena o arquivo final.

## 🛠️ Como usar

### Pré-requisitos
- Python 3.x instalado.

### Gerar Arquivo

1. Prepare seu arquivo de entrada (ex: `nomes.txt`):
   ```text
   Joao Silva
   Maria Oliveira
   ```

### Execução
O script utiliza argumentos de linha de comando para facilitar a automação:

```bash
python3 gerar_wordlist.py -l nomes.txt -o minha_wordlist.txt
```

**Argumentos:**
- `-l` ou `--lista`: Caminho para o arquivo `.txt` contendo a lista de nomes (obrigatório).
- `-o` ou `--output`: Nome do arquivo de saída (opcional, padrão: `wordlist_ad.txt`).

## 📁 Exemplo de Saída
Para o nome `Joao Silva`, o script gerará:
- joao.silva
- Joao.Silva
- jsilva
- JSilva123
- joao_silva2024
- (e muitos outros...)


## ⚠️ Aviso Legal
Este script foi criado apenas para fins educacionais e testes de segurança autorizados. O uso indevido desta ferramenta para atacar alvos sem permissão prévia é ilegal.

