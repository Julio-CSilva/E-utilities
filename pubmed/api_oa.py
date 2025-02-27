import requests
import os
from lxml import etree

url = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi"
params = {"id": "PMC9062866"}  # Substitua pelo PMC ID desejado

#requisição
response = requests.get(url, params=params)

#tratemento do XML
parser = etree.XMLParser(remove_blank_text=True)
root = etree.fromstring(response.text.encode("utf-8"), parser)
pretty_xml = etree.tostring(root, pretty_print=True, encoding="utf-8").decode()

results_dir = os.path.join(os.getcwd(), "results")
os.makedirs(results_dir, exist_ok=True)
with open(f"{os.getcwd()}/results/api_oa(result_{params["id"]}).xml", "w", encoding="utf-8") as file:
    file.write(pretty_xml)  # Salva XML com os dados do artigo
