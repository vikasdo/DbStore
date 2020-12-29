import sys,time,os
import collections,pathlib
import json,time
class helperfunctions:

	def check_dict_constraints(d):
		if int(d.__sizeof__())>(1000*1024*1024):
			print("The size of Dictionary is exceeded the limit 1GB")
			return False
		return True

	def check_key_constraints(key):
		if len(key)>32 and key.isalpha() :
			print("The size of key you entered is exceeded the limit OF 32 chars")
			return False
		
		return True
	def check_val_constraints(val):
		if sys.getsizeof(val)>(16*1024):
			print("The size of val you entered is exceeded the limit OF 16 KB")

			return false
		return True
	def read_file(path):

		with open(path, "r") as read_file:
			data = json.load(read_file)
		return dict(data)

	def write_file(path,data):
		with open(path, "w") as write_file:
			json.dump(data, write_file)
		


class dbstore:

	def __init__(self,path=pathlib.Path().absolute()):
		self.data={}
		self.value = collections.namedtuple('value',['val','ttl']) 
		self.path=os.path.join(path,'new_data.json')
		try:

			self.data=helperfunctions.read_file(self.path)
		except:
			pass

		helperfunctions.write_file(self.path,self.data)

	def add(self,key,value,timeout=0):
		# print(key,value,timeout)
		self.data=helperfunctions.read_file(self.path)
		# print(self.data)
		try:
			if key in self.data:
				raise Exception(f"The Given key : {key} is created already..")
		
		
			if helperfunctions.check_dict_constraints(self.data) and helperfunctions.check_key_constraints(key) and helperfunctions.check_val_constraints(value) :
				if timeout==0:

					self.data[key]=self.value(value,timeout)
				else:
					self.data[key]=self.value(value,time.time()+timeout)

				helperfunctions.write_file(self.path,self.data)
				# time.sleep(1)


		except Exception as e:
			print("The error is {}".format(e))
		

	def read(self,key,value,timeout):
		# print(self.data)
		self.data=helperfunctions.read_file(self.path)

		try:
			if key not in self.data:
				raise Exception("The Given key is not found Enter another Key..")
			else:
				val,ttl=tuple(self.data[key])
				# print(key_data)
				if ttl==0 or 	ttl>time.time():

					print("The Value for {} : {}".format(key,val))
				else:

					raise Exception("The Given key Time to live has been expired.")
			
		except Exception as e:
			print("The error is {} ".format(e))



	def  delete(self,key,val,t):

		try:
			self.data=helperfunctions.read_file(self.path)
			# print(self.data)
			if key not in self.data:
				raise Exception("The Given key is not found Enter another Key..")
			else:
				key_data = self.value(self.data[key][0],self.data[key][1])
				if 	key_data.ttl<time.time():
					del self.data[key]
					helperfunctions.write_file(self.path,self.data)

					print(f"The key : {key} is deleted now ...")
				else:
					raise Exception("The Given key: {} Time to live has been expired.".format(key))

		except Exception as e:
			print("The error is {} ".format(e))
