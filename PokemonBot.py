import discord
import random
from discord.ext import commands
from fractions import Fraction
from decimal import Decimal
import sys
from discord.ext.commands.cooldowns import BucketType
import string_utils
import csv
from datetime import date
from datetime import datetime
from discord.utils import get
from idlelib.configdialog import is_int
#from random import random
import math
import time
import wordlist
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


ListErratic = ["Appletun", "Applin", "Flapple", "Feebas", "Milotic", "Nincada", "Ninjask", "Shedinja", "Altaria", #25
               "Anorith", "Armaldo", "Bastiodon","Clamperl","Cradily","Cranidos","Finneon","Gorebyss","Huntail",
               "Lileep","Lumineon","Rampardos","Shieldon","Swablu","Volbeat","Zangoose"]
ListFast = ["Boltund", "Clefable", "Clefairy", "Cleffa", "Cinccino", "Corsola", "Cursola", "Delibird", "Duskull", #62
            "Dusclops", "Dusknoir", "Indeedee", "Lunatone", "Mawile", "Minccino", "Munna", "Musharna", "Nickit",
            "Pyukumuku", "Solrock", "Theivul", "Togekiss", "Togepi", "Togetic", "Wishiwashi", "Yamper","Aipom",
            "Alomomola","Ambipom","Ariados","Audino","Azumarill","Marill","Azurill","Banette","Shuppet","Blissey",
            "Chansey","Happiny","Chimecho","Chingling","Comfey","Delcatty","Skitty","Glameow","Purugly","Granbull",
            "Snubbull","Igglybuff","Jigglypuff","Wigglytuff","Klefki","Ledian","Ledyba","Luvdisc","Misdreavus","Mismagius",
            "Smeargle","Spinarak","Spinda","Spoink","Grumpig"]
ListMFast = ["Accelgor", "Aegislash", "Alcremie", "Amaura", "Amoonguss", "Araquanid", "Arbok","Archen", "Archeops", "Aromatisse", #372
             "Aurorus", "Avalugg", "Baltoy", "Barbaracle", "Barboach", "Basculin", "Beartic", "Beautifly", "Beedrill",
             "Beheeyem", "Bergmite", "Bewear", "Bibarel", "Bidoof", "Binacle", "Bisharp", "Blipbug", "Blitzle",
             "Bonsly", "Bouffalant", "Bronzong", "Bronzor", "Bruxish", "Buizel", "Buneary", "Bunnelby", "Burmy",
             "Butterfree", "Camerupt","Carracosta","Cascoon","Castform", "Caterpie", "Centiskorch", "Charjabug",
             "Cherrim", "Cherubi", "Chewtle", "Claydol", "Cofagrigus", "Copperajah", "Cottonee", "Crabominable",
             "Crabrawler","Cramorant", "Croagunk","Crobat", "Crustle", "Cryogonal", "Cubchoo", "Cubone", "Cufant",
             "Cutiefly", "Dedenne", "Deerling","Dewgong", "Dewpider", "Dhelmise", "Diggersby", "Diglett", "Ditto",
             "Dodrio","Doduo", "Donphan", "Dottler", "Doublade", "Drampa", "Drednaw", "Drilbur", "Drowzee", "Druddigon",
             "Dubwool", "Ducklett", "Dugtrio", "Dunsparce", "Duraludon", "Durant", "Dustox", "Dwebble", "Eevee", "Ekans",
             "Eldegoss", "Electabuzz", "Electivire", "Electrode", "Elekid", "Elgyem", "Emolga", "Escavalier", "Espeon",
             "Espurr", "Excadrill", "Falinks", "Farfetch'd", "Fearow", "Ferroseed", "Ferrothorn", "Flabebe", "Flareon",
             "Floatzel","Floette","Florges","Fomantis","Foongus","Forretress","Frillish", "Froslass", "Frosmoth", "Furfrou",
             "Furret", "Galvantula", "Garbodor", "Gastrodon", "Girafarig", "Glaceon", "Glalie", "Gogoat","Golbat","Goldeen",
             "Golduck", "Golett", "Golisopod", "Golurk", "Gossifleur", "Gourgeist", "Greedent", "Grimer", "Grimmsnarl",
             "Grubbin", "Gumshoos", "Hawlucha", "Heatmor", "Helioptile", "Heliolisk", "Hitmonchan", "Hitmonlee","Hitmontop",
             "Honedge", "Hoothoot", "Horsea","Hypno", "Impidimp", "Inkay", "Jellicent", "Jolteon", "Joltik", "Jynx", "Kabuto",
             "Kabutops", "Kakuna", "Kangaskhan", "Karrablast", "Kingdra", "Kingler", "Koffing", "Krabby", "Leafeon", "Lickilicky",
             "Lickitung","Liepard", "Lilligant", "Linoone", "Lopunny", "Lurantis", "Lycanroc", "Magby", "Magcargo", "Magmar",
             "Magmortar", "Magnemite", "Magneton", "Magnezone", "Malamar", "Mankey", "Maractus", "Mareanie","Marowak","Masquerain",
             "Medicham","Meditite", "Meowstic", "Meowth", "Metapod", "Mightyena", "Milcery", "Mime Jr.", "Mimikyu", "Minun",
             "Morelull", "Morgrem", "Morpeko", "Mothim", "Mr. Mime", "Mr. Rime", "Mudbray", "Mudsdale", "Muk", "Natu", "Ninetales",
             "Noctowl", "Noibat", "Noivern", "Nosepass", "Numel", "Obstagoon", "Octillery", "Omanyte", "Omastar", "Onix", "Orbeetle",
             "Oricorio", "Pachirisu", "Palossand", "Pancham", "Pangoro", "Panpour", "Pansage", "Pansear", "Paras", "Parasect", "Patrat",
             "Pawniard", "Pelipper", "Perrserker", "Persian", "Petilil", "Phanpy", "Phantump", "Pichu", "Pikachu", "Pikipek", "Pincurchin",
             "Pineco", "Plusle", "Polteageist", "Ponyta", "Poochyena", "Porygon", "Porgyon-Z", "Porygon2", "Primeape", "Probopass",
             "Psyduck", "Pumpkaboo", "Purrloin", "Quagsire", "Qwilfish", "Raichu", "Rapidash", "Raticate", "Rattata", "Remoraid",
             "Ribombee", "Rockruff", "Rotom", "Runerigus", "Salandit", "Salazzle", "Sandaconda", "Sandshrew", "Sandslash", "Sandygast",
             "Sawk", "Sawsbuck", "Scatterbug","Scizor", "Scrafty", "Scraggy", "Scyther", "Seadra", "Seaking", "Seel",
             "Sentret", "Shellos", "Shelmet", "Shiinotic", "Sigilyph", "Silcoon", "Silicobra", "Simipour", "Simisage",
             "Simisear", "Sinistea", "Sirfetch'd", "Sizzlipede", "Skiddo","Skrelp", "Skuntank", "Skwovet", "Slowbro",
             "Slowking", "Slowpoke","Slugma", "Slurpuff", "Smoochum", "Snom", "Snorunt", "Spearow", "Spewpa", "Spiritomb",
             "Spritzee", "Steelix", "Stufful", "Stunfisk", "Stunky", "Sudowoodo", "Surskit","Swanna", "Swirlix", "Swoobat",
             "Sylveon", "Tangela", "Tangrowth", "Teddiursa", "Throh", "Tirtouga", "Togedemaru", "Torkoal", "Toucannon",
             "Toxapex", "Toxicroak", "Trevenant", "Trubbish", "Trumbeak", "Turtonator", "Tyrantrum", "Tyrogue", "Tyrunt",
             "Umbreon", "Unown", "Ursaring", "Vaporeon", "Venomoth", "Venonat", "Vikavolt", "Vivillon", "Voltorb",
             "Vulpix", "Watchog", "Weedle", "Weezing", "Whimsicott", "Whiscash", "Wimpod", "Wingull", "Wobbuffet", "Woobat",
             "Wooloo", "Wooper", "Wormadam", "Wumrple", "Wynaut", "Xatu", "Yamask", "Yanma", "Yanmega", "Yungoos",
             "Zebstrika", "Zigzagoon", "Zubat"]
