import os
import requests
import json
from bs4 import BeautifulSoup

ids = "7615339"  #  ID desejados sem o PMC
bd_request = "pmc" #Substitua pelo banco desejado: pubmed / pmc
return_format = "json" # Substitua pelo formato desejado: json / html (apenas para citation)
structured_results = "ris"  # citation
                            # csl
                            # ris
                            # medline

url = f"https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/{bd_request}/"
params = {
    "id": ids,
    "format": structured_results,
    "contenttype": return_format
}
response = requests.get(url, params=params)

results_dir = os.path.join(os.getcwd(), "results")
os.makedirs(results_dir, exist_ok=True)
if structured_results == "ris":
    with open(f"{os.getcwd()}/results/api_LCE(result_{structured_results}).ris", "w", encoding="utf-8") as file:
        file.write(response.text)
elif structured_results == "medline":
    with open(f"{os.getcwd()}/results/api_LCE(result_{structured_results}).nbib", "w", encoding="utf-8") as file:
        file.write(response.text)# Salva RIS com os dados dos artigos
else:
    if return_format == "json" or return_format == "csl":
        with open(f"{os.getcwd()}/results/api_LCE(result_{structured_results}).json", "w", encoding="utf-8") as file:
            file.write(json.dumps(response.json(), indent=4))  # Salva JSON com os dados dos artigos
    else:
        with open(f"{os.getcwd()}/results/api_LCE(result_{structured_results}).html", "w", encoding="utf-8") as file:
            file.write(BeautifulSoup(response.text, "html.parser").prettify())  # Salva HTML com os dados dos artigos