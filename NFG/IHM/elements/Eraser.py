from IHM.elements.Element import Element
import numpy as np


class Eraser(Element):
	"""
	Class that extends Element, implements the Eraser
	"""
	def __init__(self):
		super().__init__()

	def getType(self):
		"""
		Getter of type 
		:return: "eraser"
		:rtype: str
		"""
		return "eraser"

	def start(self, **kwargs):
		"""
		Not implemented function for this element
		"""
		pass


	def motion(self, **kwargs):
		"""
		Not implemented function for this element
		"""
		pass

	def end(self, **kwargs):
		"""
		Remove the element if the release is on the same element as at the beginning
		:key event: event on canvas
		:type event: Event
		:key canvas: the canvas
		:type canvas: tkinter canvas
		:key NF: the Navon's Figure
		:type NF: NF
		:return: method return nothing
		:rtype:None
		"""
		event = kwargs.get('event')
		canvas = kwargs.get('canvas')
		NF = kwargs.get('NF')
		# onClick is a list of elements found nearby the click on the canvas but only the first created among all will be used
		# onClick is a list because find_overlapping return a list
		# https://mail.python.org/pipermail/tutor/2012-November/092795.html
		onClick = canvas.find_overlapping(event.x-1, event.y-1, event.x+1, event.y+1)

		# If the mouse is on the same element
		# Remove it from the NF
		if(onClick):
			for element in NF.elements:
				if element.getId() == onClick[0]:
					# https://www.kite.com/python/answers/how-to-delete-values-from-a-numpy-array-in-python#:~:text=from%20an%20array-,Use%20numpy.,that%20match%20the%20specified%20condition%20.	
					NF.removeElement(element)
						

					#Remove its intersections
					tag = f"-{element.getId()}" #self.tag from element and self.id to make a personal tag
					canvas.delete(tag)

					# Remove it from the canvas
					canvas.delete(element.getId())

					

	def getL(self):
		pass

	def interpolate(self):
		pass

	def findNeighbors(self,**kwargs):
		pass