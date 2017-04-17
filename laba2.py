from spyre import server
import urllib2
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plot


class Lab2App(server.App):
    title = "Second Lab"

    inputs = [{
		"type": 'dropdown',
		"label": 'Choose the region',
		"options" : [ {"label": "Vinnitsya", "value": 24},
                          {"label": "Volyn", "value": 25},
                          {"label": "Dnopropetrovs'k", "value": 5},
                          {"label": "Donets'k", "value": 6},
                          {"label": "Zhytomyr", "value": 27},
                          {"label": "Transcarpsthia", "value": 23},
                          {"label": "Zaporyzhzha", "value": 26},
                          {"label": "Ivano-Frankivs'k", "value": 7},
                          {"label": "Kiev City", "value": 11},
                          {"label": "Kirovohrad", "value": 13},
                          {"label": "Luhans'k", "value": 14},
                          {"label": "L'viv", "value": 15},
                          {"label": "Mikolyaiv", "value": 16},
                          {"label": "Odessa", "value": 17},
                          {"label": "Poltava", "value": 18},
                          {"label": "Rivne", "value": 19},
                          {"label": "Sumy", "value": 21},
                          {"label": "Ternopil'", "value": 22},
                          {"label": "Kharkiv", "value": 8},
                          {"label": "Kherson", "value": 9},
                          {"label": "Khmel'nyts'kyy", "value": 10},
                          {"label": "Cherkasy", "value": 1},
                          {"label": "Chernyvtsy", "value": 3},
                          {"label": "Chernihiv", "value": 2},
                          {"label": "Crimea", "value": 4}],
		"variable_name": 'region',
		"value": 12,
     "action_id": "load_table"
	}, {
		"type": 'dropdown',
        "label": 'Choose index',
        "options" : [ {"label": "VHI", "value":"VHI"},
                                  {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"}],
        "variable_name": 'index',
		"value": "VHI",
     "action_id": "load_table"
	}
	, {
        	"input_type":"text",
		"variable_name":"week1",
		"label": "Enter the first week",
		"value":11,
		"key": 'week1',
     "action_id": "load_table"
    	}, {
		"input_type":"text",
		"variable_name":"week2",
		"label": "Enter the last week",
		"value":52,
		"key": 'week2',
    "action_id": "load_table"}]

    controls = [
        {
            "type": "hidden",
            "id": "load_table"
        }
    ]

    outputs = [
        {
            "type": "table",
            "id": "table_id",
            "control_id": "load_table",
            "tab": "Table"
        }, {
            "type": "plot",
            "id": "plot_id",
            "tab": "Plot",
			"control_id": "load_table"
        }
    ]

    tabs = ["Plot","Table"]

    def getData(self, params):
		week1 = int(params['week1'])
		index = str(params['index'])
		week2 = int(params['week2'])
		region = int(params['region'])
		df = pd.read_csv('/home/yarik/SRP/lab2/clean_data/vhi_id_'+str(region)+'.csv',',')
		df = df[['year','week','SMN','SMT','VCI','TCI','VHI']]
		df1 = df[['year','week',index]]

		df2 = df1[:(week2-1)]
		return df2[(week1-2):]


    def getPlot(self, params):
		index = str(params['index']) 
		data = self.getData(params)# get data
		figure = plot.figure()# make figure object
		subplot = figure.add_subplot(111)
		ind = numpy.arange(len(data['week']))
		width = 0.4
		subplot.bar(ind, data[index], width)
		subplot.set_ylabel(index)
		subplot.set_title(index)
		subplot.set_xticks(ind + width/2 )
		subplot.set_xticklabels(data['week'].tolist())
		figure.autofmt_xdate(rotation=90)
		return figure

app = Lab2App()
app.launch()
