import json


def par_file_reader(file=None):
    if not file:
        file = "./parameters/par1.json"
    with open(file) as f:
        parameters = json.load(f)
    return parameters


if __name__ == '__main__':
    pars = par_file_reader("par1.json")
    print("Parameters:")
    mx_key = len(max(pars.keys(), key=len))
    for k, v in pars.items():
        print(f" {k:>{mx_key}} : {v}")
