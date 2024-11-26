from drafter import *
from dataclasses import dataclass

hide_debug_information()
set_website_title("Chem Creativity Portion")
set_website_framed(True)



@dataclass
class Element:
    name: str
    mw: float
    
@dataclass
class State:
    element: list[Element]
    caculator_str: str
    
#data from Periodic table of UD
Molar_mass_dic = [
    Element("", 0.0),             # 0
    Element("H", 1.008),       # 1
    Element("He", 4.003),      # 2
    Element("Li", 6.941),      # 3
    Element("Be", 9.012),      # 4
    Element("B", 10.811),      # 5
    Element("C", 12.011),      # 6
    Element("N", 14.007),      # 7
    Element("O", 15.999),      # 8
    Element("F", 18.998),      # 9
    Element("Ne", 20.180),     # 10
    Element("Na", 22.990),     # 11
    Element("Mg", 24.305),     # 12
    Element("Al", 26.982),     # 13
    Element("Si", 28.086),     # 14
    Element("P", 30.974),      # 15
    Element("S", 32.066),      # 16
    Element("Cl", 35.453),     # 17
    Element("Ar", 39.948),     # 18
    Element("K", 39.098),      # 19
    Element("Ca", 40.078),     # 20
    Element("Sc", 44.956),     # 21
    Element("Ti", 47.867),     # 22
    Element("V", 50.942),      # 23
    Element("Cr", 51.996),     # 24
    Element("Mn", 54.938),     # 25
    Element("Fe", 55.845),     # 26
    Element("Co", 58.933),     # 27
    Element("Ni", 58.693),     # 28
    Element("Cu", 63.546),     # 29
    Element("Zn", 65.380),     # 30
    Element("Ga", 69.723),     # 31
    Element("Ge", 72.631),     # 32
    Element("As", 74.922),     # 33
    Element("Se", 78.971),     # 34
    Element("Br", 79.904),     # 35
    Element("Kr", 84.798),     # 36
    Element("Rb", 85.468),     # 37
    Element("Sr", 87.620),     # 38
    Element("Y", 88.906),      # 39
    Element("Zr", 91.224),     # 40
    Element("Nb", 92.906),     # 41
    Element("Mo", 95.950),     # 42
    Element("Tc", 98.907),     # 43
    Element("Ru", 101.070),    # 44
    Element("Rh", 102.906),    # 45
    Element("Pd", 106.420),    # 46
    Element("Ag", 107.868),    # 47
    Element("Cd", 112.414),    # 48
    Element("In", 114.818),    # 49
    Element("Sn", 118.711),    # 50
    Element("Sb", 121.760),    # 51
    Element("Te", 127.600),    # 52
    Element("I", 126.904),     # 53
    Element("Xe", 131.294),    # 54
    Element("Cs", 132.905),    # 55
    Element("Ba", 137.328),    # 56
    Element("La", 138.905),    # 57
    Element("Ce", 140.116),    # 58
    Element("Pr", 140.908),    # 59
    Element("Nd", 144.243),    # 60
    Element("Pm", 144.913),    # 61
    Element("Sm", 150.360),    # 62
    Element("Eu", 151.964),    # 63
    Element("Gd", 157.250),    # 64
    Element("Tb", 158.925),    # 65
    Element("Dy", 162.500),    # 66
    Element("Ho", 164.930),    # 67
    Element("Er", 167.259),    # 68
    Element("Tm", 168.934),    # 69
    Element("Yb", 173.055),    # 70
    Element("Lu", 174.967),    # 71
    Element("Hf", 178.490),    # 72
    Element("Ta", 180.948),    # 73
    Element("W", 183.840),     # 74
    Element("Re", 186.207),    # 75
    Element("Os", 190.230),    # 76
    Element("Ir", 192.217),    # 77
    Element("Pt", 195.085),    # 78
    Element("Au", 196.967),    # 79
    Element("Hg", 200.592),    # 80
    Element("Tl", 204.383),    # 81
    Element("Pb", 207.200),    # 82
    Element("Bi", 208.980),    # 83
    Element("Po", 208.982),    # 84
    Element("At", 209.987),    # 85
    Element("Rn", 222.018),    # 86
]


    
@route
def caculating1(state: State) -> Page:     
    return Page(state, ["Chem103 Creative Portion",
                        "Molar mass Caculator",
                        "It only supports the element 1 - 86 (H - Rn).",
                        "Pay attention to the spelling and capitalization",
                        "Enter the name at the first column, number at the second column.",
                        TextBox("element1", ""),
                        TextBox("num1", "0"),
                        "<br>",
                        TextBox("element2", ""),
                        TextBox("num2", "0"),
                        "<br>",
                        TextBox("element3", ""),
                        TextBox("num3", "0"),
                        "<br>",
                        TextBox("element4", ""),
                        TextBox("num4","0"),
                        "<br>",
                        TextBox("element5", ""),
                        TextBox("num5", "0"),
                        "<br>",
                        Button("save", caculating2),
                        "<br>",
                        "<br>",
                        "Examle: ",
                        Image("example3.png", 300, 190),
                        Image("example4.png", 300, 190),
                        ])

