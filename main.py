# YOU INSTALL POCKETBASE with pip install pocketbase
from flet import *
from pocketbase import PocketBase
import os
import glob
from pocketbase.client import FileUpload

folder_path = "myfile/"
# AND INSERT URL pocketbase here
url = 'https://sparse-vegetable.pockethost.io'
client = PocketBase(url)


def main(page:Page):
	page.window_width = 400
	listfilefordrag = Row(wrap=True)

	# AND NOW I WILL SCAN folder myfile and find all
	# file and show to container
	file_list = glob.glob(os.path.join(folder_path,"*"))
	for file_path in file_list:
		if os.path.isfile(file_path):
			file_name = os.path.basename(file_path)
			# AND NOW PUSH TO MY LITS WIDGET
			listfilefordrag.controls.append(
				# CREATE DRAGABLE 
				Draggable(
					content=Container(
						bgcolor="green200",
						padding=10,
						content=Column([
							Icon(name="image"),
							Text(file_name,size=25)
							])
						)
					)
				)



	def you_willaccept(e):
		# THIS FUNCTION IF YOU WILL DRAG TO CONTAINER
		e.control.content.bgcolor = "orange"
		e.control.content.width = 400
		e.control.content.height = 300
		page.update()



	def youaccept(e):
		src = page.get_control(e.src_id)
		# THIS GET TEXT FROM GREEN CONTAINER FILE NAME
		name_fileyou = src.content.content.controls[1].value
		print(name_fileyou)
		try:
			res = client.collection("youtube_flet").create({
				# YOU FIELD FIELD IN POCKETBASE HERE
				"name_here":name_fileyou,
				"file_one_this":FileUpload((name_fileyou,open(f"myfile/{name_fileyou}","rb")))

				})
			# show MESSAGE IF SUCCESS UPLAOD
			page.snack_bar = SnackBar(
				Text("success upload",size=30)
				)
			page.snack_bar.open = True
			page.update()
		except Exception as e:
			print(e)


	def youleave(e):
		# THIS IF YOU LEAVE NOT ACCEPT
		e.control.content.bgcolor = "blue200"
		e.control.content.width = 350
		e.control.content.height = 150
		page.update()

	page.add(
		AppBar(
			title=Text("Flet pocket",size=30),
			bgcolor="blue"
			),
		Column([
			listfilefordrag,
			# CREATE DRAG TARGET FOR UPLOAD FILE
			DragTarget(
				on_will_accept=you_willaccept,
				on_accept=youaccept,
				on_leave=youleave,
				content=Container(
					bgcolor="blue200",
					width=300,
					height=150,
					padding=10,
					content=Text("UPLOAD HERE GUYS",size=30)
					)
				)

			])
		)
flet.app(target=main)

# NOW I HAVE SAMPLE IMAGE IN FOLDER myfile FOr upload to pocketbase
# i will scan folder myfile and find all file in folder myfile
# and show file in flet container

