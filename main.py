from argparse import ArgumentParser
import pandas as pandas
from func import functions

parser=ArgumentParser(description="Program created to obtain info about movies in IMBD)

parser.add_argument("-rk","ranking",help='Search position in Ranking',action='store_true')
parser.add_argument("-d","director",help='Search name in Director',action='store_true')
parser.add_argument("-m","movie",help='Search title in Title',action='store_true')
parser.add_argument("-g","genre",help='Search movie-genre in Genre',action='store_true')
parser.add_argument("-y","year",help='Search when in Year',action='store_true')
parser.add_argument("-M$","revenue",help='Search how_much in Revenue(M$)',action='store_true')
parser.add_argument("-tp","topcast",'action='store_true')
parser.add_argument("-v","versions",action='store_true')
parser.add_argument("-pg","parental-guide",action='store_true')
parser.add_argument("-aw","award-winner",action='store_true')
parser.add_argument("-fl","filminglocation",action='store_true')
args=parser.parse_args()
print(args)




if __name__=="__main__":
print(main())