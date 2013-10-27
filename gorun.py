# -*- coding: utf-8 -*-  
import sublime, sublime_plugin,os
# run go program
class GorunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")

		fname =str(self.view.file_name())
		tmp = fname.rfind('/')
		if tmp<0:
			tmp = fname.rfind('\\')
		
		tmpfile = fname[0:tmp+1]+"tmp.txt"
		cm = "go run " + fname + " >"+tmpfile 
		print "[execute]:"+cm
		
		
		os.system(str(cm))

		txt = str("")

		file_object = open(tmpfile)
		try:
  		   txt = file_object.read( )
		finally:
			file_object.close( )
			print txt
			os.remove(tmpfile)

# format the current file of go
class GofmtCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")

		fname =str(self.view.file_name())
		cm = "go fmt "+ fname
		print "[execute]:"+cm

		#print self.view.window().open_file(fname)
		#os.system(str(cm))
		print "hello"
		self.view.run_command("revert")

		

