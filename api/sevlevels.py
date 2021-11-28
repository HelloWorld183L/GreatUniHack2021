levels = {
    'low': {
        'radiation_label': 'low',
        'min_value': 0,
        'max_value': 12,
        'description': 'Little to no radiation',
        'advice': 'Enjoy the outdoors without a worry!'
    },
    "average": {
        "radiation_label": "average",
        "min_value": 12,
        "max_value": 25,
        "description": "Average Background Radiation, Not dangerous.",
        "advice": "Nothing to worry about."
    },
    "slightly_above_average": {
        "radiation_label": "slightly_above_average",
        "min_value": 25,
        "max_value": 50,
        "description": "Short Radiation Peak Detected",
        "advice": "It is normal to occasionally get short duration peaks above normal background for any location."
    },
    "above_average": {
        "radiation_label": "above_average",
        "min_value": 50,
        "max_value": 60,
        "description": "Moderate Radiation Peak Detected",
        "advice": "Larger peaks of longer duration indicate detection of a hotspot, or a cloud of radiation passing through."
    },
    "high": {
        "radiation_label": "high",
        "min_value": 60,
        "max_value": 100,
        "description": "High Radiation Peak Detected",
        "advice": "Larger peaks of longer duration indicate detection of a hotspot, or a cloud of radiation passing through. Check local news and try and find a safer place."
    },
    "very_high": {
        "radiation_label": "very_high",
        "min_value": 100,
        "max_value": 150,
        "description": "Radiation levels Very Dangerous",
        "advice": "Detections of 1.0 uSv/hr are very dangeorus. Find shelter or leave immediately."
    },
    "extremely_high": {
        "radiation_label": "extremely_high",
        "min_value": 150,
        "max_value": 500,
        "description": "Radiation levels Extremely Dangerous",
        "advice": "Extremely dangeorus radiation. Find shelter or leave immediately."
    },
    "disaster": {
        "radiation_label": "disaster",
        "min_value": 500,
        "max_value": 50000,
        "description": "Nuclear Disaster",
        "advice": "Nuclear Disaster detected. There might be bad news for you. Please check disaster safety instructions in your area to keep yourself safe."
    }
}