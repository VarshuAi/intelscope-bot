import re
import os
import requests

# State code mapping for Indian RTOs
STATE_CODES = {
    "AN": "Andaman and Nicobar Islands",
    "AP": "Andhra Pradesh",
    "AR": "Arunachal Pradesh",
    "AS": "Assam",
    "BR": "Bihar",
    "CH": "Chandigarh",
    "CG": "Chhattisgarh",
    "DD": "Daman and Diu",
    "DN": "Dadra and Nagar Haveli",
    "DL": "Delhi",
    "GA": "Goa",
    "GJ": "Gujarat",
    "HR": "Haryana",
    "HP": "Himachal Pradesh",
    "JK": "Jammu and Kashmir",
    "JH": "Jharkhand",
    "KA": "Karnataka",
    "KL": "Kerala",
    "LA": "Ladakh",
    "LD": "Lakshadweep",
    "MP": "Madhya Pradesh",
    "MH": "Maharashtra",
    "MN": "Manipur",
    "ML": "Meghalaya",
    "MZ": "Mizoram",
    "NL": "Nagaland",
    "OD": "Odisha",
    "PY": "Puducherry",
    "PB": "Punjab",
    "RJ": "Rajasthan",
    "SK": "Sikkim",
    "TN": "Tamil Nadu",
    "TS": "Telangana",
    "TR": "Tripura",
    "UP": "Uttar Pradesh",
    "UA": "Uttarakhand",
    "UK": "Uttarakhand",
    "WB": "West Bengal"
}

def validate_and_clean_plate(plate):
    """
    Cleans up whitespace and validates the basic format of an Indian vehicle plate.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', plate).upper()
    
    # Format pattern: State(2) + RTO(2) + Optional Letters(1-3) + Number(4)
    # Examples: DL3CA1234, MH12AB1234, KA031234
    pattern = r'^([A-Z]{2})([0-9]{2})([A-Z]{0,3})([0-9]{4})$'
    
    match = re.match(pattern, cleaned)
    if match:
        return cleaned, match.groups()
    return None, None

def lookup_vehicle(plate_number):
    """
    Performs vehicle details lookup. If a RapidAPI Key is present, it attempts a real search.
    Otherwise, it parses state/RTO details and generates a mock payload demonstrating how
    masked privacy records are represented in compliant setups.
    """
    cleaned_plate, groups = validate_and_clean_plate(plate_number)
    if not cleaned_plate:
        return {"status": "error", "message": "Invalid Indian plate format. Example: MH12AB1234"}
    
    state_code, rto_code, series, unique_id = groups
    state_name = STATE_CODES.get(state_code, "Unknown State/UT")
    
    # Try loading RapidAPI key if the user wants to configure a real external provider later
    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("RAPIDAPI_HOST", "rto-vehicle-information-verification-india.p.rapidapi.com")
    
    if api_key:
        try:
            url = f"https://{api_host}/api/v1/vehicle/{cleaned_plate}"
            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": api_host
            }
            # Timeout set to 8 seconds to prevent hanging the bot
            response = requests.get(url, headers=headers, timeout=8)
            if response.status_code == 200:
                data = response.json()
                # Apply security masking to owner name if not already masked by the provider
                raw_owner = data.get("owner_name", "UNKNOWN")
                if raw_owner and raw_owner != "UNKNOWN":
                    # Mask all but the first/last characters of names to preserve privacy
                    words = raw_owner.split()
                    masked_words = []
                    for w in words:
                        if len(w) > 2:
                            masked_words.append(f"{w[0]}{'*' * (len(w)-2)}{w[-1]}")
                        else:
                            masked_words.append(f"{w[0]}*")
                    data["owner_name"] = " ".join(masked_words)
                
                data["state"] = state_name
                data["status"] = "success"
                return data
        except Exception as e:
            # Fallback to local parsing on network/API failure
            pass
            
    # Compliant simulation showing localized RTO details and masked identity data
    # (Extracts metadata dynamically from the vehicle plate)
    masked_simulated_name = f"V***S*** G***D"
    
    return {
        "status": "success",
        "simulated": True,
        "registration_number": cleaned_plate,
        "state": state_name,
        "rto_code": f"{state_code}-{rto_code}",
        "owner_name": masked_simulated_name,
        "make_model": "Maruti Suzuki Swift VXI",
        "fuel_type": "PETROL / CNG",
        "vehicle_class": "Motor Car (LMV)",
        "registration_date": "14-Aug-2021",
        "fitness_upto": "13-Aug-2036",
        "insurance_validity": "10-Aug-2026",
        "rto_office": f"{state_name} RTO Office (Code: {rto_code})"
    }
