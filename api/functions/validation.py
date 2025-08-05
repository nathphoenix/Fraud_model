REQUIRED_TRANSACTION_FIELDS = [
    'transaction_amount',
    'transaction_type',
    'device_type',
    'location',
    'time_of_day',
    'day_of_week',
    'is_foreign_transaction',
    'is_high_risk_country',
    'previous_fraud_flag',
    'risk_score'
]

def validate_transaction_payload(payload):
    """Validate transaction payload against required fields"""
    missing_fields = [field for field in REQUIRED_TRANSACTION_FIELDS if field not in payload]
    
    if missing_fields:
        error_message = {
            "error": "Missing required fields",
            "missing_fields": missing_fields,
            "message": f"The following fields are required: {', '.join(missing_fields)}"
        }
        return error_message, 400
    
    # Additional type validation if needed
    type_checks = {
        'transaction_amount': (int, float),
        'is_foreign_transaction': int,
        'is_high_risk_country': int,
        'previous_fraud_flag': int,
        'risk_score': (int, float),
        'hour': int,
        'is_weekend': int
    }
    
    type_errors = {}
    for field, expected_type in type_checks.items():
        if field in payload and not isinstance(payload[field], expected_type):
            type_errors[field] = f"Expected type {expected_type.__name__}, got {type(payload[field]).__name__}"
    
    if type_errors:
        error_message = {
            "error": "Type validation failed",
            "type_errors": type_errors,
            "message": "Some fields have incorrect data types"
        }
        return error_message, 400
    
    return None  # No errors


# Mapping dictionaries
mappings = {
    'time_of_day': {'evening':4, 'night':1, 'afternoon':3, "morning":2},
    'transaction_type': {'POS':2, 'Online':1, 'ATM':0, 'Transfer':3},
    'device_type': {'Mobile':1, 'POS Terminal':2, 'ATM Machine':0, 'Web': 3},
    'location': {'Lagos':3, 'Port Harcourt':4, 'Ibadan':1, 'Abuja':0, 'Kano':2},
    'day_of_week': {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}
}


# Function to safely map values
def map_value(key, value, mappings):
    """Map a value using the specified mapping dictionary with case-insensitive key matching"""
    mapping = mappings.get(key, {})
    # Convert both keys and input to lowercase for case-insensitive matching
    lower_mapping = {k.lower(): v for k, v in mapping.items()}
    return lower_mapping.get(str(value).lower(), value)  # Return original if not found

# Create new mapped dictionary
def transform(dict_data):
    return {
        key: map_value(key, value, mappings) 
        for key, value in dict_data.items()
    }

# Usage example:
# validation_result = validate_transaction_payload(transaction_data)
# if validation_result:
#     return validation_result