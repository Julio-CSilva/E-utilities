import os
import requests
import json
from lxml import etree

pmc_id = "PMC7615339"  # Substitua pelo PMC ID desejado
type_arq_return = "json" # Substitua pelo formato desejado: xml ou json

url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_{type_arq_return}/{pmc_id}/unicode"
response = requests.get(url)

results_dir = os.path.join(os.getcwd(), "results")
os.makedirs(results_dir, exist_ok=True)
if type_arq_return == "json":
    with open(f"{os.getcwd()}/results/api_bioc(result_{pmc_id}).json", "w", encoding="utf-8") as file:
        file.write(json.dumps(response.json(), indent=4))  # Salva JSON com os dados dos artigos
else:
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.fromstring(response.text.encode("utf-8"), parser)
    pretty_xml = etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

    with open(f"{os.getcwd()}/results/api_bioc(result_{pmc_id}).xml", "w", encoding="utf-8") as file:
        file.write(pretty_xml)  # Salva XML com os dados do artigo