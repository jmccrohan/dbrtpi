/*
 * dbrtpi.c
 *
 * Copyright (C) 2011 - Jonathan McCrohan
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

// gcc dbrtpi.c -o dbrtpi `pkg-config --libs --cflags libcurl`

#include <stdio.h>
#include <string.h>
#include <curl/curl.h>

#define URL "http://rtpi.dublinbus.biznetservers.com/DublinBusRTPIService.asmx"

int main(int argc, char *argv[]) {

	char soaprequest[1024];
	int stopid = 403;
	sprintf(
			soaprequest,
			"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap12:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">\n<soap12:Body>\n<GetRealTimeStopData xmlns=\"http://dublinbus.ie/\">\n<stopId>%d</stopId>\n<forceRefresh>1</forceRefresh>\n</GetRealTimeStopData>\n</soap12:Body>\n</soap12:Envelope>",
			stopid);

	struct curl_slist *header = NULL;
	header = curl_slist_append(header,
			"Content-Type: application/soap+xml; charset=utf-8");
	header = curl_slist_append(header, "Accept: text/xml");

	CURL *curl;
	CURLcode res;

	curl = curl_easy_init();
	if (curl) {
		curl_easy_setopt(curl, CURLOPT_URL, URL);
		curl_easy_setopt(curl, CURLOPT_POSTFIELDS, soaprequest);
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, header);
		curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE_LARGE, (curl_off_t) - 1);
		res = curl_easy_perform(curl);

		curl_easy_cleanup(curl);

		printf("%s", res);
	}
}

