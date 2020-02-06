import copy

class Location:
    creatures_lst = []
    
    def __init__(self, name, creatures_lst):
        self.name = name
        self.creatures_lst = creatures_lst
                
    def show(self):
        print(self.name, ':')
        """ for item in self.creatures_lst:
            item.show() """
        print(self.creatures_lst)

    def check1(self):
        if 'Goose' in self.creatures_lst and 'Fox' in self.creatures_lst and 'Farmer' not in self.creatures_lst:
            return False
        if 'Goose' in self.creatures_lst and 'Beans' in self.creatures_lst and 'Farmer' not in self.creatures_lst:
            return False
        return True

    def check2(self):
        if 'Farmer' not in self.creatures_lst and len(self.creatures_lst) > 0:
            return False
        return True

    def check3(self):
        if len(self.creatures_lst) > 2:
            return False
        return True

class Arrangement():
    desirable = True
    
    def __init__(self, Left_shore, Boat, Right_shore):
        self.left_shore = Left_shore
        self.boat = Boat
        self.right_shore = Right_shore 
        
    def show(self):
        print('Desirable: ', self.desirable)
        self.left_shore.show()
        self.boat.show()
        self.right_shore.show()

    def check_rules(self):
        if self.left_shore.check1() == False or self.right_shore.check1() == False or self.boat.check2() == False or self.boat.check3() == False:
            self.desirable = False
        else:
            self.desirable = True

    def location_from_number(self, num):
        switcher = {
            1 : self.left_shore,
            2 : self.boat,
            3 : self.right_shore
        }
        return switcher[num]

    def farmer_location(self):
        switcher = {
            self.left_shore : 1,
            self.boat : 2,
            self.right_shore : 3
        }
        for key in switcher.keys():
            if 'Farmer' in key.creatures_lst:
                return switcher[key]

    def move (self, num_loc1, num_loc2, taken_creature):
        assert taken_creature in self.location_from_number(num_loc1).creatures_lst, 'Attention! This creature is not in choosen location!'
        self.location_from_number(num_loc1).creatures_lst.remove(taken_creature)
        self.location_from_number(num_loc2).creatures_lst.append(taken_creature)
        self.check_rules()
        return self

    def all_moves (self, num_loc1, num_loc2):
        assert 'Farmer' in self.location_from_number(num_loc1).creatures_lst, "Farmer isn't in this location!!!"
        arr_lst = []       
        arr_lst.append(copy.deepcopy(self.move(num_loc1, num_loc2, 'Farmer')))
        list_of_creatures_loc1 = self.location_from_number(num_loc1).creatures_lst.copy()
        
        for each in list_of_creatures_loc1:
            arr_lst.append(copy.deepcopy(self.move(num_loc1, num_loc2, each)))
            self.move(num_loc2, num_loc1, each)
        
        self.move(num_loc2, num_loc1, 'Farmer')

        return arr_lst


Left_shore = Location('Left_shore', ['Farmer', 'Goose', 'Beans', 'Fox'])
Right_shore = Location('Right_shore', [])
Boat = Location('Boat', [])
cur_arr = Arrangement(Left_shore, Boat, Right_shore)
prev_arr = cur_arr
i = 0

print(cur_arr.farmer_location())

while set(cur_arr.right_shore.creatures_lst) != {'Fox', 'Goose', 'Beans', 'Farmer'}:
    assert i < 20, 'The alrorithm went to cycle'
    
    print('ITERATION ', i, ':')
    cur_arr.show()
    print(cur_arr.farmer_location())
    if cur_arr.farmer_location() == 2:    
        arr_lst = cur_arr.all_moves(2,1)
        arr_lst.extend(cur_arr.all_moves(2,3))
    elif cur_arr.farmer_location() == 3:
        arr_lst = cur_arr.all_moves(3,2)
    else:
        arr_lst = cur_arr.all_moves(1,2)  
    """ print('ARRANGEMENTS:') 
    for arr in arr_lst:
        arr.show()  """       
    if i > 0:
        for item in arr_lst:
            if set(item.left_shore.creatures_lst) == set(prev_arr.left_shore.creatures_lst) \
                and set(item.boat.creatures_lst) == set(prev_arr.boat.creatures_lst) \
                    and set(item.right_shore.creatures_lst) == set(prev_arr.right_shore.creatures_lst):
                        arr_lst.remove(item)
    des_arr_lst = []
    for arr in arr_lst:
        if arr.desirable == True:        
            des_arr_lst.append(arr)
    if len(des_arr_lst) == 0:
        print('There are no desirable arrangements')
        break
    else:
        prev_arr = copy.deepcopy(cur_arr) 
        cur_arr = des_arr_lst[0]
    i += 1
else:
    print('Successfuly finished')







































