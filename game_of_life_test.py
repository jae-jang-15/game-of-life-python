from game_of_life import next_board_state
from game_of_life import print_board

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_board_1 = next_board_state(init_state1)
    if actual_board_1 == expected_next_state1:
        print("PASSED TEST 1: Empty Grid")
    else:
        print("FAILED TEST 1: Empty Grid")
        print("Initial:")
        print_board(init_state1)
        print("Expected:")
        print_board(expected_next_state1)
        print("Actual:")
        print_board(actual_board_1)


    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_board_2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_board_2 = next_board_state(init_state2)

    if actual_board_2 == expected_board_2:
        print ("PASSED Test 2: 3 neighbors")
    else:
        print ("FAILED Test 2: 3 neighbors")
        print ("Initial:")
        print_board(init_state2)
        print ("Expected:")
        print_board(expected_board_2)
        print ("Actual:")
        print_board(actual_board_2)


    # Test 3: Still Life (Should remain unchanged after each generation)
    init_state3 = [
        [0,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ]
    expected_board_3 = [
        [0,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ]
    actual_board_3 = next_board_state(init_state3)  

    if actual_board_3 == expected_board_3:
        print ("PASSED Test 3: Still Life")
    else:
        print ("FAILED Test 3: Still Life")
        print ("Initial:")
        print_board(init_state3)
        print ("Expected:")
        print_board(expected_board_3)
        print ("Actual:")
        print_board(actual_board_3)


    # Test 4: Oscillator (Should repeat its state in cycles)
    init_state4 = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ]
    expected_board_4 = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    actual_board_4 = next_board_state(init_state4)  

    if actual_board_4 == expected_board_4:
        print ("PASSED Test 4: Oscillator")
    else:
        print ("FAILED Test 4: Oscillator")
        print ("Initial:")
        print_board(init_state4)
        print ("Expected:")
        print_board(expected_board_4)
        print ("Actual:")
        print_board(actual_board_4)


    # Test 5: Glider (Should move diagonally over time)
    init_state5 = [
        [0,1,0],
        [0,0,1],
        [1,1,1]
    ]
    expected_board_5 = [
        [0,0,0],
        [1,0,1],
        [0,1,1]
    ]
    actual_board_5 = next_board_state(init_state5)  

    if actual_board_5 == expected_board_5:
        print ("PASSED Test 5: Glider")
    else:
        print ("FAILED Test 5: Glider")
        print ("Initial:")
        print_board(init_state5)
        print ("Expected:")
        print_board(expected_board_5)
        print ("Actual:")
        print_board(actual_board_5)


    # Test 6: Overpopulation (Cells with > 3 live neighbors should die)
    init_state6 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    expected_board_6 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_board_6 = next_board_state(init_state6)  

    if actual_board_6 == expected_board_6:
        print ("PASSED Test 6: Overpopulation")
    else:
        print ("FAILED Test 6: Overpopulation")
        print ("Initial:")
        print_board(init_state6)
        print ("Expected:")
        print_board(expected_board_6)
        print ("Actual:")
        print_board(actual_board_6)


    # Test 7: Underpopulation (Live cell with < 2 neighbors dies)
    init_state7 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    expected_board_7 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_board_7 = next_board_state(init_state7)  

    if actual_board_7 == expected_board_7:
        print ("PASSED Test 7: Underpopulation")
    else:
        print ("FAILED Test 7: Underpopulation")
        print ("Initial:")
        print_board(init_state7)
        print ("Expected:")
        print_board(expected_board_7)
        print ("Actual:")
        print_board(actual_board_7)