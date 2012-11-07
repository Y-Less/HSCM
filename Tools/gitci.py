import sys
from Npp import *
import site

# You can hook pre-save events, is there a way to hook post-save events or
# explicitly trigger the save during your callback?
def gitCommit(args):
	buf = args['bufferID']
	cur = notepad.getCurrentBufferID()
	# Switch to this file to operate on.
	notepad.activateBufferID(buf)
	fname = notepad.getCurrentFilename()
	#.replace('\\', '/')
	# Get the directory.
	idx = -1
	while True:
		odx = idx
		idx = fname.find('\\', idx + 1)
		if idx == -1:
			break
	dir = fname[:odx]
	#notepad.messageBox(dir, 'File:', 0)
	# Commit this if it's in a "GIT" directory (not brilliant I know...).
	if 'GIT' in dir.upper():
		ci = 'NONE:'
		while True:
			ci = notepad.prompt('Format: "<DOC(UMENTATION)|BUG|FEAT(URE)|REF(ACTOR)|STRUC(TURE)|IN(T(ERIM))>: <Message>"', 'Commit Message', 'INTERIM: Interim commit, see subsequent commits for details.')
			if ci == None or ci == '':
				continue
			cl = ci.upper()
			if cl[:4] == 'BUG:':
				break
			elif cl[:4] == 'REF:' or cl[:9] == 'REFACTOR:':
				break
			elif cl[:5] == 'FEAT:' or cl[:8] == 'FEATURE:':
				break
			elif cl[:6] == 'STRUC:' or cl[:10] == 'STRUCTURE:':
				break
			elif cl[:4] == 'DOC:' or cl[:14] == 'DOCUMENTATION:':
				break
			elif cl[:3] == 'IN:' or cl[:4] == 'INT:' or cl[:8] == 'INTERIM:':
				break
		# Ensure the file is in the repository.
		#console.run(dir[:2])
		#console.run('cd[3:] ' + dir)
		#console.run('git add ' + fname)
		# Commit with the given message.
		# There are loads of different types of quotes here, sorry!
		console.run('cmd.exe /k ""' + notepad.getNppDir() + r'\plugins\PythonScript\scripts\gitci.bat" "' + fname + '" "' + ci + '""')
	# Return to the original active file.
	notepad.activateBufferID(cur)

notepad.callback(gitCommit, [NOTIFICATION.FILESAVED])
