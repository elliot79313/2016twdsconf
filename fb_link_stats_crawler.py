#-*- coding: UTF-8 -*-
#/usr/bin/env python
import urllib
import urllib2
import json

__access_token__ = '291463934212578|KpMfnD6zraCdnZo8vWB5kKambYQ'

def fetchSlideshareLinkStat(links):

	link_stat_dict = {}
	for link in links:

		if "slideshare" not in link: continue #不是slideshare 請跳開

		__base__ = 'https://graph.facebook.com/v2.7/' 
		form_data = {'id': link, "access_token": __access_token__ }
		payload = urllib.urlencode(form_data)

		link_stat_obj = {}

		#GET 模式
		res = urllib2.urlopen(url=__base__+"?"+payload)
		res_obj = json.load(res)
		print res_obj
		link_stat_obj["facebook_insight"] = res_obj["share"]
		

		#POST 模式
		res = urllib2.urlopen(url=__base__, data=payload)
		res_obj = json.load(res)
		link_stat_obj["slideshare_insight"] = res_obj["data"]

		link_stat_dict[link] = link_stat_obj

	return link_stat_dict


def main():
	
	f = open("./post_data.json")
	post_set = json.load(f)
	f.close()

	#篩選slideshare 
	post_set = [ item for item in post_set if "link" in item]
	post_set = [ item for item in post_set if "slideshare" in item["link"] ]
	links = [item["link"] for item in post_set ]

	link_stat_dict = fetchSlideshareLinkStat(links)

	for item in post_set:
		if "link" not in item: break

		url = item["link"]
		if url in link_stat_dict:
			item["stat"] = link_stat_dict[url]

	#DONE

	#存檔案
	w = open("./post_data_insights.json","w")
	json.dump(post_set, w)
	w.close()




if __name__ == '__main__':
	main()

