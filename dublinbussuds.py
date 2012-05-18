#!/usr/bin/env python

# 
# dublinbussuds.py
#
# Copyright (C) 2012 Jonathan McCrohan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
import suds

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

# Dublin Bus API serves broken WSDL
# no surprise there really..
imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://dublinbus.ie/')
d = ImportDoctor(imp)

# suds doesn't pick up the environmental http_proxy variable *sigh*
#p = dict(http='www-proxy.example.org:8080', https='www-proxy.example.org:8080')

# Dublin Bus WSDL URL
url = "http://rtpi.dublinbus.biznetservers.com/DublinBusRTPIService.asmx?WSDL"

# Adding Irish Rail API for future use
#url = "http://api.irishrail.ie/realtime/realtime.asmx?WSDL"

client = Client(url, proxy=p, doctor=d)

# uncomment to print WSDL service description
#print client


# Dublin Bus API methods as of 20120312
# GetAllDestinations()
# GetCurrentSettings()
# GetDestinations(xs:string filter, )
# GetRealTimeStopData(xs:int stopId, xs:boolean forceRefresh, )
# GetRoutes(xs:string filter, )
# GetRoutesServicedByStopNumber(xs:int stopId, )
# GetStopDataByAddress(xs:string address, )
# GetStopDataByRoute(xs:string route, )
# GetStopDataByRouteAndDirection(xs:string route, xs:string direction, )
# SetCurrentSettings(ArrayOfString values, )
# TestService()

requestoutput = client.service.GetRoutes('')

# multidemensional array, but all interesting data is buried in a single element
requestoutput = requestoutput[0][0]

# Print list of bus routes

for index in range(len(requestoutput)):
	print requestoutput[index][0]
