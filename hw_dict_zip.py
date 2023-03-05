from pprint import pprint as pp

companies = ["JetBrains",
             "Microsoft",
             "Google",
             "Nintendo",
             "Kaspersky Lab",
             "Nvidia",
             "AMD"]
products = ["Pycharm IDE",
            "Windows OS",
            "Google web browser",
            "Nintendo Switch",
            "Kaspersky Antivirus",
            "Nvidia GeForce RTX 3060",
            "AMD Ryzen Threadripper"]

all_together = dict(zip(companies, products))

pp(all_together)
