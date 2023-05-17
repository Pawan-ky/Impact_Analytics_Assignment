def find_total_ways(days,total_ways):
  pattern = ""
  find_permitation(days, pattern, total_ways)
  return total_ways

def find_permitation(days,pattern,arr):
  if "AAAA" in pattern:
    # skip if absent for 4 or more days
    pass
  elif days == 0:
    arr.append(pattern)
  else:
    #two possibalities
    find_permitation(days - 1, pattern + 'A', arr)  # absent in class
    find_permitation(days - 1, pattern + 'P', arr)  # present in class

def missing_ceremony_ways(total_ways):
    # last_day_absent = 0
    # for way in total_ways:
    #     if way[-1] =='A':
    #         last_day_absent+=1
    # return last_day_absent

    missing_way = list(filter(lambda x: x[-1]=="A",total_ways))
    return len(missing_way)

if __name__ == "__main__":
    try:
        print("Enter No. of days .. ")
        days = int(input())
    except ValueError:
        print("'Invalid Input, should be Integer")
    except Exception as e:
        print(e)
    else:
        total_ways = []
        valid_ways = find_total_ways(days,total_ways)
        last_day_absent = missing_ceremony_ways(valid_ways)
        print("Total Number of ways to attend classes over {} days is {}".format(days, len(valid_ways)))
        print("probability to miss graduation ceremony is {}/{}".format(last_day_absent,len(valid_ways)))