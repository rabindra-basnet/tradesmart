# Copyright (c) 2025, rabindra and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CIFIDTF(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		account_number: DF.Data | None
		address: DF.Data | None
		amended_from: DF.Link | None
		beneficiary_name: DF.Data
		channel: DF.Data | None
		cif_id: DF.Data
		city: DF.Data | None
		country: DF.Literal["Nepal", "India", "Bangladesh"]
		date_of_issue: DF.Data | None
		email1: DF.Data | None
		email: DF.Data | None
		first_name: DF.Data
		last_name: DF.Data
		mobile_code: DF.Data | None
		pan_no: DF.Data | None
		phone: DF.Data | None
		phone_number: DF.Data
		postal_code1: DF.Data | None
		postal_code: DF.Data | None
		province: DF.Literal[None]
		street: DF.Data | None
	# end: auto-generated types
	pass
