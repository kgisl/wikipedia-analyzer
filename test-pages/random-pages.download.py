#!/usr/bin/env python
"""
This program takes the wikipedia names associated with the topics in the Knewton ontology and
downloads those pages
These pages will form the training set
"""
import wikipedia

def get_page(f, page):
    print "WIKIPAGE: " + page
    f.write("WIKIPAGE: " + page + "\n")
    text = wikipedia.WikipediaPage(page).content.encode('ascii', 'xmlcharrefreplace')
    f.write(text)
    f.write('\n')

def main():
    filename = 'random-pages.download.raw.dat'
    f = open(filename, 'a')
    """
    get_page(f, "11Eleven Project")
    get_page(f, "2009 Pilot Pen Tennis")
    get_page(f, "687 BC")
    get_page(f, "7976 Pinigin")
    get_page(f, "A Kiss Before Dying (novel)")
    get_page(f, "A Possible Projection of the Future / Childhood's End")
    get_page(f, "A320 Airbus (video game)")
    get_page(f, "Abraham Erasmus van Wyk")
    get_page(f, "Acalypha suirenbiensis")
    get_page(f, "Adam tablet")
    get_page(f, "Adilson dos Santos Souza")
    get_page(f, "Agonidium birmanicum")
    get_page(f, "Ahmadiyya Hospital Newbussa")
    get_page(f, "Angel Falls (Georgia)")
    get_page(f, "Angie Moretto")
    get_page(f, "Arbiter (electronics)")
    get_page(f, "Archips mortuanus")
    get_page(f, "Army Group Oberrhein (Germany)")
    get_page(f, "Arthur Harkins")
    get_page(f, "Asa Brainard")
    get_page(f, "Asia 2001")
    get_page(f, "Banda Sea Plate")
    get_page(f, "Bangor Normal College")
    get_page(f, "Belona, Virginia")
    get_page(f, "Big Tiger")
    get_page(f, "Braciejowice")
    get_page(f, "Bristol Naturalists' Society")
    get_page(f, "Buck Rogers: A Life in the Future")
    get_page(f, "Calendar (Microsoft service)")
    get_page(f, "Cameroonian parliamentary election, 1970")
    get_page(f, "Carnie Smith Stadium")
    get_page(f, "Cat Bi International Airport")
    get_page(f, "Cecilia Lundqvist")
    get_page(f, "Chaotian (geology)")
    get_page(f, "Charmileh")
    get_page(f, "Citron (color)")
    get_page(f, "Coventry Telegraph")
    get_page(f, "Covington River")
    get_page(f, "Cruise Critic")
    get_page(f, "Curtis Billsten")
    get_page(f, "Cy Neighbors")
    get_page(f, "David Larson")
    get_page(f, "DeAnne Hemmens")
    get_page(f, "Debagging")
    get_page(f, "Dee Martin")
    get_page(f, "Delaware AeroSpace Education Foundation")
    get_page(f, "Don Scott (Canadian football)")
    get_page(f, "Durbin Ward")
    get_page(f, "Dutch Supercar Challenge")
    get_page(f, "Dyasma")
    get_page(f, "East Timor Trade Union Confederation")
    get_page(f, "Edward Moon")
    get_page(f, "Elections in the Netherlands Antilles")
    get_page(f, "Ethnobotany")
    get_page(f, "Eulophota zonata")
    get_page(f, "Eureka Seven")
    get_page(f, "Ferdinand Minding")
    get_page(f, "Fish (surname)")
    get_page(f, "Flight interruption manifest")
    get_page(f, "Forse Castle")
    get_page(f, "Fred Hersch")
    get_page(f, "Frederick Pabst")
    get_page(f, "Garry Hogg")
    get_page(f, "Gaston Rakotobezanahary")
    get_page(f, "Geoffrey FitzClarence, 3rd Earl of Munster")
    get_page(f, "George Clooney filmography")
    get_page(f, "Glamorgan County Council election, 1895")
    get_page(f, "Golina, Jarocin County")
    get_page(f, "Gretton Halt railway station")
    get_page(f, "Heinz Hauser")
    get_page(f, "Henry Culley")
    get_page(f, "Herbert Feurer")
    get_page(f, "Hey, Hey, It's Esther Blueburger")
    get_page(f, "Hindley Earnshaw")
    get_page(f, "Home Economics (Community)")
    get_page(f, "Hugh Herbert")
    get_page(f, "ISO 3166-2:KH")
    get_page(f, "Il Male")
    get_page(f, "Irumbuliyur Junction")
    get_page(f, "Jacob Pepper")
    get_page(f, "James Howden MacBrien")
    get_page(f, "Japanese cruiser Ashigara")
    get_page(f, "Jean-Guy Guilbault")
    get_page(f, "John Baines (mathematician)")
    get_page(f, "John Forrest (rugby union)")
    get_page(f, "Joross Gamboa")
    get_page(f, "Junction Point Studios")
    get_page(f, "Karan Goddwani")
    get_page(f, "Kavilo")
    get_page(f, "Kolah Kabud, Kermanshah")
    get_page(f, "Kolenchery")
    get_page(f, "Korea Tungsten Company")
    get_page(f, "Last Angel")
    get_page(f, "List of Governors of the Northern Mariana Islands")
    get_page(f, "List of bridges documented by the Historic American Engineering Record in Pennsylvania")
    get_page(f, "Little Calf Island")
    get_page(f, "Lou Clinton")
    get_page(f, "MMP15")
    get_page(f, "Maareech ATDS")
    get_page(f, "Magdalen Redman")
    get_page(f, "Marcus Maddison")
    get_page(f, "Maurice Palgen")
    get_page(f, "Melanocytic tumors of uncertain malignant potential")
    get_page(f, "Melittia ectothyris")
    get_page(f, "Menace (Marvel Comics)")
    get_page(f, "Mervin Kelly")
    get_page(f, "Ministry of Foreign Affairs (Latvia)")
    get_page(f, "Modupe Adeyeye")
    get_page(f, "Mowtowr-e Rostam Zeynabadi")
    get_page(f, "Mt. Broderick Pullman Car")
    get_page(f, "Myrotske")
    get_page(f, "New Bongaigaon")
    get_page(f, "Obi of Onitsha")
    get_page(f, "Oxynoemacheilus seyhanensis")
    get_page(f, "Ozerov")
    get_page(f, "Palisades Hudson Financial Group")
    get_page(f, "Pandit Sundarlal Sharma (Open) University")
    get_page(f, "Paradox (theorem prover)")
    get_page(f, "Peristichia")
    get_page(f, "Peter Gabriel (1977 album)")
    get_page(f, "Pied-Noir")
    get_page(f, "Pierino Baffi")
    get_page(f, "Pitt Fall")
    get_page(f, "Pop Goodwin")
    get_page(f, "Porta Cordillera")
    get_page(f, "Pratap Singh Shah")
    get_page(f, "Privat Group")
    get_page(f, "RBW British Tag Team Championship")
    get_page(f, "Revolutionary Workers League (Oehlerite)")
    get_page(f, "Raj Raj")
    get_page(f, "Ran Rol")
    get_page(f, "Rancho Piedra Blanca")
    get_page(f, "Reckless (Gross novel)")
    get_page(f, "Rhagonycha nigriceps")
    get_page(f, "Rhinecliff Hotel")
    get_page(f, "Rival Ball")
    get_page(f, "Russian Mountains (Alaska)")
    get_page(f, "Ryuji Ito")
    get_page(f, "Saint Mary's Gaels men's basketball")
    get_page(f, "San Francisco Film Critics Circle Award for Best Animated Feature")
    get_page(f, "Sarah Vaughan Sings the Mancini Songbook")
    get_page(f, "Shaqra University")
    get_page(f, "Sharman (TV series)")
    get_page(f, "Sogdiana Jizzakh")
    get_page(f, "Sparta, Kentucky")
    get_page(f, "St Benet Fink Church, Tottenham")
    get_page(f, "St. Captain Freak Out & the Magic Bamboo Request")
    get_page(f, "St. Louis, San Francisco and Texas Railway")
    get_page(f, "Stamford and Spalding (UK Parliament constituency)")
    get_page(f, "System for Award Management")
    get_page(f, "Tap o' Noth")
    get_page(f, "Tazeh Kand-e Nasirpur")
    get_page(f, "Tesse")
    get_page(f, "The Collection (TNT DVD)")
    get_page(f, "The Life of Verdi (miniseries)")
    get_page(f, "The Open Air Meeting")
    get_page(f, "The Punisher (2011 series)")
    #get_page(f, "Jiangdong Bridge")
    get_page(f, "Troxel v. Granville")
    get_page(f, "Umar Bin Muhammad Daudpota")
    get_page(f, "Uncle Earl")
    get_page(f, "Vasara (video game)")
    get_page(f, "Victor Olofsson")
    get_page(f, "Volume 5: Poetry for the Masses (SeaShedShitheadByTheSheSore)")
    get_page(f, "Vytautas Valius")
    get_page(f, "Westmalle Abbey")
    get_page(f, "Weymouth High School")
    get_page(f, "William Craig (author)")
    get_page(f, "William Hatch (New Hampshire politician)")
    get_page(f, "William W. Dixon")
    get_page(f, "Wiremu Te Koti Te Rato")
    get_page(f, "Yasuyuki Kazama")
    get_page(f, "Zenson di Piave")
    """
    get_page(f, "Zoo Tycoon 2")
    f.close

if __name__ == '__main__':
    main()