ListMSlow = ["Abra","Absol","Alakazam","Ampharos","Bayleef","Bellossom","Bellsprout","Blastoise","Blaziken", "Boldore", #223
             "Bounsweet", "Braixen", "Brionne", "Budew", "Bulbasaur", "Cacnea", "Cacturne", "Carkol", "Celebi", "Chandelure",
             "Charizard", "Charmander", "Charmeleon", "Chatot", "Chesnaught", "Chespin", "Chikorita", "Chimchar",
             "Cinderace", "Clobbopus", "Coalossal", "Combee", "Combusken", "Conkeldurr", "Corviknight", "Corvisquire",
             "Croconaw", "Cyndaquil", "Darmanitan", "Dartrix","Darumaka", "Decidueye", "Delphox", "Dewott", "Drizzile",
             "Duosion", "Emboar", "Empoleon", "Exploud", "Fennekin", "Feraligatr", "Flaaffy", "Fletchinder","Fletchling",
             "Flygon", "Froakie", "Frogadier", "Gastly", "Gengar", "Geodude", "Gigalith", "Gligar", "Gliscor", "Gloom",
             "Golem", "Gothita", "Gothorita", "Gothitelle", "Grapploct", "Graveler", "Greninja", "Grookey", "Grotle",
             "Grovyle", "Gurdurr", "Haunter", "Herdier", "Honchkrow", "Hoppip", "Incineroar", "Infernape", "Inteleon",
             "Ivysaur", "Jumpluff", "Kadabra", "Kecleon", "Klang", "Klink", "Klinklang", "Kricketot", "Kricketune",
             "Krokorok", "Krookodile", "Lampent", "Leavanny", "Lillipup", "Litleo", "Litten", "Litwick", "Lombre", "Lotad",
             "Loudred", "Lucario", "Ludicolo", "Luxio", "Luxray", "Machamp", "Machoke", "Machop", "Mareep", "Marshtomp",
             "Meganium", "Mew", "Mienfoo", "Mienshao", "Minior", "Monferno", "Mudkip", "Murkrow", "Nidoking", "Nidoqueen",
             "Nidoran", "Nidorina", "Nidorino", "Nuzleaf", "Oddish", "Oshawott", "Palpitoad", "Pidgeot", "Pidgeotto",
             "Pidgey", "Pidove", "Pignite", "Piplup", "Politoed", "Poliwag", "Poliwhirl", "Poliwrath", "Popplio",
             "Primarina", "Prinplup", "Pyroar", "Quilava", "Quilladin", "Raboot", "Reuniclus", "Rillaboom", "Riolu",
             "Roggenrola", "Rolycoly", "Rookidee", "Roselia", "Roserade", "Rowlet", "Sableye", "Samurott", "Sandile",
             "Sceptile", "Scolipede", "Scorbunny", "Sealeo", "Seedot", "Seismitoad", "Serperior", "Servine", "Sewaddle",
             "Shaymin", "Shiftry", "Shinx", "Shuckle", "Skiploom", "Sneasel", "Snivy", "Sobble", "Solosis", "Spheal",
             "Squirtle", "Staraptor", "Staravia", "Starly", "Steenee", "Stoutland", "Sunflora", "Sunkern", "Swadloon",
             "Swampert", "Swellow", "Taillow", "Talonflame", "Tepig", "Thwackey", "Timburr", "Torchic", "Torracat",
             "Torterra", "Totodile", "Toxel", "Toxtricity", "Tranquill", "Trapinch", "Treecko", "Tsareena", "Turtwig",
             "Tympole", "Typhlosion", "Unfezant", "Venipede", "Venusaur", "Vespiquen", "Vibrava", "Victreebel", "Vileplume",
             "Walrein", "Wartortle", "Weavile", "Weepinbell", "Whirlipede","Whismur", "Zoroark","Zorua"]
ListSlow = ["Abomasnow", "Aerodactyl", "Aggron", "Arcanine", "Arceus", "Arctovish", "Arctozolt", "Aron", "Arrokuda", #205
            "Articuno", "Axew", "Azelf", "Bagon", "Barraskewda", "Beldum", "Blacephelon", "Braviary", "Buzzwole", "Calyrex",
            "Carbink", "Carnivine", "Carvanha", "Celesteela", "Chinchou", "Clauncher", "Clawitzer", "Cloyster", "Cobalion",
            "Cosmoem", "Cosmog", "Cresselia", "Darkrai", "Deino", "Deoxys", "Dialga", "Diancie", "Dracovish", "Dracozolt",
            "Dragapult", "Dragonair", "Dragonite", "Drakloak", "Drapion", "Dratini", "Dreepy", "Eelektrik", "Eelektross",
            "Eiscue", "Electrike", "Entei", "Eternatus", "Exeggcute", "Exeggutor","Fraxure", "Gabite", "Gallade",
            "Garchomp", "Gardevoir", "Genesect", "Gible", "Giratina", "Glastrier", "Goodra", "Goomy", "Groudon", "Growlithe",
            "Guzzlord", "Gyarados", "Hakamo-o", "Hatenna", "Hatterene", "Hattrem", "Haxorus", "Heatran", "Heracross",
            "Hippopotas", "Hippowdon", "Ho-Oh", "Hoopa", "Houndoom", "Houndour", "Hydreigon", "Jangmo-o", "Jirachi",
            "Kartana", "Keldeo", "Kirlia", "Komala", "Kommo-o", "Kubfu", "Kyogre", "Kyurem", "Lairon", "Landorus",
            "Lanturn", "Lapras", "Larvesta", "Larvitar", "Latias", "Latios", "Lugia", "Lunala", "Magearna", "Magikarp",
            "Mamoswine", "Manaphy", "Mandibuzz", "Manectric", "Mantine", "Mantyke", "Marshadow", "Melmetal", "Meloetta",
            "Meltan", "Mesprit", "Metagross", "Metang", "Mewtwo", "Miltank", "Moltres", "Munchlax", "Naganadel", "Necrozma",
            "Nihilego", "Oranguru", "Palkia", "Passimian", "Pheromosa", "Phione", "Piloswine", "Pinsir", "Poipole", "Pupitar",
            "Raikou", "Ralts", "Rayquaza", "Regice", "Regidrago", "Regieleki", "Regigigas", "Regirock", "Registeel",
            "Relicanth", "Reshiram", "Rhydon", "Rhyhorn", "Rhyperior", "Rufflet", "Salamence", "Sharpedo", "Shelgon",
            "Shellder", "Silvally", "Skarmory", "Skorupi", "Slaking", "Slakoth", "Sliggoo", "Snorlax", "Snover",
            "Solgaleo", "Spectrier", "Stakataka", "Stantler", "Starmie", "Staryu", "Stonjourner", "Suicune", "Swinub",
            "Tapu Bulu", "Tapu Fini", "Tapu Koko", "Tapu Lele", "Tauros", "Tentacool", "Tentacruel", "Terrakion",
            "Thundurus", "Tornadus", "Tropius", "Tynamo", "Type: Null", "Tyranitar", "Urshifu", "Uxie", "Vanillish",
            "Vanillite", "Vanilluxe", "Victini", "Vigoroth", "Virizion", "Volcanion", "Volcarona", "Vullaby", "Xerneas",
            "Xurkitree", "Yveltal", "Zacian", "Zamazenta", "Zapdos", "Zarude", "Zekrom", "Zeraora", "Zweilous", "Zygarde"]
ListFluct = ["Breloom", "Corphish", "Crawdaunt", "Drifblim", "Drifloon", "Gulpin", "Hariyama", "Illumise", "Makuhita",
             "Seviper", "Shroomish", "Swalot", "Wailmer", "Wailord"]


