def main():
  with open("input.txt", "r") as file:
    rows = file.readlines()

  # # Part 1
  # finalList = []

  # for row in rows:
  #   isAsc = True
  #   isDesc = True
  #   isInRange = True

  #   # get each row as ints
  #   valueRow = [int(stringInt) for stringInt in row.split()]

  #   # sort rows
  #   rowAsc = sorted(valueRow)
  #   rowDesc = sorted(valueRow, reverse=True)

  #   i = 0
  #   for num in valueRow:
  #     # check if row is asc
  #     if(num != rowAsc[i]):
  #       isAsc = False

  #     # check if row is desc
  #     if(num != rowDesc[i]):
  #       isDesc = False

  #     # stop processing if already unsafe
  #     if (isAsc == False and isDesc == False):
  #       i += 1
  #       break

  #     if (i != 0):
  #       # get distance
  #       distance = abs(valueRow[i-1] - valueRow[i])

  #       if (distance == 0 or distance > 3):
  #         isInRange = False

  #     i += 1

  #   # final check before adding to the list
  #   if isInRange == True and (isAsc == True or isDesc == True):
  #     finalList.append(valueRow)

  # print(len(finalList))


  # # Part 2
  finalList = []
  j = 0
  for row in rows:
    # get each row as ints
    value_row = [int(stringInt) for stringInt in row.split()]
    asc_value_row = value_row.copy()
    desc_value_row = value_row.copy()

    if(j == 7):
      print("----------------------------------------------------------------------------------")
      print("----------------------------------------------------------------------------------")
      print(f"Start processing row: {j+1}")
      print(value_row)
      print()
      is_asc = check_asc(asc_value_row)
      if(is_asc["is_asc"] == True and is_asc["is_in_range"] == True):
        finalList.append(is_asc["value_row"])
        print("is_asc = True")
        print(f"is_in_range = True")
        print(is_asc)
        print(f"adding row {is_asc['value_row']}")
      else:
        is_desc = check_desc(desc_value_row)
        if(is_desc["is_desc"] == True and is_desc["is_in_range"] == True):
          finalList.append(is_desc["value_row"])
          print("is_desc = True")
          print("is_in_range = True")
          print(is_desc)
          print(f"adding row {is_desc['value_row']}")
        else:
          print("Row not added!!")
    j += 1

  print(len(finalList))

def check_asc(asc_value_row):
  is_asc = True
  ordered_asc_value_row = sorted(asc_value_row)

  # print(f"Start of check asc: {len(asc_value_row)}")
  # print(asc_value_row)
  # print(ordered_asc_value_row)

  i = 0
  e = 0
  for num in asc_value_row:
    if(is_asc == True):
      # check if row is asc
      if(num != ordered_asc_value_row[i]):
        # when not asc remove issue level and reprocess
        e += 1

        if(e > 1):
          is_asc = False
          break
        asc_value_row.pop(i)
        print(asc_value_row)

        # reorder original list after removal
        ordered_asc_value_row = sorted(asc_value_row)
        # print(ordered_asc_value_row)
        k = 0
        for num_asc_second_check in asc_value_row:
          # print(f"Hit secondary loop - position {i}")
          if(num_asc_second_check != ordered_asc_value_row[k]):
            # print("Tried to remove to many. Moving to next row.")
            is_asc = False
            break

          k += 1

      if(e == 1):
        is_in_range = check_range_with_level_removed(asc_value_row)
      # print(f"Did not hit secondary loop - position {i}")

    i += 1
  if (e == 0):
    is_in_range = check_range(asc_value_row)
  # print(is_asc)
  # print(is_in_range)
  return {
      "is_asc": is_asc,
      "is_in_range": is_in_range,
      "value_row": asc_value_row
    }

def check_desc(desc_value_row):
  is_desc = True
  ordered_desc_value_row = sorted(desc_value_row, reverse=True)

  # print(f"Start of check desc: {len(desc_value_row)}")
  # print(desc_value_row)
  # print(ordered_desc_value_row)
  i = 0
  e = 0
  for num in desc_value_row:
    if(is_desc == True):
      # check if row is asc
      if(num != ordered_desc_value_row[i]):

        e += 1
        if(e > 1):
          is_desc = False
          break
        # when not asc remove issue level and reprocess
        desc_value_row.pop(i)
        # print(desc_value_row)

        # reorder original list after removal
        ordered_desc_value_row = sorted(desc_value_row, reverse=True)
        # print(ordered_desc_value_row)

        k = 0
        for num_desc_second_check in desc_value_row:
          # print(f"Hit secondary loop - position {i}")

          if(num_desc_second_check != ordered_desc_value_row[k]):
            # print("Tried to remove to many. Moving to next row.")

            is_desc = False
            break

          k += 1

        if(e == 1):
          is_in_range = check_range_with_level_removed(desc_value_row)
      # print(f"Did not hit secondary loop - position {i}")

    i += 1
  if(e == 0):
    is_in_range = check_range(desc_value_row)

  # print(is_desc)
  # print(is_in_range)
  return {
      "is_desc": is_desc,
      "is_in_range": is_in_range,
      "value_row": desc_value_row
    }


def check_range_with_level_removed(value_row):
  i = 0
  is_in_range = True
  for num in value_row:
    if (i != 0):
      # get distance
      distance = abs(value_row[i-1] - value_row[i])

      if (distance == 0 or distance > 3):
        is_in_range = False

    i += 1

  return is_in_range

def check_range(value_row):
  print(f"value row on entry {value_row}")
  value_row_copy = value_row.copy()
  i = 0
  e = 0
  is_in_range = True
  for num in value_row:
    if (i != 0):
      # get distance
      distance = abs(value_row[i-1] - value_row[i])

      if (distance == 0 or distance > 3):
        e += 1
        if(e > 1):
          is_in_range = False
          break

        value_row.pop(i)
        print(f"value row after pop {value_row}")


        k = 0
        for num_second_check in value_row:
          if (k != 0):
            # get distance
            distance = abs(value_row[k-1] - value_row[k])
            if (distance == 0 or distance > 3):
              is_in_range = False
              break
          k += 1

    i += 1

  return is_in_range

if __name__ == "__main__":
  main()



# # Solution is only being applied to the first number where error occurs
# below 14 is being removed and then a failure occurs on distance from 12 to 16 so the row is not added.
# When this happen we need to
# # ----------------------------------------------------------------------------------
# # Start processing row: 8
# # [9, 11, 14, 12, 16]

# # Row not added!!
# # ----------------------------------------------------------------------------------
