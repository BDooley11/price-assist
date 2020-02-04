# price-assist

Allows user to save an excel spreadseet of used stock in the format of Stock No., Reg No, Vehicle Description, Value, Online, Age, Buy User
and vehicle location.

When the script is run it will go to donedeal's price assist website and check the reg against similar cars online.

It will filter for live units and only units Dealers have for sale.

The result will be a spreadsheet showing Stock no, Reg no., Model, Age, Done Deal units, Avg selling price DD, Avg kms DD.
This allows a car dealer easily check selling price of stock compared to competitors.

Requirments: requests, bs4, xlxwriter, xlrd, time, selenium, chrome browser and latest version of chrome driver