word_list = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually","ad hoc","adamant","adaptable","add","addicted","addition","adhesive","adjoining","adjustment","admire","admit","adorable","adventurous","advertisement","advice","advise","afford","afraid","aftermath","afternoon","afterthought","aggressive","agonizing","agree","agreeable","agreement","ahead","air","airplane","airport","ajar","alarm","alcoholic","alert","alike","alive","alleged","allow","alluring","aloof","amazing","ambiguous","ambitious","amount","amuck","amuse","amused","amusement","amusing","analyze","ancient","anger","angle","angry","animal","animated","announce","annoy","annoyed","annoying","answer","ants","anxious","apathetic","apologise","apparatus","apparel","appear","applaud","appliance","appreciate","approval","approve","aquatic","arch","argue","argument","arithmetic","arm","army","aromatic","arrange","arrest","arrive","arrogant","art","ashamed","ask","aspiring","assorted","astonishing","attach","attack","attempt","attend","attract","attraction","attractive","aunt","auspicious","authority","automatic","available","average","avoid","awake","aware","awesome","awful","axiomatic","babies","baby","back","bad","badge","bag","bait","bake","balance","ball","ban","bang","barbarous","bare","base","baseball","bashful","basin","basket","basketball","bat","bath","bathe","battle","bawdy","bead","beam","bear","beautiful","bed","bedroom","beds","bee","beef","befitting","beg","beginner","behave","behavior","belief","believe","bell","belligerent","bells","belong","beneficial","bent","berry","berserk","best","better","bewildered","big","bike","bikes","billowy","bird","birds","birth","birthday","bit","bite","bite-sized","bitter","bizarre","black","black-and-white","blade","bleach","bless","blind","blink","blood","bloody","blot","blow","blue","blue-eyed","blush","blushing","board","boast","boat","boil","boiling","bolt","bomb","bone","book","books","boorish","boot","border","bore","bored","boring","borrow","bottle","bounce","bouncy","boundary","boundless","bow","box","boy","brainy","brake","branch","brash","brass","brave","brawny","breakable","breath","breathe","breezy","brick","bridge","brief","bright","broad","broken","brother","brown","bruise","brush","bubble","bucket","building","bulb","bump","bumpy","burly","burn","burst","bury","bushes","business","bustling","busy","butter","button","buzz","cabbage","cable","cactus","cagey","cake","cakes","calculate","calculating","calculator","calendar","call","callous","calm","camera","camp","can","cannon","canvas","cap","capable","capricious","caption","car","card","care","careful","careless","caring","carpenter","carriage","carry","cars","cart","carve","cast","cat","cats","cattle","cause","cautious","cave","ceaseless","celery","cellar","cemetery","cent","certain","chalk","challenge","chance","change","changeable","channel","charge","charming","chase","cheap","cheat","check","cheer","cheerful","cheese","chemical","cherries","cherry","chess","chew","chicken","chickens","chief","childlike","children","chilly","chin","chivalrous","choke","chop","chubby","chunky","church","circle","claim","clam","clammy","clap","class","classy","clean","clear","clever","clip","cloistered","close","closed","cloth","cloudy","clover","club","clumsy","cluttered","coach","coal","coast","coat","cobweb","coherent","coil","cold","collar","collect","color","colorful","colossal","colour","comb","combative","comfortable","command","committee","common","communicate","company","compare","comparison","compete","competition","complain","complete","complex","concentrate","concern","concerned","condemned","condition","confess","confuse","confused","connect","connection","conscious","consider","consist","contain","continue","control","cooing","cook","cool","cooperative","coordinated","copper","copy","corn","correct","cough","count","country","courageous","cover","cow","cowardly","cows","crabby","crack","cracker","crash","crate","craven","crawl","crayon","crazy","cream","creator","creature","credit","creepy","crib","crime","crook","crooked","cross","crow","crowd","crowded","crown","cruel","crush","cry","cub","cuddly","cultured","cumbersome","cup","cure","curious","curl","curly","current","curtain","curve","curved","curvy","cushion","cut","cute","cycle","cynical","dad","daffy","daily","dam","damage","damaged","damaging","damp","dance","dangerous","dapper","dare","dark","dashing","daughter","day","dazzling","dead","deadpan","deafening","dear","death","debonair","debt","decay","deceive","decide","decision","decisive","decorate","decorous","deep","deeply","deer","defeated","defective","defiant","degree","delay","delicate","delicious","delight","delightful","delirious","deliver","demonic","depend","dependent","depressed","deranged","describe","descriptive","desert","deserted","deserve","design","desire","desk","destroy","destruction","detail","detailed","detect","determined","develop","development","devilish","didactic","different","difficult","digestion","diligent","dime","dinner","dinosaurs","direction","direful","dirt","dirty","disagree","disagreeable","disappear","disapprove","disarm","disastrous","discover","discovery","discreet","discussion","disgusted","disgusting","disillusioned","dislike","dispensable","distance","distinct","distribution","disturbed","divergent","divide","division","dizzy","dock","doctor","dog","dogs","doll","dolls","domineering","donkey","door","double","doubt","doubtful","downtown","drab","draconian","drag","drain","dramatic","drawer","dream","dreary","dress","drink","drip","driving","drop","drown","drum","drunk","dry","duck","ducks","dull","dust","dusty","dynamic","dysfunctional","eager","ear","early","earn","earsplitting","earth","earthquake","earthy","easy","eatable","economic","edge","educate","educated","education","effect","efficacious","efficient","egg","eggnog","eggs","eight","elastic","elated","elbow","elderly","electric","elegant","elfin","elite","embarrass","embarrassed","eminent","employ","empty","enchanted","enchanting","encourage","encouraging","end","endurable","energetic","engine","enjoy","enormous","enter","entertain","entertaining","enthusiastic","envious","equable","equal","erect","erratic","error","escape","ethereal","evanescent","evasive","even","event","examine","example","excellent","exchange","excite","excited","exciting","exclusive","excuse","exercise","exist","existence","exotic","expand","expansion","expect","expensive","experience","expert","explain","explode","extend","extra-large","extra-small","exuberant","exultant","eye","eyes","fabulous","face","fact","fade","faded","fail","faint","fair","fairies","faithful","fall","fallacious","false","familiar","famous","fanatical","fancy","fang","fantastic","far","far-flung","farm","fascinated","fast","fasten","fat","faulty","fax","fear","fearful","fearless","feeble","feeling","feigned","female","fence","fertile","festive","fetch","few","field","fierce","file","fill","film","filthy","fine","finger","finicky","fire","fireman","first","fish","fit","five","fix","fixed","flag","flagrant","flaky","flame","flap","flash","flashy","flat","flavor","flawless","flesh","flight","flimsy","flippant","float","flock","flood","floor","flow","flower","flowers","flowery","fluffy","fluttering","fly","foamy","fog","fold","follow","food","fool","foolish","foot","force","foregoing","forgetful","fork","form","fortunate","found","four","fowl","fragile","frail","frame","frantic","free","freezing","frequent","fresh","fretful","friction","friend","friendly","friends","frighten","frightened","frightening","frog","frogs","front","fruit","fry","fuel","full","fumbling","functional","funny","furniture","furry","furtive","future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gate","gather","gaudy","gaze","geese","general","gentle","ghost","giant","giants","giddy","gifted","gigantic","giraffe","girl","girls","glamorous","glass","gleaming","glib","glistening","glorious","glossy","glove","glow","glue","godly","gold","good","goofy","gorgeous","government","governor","grab","graceful","grade","grain","grandfather","grandiose","grandmother","grape","grass","grate","grateful","gratis","gray","grease","greasy","great","greedy","green","greet","grey","grieving","grin","grip","groan","groovy","grotesque","grouchy","ground","group","growth","grubby","gruesome","grumpy","guarantee","guard","guarded","guess","guide","guiltless","guitar","gullible","gun","gusty","guttural","habitual","hair","haircut","half","hall","hallowed","halting","hammer","hand","handle","hands","handsome","handsomely","handy","hang","hanging","hapless","happen","happy","harass","harbor","hard","hard-to-find","harm","harmonious","harmony","harsh","hat","hate","hateful","haunt","head","heady","heal","health","healthy","heap","heartbreaking","heat","heavenly","heavy","hellish","help","helpful","helpless","hesitant","hideous","high","high-pitched","highfalutin","hilarious","hill","hissing","historical","history","hobbies","hole","holiday","holistic","hollow","home","homeless","homely","honey","honorable","hook","hop","hope","horn","horrible","horse","horses","hose","hospitable","hospital","hot","hour","house","houses","hover","hug","huge","hulking","hum","humdrum","humor","humorous","hungry","hunt","hurried","hurry","hurt","hushed","husky","hydrant","hypnotic","hysterical","ice","icicle","icky","icy","idea","identify","idiotic","ignorant","ignore","ill","ill-fated","ill-informed","illegal","illustrious","imaginary","imagine","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","impress","improve","impulse","incandescent","include","income","incompetent","inconclusive","increase","incredible","industrious","industry","inexpensive","infamous","influence","inform","inject","injure","ink","innate","innocent","inquisitive","insect","insidious","instinctive","instruct","instrument","insurance","intelligent","intend","interest","interesting","interfere","internal","interrupt","introduce","invent","invention","invincible","invite","irate","iron","irritate","irritating","island","itch","itchy","jaded","jagged","jail","jam","jar","jazzy","jealous","jeans","jelly","jellyfish","jewel","jittery","jobless","jog","join","joke","jolly","joyous","judge","judicious","juggle","juice","juicy","jumbled","jump","jumpy","juvenile","kaput","keen","kettle","key","kick","kill","kind","kindhearted","kindly","kiss","kittens","kitty","knee","kneel","knife","knit","knock","knot","knotty","knowing","knowledge","knowledgeable","known","label","labored","laborer","lace","lackadaisical","lacking","ladybug","lake","lame","lamentable","lamp","land","language","languid","large","last","late","laugh","laughable","launch","lavish","lazy","lean","learn","learned","leather","left","leg","legal","legs","lethal","letter","letters","lettuce","level","lewd","library","license","lick","lie","light","lighten","like","likeable","limit","limping","line","linen","lip","liquid","list","listen","literate","little","live","lively","living","load","loaf","lock","locket","lonely","long","long-term","longing","look","loose","lopsided","loss","loud","loutish","love","lovely","loving","low","lowly","lucky","ludicrous","lumber","lumpy","lunch","lunchroom","lush","luxuriant","lying","lyrical","macabre","machine","macho","maddening","madly","magenta","magic","magical","magnificent","maid","mailbox","majestic","makeshift","male","malicious","mammoth","man","manage","maniacal","many","marble","march","mark","marked","market","married","marry","marvelous","mask","mass","massive","match","mate","material","materialistic","matter","mature","meal","mean","measly","measure","meat","meaty","meddle","medical","meek","meeting","mellow","melodic","melt","melted","memorize","memory","men","mend","merciful","mere","mess up","messy","metal","mice","middle","mighty","military","milk","milky","mind","mindless","mine","miniature","minister","minor","mint","minute","miscreant","miss","mist","misty","mitten","mix","mixed","moan","moaning","modern","moldy","mom","momentous","money","monkey","month","moon","moor","morning","mother","motion","motionless","mountain","mountainous","mourn","mouth","move","muddle","muddled","mug","multiply","mundane","murder","murky","muscle","mushy","mute","mysterious","nail","naive","name","nappy","narrow","nasty","nation","natural","naughty","nauseating","near","neat","nebulous","necessary","neck","need","needle","needless","needy","neighborly","nerve","nervous","nest","new","next","nice","nifty","night","nimble","nine","nippy","nod","noise","noiseless","noisy","nonchalant","nondescript","nonstop","normal","north","nose","nostalgic","nosy","note","notebook","notice","noxious","null","number","numberless","numerous","nut","nutritious","nutty","oafish","oatmeal","obedient","obeisant","obese","obey","object","obnoxious","obscene","obsequious","observant","observation","observe","obsolete","obtain","obtainable","occur","ocean","oceanic","odd","offbeat","offend","offer","office","oil","old","old-fashioned","omniscient","one","onerous","open","opposite","optimal","orange","oranges","order","ordinary","organic","ossified","outgoing","outrageous","outstanding","oval","oven","overconfident","overflow","overjoyed","overrated","overt","overwrought","owe","own","pack","paddle","page","pail","painful","painstaking","paint","pale","paltry","pan","pancake","panicky","panoramic","paper","parallel","parcel","parched","park","parsimonious","part","partner","party","pass","passenger","past","paste","pastoral","pat","pathetic","pause","payment","peace","peaceful","pear","peck","pedal","peel","peep","pen","pencil","penitent","perfect","perform","periodic","permissible","permit","perpetual","person","pest","pet","petite","pets","phobic","phone","physical","picayune","pick","pickle","picture","pie","pies","pig","pigs","pin","pinch","pine","pink","pipe","piquant","pizzas","place","placid","plain","plan","plane","planes","plant","plantation","plants","plastic","plate","plausible","play","playground","pleasant","please","pleasure","plot","plough","plucky","plug","pocket","point","pointless","poised","poison","poke","polish","polite","political","pollution","poor","pop","popcorn","porter","position","possess","possessive","possible","post","pot","potato","pour","powder","power","powerful","practice","pray","preach","precede","precious","prefer","premium","prepare","present","preserve","press","pretend","pretty","prevent","previous","price","pricey","prick","prickly","print","private","probable","produce","productive","profit","profuse","program","promise","property","prose","protect","protective","protest","proud","provide","psychedelic","psychotic","public","puffy","pull","pump","pumped","punch","puncture","punish","punishment","puny","purple","purpose","purring","push","pushy","puzzled","puzzling","quack","quaint","quarrelsome","quarter","quartz","queen","question","questionable","queue","quick","quickest","quicksand","quiet","quill","quilt","quince","quirky","quiver","quixotic","quizzical","rabbit","rabbits","rabid","race","racial","radiate","ragged","rail","railway","rain","rainstorm","rainy","raise","rake","rambunctious","rampant","range","rapid","rare","raspy","rat","rate","ratty","ray","reach","reaction","reading","ready","real","realize","reason","rebel","receipt","receive","receptive","recess","recognise","recondite","record","red","reduce","redundant","reflect","reflective","refuse","regret","regular","reign","reject","rejoice","relation","relax","release","relieved","religion","rely","remain","remarkable","remember","remind","reminiscent","remove","repair","repeat","replace","reply","report","representative","reproduce","repulsive","request","rescue","resolute","resonant","respect","responsible","rest","retire","return","reward","rhetorical","rhyme","rhythm","rice","rich","riddle","rifle","right","righteous","rightful","rigid","ring","rings","rinse","ripe","risk","ritzy","river","road","roasted","rob","robin","robust","rock","rod","roll","romantic","roof","room","roomy","root","rose","rot","rotten","rough","round","route","royal","rub","ruddy","rude","ruin","rule","run","rural","rush","rustic","ruthless","sable","sack","sad","safe","sail","salt","salty","same","sand","sassy","satisfy","satisfying","save","savory","saw","scale","scandalous","scarce","scare","scarecrow","scared","scarf","scary","scatter","scattered","scene","scent","school","science","scientific","scintillating","scissors","scold","scorch","scrape","scratch","scrawny","scream","screeching","screw","scribble","scrub","sea","seal","search","seashore","seat","second","second-hand","secret","secretary","secretive","sedate","seed","seemly","selection","selective","self","selfish","sense","separate","serious","servant","serve","settle","shade","shaggy","shake","shaky","shallow","shame","shape","share","sharp","shave","sheep","sheet","shelf","shelter","shiny","ship","shirt","shiver","shivering","shock","shocking","shoe","shoes","shop","short","show","shrill","shrug","shut","shy","sick","side","sidewalk","sigh","sign","signal","silent","silk","silky","silly","silver","simple","simplistic","sin","sincere","sink","sip","sister","sisters","six","size","skate","ski","skillful","skin","skinny","skip","skirt","sky","slap","slave","sleep","sleepy","sleet","slim","slimy","slip","slippery","slope","sloppy","slow","small","smart","smash","smell","smelly","smile","smiling","smoggy","smoke","smooth","snail","snails","snake","snakes","snatch","sneaky","sneeze","sniff","snobbish","snore","snotty","snow","soak","soap","society","sock","soda","sofa","soft","soggy","solid","somber","son","song","songs","soothe","sophisticated","sordid","sore","sort","sound","soup","sour","space","spade","spare","spark","sparkle","sparkling","special","spectacular","spell","spicy","spiders","spiffy","spiky","spill","spiritual","spiteful","splendid","spoil","sponge","spooky","spoon","spot","spotless","spotted","spotty","spray","spring","sprout","spurious","spy","squalid","square","squash","squeak","squeal","squealing","squeamish","squeeze","squirrel","stage","stain","staking","stale","stamp","standing","star","stare","start","statement","station","statuesque","stay","steadfast","steady","steam","steel","steep","steer","stem","step","stereotyped","stew","stick","sticks","sticky","stiff","stimulating","stingy","stir","stitch","stocking","stomach","stone","stop","store","stormy","story","stove","straight","strange","stranger","strap","straw","stream","street","strengthen","stretch","string","strip","striped","stroke","strong","structure","stuff","stupendous","stupid","sturdy","subdued","subsequent","substance","substantial","subtract","succeed","successful","succinct","suck","sudden","suffer","sugar","suggest","suggestion","suit","sulky","summer","sun","super","superb","superficial","supply","support","suppose","supreme","surprise","surround","suspect","suspend","swanky","sweater","sweet","sweltering","swift","swim","swing","switch","symptomatic","synonymous","system","table","taboo","tacit","tacky","tail","talented","talk","tall","tame","tan","tangible","tangy","tank","tap","tart","taste","tasteful","tasteless","tasty","tawdry","tax","teaching","team","tearful","tease","tedious","teeny","teeny-tiny","teeth","telephone","telling","temper","temporary","tempt","ten","tendency","tender","tense","tent","tenuous","terrible","terrific","terrify","territory","test","tested","testy","texture","thank","thankful","thaw","theory","therapeutic","thick","thin","thing","things","thinkable","third","thirsty","thought","thoughtful","thoughtless","thread","threatening","three","thrill","throat","throne","thumb","thunder","thundering","tick","ticket","tickle","tidy","tie","tiger","tight","tightfisted","time","tin","tiny","tip","tire","tired","tiresome","title","toad","toe","toes","tomatoes","tongue","tooth","toothbrush","toothpaste","toothsome","top","torpid","touch","tough","tour","tow","towering","town","toy","toys","trace","trade","trail","train","trains","tramp","tranquil","transport","trap","trashy","travel","tray","treat","treatment","tree","trees","tremble","tremendous","trick","tricky","trip","trite","trot","trouble","troubled","trousers","truck","trucks","truculent","true","trust","truthful","try","tub","tug","tumble","turkey","turn","twig","twist","two","type","typical","ubiquitous","ugliest","ugly","ultra","umbrella","unable","unaccountable","unadvised","unarmed","unbecoming","unbiased","uncle","uncovered","understood","underwear","undesirable","undress","unequal","unequaled","uneven","unfasten","unhealthy","uninterested","unique","unit","unite","unkempt","unknown","unlock","unnatural","unpack","unruly","unsightly","unsuitable","untidy","unused","unusual","unwieldy","unwritten","upbeat","uppity","upset","uptight","use","used","useful","useless","utopian","utter","uttermost","vacation","vacuous","vagabond","vague","valuable","value","van","vanish","various","vase","vast","vegetable","veil","vein","vengeful","venomous","verdant","verse","versed","vessel","vest","victorious","view","vigorous","violent","violet","visit","visitor","vivacious","voice","voiceless","volatile","volcano","volleyball","voracious","voyage","vulgar","wacky","waggish","wail","wait","waiting","wakeful","walk","wall","wander","wandering","want","wanting","war","warlike","warm","warn","wary","wash","waste","wasteful","watch","water","watery","wave","waves","wax","way","weak","wealth","wealthy","weary","weather","week","weigh","weight","welcome","well-groomed","well-made","well-off","well-to-do","wet","wheel","whimsical","whine","whip","whirl","whisper","whispering","whistle","white","whole","wholesale","wicked","wide","wide-eyed","wiggly","wild","wilderness","willing","wind","window","windy","wine","wing","wink","winter","wipe","wire","wiry","wise","wish","wistful","witty","wobble","woebegone","woman","womanly","women","wonder","wonderful","wood","wooden","wool","woozy","word","work","workable","worm","worried","worry","worthless","wound","wrap","wrathful","wreck","wren","wrench","wrestle","wretched","wriggle","wrist","writer","writing","wrong","wry","x-ray","yak","yam","yard","yarn","yawn","year","yell","yellow","yielding","yoke","young","youthful","yummy","zany","zealous","zebra","zephyr","zesty","zinc","zip","zipper","zippy","zonked","zoo","zoom"]

