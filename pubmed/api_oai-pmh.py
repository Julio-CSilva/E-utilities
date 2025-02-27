import requests
import os
from lxml import etree

url = "https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi"
params = {
    "verb": "ListRecords",
    "metadataPrefix": "pmc",
    "from": "2024-01-01", # Artigos publicados a partir de 2024
    "until": "2024-01-01",	# Artigos publicados até 2024
}

#requisição
response = requests.get(url, params=params)

#tratemento do XML
parser = etree.XMLParser(remove_blank_text=True)
root = etree.fromstring(response.text.encode("utf-8"), parser)
pretty_xml = etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

results_dir = os.path.join(os.getcwd(), "results")
os.makedirs(results_dir, exist_ok=True)
with open(f"{os.getcwd()}/results/api_oai-pmh(results).xml", "w", encoding="utf-8") as file:
    file.write(pretty_xml)  # Salva XML com os dados do artigo
