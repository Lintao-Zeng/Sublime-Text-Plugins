import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, "Hello, World!")
		strArr = self.view.substr(sublime.Region(0,self.view.size())).split('\n@@@@\n')
		strArr2 = strArr[0].split('\n')
		strArr3 = strArr[1].split('\n')
		strArr4 = ""
		for i in range(0, len(strArr2)):
			strArr4 += strArr2[i] + "@@" + strArr3[i] + "\n"
		self.view.insert(edit, self.view.size(), "\n\n\n" + strArr4)