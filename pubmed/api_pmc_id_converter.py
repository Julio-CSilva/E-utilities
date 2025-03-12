import os
import requests
import json
import csv
from lxml import etree

ids = "33024307"  # PMC ID desejados (Até 200 ID's separados por vírgula)
type_id = "pmid"  # Substitua pelo tipo de busca: pmcid / pmid / mid / doi
return_format = "html" # Substitua pelo formato desejado: xml / html / json / csv
versions_articles = "no"  # Substitua por "yes" para retornar todas as versões dos artigos
email_maintenance = ""  # Substitua pelo seu e-mail


url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
params = {
    "ids": ids,
    "idtype": type_id,
    "format": return_format,
    "versions": versions_articles,
    "showaiid": "no",
    "tool": "api_pmc_id_converter.py",
    "email": email_maintenance 
}
response = requests.get(url, params=params)

results_dir = os.path.join(os.getcwd(), "results")
os.makedirs(results_dir, exist_ok=True)
if return_format == "json":
    with open(f"{os.getcwd()}/results/api_pmc_id_converter(result_{ids}).json", "w", encoding="utf-8") as file:
        file.write(json.dumps(response.json(), indent=4))  # Salva JSON com os dados dos artigos
elif return_format == "xml":
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.fromstring(response.text.encode("utf-8"), parser)
    pretty_xml = etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

    with open(f"{os.getcwd()}/results/api_pmc_id_converter(result_{ids}).xml", "w", encoding="utf-8") as file:
        file.write(pretty_xml)  # Salva XML com os dados do artigo
elif return_format == "html":
    with open(f"{os.getcwd()}/results/api_pmc_id_converter(result_{ids}).html", "w", encoding="utf-8") as file:
        file.write(response.text)
else:
    with open(f"{os.getcwd()}/results/api_pmc_id_converter(result_{ids}).csv", mode="w", newline="", encoding="utf-8") as file:
        file.write(response.text)  # Salva CSV com os dados dos artigos