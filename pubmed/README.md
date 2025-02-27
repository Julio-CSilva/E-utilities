## Notações Importantes

<br/>

# 📖 PMID / PMCID / DOI

* PMID (PubMed Identifier)
    
      É o identificador de um artigo no PubMed.
      Usado para referenciar apenas o resumo e os metadados do artigo.
      Exemplo: PMID: 12345678
      Não garante acesso ao texto completo.
    
* PMCID (PubMed Central Identifier)

      É o identificador de um artigo no PubMed Central (PMC).
      Indica que o artigo está disponível gratuitamente em texto completo no PMC.
      Exemplo: PMCID: PMC7071504
      Garante acesso ao texto completo se estiver em acesso aberto.

* DOI

      O DOI (Digital Object Identifier) é um identificador único para conteúdos digitais, especialmente artigos científicos, livros e teses. Ele funciona como um "CPF" para publicações acadêmicas, garantindo um link permanente para o conteúdo.

<br/>

# [API OA (Open Access)](https://pmc.ncbi.nlm.nih.gov/tools/oa-service/)
Este script Python realiza uma requisição à API Open Access (OA) do PubMed Central (PMC) para obter metadados de um artigo a partir de seu **PMC ID**. O resultado da consulta é salvo em um arquivo XML formatado.

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python necessárias:
  - `requests`
  - `lxml`

Caso precise instalar as dependências, utilize:
```sh
pip install requests lxml
```

## Uso
1. Substitua o valor do parâmetro `id` na variável `params` pelo **PMC ID** do artigo desejado.
2. Execute o script com o comando:
   ```sh
   python3 script.py
   ```
3. O arquivo XML com os metadados do artigo será salvo no diretório `results/` como `api_oa(result_PMCXXXXXXX).xml`.

<br/>

# [API OAI-PMH](https://pmc.ncbi.nlm.nih.gov/tools/oai/)
Este script Python realiza uma requisição à API OAI-PMH do PubMed Central (PMC) para listar registros de artigos dentro de um intervalo de datas. O resultado da consulta é salvo em um arquivo XML formatado.

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python necessárias:
  - `requests`
  - `lxml`

Caso precise instalar as dependências, utilize:
```sh
pip install requests lxml
```

## Uso
1. O script já está configurado para buscar registros do dia **2024-01-01**. Caso queira alterar o intervalo de datas, modifique os parâmetros `from` e `until` na variável `params`.
2. Execute o script com o comando:
   ```sh
   python3 script.py
   ```
3. O arquivo XML com os registros será salvo no diretório `results/` como `api_oai-pmh(results).xml`.

<br/>

# [API BioC](https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/)
Este script Python realiza uma requisição à API BioC do PubMed Central (PMC) para obter metadados de um artigo no formato JSON ou XML. O resultado da consulta é salvo em um arquivo formatado conforme a escolha do usuário.

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python necessárias:
  - `requests`
  - `json`
  - `lxml` (caso use XML)

Caso precise instalar as dependências, utilize:
```sh
pip install requests lxml
```

## Uso
1. Substitua o valor da variável `pmc_id` pelo **PMC ID** do artigo desejado.
2. Escolha o formato de saída (`json` ou `xml`) alterando a variável `type_arq_return`.
3. Execute o script com o comando:
   ```sh
   python3 script.py
   ```
4. O arquivo com os metadados do artigo será salvo no diretório `results/` como:
   - `api_bioc(result_PMCXXXXXXX).json` (para JSON)
   - `api_bioc(result_PMCXXXXXXX).xml` (para XML)

<br/>

# [API PMC ID Converter](https://pmc.ncbi.nlm.nih.gov/tools/id-converter-api/)
Este script Python utiliza a API de conversão de IDs do PubMed Central (PMC) para converter IDs de artigos para diferentes formatos (JSON, XML ou CSV). O resultado da consulta é salvo em um arquivo formatado conforme a escolha do usuário.

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python necessárias:
  - `requests`
  - `json`
  - `csv`
  - `lxml` (caso use XML)

Caso precise instalar as dependências, utilize:
```sh
pip install requests lxml
```

## Uso
1. Substitua os valores das variáveis conforme necessário:
   - `pmc_ids`: IDs dos artigos a serem convertidos (separados por vírgula).
   - `return_format`: Formato de saída desejado (`xml`, `json` ou `csv`).
   - `versions_articles`: Use "yes" para retornar todas as versões dos artigos ou "no" para apenas a versão principal.
   - `email_maintenance`: Seu e-mail (recomendado para identificação na API).
2. Execute o script com o comando:
   ```sh
   python script.py
   ```
3. O arquivo com os dados convertidos será salvo no diretório `results/` com o nome:
   - `api_pmc_id_converter(result_IDS).json` (para JSON)
   - `api_pmc_id_converter(result_IDS).xml` (para XML)
   - `api_pmc_id_converter(result_IDS).csv` (para CSV)

<br/>

# [API LCE - Literature Citation Exporter](https://api.ncbi.nlm.nih.gov/lit/ctxp/)
Este script Python consulta a API **Literature Citation Exporter (LCE)** do NCBI para recuperar informações formatadas sobre artigos científicos a partir de seus IDs. Ele permite escolher diferentes bancos de dados (PubMed ou PMC) e formatos estruturados de saída.

## Requisitos
Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python necessárias:
  - `requests`
  - `json`
  - `beautifulsoup4` (caso use HTML)

Caso precise instalar as dependências, utilize:
```sh
pip install requests beautifulsoup4
```

## Uso
1. Substitua os valores das variáveis conforme necessário:
   - `ids`: IDs dos artigos desejados (sem o prefixo "PMC" para artigos PMC).
   - `bd_request`: Banco de dados a ser consultado (`pubmed` ou `pmc`).
   - `return_format`: Formato de saída (`json` ou `html` - apenas para `citation`).
   - `structured_results`: Formato estruturado desejado:
     - `citation`
     - `csl`
     - `ris`
     - `medline`
2. Execute o script com o comando:
   ```sh
   python3 script.py
   ```
3. O arquivo com os dados dos artigos será salvo no diretório `results/` com o nome:
   - `api_LCE(result_citation).json` (para JSON)
   - `api_LCE(result_citation).html` (para HTML)
   - `api_LCE(result_ris).ris` (para RIS)
   - `api_LCE(result_medline).nbib` (para MEDLINE)

## Observações
- O script suporta múltiplos IDs separados por vírgula.
- Caso o diretório `results/` não exista, ele será criado automaticamente.
- O formato **HTML** só é suportado para **citation**.