print(len(ListFast))
print(len(ListMFast))
print(len(ListMSlow))
print(len(ListSlow))

mymods = 0

client = commands.Bot(command_prefix='!')
@commands.cooldown(1,5,commands.BucketType.user)
# Limit how often a command can be used, (num per, seconds, BucketType)

@commands.max_concurrency(2, per=BucketType.default, wait=False)


@client.event
async def on_ready():
    print('Bot is ready.')

#@client.event
#async def on_reaction_add(reaction, user):
#    if reaction.emoji == "<:SmashGamer:764162333240066058":
 #       role = discord.utils.get(user.server.roles, name="Smash Gamer")
  #      print("pog")
   #     await client.add_roles(user, role)
    #else:
     #   print("unpog")


@client.event
async def on_message(message):
    global mymods
    if message.author.id == 694319088830251112:
        return
    #if message.author == client.user:
     #   return
    #elif (message.author.id == 218903339990122496 or message.author.id == 341395025545920513 or message.author.id == 192391343757066240) and message.content.startswith('pog.'):
    #    return

    str1 = message.content
    str2 = "Fuck english"
    str7 = "buzz"
    #str8 = "r"
    str9 = "stuff"
    str10 = "fucking"
    str11 = "hello there"
    if str1 == str1:
        await message.remove_reaction("\U0001F913",message.author)
    if str1.lower() == str2.lower():
        await message.pin()
    #if str1.lower() == str3.lower() or str1.lower() == str4.lower() or str1.lower() == str5.lower() :
    #    await message.author.kick()
    if message.author.id == 717220147743424603:
       await message.channel.send(f'Fuck off')
    if "\U0001F913" in str1:
        await message.delete()
    if str1.lower() == "mod".lower():
        mymods = message.author.id
        #await message.channel.send(mods)
        await message.delete()
        await message.channel.send(f'{message.author} Imperator Maximus est')
    #await message.channel.send(mymods)
    #members = [message.guild.get_member(member_id) for member_id in mods]
    #await message.channel.send(mods)
    if str1.lower() == str7.lower() or str1.lower() == "blip".lower() or str1.lower() == "b".lower() or str1.lower() == "blammo".lower():

        mil = time.time()
        digits = [int(d) for d in str(math.floor(mil))]
        mil1 = round(mil,4)
        decs = (mil1/1) - (mil1//1)

        time1 = time.strftime("%I:%M:%S")
        await message.delete()
        await message.channel.send(f'{message.author.nick}\n{time1}, {digits[-2]}{digits[-1]}{decs}')
        #print(mod)
        #await message.channel.send(mods)
        vc = message.author.voice.channel

        for member in vc.members:
            #await message.channel.send(member.id)
            #await message.channel.send(mymods)
            if member.id == mymods:
                #await message.channel.send(member)
            #if member.id == 689990282665918488:  # bering
            #if member.id == 414936271861973012: #abhinav
            #if member.id == 488020727702749185: #jasmine
            #if member.id == 515178574660239380: #eli
            #if member.id == 672146682791854091:
            #if member.id == 693550665926180914:
            #if member.id == 694319961765576744:
                if member.voice.self_mute != True:
                    await member.edit(mute=True)
                    time.sleep(0.3)
                    await member.edit(mute=False)
    #if str1.lower() == str8.lower():
        #print(message.author, message.created_at)
     #   vc = message.author.voice.channel
      #  for member in vc.members:
            #if member.id == 689990282665918488: #bering
            #if member.id == 414936271861973012: #abhinav
            #if member.id == 488020727702749185: #jasmine
            #if member.id == 515178574660239380: #eli
            #if member.id == 672146682791854091:
            #if member.id == 693550665926180914:
       #     if member.id == 694319961765576744:
        #        await member.edit(mute=False)
   # if str9.lower() in str1.lower():
   #     await message.channel.send("I'm stuff")
    #if str10.lower() in str1.lower():
    #    await message.channel.send("What about regular")

    if str11.lower() in str1.lower():
        await message.channel.send("General Kenobi")
    #if "kushaal" in str1.lower():
    #    await message.channel.send("<@672146682791854091>")
    if str1.lower() == "c".lower():
        await message.delete()
        await message.channel.send("------------------------------------------------------------------------")
    await client.process_commands(message)





@client.command()
async def type(ctx, member: discord.Member):
    await ctx.send(ctx.message.author.id)
    await ctx.send(member.id)
def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel

@client.command(pass_context=True)
#@commands.has_role("Bot")
async def hehe(ctx):
        member = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Sigmas")
        await ctx.channel.purge(limit=1)
        await member.add_roles(role)

async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await client.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            continue

@client.command(pass_context=True)
async def exp(ctx):
    message = await ctx.send("Which Pokemon are you leveling up?")
    pkmn = await get_input_of_type(str, ctx)
    await ctx.channel.purge(limit=1)
    await message.edit(content="How much exp do they currently have?")
    exp0 = await get_input_of_type(int, ctx)
    await ctx.channel.purge(limit=1)
    if pkmn in ListErratic:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        await ctx.channel.purge(limit=1)
        if n >= 2 and n <= 50:
            exp = (1 / 50) * pow(n, 3) * (100 - n)
        elif n > 50 and n <= 68:
            exp = (1 / 100) * pow(n, 3) * (150 - n)
        elif n > 68 and n <= 98:
            exp = (1 / 1500) * pow(n, 3) * (1911 - 10 * n)
        elif n > 98 and n <= 100:
            exp = (1 / 100) * pow(n, 3) * (160 - n)
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        #await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        #await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        #await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        #await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        #await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)


    elif pkmn in ListFast:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        if n >= 2 and n <= 100:
            exp = 0.8 * pow(n, 3)
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        # await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        # await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        # await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        # await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        # await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))        
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)

    elif pkmn in ListMFast:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        await ctx.channel.purge(limit=1)
        if n >= 2 and n <= 100:
            exp = pow(n, 3)
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        #await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        #await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        #await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        #await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        #await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)

    elif pkmn in ListMSlow:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        await ctx.channel.purge(limit=1)
        if n >= 2 and n <= 100:
            exp = 1.2 * pow(n, 3) - 15 * pow(n, 2) + 100 * n - 140
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        #await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        #await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        #await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        #await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        #await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)

    elif pkmn in ListSlow:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        await ctx.channel.purge(limit=1)
        if n >= 2 and n <= 100:
            exp = 1.25 * pow(n, 3)
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        #await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        #await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        #await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        #await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        #await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)


    elif pkmn in ListFluct:
        await message.edit(content="Which level do you want to grow your Pokemon to?")
        n = await get_input_of_type(int, ctx)
        await ctx.channel.purge(limit=1)
        if n >= 2 and n <= 15:
            exp = (1 / 150) * pow(n, 3) * (n + 73)
        elif n > 15 and n <= 36:
            exp = (1 / 50) * pow(n, 3) * (n + 14)
        elif n > 36 and n <= 100:
            exp = (1 / 50) * pow(n, 3) * (0.5 * n + 32)
        else:
            await message.edit(content="Pokemon can't level up past level 100!")

        exp = exp - exp0

        exp = math.floor(exp)
        #await ctx.send("Total experience needed: " + str(exp))
        candyxs = math.ceil(exp / 100)
        #await ctx.send("XS candies needed: " + str(candyxs))

        candys = math.ceil(exp / 800)
        #await ctx.send("S candies needed: " + str(candys))

        candym = math.ceil(exp / 3000)
        #await ctx.send("M candies needed: " + str(candym))

        candyl = math.ceil(exp / 10000)
        #await ctx.send("L candies needed: " + str(candyl))

        candyxl = math.ceil(exp / 30000)
        #await ctx.send("XL candies needed: " + str(candyxl))
        res = ''
        res = res + "XS: " + str(candyxs) + "\nS: " + str(candys) + "\nM: " + str(candym) + "\nL: " + str(
            candyl) + "\nXL: " + str(candyxl)
        await message.edit(content=res)

