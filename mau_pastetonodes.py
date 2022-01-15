#--------------------------------------------------
# mau_pastetonodes.py
# version: 1.0.0
# last updated: 29.10.18 (DD.MM.YY)
#--------------------------------------------------
#based on JohannesMasanz PasteToNode

import nuke
import nukescripts

def PasteToNodes():
	n = nuke.selectedNodes()
	if len(n) == 0:
		nuke.message('please, select a node first!')
	else:
		for i in nuke.selectedNodes():
			i.setSelected(True)
			nuke.nodePaste("%clipboard%")
			
	nukescripts.clear_selection_recursive()
