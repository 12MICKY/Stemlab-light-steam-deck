cd ~/SynologyDrive/Programming/Stemlab && cat > toggle_blower_fan.py <<'EOF'
import os, requests
from dotenv import load_dotenv

load_dotenv()
HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")
ENTITY = "fan.workshop_blower_fan"

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
    f"{HA_URL}/api/services/fan/{service}",
    json={"entity_id": ENTITY},
    headers=H,
    timeout=5
)

print(f"🔘 Blower Fan -> {service.replace('turn_','').upper()}")
EOF
