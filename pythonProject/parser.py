from json import loads


def process(name) -> str:
    with open(name) as f:
        data = f.read()
        return loads(data)
def printout(data, title):
    print("# " + title)
    print("### TTPs")
    for list_index in range(len(data["procedures"])):
        for key,value in data["procedures"][list_index].items():
            if key in ["Utility"]:
                continue
            elif key in ["tactic"]:
                if value == "c2": value = "Command and Control"
                try:
                    print(f"- Tactic: {value}, Technique: {data["procedures"][list_index]["technique"]}")
                except IndexError:
                    continue
            else:
                continue
def get_iocs(data):
    if not data.get("iocs", False): return False
    print("### IOCs")
    for iocType, iocValues in data["iocs"].items():
        iocs = ", ".join(iocValues) #iocValues.replace(",", " ").replace("[", "").replace("]", "")
        print(f"- {iocType}: {iocs}")




data = process("scenarios_test")
printout(data, "Lazarus")
get_iocs(data)
