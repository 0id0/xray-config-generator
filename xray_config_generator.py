import json
import yaml
import os
from datetime import datetime

def load_nodes():
    with open("data/nodes.yaml", "r") as f:
        return yaml.safe_load(f)

def load_template():
    with open("templates/vmess_template.json", "r") as f:
        return json.load(f)

def generate_config(node):
    template = load_template()
    template["outbounds"][0]["settings"]["vnext"][0]["address"] = node["address"]
    template["outbounds"][0]["settings"]["vnext"][0]["port"] = node["port"]
    template["outbounds"][0]["settings"]["vnext"][0]["users"][0]["id"] = node["uuid"]
    return template

def save_config(name, config):
    path = os.path.join("configs", f"{name}.json")
    with open(path, "w") as f:
        json.dump(config, f, indent=2)

def main():
    os.makedirs("configs", exist_ok=True)
    nodes = load_nodes()
    for node in nodes:
        config = generate_config(node)
        save_config(node["name"], config)
        print(f"[{datetime.now()}] Generated: {node['name']}.json")

if __name__ == "__main__":
    main()