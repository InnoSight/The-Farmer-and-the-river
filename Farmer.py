import copy
import turtle


class Location:  # class for left shore/right shore/boat and for creatures that it contains

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


class Arrangement():  # class for possible combination of Farmer/Goose/Beans/Fox on left shore/boat/right shore
    desirable = True
    x_start_draw = 18
    y_start_draw = -20
    column_width = 36
    column_height = 112
    y_delay = -25

    def __init__(self, Left_shore, Boat, Right_shore):
        self.left_shore = Left_shore
        self.boat = Boat
        self.right_shore = Right_shore

    def show(self):
        print('Desirable: ', self.desirable)
        self.left_shore.show()
        self.boat.show()
        self.right_shore.show()

    def check_rules(self):  # func for checking main rules of the game
        if self.left_shore.check1() == False or self.right_shore.check1() == False or self.boat.check2() == False or self.boat.check3() == False:
            self.desirable = False
        else:
            self.desirable = True

    def location_from_number(self, num):
        switcher = {
            1: self.left_shore,
            2: self.boat,
            3: self.right_shore
        }
        return switcher[num]

    def farmer_location(self):
        switcher = {
            self.left_shore: 1,
            self.boat: 2,
            self.right_shore: 3
        }
        for key in switcher.keys():
            if 'Farmer' in key.creatures_lst:
                return switcher[key]

    def move(self, num_loc1, num_loc2, taken_creature):  # one move of the Farmer
        assert taken_creature in self.location_from_number(
            num_loc1).creatures_lst, 'Attention! This creature is not in choosen location!'
        self.location_from_number(
            num_loc1).creatures_lst.remove(taken_creature)
        self.location_from_number(
            num_loc2).creatures_lst.append(taken_creature)
        self.check_rules()
        return self  # returns the same object of Arrangement class with the Farmer moved

    def all_moves(self, num_loc1, num_loc2):  # all possible moves of the Farmer
        assert 'Farmer' in self.location_from_number(
            num_loc1).creatures_lst, "Farmer isn't in this location!!!"
        arr_lst = []
        arr_lst.append(copy.deepcopy(self.move(num_loc1, num_loc2, 'Farmer')))
        list_of_creatures_loc1 = self.location_from_number(
            num_loc1).creatures_lst.copy()

        for each in list_of_creatures_loc1:
            arr_lst.append(copy.deepcopy(self.move(num_loc1, num_loc2, each)))
            self.move(num_loc2, num_loc1, each)

        self.move(num_loc2, num_loc1, 'Farmer')

        return arr_lst  # returns list of objects of Arrangement class

    def draw_lines(self, x, y):  # func for drawing
        tur = turtle.Turtle()
        tur.speed(10)
        tur.hideturtle()
        tur.penup()
        tur.goto(x, y)
        tur.pendown()
        tur.fd(3*self.column_width)
        tur.right(90)
        tur.fd(self.column_height)
        tur.right(90)
        tur.fd(3*self.column_width)
        tur.right(90)
        tur.fd(self.column_height)
        tur.penup()
        tur.goto(x+self.column_width, y)
        tur.pendown()
        tur.bk(self.column_height)
        tur.penup()
        tur.goto(x+2*self.column_width, y)
        tur.pendown()
        tur.bk(self.column_height)
        tur.penup()
        tur.right(90)
        tur.goto(x, y)

    def shape_of_turtle(self, tur, creature):
        if creature == 'Farmer':
            tur.shape(farmer_shape)
        elif creature == 'Fox':
            tur.shape(fox_shape)
        elif creature == 'Beans':
            tur.shape(beans_shape)
        else:
            tur.shape(goose_shape)

    def draw(self, x, y):  # func for drawing
        self.draw_lines(x, y)
        if self.left_shore.creatures_lst:
            i = 0
            y_pos = self.y_start_draw

            for creature in self.left_shore.creatures_lst:
                tur = turtle.Turtle()
                tur.hideturtle()
                tur.speed(20)
                tur.penup()
                tur.goto(x, y)
                self.shape_of_turtle(tur, creature)
                tur.goto(x + self.x_start_draw, y + y_pos + i * self.y_delay)
                tur.showturtle()
                i += 1

        if self.boat.creatures_lst:
            i = 0
            y_pos = self.y_start_draw

            for creature in self.boat.creatures_lst:
                tur = turtle.Turtle()
                tur.hideturtle()
                tur.penup()
                self.shape_of_turtle(tur, creature)
                tur.goto(x + self.column_width +
                         self.x_start_draw, y + y_pos + i * self.y_delay)
                tur.showturtle()
                i += 1

        if self.right_shore.creatures_lst:
            i = 0
            y_pos = self.y_start_draw

            for creature in self.right_shore.creatures_lst:
                tur = turtle.Turtle()
                tur.hideturtle()
                tur.penup()
                self.shape_of_turtle(tur, creature)
                tur.goto(x + 2*self.column_width +
                         self.x_start_draw, y + y_pos + i * self.y_delay)
                tur.showturtle()
                i += 1

        x_1 = x + 3 * self.column_width
        y_1 = y - 0.5 * self.column_height
        return x_1, y_1