@route
def caculating2(state: State, element1: str, num1: str, element2: str, num2: str, element3: str, num3: str, element4: str, num4: str, element5: str, num5: str) -> Page:
    string1 = ""
    string2 = ""
    string3 = ""
    string4 = ""
    string5 = ""
    nn = ""
    nn2 = ""
    nn3 = ""
    nn4 = ""
    nn5 = ""
    mw1 = -99999
    mw2 = -99999
    mw3 = -99999
    mw4 = -99999
    mw5 = -99999
    verify = num1 + num2 + num3 + num4 + num5
    try:
        verify = int(verify)
    except ValueError:
        return Page(state, ["You can only enter number on the second column.",
                            Button("Back", caculating1)])
    for each1 in state.element:
        if each1.name == element1:
            mw1 = each1.mw
            nn = each1
            break
        
    for each2 in state.element:
        if each2.name == element2:
            mw2 = each2.mw
            nn2 = each2
            break
    for each3 in state.element:
        if each3.name == element3:
            mw3 = each3.mw
            nn3 = each3
            break
    for each4 in state.element:
        if each4.name == element4:
            mw4 = each4.mw
            nn4 = each4
            break
    for each5 in state.element:
        if each5.name == element5:
            mw5 = each5.mw
            nn5 =each5
            break
    total = mw1 + mw2 + mw3 + mw4 + mw5
    if total < 0:
        return Page(state, ["You make some mistakes at the first colum.",
                            "Be careful with your spelling and capitalization",
                            "And it only supports element 1 - 86 (H - Rn)",
                            Button("Back", caculating1)])
    result = round(mw1 * int(num1) + mw2 * int(num2) + mw3 * int(num3) + mw4 * int(num4) + mw5 * int(num5), 3)
    if int(num1) != 0:
        string1 = f"percent mass of {nn.name} is {round(mw1 * int(num1) / result * 100, 3)} %"
    if int(num2) != 0:
        string2 = f"percent mass of {nn2.name} is {round(mw2 * int(num2) / result * 100, 3)} %"
    if int(num3) != 0:
        string3 = f"percent mass of {nn3.name} is {round(mw3 * int(num3) / result * 100, 3)} %"
    if int(num4) != 0:
        string4 = f"percent mass of {nn4.name} is {round(mw4 * int(num4) / result * 100, 3)} %"
    if int(num5) != 0:
        string5 = f"percent mass of {nn5.name} is {round(mw5 * int(num5) / result * 100, 3)} %"
    return Page(state, ["The molar mass is: ",
                        f"{result} g/mol",
                        string1,
                        string2,
                        string3,
                        string4,
                        string5,
                        Image("atoms.jpeg", 300, 300),
                        Button("One more time", caculating1),
                        "<br>",
                        Button("exit", index)])


@route
def index(state: State) -> Page:
    show_str = ''
    show = ''
    if state.caculator_str:
        show_str = "Congratulations! You have unlocked the secret prize!"
        show = Button("Caculator of Molar Mass", caculating1)
    return Page(state, ["The topic: The Periodic Table",
                        "Chem103090 Creativity Project",
                        "Heng Luo",
                        "Prof. Lauren Genova",
                        Image("chem.png", 400, 350),
                        "<br>",
                        "Unfortunatelly, this project is a test about the table.",
                        "But you will get prize after accomplishing it!",
                        Button("Begin", test1),
                        show_str,
                        show])

@route
def test1(state: State) -> Page:
    return Page(state, ["Enter the number from 1 - 18",
                         "1. Which group is Alkali Metal in?",
                         TextBox("q1"),
                         "2. Which group is Alkali Earth Metal in?",
                         TextBox("q2"),
                         "3. Which group is Chalcogens in?",
                         TextBox("q3"),
                         "4. Which group is Halogen in?",
                         TextBox("q4"),
                         "5. Which group is Noble Gas in?",
                         TextBox("q5"),
                         "<br>",
                         Button("Save", test2)])

@route
def test2(state: State, q1: str, q2: str, q3: str, q4: str, q5: str) -> Page:
    if q1 == "999":
        state.caculator_str += "ss"
        return index(state)
    try:
        qq = int(q1 + q2 + q3 + q4 + q5)
    except ValueError:
        return Page(state, ["Please just enter number!",
                            Button("back", test1)])
    hint = ''
    if q1 != "1":
        hint += "The question 1 is wrong!" + "<br>"
    if q2 != "2":
        hint += "The question 2 is wrong!" + "<br>"
    if q3 != "16":
        hint += "The question 3 is wrong!" + "<br>"
    if q4 != "17":
        hint += "The question 4 is wrong!" + "<br>"
    if q5 != "18":
        hint += "The question 5 is wrong!" + "<br>"
    
    if not hint:
        return Page(state, ["You master the knowledge well!",
                            "Let's continue!",
                            Image("table.png", 900, 600),
                            "<br>",
                            Button("next", test3),])
    else:
        return Page(state, ["You have made some mistakes!",
                            "Please try again",
                            "Hint:",
                            hint,
                            Button("try again", test1)])
    
