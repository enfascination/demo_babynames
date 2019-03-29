def loadSSADataByGender( year, dgender ):
    """
    Takes a year and a gender and  returns a dictionary mapping all names within that gender to its number of occurrences.
    year, an integer,  is everything 1990 to 2017 (and 1970)
    gender can be "M" or "F"
    this function assumes that the working directory contains the social security administration's annual public "yobYYYY.txt" files
    """
    NAMES_LIST = "yob" + str(year) + ".txt"
    boys = {}
    girls = {}
    for line in open(NAMES_LIST, 'r').readlines():
        name, gender, count = line.strip().split(",")
        count = int(count)

        if gender == "F":
            girls[name.lower()] = count
        elif gender == "M":
            boys[name.lower()] = count
    if rGender == "M":
        name_counts = boys
    else:
        name_counts = girls
    return( name_counts )
