import random
from urllib import urlopen
import sys

WORLD_URL = 'http://www.learncodethehardway.org/words.txt'
WORDS = []

PHRASES = {
  'class %%%(%%%):':
    'Make a class named %%% that is a %%%.'

}