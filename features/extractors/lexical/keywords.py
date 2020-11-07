import os
import sys
import _specify_dir
from features.extractors.process_data import ProcessData
from features.extractors.utils import java_keywords
from typing import List
from math import floor, log10


class KeywordExtractor(ProcessData):
	"""Extracts frequency of keywords"""
	def __init__(self) -> None:
		super().__init__()
		self.java_keywords = java_keywords
	
	def __repr__(self) -> str:
		return f"Class: {self.__class__.__name__}"

	def __str__(self) -> str:
		return f"Java keywords: {self.java_keywords}"

	@property
	def get_keyword_frequency(self) -> List[int]:
		keyword_frequency = []
		for file in self.sourcecode:
			temp = [word for word in file.split() if word in self.java_keywords]
			keyword_frequency.append(self.__len__(temp))
		return keyword_frequency
	
	def extract_keywords(self) -> List[int]:
		lexical_features = []
		for cf, kf in zip(self.get_character_frequency, self.get_keyword_frequency):
			try:
				lexical_features.append(floor(log10(cf / kf)))
			except ZeroDivisionError:
				lexical_features.append(0)
		return lexical_features


if __name__ == "__main__":
	KeywordExtractor().extract_keywords()