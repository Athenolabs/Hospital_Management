from frappe import _

def get_data():
	return [
		{
			"label": _("Master"),
			"items": [
				{
					"type": "doctype",
					"name": "Specialities",
					"label": _("Specialities"),
					"description": _("Specialities Database"),
					"hide_count": True
				},
				{
					"type": "doctype",
					"name": "Hospital Registration",
					"label": _("Hospital Registration"),
					"description": _("Hospital Registration Database"),
					"hide_count": True
				},
			]
		},
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Patient Allotment",
					"label": _("Patient Recommendation"),
					"description": _("Patient Allotment Database"),
					"hide_count": True
				},
				{
					"type": "page",
					"name": "hospital-search",
					"label": _("Hospital Search and Allocation"),
					"description": _("Hospital Search and Allocation Page"),
					"hide_count": True
				},
				{
					"type": "page",
					"name": "patient-allot-reject",
					"label": _("Patient Allotment and Updation"),
					"description": _("Patient Allotment and Updation Page"),
					"hide_count": True
				},
			]
		},
		{
			"label": _("Reports"),
			"icon": "icon-table",
			"items": [
				{
					"type": "report",
					"name": "Hospital-wise Bed Availability Details",
					"doctype": "Hospital Registration",
					"is_query_report": True,
				},
				{
					"type": "page",
					"name": "occupancy-report",
					"label":_("Hospital Occupancy Report"),
					"description": _("Hospital Occupancy Report Page"),
					"hide_count": True
				},
				{
					"type": "page",
					"name": "dashboard",
					"label": _("Global Dashboard"),
					"description": _("Global Dashboard"),
					"hide_count": True
				},
			]
		},
		{
			"label": _("Tools"),
			"items": [
				{
					"type": "page",
					"name": "data-import-tool",
					"label": _("Patient Data Updation Tool"),
					"description": _("Data Import Tool"),
					"hide_count": True
				},
			]
		}
	]