@client.command()
async def kick(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    #await member.kick()
    await ctx.send(f'{member} has been kicked')

@client.command()
#@commands.has_any_role(620989628010201089)
async def clear(ctx, *, amount):
    await ctx.channel.purge(limit=int(amount))

@client.command(passContext=True)
async def dice(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(random.randint(1,6))


@client.command()
async def bj(ctx):
        await ctx.channel.purge(limit=1)
        #playing = False
        #if playing:
        #    await ctx.send("Wait a moment")
        #    return
        play = random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11]) + random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11])
        deal = random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11]) + random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11])

        message = await ctx.send(f'player hand: {play}\ndealer hand: {deal}')

        while play < 21 and deal < 21:
            await ctx.send("Do you want hit (h) or stand (s)?")
            option = await get_input_of_type(str, ctx)
            await ctx.channel.purge(limit=2)
            if option == "h":
                if deal < 17:
                    play = play + random.choice([2,3,4,5,6,7,8,9,10,10,10,10,11])
                    deal = deal + random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
                    await message.edit(content=f'player hand: {play}\ndealer hand: {deal} ')
                else:
                    play = play + random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
                    await message.edit(content=f'player hand: {play}\ndealer hand: {deal}')
            elif option == "s":
                while deal < 17:
                    deal = deal + random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
                    await message.edit(content=f'player hand: {play}\ndealer hand: {deal}')
                #await ctx.send(f'player hand: {play}\ndealer hand: {deal}')
                break
            elif option == "stop":
                break
        await message.edit(content=f'player hand: {play}\ndealer hand: {deal}')
        if play == deal:
            await message.edit(content=f'You tied! \nplayer hand: {play}\ndealer hand: {deal} ')
        elif play <= 21 and deal <= 21 and play < deal:
            await message.edit(content=f'You lose! \nplayer hand: {play}\ndealer hand: {deal} ')
        elif play <= 21 and deal <= 21 and play > deal:
            await message.edit(content=f'You win! \nplayer hand: {play}\ndealer hand: {deal} ')
        elif play > 21:
            await message.edit(content=f'You lose! \nplayer hand: {play}\ndealer hand: {deal} ')
        elif play <= 21:
            await message.edit(content=f'You win!\nplayer hand: {play}\ndealer hand: {deal} ')
        else:
            await message.edit(content=f'You lose! \nplayer hand: {play}\ndealer hand: {deal} ')
        #playing = False





