cd ~/SynologyDrive/Programming/Stemlab && cat > toggle_air_compressor.py <<'EOF'
import os, requests
from dotenv import load_dotenv

load_dotenv()
HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")
ENTITY = "switch.air_compressor"

H = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

state = requests.get(
    f"{HA_URL}/api/states/{ENTITY}",
    headers=H,
    timeout=5
).json()["state"]

service = "turn_off" if state == "on" else "turn_on"

requests.post(
    f"{HA_URL}/api/services/switch/{service}",
    json={"entity_id": ENTITY},
    headers=H,
    timeout=5
)

print(f"🔘 Air Compressor -> {service.replace('turn_','').upper()}")
EOF
