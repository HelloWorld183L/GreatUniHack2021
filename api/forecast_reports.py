forecast = {
	"low": {
		"report _type": "forecast",
		"radiation_label": "low",
		"min_value": 0,
		"max_value": 12,
		"description": "Little to no Radiation",
		"advice": "Expect to enjoy the outdoors without a worry!"
	},
	"average": {
		"report _type": "forecast",
		"radiation_label": "average",
		"min_value": 12,
		"max_value": 25,
		"description": "Average Background Radiation, Not dangerous.",
		"advice": "Expect an average amount of radiation. Nothing dangeorus."
	},
	"slightly_above_average": {
		"report _type": "forecast",
		"radiation_label": "slightly_above_average",
		"min_value": 25,
		"max_value": 50,
		"description": "Short Radiation Peak Detected",
		"advice": "Expect a short radiation spike. If it lasts longer or is stronger, it might be dangerous. Occasional behaviour is normal"
	},
	"above_average": {
		"report _type": "forecast",
		"radiation_label": "above_average",
		"min_value": 50,
		"max_value": 60,
		"description": "Moderate Radiation Peak Detected",
		"advice": "Expect a moderate radiation spike. Larger peaks of longer duration indicate detection of a hotspot, or a cloud of radiation passing through."
	},
	"high": {
		"report _type": "current",
		"radiation_label": "high",
		"min_value": 60,
		"max_value": 100,
		"description": "High Radiation Peak Detected",
		"advice": "Expect a large radiation spike. Your area may be a radiation hotspot or there might be a radiation cloud passing by. Be very cautious."
	},
	"very_high": {
		"report _type": "current",
		"radiation_label": "very_high",
		"min_value": 100,
		"max_value": 150,
		"description": "Radiation levels Very Dangerous",
		"advice": "Your area is expected to have very high and dangerous radiation levels. Find shelter or leave immediately."
	},
	"extremely_high": {
		"report _type": "current",
		"radiation_label": "extremely_high",
		"min_value": 150,
		"max_value": 500,
		"description": "Radiation levels Extremely Dangerous",
		"advice": "Your area is expected to have extremely high and dangerous radiation levels. Find shelter or leave immediately."
	},
	"disaster": {
		"report _type": "current",
		"radiation_label": "disaster",
		"min_value": 500,
		"max_value": 50000,
		"description": "Nuclear Disaster",
		"advice": "Your area is expected to have radiation levels of a Nuclear Disaster. Seek shelter or leave immediately. Please check disaster safety instructions in your area to keep yourself safe."
	}
}