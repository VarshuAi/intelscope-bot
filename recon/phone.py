import re
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    PHONENUMBERS_AVAILABLE = True
except ImportError:
    PHONENUMBERS_AVAILABLE = False

def lookup_phone(phone_string):
    """
    Performs OSINT parsing on a phone number.
    Extracts carrier, location, timezone, and formatting information.
    """
    if not PHONENUMBERS_AVAILABLE:
        return {
            "status": "error",
            "message": "The 'phonenumbers' package is missing. Run `pip install phonenumbers` to enable this."
        }
        
    try:
        # Clean inputs: keep only +, digits
        cleaned = re.sub(r'[^\d+]', '', phone_string)
        if not cleaned.startswith('+'):
            # Assume international prefix is missing, notify user
            return {
                "status": "error",
                "message": "Please include the country code prefix (e.g., +919876543210)"
            }
            
        parsed_num = phonenumbers.parse(cleaned)
        
        if not phonenumbers.is_valid_number(parsed_num):
            return {
                "status": "error",
                "message": "Provided number is invalid according to ITU-T standards."
            }
            
        # Get details
        number_carrier = carrier.name_for_number(parsed_num, "en") or "Unknown Carrier"
        number_location = geocoder.description_for_number(parsed_num, "en") or "Unknown Location"
        number_timezones = ", ".join(timezone.time_zones_for_number(parsed_num)) or "Unknown Timezone"
        country_code = parsed_num.country_code
        
        # Determine country name
        region = phonenumbers.region_code_for_number(parsed_num)
        
        return {
            "status": "success",
            "number": cleaned,
            "intl_format": phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "carrier": number_carrier,
            "location": number_location,
            "timezones": number_timezones,
            "region": region,
            "valid": True
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Parsing failed: {str(e)}"
        }