@client.command()
async def frac(ctx, * , message):
    decimal = float(message)
    a = 0
    b = 1
    c = 1
    d = 1
    mediant = (a + c) / (b + d)
    i = 0
    while i < 1000:
        i = i + 1
        if decimal < mediant:
            d = b + d
            c = a + c
            mediant = (a + c) / (b + d)
        elif decimal > mediant:
            a = a + c
            b = b + d
            mediant = (a + c) / (b + d)
        else:
            break

    await ctx.send(Fraction(a + c, b + d))
    #await ctx.send(mediant)

@client.command(passContext=True)
async def word(ctx):
    await ctx.channel.purge(limit=1)
    words = []
    for each in word_list:
        if len(each) == 5:
            word_list.append(each)
    word = random.choice(words)
    tries = 6

    while tries > 0:
        await ctx.send("Guess a five letter word")
        guess = await get_input_of_type(str, ctx)
        if len(guess) != 5:
            await ctx.send("Bruh. That's not a five letter word. Learn to play the game.")
            break
        spl1 = list(word)
        spl2 = list(guess)
        right = 0
        ish = 0
        for i in spl2:
            if spl2.index(i) == spl1.index(i):
                right = right + 1
            elif i in spl1 and spl2.index(i) != spl1.index(i):
                ish = ish + 1
        await ctx.send(f'You have {right} letters in the correct place and {ish} letters correct, but in the wrong place. ')
        tries = tries - 1





