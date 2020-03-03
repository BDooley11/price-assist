import requests , bs4, xlsxwriter, xlrd, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#creates and formats final spreadsheet
workbook = xlsxwriter.Workbook('Price Check.xlsx') 
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
formatting = workbook.add_format({'num_format': '#,##0'})
worksheet.write("A1", "Stock No",bold)
worksheet.write("B1", "Reg",bold)
worksheet.write("C1", "Model",bold)
worksheet.write("D1", "Age   ",bold)
worksheet.write("E1", "DD Units",bold)
worksheet.write("F1", "Avg Sell Price",bold)
worksheet.write("G1", "Avg Kms",bold)

#opens stock spreadsheet
loc =r"Used Stock.xlsx"
spreadsheet = xlrd.open_workbook(loc)
sheet = spreadsheet.sheet_by_index(0) 

#activates chromedriver and navigates to Done Deal website
browser = webdriver.Chrome()
browser.get('https://priceassist.donedeal.ie/')

RowCount= sheet.nrows
Row = 1

# while condition makes sure that there's something in the used stock spreadsheet.
while (Row < RowCount):
	Reg = sheet.cell_value(Row, 1) 
	regnumber = browser.find_element_by_id('registration-number-string-id')
	regnumber.send_keys(Reg)
	odometer = browser.find_element_by_id('odometer-string-id')
	odometer.send_keys('')
	buttonpath = '//*[@id="submitRegistrationNumberButton"]'
	button = browser.find_element_by_xpath(buttonpath)
	button.click()
	r = browser.page_source
	soup = bs4.BeautifulSoup(r,'html.parser')
	data = soup.find("span", id="tot-selected").text

	# try to select dealer and live, if no units satisfy this then will go the except as no dealer units for sale.
	try:
		select = Select(browser.find_element_by_id('dealerSelector'))
		select.select_by_visible_text("Dealer")
		select1 = Select(browser.find_element_by_id('statusSelector'))
		select1.select_by_visible_text("Live")
		r1 = browser.page_source
		soup1 = bs4.BeautifulSoup(r1,'html.parser')
		stockNo = sheet.cell_value(Row, 0)
		regno = sheet.cell_value(Row, 1)
		model = sheet.cell_value(Row, 2)
		age = sheet.cell_value(Row, 5)
		totalSelected = int(data)
		avgPriceFind = soup1.find("span", id="priceAverage").text
		avgPriceFormat = avgPriceFind.replace(',','')
		avgPrice = int(avgPriceFormat.replace('€',''))
		avgMileFind = soup1.find("span", id="milAverage").text 
		avgMileFormat =(avgMileFind.replace(' km','')) 
		avgMile = int(avgMileFormat.replace(',',''))  
		worksheet.write(Row, 0, stockNo)
		worksheet.write(Row, 1, regno)
		worksheet.write(Row, 2, model)
		worksheet.write(Row, 3, age)
		worksheet.write(Row, 4, totalSelected)
		worksheet.write(Row, 5, avgPrice,formatting)
		worksheet.write(Row, 6, avgMile,formatting)
		Row += 1
		time.sleep(5)
		browser.get('https://priceassist.donedeal.ie/')

	# if there are no similar dealer units for sale the except activated which just prints original stock details to spreadsheet.
	except:
		stockNo = sheet.cell_value(Row, 0)
		regno = sheet.cell_value(Row, 1)
		model = sheet.cell_value(Row, 2)
		age = sheet.cell_value(Row, 5)
		worksheet.write(Row, 0, stockNo)
		worksheet.write(Row, 1, regno)
		worksheet.write(Row, 2, model)
		worksheet.write(Row, 3, age)
		Row += 1
		time.sleep(5)
		browser.get('https://priceassist.donedeal.ie/')

workbook.close()










