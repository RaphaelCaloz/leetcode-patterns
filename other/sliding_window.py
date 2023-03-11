def sliding_window(data):  # NOTE: Data can be string/list
    left, right = 0, 0
    # Init a DS to keep track of the condition that makes a window
    # valid or not.

    ### NOTE ###
    # DS is generally hashmap, 
    # but can be int or list depending on problem
    # ds is used to keep track of the condition that makes a window
    # valid or not.
    ############

    while right < len(data):
        # Add data[right] to DS
        while # window not valid:
            # Remove data[left] from DS
            left += 1  # Contract window
        # Process valid window (update a result/return)
        # NOTE: (right-left+1) to get window length. Often useful for processing step.
        right += 1  # Expand window
    # return result/False