@client.command(passContext=True)
async def guess(ctx, *, message):
    await ctx.channel.purge(limit=1)
    turns = int(message)
    guesses = ''
    word = random.choice(word_list)
    blank = ''
    print(word)
    i = 0
    #while i < len(word):
    #    blank += "- "
    #    i += 1
    #await ctx.send(blank)

    while turns > 0:
        failed = 0
        for char in word:


            if char in guesses:
                #blank.insert(char,0)
                blank += char

            else:
                failed += 1
                blank += "- "

        await ctx.send(blank)
        blank = ''
        if failed == 0:
            await ctx.send("You win!")
            await ctx.send(f'The word was "{word}" ')
            break
        await ctx.send("Guess a letter.")
        guess = await get_input_of_type(str, ctx)
        guess = guess.lower()
        if len(guess) != 1:
            await ctx.send("Bruh, it needs to be one letter")
        if guess not in word:
            if guess in guesses:
                await ctx.send("You've already guessed that!")

            else:
                turns -= 1
                await ctx.send(f'Rip, you have {turns} more guesses')
                if turns == 0:
                    await ctx.send("You lose!")
                    await ctx.send(f'The word was "{word}" ')
        guesses += guess
def remove(string):
    return string.replace(" ", "_")

@client.command(passContext=True)
async def wiki(ctx, *, message):
    await ctx.channel.purge(limit=1)
    msg = remove(message)
    await ctx.send(f'https://wikipedia.org/wiki/{msg}')


@client.command(passContext=True)
async def goog(ctx, *, message):
    await ctx.channel.purge(limit=1)
    msg = remove(message)
    await ctx.send(f'https://www.google.com/search?q={msg}')

@client.command(passContext=True)
async def anagram(ctx, *, message):
    await ctx.channel.purge(limit=1)
    turns = int(message)
    word = random.choice(word_list)
    scr = string_utils.shuffle(word)
    print(word)
    while turns > 0:
        await ctx.send(f'Unscramble this word: {scr}')
        guess = await get_input_of_type(str, ctx)
        if word.lower() == guess.lower():
            await ctx.send("You win!")
            await ctx.send(f'The word was "{word}"')
            turns = -100
        else:
            turns -= 1
            await ctx.send(f'Rip, try again. You have {turns} more guesses')
    if turns == 0:
        await ctx.send("You lose!")
        await ctx.send(f'The word was "{word}"')

