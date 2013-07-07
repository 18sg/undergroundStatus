from time import time
import requests
import xml.etree.ElementTree as et

class Status(object):
	def __init__(self):
		self.update_url = "http://cloud.tfl.gov.uk/TrackerNet/LineStatus"
		self.lines = {}
		self.last_update = 0
		self.update_time = 30 #TfL asks for 30 seconds between requests

	def updateStatus(self):
		if (time() - self.last_update) > self.update_time:
			r = requests.get(self.update_url)
			self.last_update = time()

			root = et.fromstring(r.content)
			for child in root:
				self.lines[child[1].get('Name')] = child[2].get('ID')

	def getStatus(self, line_code):
		self.updateStatus()
		if line_code in self.lines:
			return self.lines[line_code]
		else:
			return None

status = Status()
