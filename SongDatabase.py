from dataclasses import dataclass


@dataclass
class SongDatabase:
    stringOne = "C C F C F C G C C F C G C F C G C C F C F C G C"
    songOne = stringOne.split(" ")
    songOneName = "Twinkle, Twinkle, Little Star"
    # print(songOne)

    stringTwo = "A D D E E F A D D G F A D D E G F G F E D G F E G F D E F E D B D D C B A D C B A G F G F D E D D D E E F A D D E G F G F D B G F G F E D E F E D B D C B A D C B A G F G F D E D"
    songTwo = stringTwo.split(" ")  #
    songTwoName = "Queen - I Want To Break Free"  # (1 octave, simplified)

    stringThree = "E4 D4 D4 C4 D4 C4 E4 D4 C4 A D4 C4 D4 C4 E4 D C4 A E4 D4 C4 D4 C4 E4 D C4 A C4 D4 C4 D4 C4 E4 D C4 D4 C4 D4 C4 D C4 D4 C4 D C D4 C4 D D4 D4 D4 C4 D4 D4 C4 D4 C4 D4 C4 D4 D D4 D4 C4 D4 E4 C4 E4 D D4 C4 D4 C D4 E4 C4 A C4 A G G4 F4 G4 F4 E4 D4 E4 D4 C4 E4 C4 A G G G4 F4 G4 E4 E4 A4 E4 G4 E4 D4 C4 C4 D4 E4 C4"
    songThree = stringThree.split(" ")  #
    songThreeName = "Oasis - Don't Look Back In Anger"  # (2 octaves)

    stringFour = "E2 E2 E2 C2 E2 G2 G C2 G E A B A A G E2 G2 A2 F2 G2 E2 C2 D2 B C2 G E A B A A G E2 G2 A2 F2 G2 E2 C2 D2 B G2 F2 F2 D2 E2 G A C2 A C2 D2 G2 F2 F2 D2 E2 C3 C3 C3 G2 F F2 D2 E2 G A C2 A C2 D2 D2 D2 C2 C2 C2 C2 C2 D2 E2 C2 A G C2 C2 C2 C2 D2 E2 C2 C2 C2 C2 D2 E2 C2 A G E2 E2 E2 C2 E2 G2 G C2 G E A B A A G E2 G2 A2 F2 G2 E2 C2 D2 B C2 G E A B A A G E2 G2 A2 F2 G2 E2 C2 D2 B E2 C2 G G A F2 F2 A B A2 A2 A2 G2 F2 E2 C2 A G E2 C2 G G A F2 F2 A B F2 F2 F2 E2 D2 C2 G E C C2 G E A B A G A G G F G E2 C2 G G A F2 F2 A B F2 F2 F2 E2 D2 C2 G E C C G E A B A G A G G F G"
    songFour = stringFour.split(" ")
    songFourName = "Super Mario Bros Theme"  # (3 octaves!!)

    # songIndex = 0
    # isSelected = False
    #
    # if songIndex == 1:
    #     isSelected = True
    # elif songIndex == 2:
    #     isSelected = True
    # elif songIndex == 3:
    #     isSelected = True
    # elif songIndex == 4:
    #     isSelected = True
    # else:
    #     isSelected = False
