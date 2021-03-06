def help():
	print \
"""
yot commands:

help, h, ?:
	Display this help message
index, i:
	Display the current board's front page
refresh, r:
	Refresh the current board and display its front page
board [boardName], b [boardName]:
	Select a new board (by abbreviation) and display its front page
	Example: Type "board g", "b r9k" to select either /g/ or /r9k
thread [threadNum], t [threadNum], [threadNum]:
	Select a thread from the index, starting with 1
	Use the thread index, not the thread number!
	Example:
		Displayed in board index: "1: No. 8675309"
		Type "thread 1", "t 1", or simply "1" to display thread no. 8675309
"""