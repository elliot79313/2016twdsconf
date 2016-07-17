#-*- coding: UTF-8 -*-
#/usr/bin/env python
import urllib
import urllib2
import json

__access_token__ = '291463934212578|KpMfnD6zraCdnZo8vWB5kKambYQ'


def fetchPost(pageid, limit=200):

	__base__ = 'https://graph.facebook.com/v2.7/%(pageid)s/posts' % {'pageid': pageid}

	form_data= {
		"fields":"id,message,created_time,shares,likes.limit(0).summary(1),link,name",
		"access_token": __access_token__
	}

	payload = urllib.urlencode(form_data)
	url = __base__ + "?" + payload

	post_set = []
	
	while True:
		res = urllib2.urlopen(url)
		res_obj = json.load(res)

		post_set = post_set + res_obj["data"] #整理在一個 set 內

		if len(post_set)>=limit: break #不幹了
		if "paging" not in res_obj: break #沒有上下頁
		if "next" not in res_obj["paging"]: break #沒有下一頁

		next_paging = res_obj["paging"]["next"]

		url = next_paging

	return post_set


def main():

	pageid = 'twdsconf' #資料科學年會
	post_set = fetchPost(pageid, limit=100)
	#print len(post_set)

	#存檔案
	w = open("./post_data.json","w")
	json.dump(post_set, w)
	w.close()


if __name__ == '__main__':
	main()
