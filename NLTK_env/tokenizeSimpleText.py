import nltk
import PyPDF2
import textblob as TextBlob
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = "Red tide in the upwelling region of Baja California1 Dolors Blasco Bigelow Laboratory for Ocean Sciences, West Boothbay Harbor, Maine 04575 Abstract Predominant organisms in a red water dinoflagellate bloom during the seasonal onset of coastal upwelling off Baja California were Gonyaulax polyedra, Ceratium furca, and Gymnodinium sp. The major part of the chlorophyll and the lﬂC assimilation in the area was related to the G. polyedra population. The maximum concentration of these organisms was associated with low salinity water of the surface California Current. The dinoflagel- lates remained in the area during the 20-day cruise, although the vertical stability coeffi- cient was low, with no steep temperature gradient. The high concentrations of small copepods suggest them as major grazers of G. polyedra. Red tides have been observed and de- scribed in many parts of the ocean. Except for extensive rcscarch on the west coast of Florida and on the southern part of the California coast, early studies usually de- scribed sporadic observations of a mature red tide without any discussion of the de- velopment of the bloom, The onset of red water was thought to be related to an in- crease in vertical stability, or to freshwater runoff. Several recent studies have de- scribed the characteristics of these blooms in semiarid upwelling regions and have stressed the importance of dinoflagellate blooms in pelagic food webs. I here pre- sent observations of a red tide made during a 20-day cruise (MESCAL I) to the up- welling region of Baja California, with the RV Thomas G. Thompson of the Univer- sity of Washington. The west coast of Baja California is a typical coastal upwelling system, fret from heavy rainfall and river runoff. In these conditions it should be possible to distinguish between the oceanic and terrestrial factors thought to be respon- sible for generation of red water outbreaks. I thank the Fundacion Juan March of Spain for supporting this research, R. C. Dugdale for the opportunity to participate l Contribution 75019 from the Bigelow Labora- tory for Ocean Sciences. Contribution 801 from the Department of Oceanography, University of Washington. This work was supported by Na- tional Science Foundation grants IDOE GX- 33502 (CUEA 1-12) and GB-18568 as a part of the U.S. IBP Upwelling Biome. in the MESCAL I expedition, and my fel- low oceanographers for kindly providing the hydrographic and biological data. Methods The stations occupied between 5 and 23 March 1972 are shown in Fig. 1. Phyto- plankton samples were taken at productiv- ity stations from depths corresponding to radiance levels of 100, 50, 25, 10, 7, 3, and 1% of surface light, and at some hydro- graphic stations at the standard depths of 0, 10, 20, 30, 40, and 50 m. The samples were preserved with a few drops of Lugol™s solution (Margalef 1973). Cells were counted and identified with an inverted mi- croscope (Utermohl 1958; Blasco 1971). I tried to identify all cells to species, but many were flagellates and small dinoflagel- lates that could not be identified. Chemi- cal and physical observations were made at all depths for all stations. Nutrient analy- ses were made by AutoAnalyzer with the methods of Murphy and Riley (1962) for reactive phosphorus, Armstrong et al. (1967) for nitrate and silicate, and Slawyk and MacIsaac (1972) for ammonia. Each pro- ductivity station included chlorophyll ( SCOR-UNESCO 1966)) particulate car- bon ( Menzel and Vaccaro 1964)) particu- late nitrogen (Pavlou et al. 1974), rate mea- surcments of phytoplankton nitrate uptake by the lﬂN method (Dugdale and Goering 1967), estimates of nitrate rcductase (Pack- ard et al. 1971)) and 14C uptake measure- ments (Wolfe and Schelske 1967). LIMNOLOGY AND OCEANOGRAPHY 255 MARCH 1977, V. 22(2) "


from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()
blob = TextBlob(text, np_extractor=extractor)
print(blob.noun_phrases)