window = turtle.Screen()
window.screensize(2250, 1000)
farmer_shape = 'D:\\work_projects\\farmer_river\\pictures\\farmer_medium.gif'
goose_shape = 'D:\\work_projects\\farmer_river\\pictures\\goose_medium.gif'
fox_shape = 'D:\\work_projects\\farmer_river\\pictures\\fox_medium.gif'
beans_shape = 'D:\\work_projects\\farmer_river\\pictures\\beans_medium.gif'
window.register_shape(farmer_shape)
window.register_shape(goose_shape)
window.register_shape(beans_shape)
window.register_shape(fox_shape)


# initiating objects in start position
Left_shore = Location('Left_shore', ['Farmer', 'Goose', 'Beans', 'Fox'])
Right_shore = Location('Right_shore', [])
Boat = Location('Boat', [])
cur_arr = Arrangement(Left_shore, Boat, Right_shore)

x_0, y_0 = -1120, 220
x_1, y_1 = cur_arr.draw(x_0, y_0)
prev_arr = cur_arr
i = 0

print(cur_arr.farmer_location())

# checking if the game finished or not
while set(cur_arr.right_shore.creatures_lst) != {'Fox', 'Goose', 'Beans', 'Farmer'}:
    assert i < 20, 'The alrorithm went to cycle'

    print('ITERATION ', i, ':')
    cur_arr.show()
    x_0 += 150

    # creating the list of all possible combinations of moves of the Farmer to one step
    print(cur_arr.farmer_location())
    if cur_arr.farmer_location() == 2:
        arr_lst = cur_arr.all_moves(2, 1)
        arr_lst.extend(cur_arr.all_moves(2, 3))
    elif cur_arr.farmer_location() == 3:
        arr_lst = cur_arr.all_moves(3, 2)
    else:
        arr_lst = cur_arr.all_moves(1, 2)

    # finding the previous arrangement in a new list and removing it
    if i > 0:
        for item in arr_lst:
            if set(item.left_shore.creatures_lst) == set(prev_arr.left_shore.creatures_lst) \
               and set(item.boat.creatures_lst) == set(prev_arr.boat.creatures_lst)  \
               and set(item.right_shore.creatures_lst) == set(prev_arr.right_shore.creatures_lst):
                arr_lst.remove(item)

    # defining desirable arrangements through all arrangements
    des_arr_lst = []
    for arr in arr_lst:
        if arr.desirable == True:
            des_arr_lst.append(arr)
    if len(des_arr_lst) == 0:
        print('There are no desirable arrangements')
        break
    else:
        prev_arr = copy.deepcopy(cur_arr)
        # this is an arrangement that we choose on this step
        cur_arr = des_arr_lst[0]

    # finding choosen arrangement through all arrangements (need for printing) and printing an arrow
    k = 0
    for arr in arr_lst:
        x_2, y_2 = arr.draw(x_0, y_0 - k * 150)
        if set(arr.left_shore.creatures_lst) == set(cur_arr.left_shore.creatures_lst) \
                and set(arr.boat.creatures_lst) == set(cur_arr.boat.creatures_lst)  \
                and set(arr.right_shore.creatures_lst) == set(cur_arr.right_shore.creatures_lst):
            tur = turtle.Turtle()
            tur.hideturtle()
            tur.penup()
            tur.goto(x_1, y_1)
            tur.pendown()
            tur.showturtle()
            tur.goto(x_0, y_0 - k * 150 - 0.5 * arr.column_height)
            x_1, y_1 = x_2, y_2
        k += 1

    i += 1
else:
    print('Successfuly finished')

turtle.done()