@route
def test3(state: State) -> Page:
    return Page(state, ["Please enter decrease or increase.",
                        "1. Atomic radius",
                        "How does the atomic radius change down the group?",
                        TextBox("q1"),
                        "How does the atomic radius change across the period?",
                        TextBox("q2"),
                        "2. Ionization Energy",
                        "How does the Ionization Energy change down the group?",
                        TextBox("q3"),
                        "How does the Ionization Energy change across the period?",
                        TextBox("q4"),
                        "3. Electronegativity",
                        "How does the Electronegativity change down the group?",
                        TextBox("q5"),
                        "How does the Electronegativity change across the period?",
                        TextBox("q6"),
                        "4. Electron Affinity",
                        "How does the Electron Affinity change down the group?",
                        TextBox("q7"),
                        "How does the Electron Affinity change across the period?",
                        TextBox("q8"),
                        "<br>",
                        Button("save", test4)])

@route
def test4(state, q1, q2, q3, q4, q5, q6, q7, q8) -> Page:
    hint = ""
    if q1 != "increase":
        hint += "1-1 is wrong <br>" 
    if q2 != "decrease":
        hint += "1-2 is wrong <br>"
    if q3 != "decrease":
        hint += "2-1 is wrong <br>"
    if q4 != "increase":
        hint += "2-2 is wrong <br>"
    if q5 != "decrease":
        hint += "3-1 is wrong <br>"
    if q6 != "increase":
        hint += "3-2 is wrong <br>"
    if q7 != "decrease":
        hint += "4-1 is wrong <br>"
    if q8 != "increase":
        hint += "4-2 is wrong <br>"
        
    if not hint:
        return Page(state, ["I am proud of you!",
                            Image("table2.png", 800, 500),
                            Button("next", game1)
                                   ])
    else:
        return Page(state, ["I know it is hard",
                            "Check the hint and I am sure you will know the anwser.",
                            "But please memorize it!",
                            "Hint:",
                            hint,
                            Button("try again", test3)])
    
@route
def game1(state):
    return Page(state, ["Good Job!",
                        "Let's play some games now.",
                        "Try to select your favourite element below.",
                        "And it will show the personality represented by this element.",
                        "Let us see if this is the same as you thought!",
                        SelectBox("choice", ["H", "O", "Cl", "Fe", "Au", "He"]),
                        Button("next", game2)])
@route
def game2(state, choice):
    state.caculator_str = "1"
    result = ''
    image = ''
    if choice == "H":
        result = '''Hydrogen(H) <br> Personality: Lively, Light-hearted <br>
                    Description: Hydrogen is the lightest element in the universe,
                    symbolizing youth and a carefree nature,
                    often described as vibrant and full of exploratory spirit.'''
        image = Image("h.png")
    elif choice == "Fe":
        result = '''Iron (Fe) <br>
                    Personality: Tenacious, Reliable <br>
                    Description: Iron is a strong and durable metal,
                    representing steadfastness and reliability,
                    well-suited to be seen as a supporter among friends and partners.'''
        image = Image("fe.png")
    elif choice == "Cl":
        result = '''Chlorine (Cl) <br>
                    Personality: Sharp, Curious <br>
                    Description: Chlorine is a highly reactive element commonly used for disinfection,
                    representing curiosity about new things and a keen awareness of the environment,
                    always ready to explore the unknown.'''
        image = Image("cl.png")
    elif choice == "Au":
        result = '''Gold (Au) <br>
                    Personality: Luxurious, Confident <br>
                    Description: Gold is a precious metal, symbolizing luxury and confidence,
                    representing the pursuit of success and the appreciation of the beautiful
                    things in life.'''
        image = Image("au.png")
    elif choice == "O":
        result = '''Oxygen (O) <br>
                    Personality: Warm, Caring <br>
                    Description: Oxygen is an essential element for life, symbolizing warmth and care,
                    representing those who are helpful and willing to take care of others.'''
        image = Image("o.png")
    elif choice == "He":
        result = '''Helium (He) <br>
                    Personality: Humorous, Easy-going <br>
                    Description: Helium is a light gas commonly used in balloons, symbolizing humor and an easy-going nature,
                    always bringing joy and relaxation to those around.'''
        image = Image("he.png")
    return Page(state, [result,
                        image,
                        Button("try again", game1),
                        Button("Something seems to be unlocked...", index),
                        ])

        
        
                        
                        
                         
                         
    
                        

    
    
    

start_server(State(Molar_mass_dic, ""))
                        
                        
                        
    