@client.command(passContext=True)
async def um(ctx, *, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await member.edit(mute=False)

@client.command(aliases=['1', 'GeorgeWashington'])
async def washington(ctx):
    await ctx.send(
        f'Name: George Washington\nNumber: First President\nParty: Unaffiliated(Federalist)\nMore Info: https://en.wikipedia.org/wiki/George_Washington')


@client.command(aliases=['2', 'JohnAdams'])
async def adams2(ctx):
    await ctx.send(
        f'Name: John Adams\nNumber: Second President\nParty: Federalist\nMore Info: https://en.wikipedia.org/wiki/John_Adams')


@client.command(aliases=['3', 'ThomasJefferson'])
async def jefferson(ctx):
    await ctx.send(
        f'Name: Thomas Jefferson\nNumber: Third President\nParty: Democratic-Republican\nMore Info: https://en.wikipedia.org/wiki/Thomas_Jefferson')


@client.command(aliases=['4', 'JamesMadison'])
async def madison(ctx):
    await ctx.send(
        f'Name: James Madison\nNumber: Fourth President\nParty: Democratic-Republican\nMore Info: https://en.wikipedia.org/wiki/James_Madison')


@client.command(aliases=['5', 'JamesMonroe'])
async def monroe(ctx):
    await ctx.send(
        f'Name: James Monroe\nNumber: Fifth President\nParty: Democratic-Republican\nMore Info: https://en.wikipedia.org/wiki/James_Monroe')


@client.command(aliases=['6', 'JohnQuincyAdams'])
async def adams6(ctx):
    await ctx.send(
        f'Name: John Quincy Adams\nNumber: Sixth President\nParty: Democratic-Republican\nMore Info: https://en.wikipedia.org/wiki/John_Quincy_Adams')


@client.command(aliases=['7', 'AndrewJackson'])
async def jackson(ctx):
    await ctx.send(
        f'Name: Andrew Jackson\nNumber: Seventh President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Andrew_Jackson')


@client.command(aliases=['8', 'MartinVanBuren'])
async def vanburen(ctx):
    await ctx.send(
        f'Name: Martin Van Buren\nNumber: Eighth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Martin_Van_Buren')


@client.command(aliases=['9', 'WilliamHenryHarrison', 'WilliamHarrison'])
async def harrison9(ctx):
    await ctx.send(
        f'Name: William Henry Harrison\nNumber: Ninth President\nParty: Whig\nMore Info: https://en.wikipedia.org/wiki/William_Henry_Harrison')


@client.command(aliases=['10', 'JohnTyler'])
async def tyler(ctx):
    await ctx.send(
        f'Name: John Tyler\nNumber: Tenth President\nParty: Whig\nMore Info: https://en.wikipedia.org/wiki/John_Tyler')


@client.command(aliases=['11', 'JamesKPolk', 'JamesKnoxPolk', 'JamesPolk'])
async def polk(ctx):
    await ctx.send(
        f'Name: James K. Polk\nNumber: Eleventh President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/James_K._Polk')


@client.command(aliases=['12', 'ZacharyTaylor'])
async def taylor(ctx):
    await ctx.send(
        f'Name: Zachary Taylor\nNumber: Twelfth President\nParty: Whig\nMore Info: https://en.wikipedia.org/wiki/Zachary_Taylor')


@client.command(aliases=['13', 'MillardFillmore'])
async def fillmore(ctx):
    await ctx.send(
        f'Name: Millard Fillmore\nNumber: Thirteenth President\nParty: Whig\nMore Info: https://en.wikipedia.org/wiki/Millard_Fillmore')


@client.command(aliases=['14', 'FranklinPierce'])
async def pierce(ctx):
    await ctx.send(
        f'Name: Franklin Pierce\nNumber: Fourteenth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Franklin_Pierce')


@client.command(aliases=['15', 'JamesBuchanan'])
async def buchanan(ctx):
    await ctx.send(
        f'Name: James Buchanan\nNumber: Fifteenth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/James_Buchanan')


@client.command(aliases=['16', 'AbrahamLincoln', 'HonestAbe'])
async def lincoln(ctx):
    await ctx.send(
        f'Name: Abraham Lincoln\nNumber: Sixteenth President\nParty: Republican/National Union\nMore Info: https://en.wikipedia.org/wiki/Abraham_Lincoln')


@client.command(aliases=['17', 'AndrewJohnson'])
async def johnson17(ctx):
    await ctx.send(
        f'Name: Andrew Johnson\nNumber: Seventeenth President\nParty: Republican/National Union\nMore Info: https://en.wikipedia.org/wiki/Andrew_Johnson')


@client.command(aliases=['18', 'UlyssesSGrant', 'UlyssesGrant'])
async def grant(ctx):
    await ctx.send(
        f'Name: Ulysses S Grant\nNumber: Eighteenth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Ulysses_S._Grant')


@client.command(aliases=['19', 'RutherfordBHayes', 'RutherfordHayes'])
async def hayes(ctx):
    await ctx.send(
        f'Name: Rutherford B Hayes\nNumber: Nineteenth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Rutherford_B._Hayes')


@client.command(aliases=['20', 'JamesAGarfield', 'JamesGarfield'])
async def garfield(ctx):
    await ctx.send(
        f'Name: James A Garfield\nNumber: Twentieth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/James_A._Garfield')


@client.command(aliases=['21', 'ChesterAArthur', 'ChesterArthur'])
async def arthur(ctx):
    await ctx.send(
        f'Name: Chester A Arthur\nNumber: Twenty-First President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Chester_A._Arthur')


@client.command(aliases=['22', 'GroverCleveland', '24'])
async def cleveland22(ctx):
    await ctx.send(
        f'Name: Grover Cleveland\nNumber: Twenty-Second and Twenty-Fourth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Grover_Cleveland')


@client.command(aliases=['23', 'BenjaminHarrison'])
async def harrison23(ctx):
    await ctx.send(
        f'Name: Benjamin Harrison\nNumber: Twenty-Third President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Benjamin_Harrison')


@client.command(aliases=['25', 'WilliamMcKinley'])
async def mckinley(ctx):
    await ctx.send(
        f'Name: William McKinley\nNumber: Twenty-Fifth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/William_McKinley')


@client.command(aliases=['26', 'TheodoreRoosevelt'])
async def roosevelt26(ctx):
    await ctx.send(
        f'Name: Theodore Roosevelt\nNumber: Twenty-Sixth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Theodore_Roosevelt')


@client.command(aliases=['27', 'WilliamHowardTaft', 'WilliamHTaft', 'WilliamTaft'])
async def taft(ctx):
    await ctx.send(
        f'Name: William Howard Taft\nNumber: Twenty-Seventh President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/William_Howard_Taft')


@client.command(aliases=['28', 'WoodrowWilson'])
async def wilson(ctx):
    await ctx.send(
        f'Name: Woodrow Wilson\nNumber: Twenty-Eighth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Woodrow_Wilson')


@client.command(aliases=['29', 'WarrenGHarding', 'WarrenHarding', 'WarrenGamalielHarding'])
async def harding(ctx):
    await ctx.send(
        f'Name: Warren G Harding\nNumber: Twenty-Ninth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Warren_G._Harding')


@client.command(aliases=['30', 'CalvinCoolidge'])
async def coolidge(ctx):
    await ctx.send(
        f'Name: Calvin Coolidge\nNumber: Thirtieth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Calvin_Coolidge')


@client.command(aliases=['31', 'HerbertHoover'])
async def hoover(ctx):
    await ctx.send(
        f'Name: Herbert Hoover\nNumber: Thirty-First President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Herbert_Hoover')


@client.command(aliases=['32', 'FranklinDRoosevelt', 'FDR', 'FranklinDelanoRoosevelt', 'FranklinRoosevelt'])
async def roosevelt32(ctx):
    await ctx.send(
        f'Name: Franklin D. Roosevelt\nNumber: Thirty-Second President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Franklin_D._Roosevelt')


@client.command(aliases=['33', 'HarrySTruman', 'HarryTruman'])
async def truman(ctx):
    await ctx.send(
        f'Name: Harry S Truman\nNumber: Thirty-Third President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Harry_S._Truman')


@client.command(aliases=['34', 'DwightDEisenhower', 'DwightEisenhower', 'DwightDavidEisenhower', 'Ike'])
async def eisenhower(ctx):
    await ctx.send(
        f'Name: Dwight D Eisenhower\nNumber: Thirty-Fourth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Dwight_D._Eisenhower')


@client.command(aliases=['35', 'JohnFKennedy', 'JohnFitzgeraldKennedy', 'JohnKennedy', 'JFK'])
async def kennedy(ctx):
    await ctx.send(
        f'Name: John F Kennedy\nNumber: Thirty-Fifth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/John_F._Kennedy')


@client.command(aliases=['36', 'LyndonBJohnson', 'LBJ', 'LyndonJohnson', 'LyndonBainesJohnson'])
async def johnson36(ctx):
    await ctx.send(
        f'Name: Lyndon B Johnson\nNumber: Thirty-Sixth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Lyndon_B._Johnson')


@client.command(aliases=['37', 'RichardNixon', 'TrickyDick'])
async def nixon(ctx):
    await ctx.send(
        f'Name: Richard Nixon\nNumber: Thirty-Seventh President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Richard_Nixon')


@client.command(aliases=['38', 'GeraldFord'])
async def ford(ctx):
    await ctx.send(
        f'Name: Gerald Ford\nNumber: Thirty-Eighth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Gerald_Ford')


@client.command(aliases=['39', 'JimmyCarter'])
async def carter(ctx):
    await ctx.send(
        f'Name: Jimmy Carter\nNumber: Thirty-Ninth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Jimmy_Carter')


@client.command(aliases=['40', 'RonaldReagan'])
async def reagan(ctx):
    await ctx.send(
        f'Name: Ronald Reagan\nNumber: Fourtieth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Ronald_Reagan')


@client.command(aliases=['41', 'GeorgeHWBush', 'GeorgeHerbertWalkerBush'])
async def bush41(ctx):
    await ctx.send(
        f'Name: George H W Bush\nNumber: Fourty-First President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/George_H._W._Bush')


@client.command(aliases=['42', 'BillClinton'])
async def clinton(ctx):
    await ctx.send(
        f'Name: Bill Clinton\nNumber: Fourty-Second President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Bill_Clinton')


@client.command(aliases=['43', 'GeorgeWBush', 'GeorgeWalkerBush'])
async def bush43(ctx):
    await ctx.send(
        f'Name: George W Bush\nNumber: Fourty-Third President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/George_W._Bush')


@client.command(aliases=['44', 'BarackObama'])
async def obama(ctx):
    await ctx.send(
        f'Name: Barack Obama\nNumber: Fourty-Fourth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Barack_Obama')


@client.command(aliases=['45', 'DonaldTrump', 'Cheeto'])
async def trump(ctx):
    await ctx.send(
        f'Name: Donald Trump\nNumber: Fourty-Fifth President\nParty: Republican\nMore Info: https://en.wikipedia.org/wiki/Donald_Trump')

@client.command(aliases=['46', 'JoeBiden', 'Sleepy'])
async def biden(ctx):
    await ctx.send(
        f'Name: Joseph Biden\nNumber: Fourty-Sixth President\nParty: Democratic\nMore Info: https://en.wikipedia.org/wiki/Joe_Biden')

@client.command(passContext=True)
async def qr(ctx, text, person, channel):
    await ctx.channel.purge(limit=1)
    day = date.today().strftime("%m/%d/%Y")
    await ctx.send(f'"{text}" - {person}, {channel} ({day})')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    await ctx.channel.purge(limit=1)
    responses = ['It is certain.', 'Ask again later.', 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def certamen(ctx):
    await ctx.send(f'Certamen Commands:\n"c" to clear the previous question')


@client.command(aliases=['q'])
async def question(ctx):
    sheet = pd.read_excel('CertamenQs.xlsx')
    valuearray = []
    for row in sheet.index:
        valuearray.append([row])
    embed = discord.Embed(title="Category",description=f'1. Language\n2. Literature\n3. History\n4. Mythology\n5. Life\n6. Everything')
    await ctx.send(embed=embed)
    choice = await get_input_of_type(int, ctx)

    if choice == 1:
        sheet = sheet[sheet['Category'].str.contains('Lang')]
    elif choice == 2:
        sheet = sheet[sheet['Category'].str.contains('Lit')]
    elif choice == 3:
        sheet = sheet[sheet['Category'].str.contains('History')]
    elif choice == 4:
        sheet = sheet[sheet['Category'].str.contains('Myth')]
    elif choice == 5:
        sheet = sheet[sheet['Category'].str.contains('Life')]
    else:
        await ctx.send("Have fun with all of the categories!")

    questions = sheet["Question"].tolist()
    answers = sheet["Answer"].tolist()
    category = sheet["Category"].tolist()
    qs = random.choice(questions)
    ind = questions.index(qs)
    ans = answers[ind]
    cat = category[ind]
    embed2 = discord.Embed(title=qs,description=f'Category: {cat}')
    embed2.set_author(name=ctx.message.author)
    embed2.add_field(name="Answer",value=f'||{ans}||')
    await ctx.send(embed=embed2)

KEY = os.environ["KEY"]
client.run(KEY)
