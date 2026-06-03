# ---------------------------------------------------------
# IntelScope OSINT Telegram Bot
# Developed by: VarshuAi (Owner & Developer)
# Source Code Credit: VarshuAi (https://github.com/VarshuAi)
# Licensed under MIT License
# ---------------------------------------------------------

import requests

def get_ip_geo(ip):
    # Free geolocation and ASN API
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    try:
        resp = requests.get(url, timeout=4)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == "success":
                return data
    except Exception:
        pass
    return None

def get_ip_threat(ip):
    # Check threat indicators on AlienVault Open Threat Exchange (OTX)
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            pulse_info = data.get("pulse_info", {})
            pulses = pulse_info.get("pulses", [])
            threat_score = len(pulses)
            
            summary = {
                "threat_score": threat_score,
                "reputation": "Suspicious / Malicious" if threat_score > 0 else "Clean / Good",
                "references": [p.get("name", "Unknown Pulse") for p in pulses[:5]]
            }
            return summary
    except Exception:
        pass
    return {
        "threat_score": 0,
        "reputation": "Unknown (Threat API Limit/Timeout)",
        "references": []
    }
