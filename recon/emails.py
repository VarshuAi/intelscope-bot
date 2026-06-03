# ---------------------------------------------------------
# IntelScope OSINT Telegram Bot
# Developed by: VarshuAi (Owner & Developer)
# Source Code Credit: VarshuAi (https://github.com/VarshuAi)
# Licensed under MIT License
# ---------------------------------------------------------

import smtplib
import socket
import dns.resolver

def verify_email(email):
    # Parse domain
    try:
        _, domain = email.split('@')
    except ValueError:
        return {"status": "Invalid Format", "mx_records": [], "smtp_status": "Failed"}
        
    # 1. Fetch MX Records
    mx_hosts = []
    try:
        answers = dns.resolver.resolve(domain, 'MX', lifetime=3)
        for rdata in answers:
            mx_hosts.append((rdata.preference, str(rdata.exchange).rstrip('.')))
        mx_hosts.sort()  # Sort by preference (lowest preference = highest priority)
    except Exception:
        return {"status": "No MX Records Found", "mx_records": [], "smtp_status": "Failed"}
        
    if not mx_hosts:
        return {"status": "No MX Records Found", "mx_records": [], "smtp_status": "Failed"}
        
    # 2. Query lowest-preference mail server with HELO/RCPT TO
    target_mx = mx_hosts[0][1]
    smtp_status = "Unknown"
    
    try:
        # Establish connection with increased timeout
        server = smtplib.SMTP(timeout=10)
        server.connect(target_mx, 25)
        server.helo("osint.intelscope.local")
        
        # Sender address (use dummy/generic)
        server.mail("audit@intelscope.local")
        
        # Handshake verification (RCPT TO)
        code, message = server.rcpt(email)
        server.quit()
        
        # SMTP code 250 means Mail Action completed successfully / User exists
        if code == 250:
            smtp_status = "Active Account (SMTP 250)"
        elif code == 550:
            smtp_status = "User Not Found (SMTP 550)"
        else:
            smtp_status = f"SMTP Code {code} - {message.decode('utf-8', errors='ignore')}"
            
    except socket.timeout:
        smtp_status = "Timeout (Port 25 likely blocked by ISP)"
    except Exception as e:
        smtp_status = f"Handshake Aborted: {str(e)}"
        
    return {
        "status": "Verified" if "Active" in smtp_status else "Unverified",
        "mx_records": [host[1] for host in mx_hosts[:3]],
        "smtp_status": smtp_status
    }
