import pickle from tabulate import tabulate import pdfkit

if __name__ == "__main__":
	#get date of file to be printed
	dateFile = "31_04_2021.p"
	persons = pickle.load(open(dateFile, 'rb'))

	table = []
	for person in persons:
		table.append(person.getList())
	headers = ["Vorname", "Nachname", "GebDatum", "TelefonNr", "Straße", "HausNr", "PLZ", "Ort"]
	tableHTML = str(tabulate(table, headers, tablefmt="html"))

	# css
	css = "<style>table {border-spacing: 15px 10px;border-collapse: separate;}th {font-size: 20px;line-height: 1.5;}tr {background-color: antiquewhite;}</style>"
	tableHTML = tableHTML + css

	# TODO: only testing
	f = open('tableHTML.html', 'w')
	f.write(tableHTML)
	f.close()

	#write to pdf
	pdfkit.from_string(tableHTML, 'out.pdf')
