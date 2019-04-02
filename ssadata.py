import gzip

def loadSSADataByGender( path, dgender ):
    """
    Takes a year and a gender and  returns a dictionary mapping all names within that gender to its number of occurrences.
    year, an integer,  is everything 1990 to 2017 (and 1970)
    gender can be "M" or "F"
    this function assumes that the working directory contains the social security administration's annual public "yobYYYY.txt" files
    """
    NAMES_LIST = path
    boys = {}
    girls = {}
    with gzip.open(NAMES_LIST, 'rt') as f:
        for line in f:
            name, gender, count = line.strip().split(",")
            count = int(count)

            if gender == "F":
                girls[name.lower()] = count
            elif gender == "M":
                boys[name.lower()] = count
    if dgender == "M":
        name_counts = boys
    else:
        name_counts = girls
    return( name_counts )

def loadSSADataIntoColab( year):
    boys = loadSSADataByGender( "/content/demo_babynames/ssadata/" + "yob" + str(year) + ".txt.gz", "M")
    girls = loadSSADataByGender( "/content/demo_babynames/ssadata/" + "yob" + str(year) + ".txt.gz", "F")
    all = dict( boys )
    for name, count in girls.items():
        if name in all:
            all[ name ] = all[ name ] + count
        else:
            all[ name ] = 0 + count
    return( boys, girls, all )

NAMES_LIST = "yob2013.txt"
NAMES_PATH = "ssadata/" + NAMES_LIST+ ".gz"
boys = loadSSADataByGender( NAMES_PATH, 'M' )
girls = loadSSADataByGender( NAMES_PATH, 'F' )
all = dict( boys )
for name, count in girls.items():
    if name in all:
        all[ name ] = all[ name ] + count
    else:
        all[ name ] = 0 + count
print( all )
