from member_class import Member
#dictionary to store all the member of the Family Tree with the name as a key
family_tree = {
#Otto's side (husband) (Nazar)
    "otto emmersohn": Member("Otto Emmersohn", birth_date="18/12/1985", death_year=None, father="Henry Emmersohn", mother="Helen Emmersohn"),
    "tracy emmersohn": Member("Tracy Emmersohn", birth_date="15/07/2009", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "james emmersohn": Member("James Emmersohn", birth_date="15/07/2011", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "charley emmersohn": Member("Charley Emmersohn", birth_date="15/07/2007", death_year=None, father="Otto Emmersohn", mother="Cornelia Emmersohn"),
    "henry emmersohn": Member("Henry Emmersohn", birth_date="08/06/1978", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
    "richard emmersohn": Member("Richard Emmersohn", birth_date="12/07/1925", death_year="2007", father="Diego Emmersohn", mother="Maria Emmersohn"),
    "diego emmersohn": Member("Diego Emmersohn", birth_date="09/04/1899", death_year="1980", father=None, mother=None),
    "maria emmersohn": Member("Maria Emmersohn", birth_date="03/01/1904", death_year="1979", father=None, mother=None),
    "oliver thomas": Member("Oliver Thomas", birth_date="16/08/1901", death_year="1988", father=None, mother=None),
    "emilia thomas": Member("Emilia Thomas", birth_date="29/05/1906", death_year="1996", father=None, mother=None),
    "katrin emmersohn": Member("Katrin Emmersohn", birth_date="07/12/1925", death_year="2007", father="Oliver Thomas", mother="Emilia Thomas"),
    "helen emmersohn": Member("Helen Emmersohn", birth_date="04/03/1960", death_year=None, father="John Balan", mother="Lily Balan"),
    "john balan": Member("John Balan", birth_date="13/09/1928", death_year="2004", father="Andrei Balan", mother="Elena Balan"),
    "andrei balan": Member("Andrei Balan", birth_date="30/10/1902", death_year="1991", father=None, mother=None),
    "elena balan": Member("Elena Balan", birth_date="02/02/1904", death_year="1990", father=None, mother=None),
    "lily balan": Member("Lily Balan", birth_date="05/08/1930", death_year="2024", father="Bernard Meyer", mother="Lina Meyer"),
    "bernard meyer": Member("Bernard Meyer", birth_date="22/01/1903", death_year="1989", father=None, mother=None),
    "lina meyer": Member("Lina Meyer", birth_date="10/10/1907", death_year="1986", father=None, mother=None),
    "nicole fernandes": Member("Nicole Fernandes", birth_date="24/03/1963", death_year=None, father="John Balan", mother="Lily Balan"),
    "ahmed fernandes": Member("Ahmed Fernandes", birth_date="01/05/1961", death_year=None, father=None, mother=None),
    "jerry fernandes": Member("Jerry Fernandes", birth_date="11/12/2019", death_year=None, father="Ahmed Fernandes", mother="Nicole Fernandes"),
    "ali balan": Member("Ali Balan", birth_date="15/07/1959", death_year="2020", father="John Balan", mother="Lily Balan"),
    "harry jones": Member("Harry Jones", birth_date="28/02/2013", death_year=None, father="Oliver Jones", mother="Lucy Jones"),
    "lucy jones": Member("Lucy Jones", birth_date="14/11/1988", death_year=None, father="Henry Emmersohn", mother="Helen Emmersohn"),
    "oliver jones": Member("Oliver Jones", birth_date="06/09/1983", death_year=None, father=None, mother=None),
    "cristian rodgers": Member("Cristian Rodgers", birth_date="21/09/1990", death_year=None, father="Paul Rodgers", mother="Angela Rodgers"),
    "paul rodgers": Member("Paul Rodgers", birth_date="17/02/1959", death_year=None, father=None, mother=None),
    "angela rodgers": Member("Angela Rodgers", birth_date="26/10/1960", death_year=None, father="Richard Emmersohn", mother="Katrin Emmersohn"),
    "harry emmersohn": Member("Harry Emmersohn", birth_date="23/03/1923", death_year=None, father="Diego Emmersohn", mother="Maria Emmersohn"),
#Cornelia side (wife) (Roman)
    "cornelia emmersohn": Member("Cornelia Emmersohn", birth_date="21/07/1990", death_year=None, father="Ravi Patel", mother="Priya Gupta"),
    "andrew emmersohn": Member("Andrew Emmersohn", birth_date="21/07/1990", death_year=None, father=None, mother=None),
    "james sunak": Member("James Sunak", birth_date="09/11/1992", death_year=None, father="Ashok Sunak", mother="Kavita Singh"),
    "kavita singh": Member("Kavita Singh", birth_date="04/01/1965", death_year=None, father=None, mother=None),
    "ashok sunak": Member("Ashok Sunak", birth_date="27/06/1978", death_year=None, father=None, mother=None),
    "sarah gupta": Member("Sarah Gupta", birth_date="07/07/1995", death_year=None, father="Suresh Gupta", mother="Antoana Gupta"),
    "suresh gupta": Member("Suresh Gupta", birth_date="03/03/1969", death_year=None, father=None, mother=None),
    "antoana gupta": Member("Antoana Gupta", birth_date="29/07/1970", death_year=None, father=None, mother=None),
    "priya gupta": Member("Priya Gupta", birth_date="13/12/1976", death_year=2020, father="Suraj Gupta", mother="Meera Gupta"),
    "suraj gupta": Member("Suraj Gupta", birth_date="05/03/1920", death_year=1980, father="Rajesh Gupta", mother="Lakshmi Gupta"),
    "meera gupta": Member("Meera Gupta", birth_date="11/04/1925", death_year=1993, father="Naveen Kumar", mother="Priya Kumar"),
    "rajesh gupta": Member("Rajesh Gupta", birth_date="01/11/1890", death_year=1950, father=None, mother=None),
    "lakshmi gupta": Member("Lakshmi Gupta", birth_date="15/07/1900", death_year=1968, father=None, mother=None),
    "naveen kumar": Member("Naveen Kumar", birth_date="20/02/1902", death_year=1975, father=None, mother=None),
    "priya kumar": Member("Priya Kumar", birth_date="08/12/1893", death_year=1963, father=None, mother=None),
    "philip patel": Member("Philip Patel", birth_date="21/06/1927", death_year=2001, father="Yana Shinpilin", mother="Anton Patel"),
    "anne patek": Member("Anne Patek", birth_date="14/02/1929", death_year=2010, father="Viktor Patek", mother="Elena Patek"),
    "anton patel": Member("Anton Patel", birth_date="30/05/1906", death_year=1972, father=None, mother=None),
    "yana shinpilin": Member("Yana Shinpilin", birth_date="19/09/1896", death_year=1965, father=None, mother=None),
    "viktor patek": Member("Viktor Patek", birth_date="25/08/1892", death_year=1958, father=None, mother=None),
    "elena patek": Member("Elena Patek", birth_date="13/03/1889", death_year=1947, father=None, mother=None),
    "ravi patel": Member("Ravi Patel", birth_date="06/09/1965", death_year=None, father="Philip Patel", mother="Anne Patek"),
}

#Assigning spouses
#Otto side spouses
family_tree["cornelia emmersohn"].add_spouse("otto emmersohn")
family_tree["richard emmersohn"].add_spouse("katrin emmersohn")
family_tree["katrin emmersohn"].add_spouse("richard emmersohn")
family_tree["diego emmersohn"].add_spouse("maria emmersohn")
family_tree["maria emmersohn"].add_spouse("diego emmersohn")
family_tree["angela rodgers"].add_spouse("paul rodgers")
family_tree["paul rodgers"].add_spouse("angela rodgers")
family_tree["oliver thomas"].add_spouse("emilia thomas")
family_tree["emilia thomas"].add_spouse("oliver thomas")
family_tree["henry emmersohn"].add_spouse("helen emmersohn")
family_tree["helen emmersohn"].add_spouse("henry emmersohn")
family_tree["john balan"].add_spouse("lily balan")
family_tree["lily balan"].add_spouse("john balan")
family_tree["andrei balan"].add_spouse("elena balan")
family_tree["bernard meyer"].add_spouse("lina meyer")
family_tree["lina meyer"].add_spouse("bernard meyer")
family_tree["lucy jones"].add_spouse("oliver jones")
family_tree["oliver jones"].add_spouse("lucy jones")
family_tree["nicole fernandes"].add_spouse("ahmed fernandes")
family_tree["ahmed fernandes"].add_spouse("nicole fernandes")
#Cornelia side spouses
family_tree["otto emmersohn"].add_spouse("cornelia emmersohn")
family_tree["kavita singh"].add_spouse("ashok sunak")
family_tree["ashok sunak"].add_spouse("kavita singh")
family_tree["suresh gupta"].add_spouse("antoana gupta")
family_tree["antoana gupta"].add_spouse("suresh gupta")
family_tree["priya gupta"].add_spouse("ravi patel")
family_tree["ravi patel"].add_spouse("priya gupta")
family_tree["suraj gupta"].add_spouse("meera gupta")
family_tree["meera gupta"].add_spouse("suraj gupta")
family_tree["rajesh gupta"].add_spouse("lakshmi gupta")
family_tree["lakshmi gupta"].add_spouse("rajesh gupta")
family_tree["naveen kumar"].add_spouse("priya kumar")
family_tree["priya kumar"].add_spouse("naveen kumar")
family_tree["philip patel"].add_spouse("yana shinpilin")
family_tree["yana shinpilin"].add_spouse("philip patel")
family_tree["anne patek"].add_spouse("anton patel")
family_tree["anton patel"].add_spouse("anne patek")
family_tree["viktor patek"].add_spouse("elena patek")
family_tree["elena patek"].add_spouse("viktor patek")