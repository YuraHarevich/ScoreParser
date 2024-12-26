def brakets(target_string: str):
    second_part_start = target_string.find('«') + 1
    second_part_end = target_string.find('»')
    return target_string[second_part_start:second_part_end]
