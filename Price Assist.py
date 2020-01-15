import requests , bs4, xlsxwriter, xlrd, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

workbook = xlsxwriter.Workbook('Wexford Price Check.xlsx') 
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

loc =r"C:\Users\barry\Desktop\JAB Used Stock.xlsx"
spreadsheet = xlrd.open_workbook(loc)
sheet = spreadsheet.sheet_by_index(0) 

browser = webdriver.Chrome()
browser.get('https://priceassist.donedeal.ie/')

RowCount= sheet.nrows
Row = 1

while (Row < RowCount):
	Reg = sheet.cell_value(Row, 1) 
	emailElem = browser.find_element_by_id('registration-number-string-id')
	emailElem.send_keys(Reg)
	passwordElem = browser.find_element_by_id('odometer-string-id')
	passwordElem.send_keys('')
	buttonpath = '//*[@id="submitRegistrationNumberButton"]'
	button = browser.find_element_by_xpath(buttonpath)
	button.click()
	r = browser.page_source
	soup = bs4.BeautifulSoup(r,'html.parser')
	data = soup.find("span", id="tot-selected").text
	data6 = int(data)
	if data6 <=0:
		data1 = sheet.cell_value(Row, 0)
		data2 = sheet.cell_value(Row, 1)
		data3 = sheet.cell_value(Row, 2)
		data4 = sheet.cell_value(Row, 5)
		TextData = soup.find("span", id="tot-selected").text
		data7 = int(TextData)
		TextData2 = soup.find("span", id="priceAverage").text
		TextData3 = TextData2.replace(',','')
		data8 = int(TextData3.replace('€',''))
		TextData4 = soup.find("span", id="milAverage").text
		TextData5 =(TextData4.replace(' km','')) 
		data9 = int(TextData5.replace(',',''))  
		worksheet.write(Row, 0, data1)
		worksheet.write(Row, 1, data2)
		worksheet.write(Row, 2, data3)
		worksheet.write(Row, 3, data4)
		worksheet.write(Row, 4, data7)
		worksheet.write(Row, 5, data8,formatting)
		worksheet.write(Row, 6, data9,formatting)
		Row += 1
		time.sleep(2)
		browser.get('https://priceassist.donedeal.ie/')
	else:
		select = Select(browser.find_element_by_id('dealerSelector'))
		select.select_by_visible_text("Dealer")
		select1 = Select(browser.find_element_by_id('statusSelector'))
		select1.select_by_visible_text("Live")
		r1 = browser.page_source
		soup1 = bs4.BeautifulSoup(r1,'html.parser')
		data1 = sheet.cell_value(Row, 0)
		data2 = sheet.cell_value(Row, 1)
		data3 = sheet.cell_value(Row, 2)
		data4 = sheet.cell_value(Row, 5)
		TextData = soup1.find("span", id="tot-selected").text
		data7 = int(TextData)
		TextData2 = soup1.find("span", id="priceAverage").text
		TextData3 = TextData2.replace(',','')
		data8 = int(TextData3.replace('€',''))
		TextData4 = soup1.find("span", id="milAverage").text 
		TextData5 =(TextData4.replace(' km','')) 
		data9 = int(TextData5.replace(',',''))  
		worksheet.write(Row, 0, data1)
		worksheet.write(Row, 1, data2)
		worksheet.write(Row, 2, data3)
		worksheet.write(Row, 3, data4)
		worksheet.write(Row, 4, data7)
		worksheet.write(Row, 5, data8,formatting)
		worksheet.write(Row, 6, data9,formatting)
		Row += 1
		time.sleep(2)
		browser.get('https://priceassist.donedeal.ie/')
workbook.close()










