# xray_config_generator.py
import json, uuid

def generate_config():
    config = {
        "server": "example.com",
        "port": 443,
        "uuid": str(uuid.uuid4()),
        "protocol": "vless"
    }
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

generate_config()