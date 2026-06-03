# ---------------------------------------------------------
# IntelScope OSINT Telegram Bot
# Developed by: VarshuAi (Owner & Developer)
# Source Code Credit: VarshuAi (https://github.com/VarshuAi)
# Licensed under MIT License
# ---------------------------------------------------------

import dns.resolver
import requests
import json
import re

def resolve_dns(domain):
    records = {}
    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]
    
    for r_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, r_type, lifetime=3)
            records[r_type] = [str(r) for r in answers]
        except Exception:
            records[r_type] = []
            
    return records

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            subdomains = set()
            for entry in data:
                name_value = entry.get("name_value", "")
                # crt.sh returns wildcard entries, clean them
                for sub in name_value.split("\n"):
                    sub = sub.strip().lower()
                    if sub and not sub.startswith("*.") and sub != domain:
                        subdomains.add(sub)
            return sorted(list(subdomains))[:40] # Cap at 40 to avoid massive lists
    except Exception:
        pass
    return []
