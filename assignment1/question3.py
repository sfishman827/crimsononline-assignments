"""question 3

a)  Implement classes representing people and buildings. People should support
    name and gender, seamlessly verifying that gender is either M or F (if it
    isn't, what's the best way to inform the calling code that a mistake was
    made?) and enforcing capitalization of both first name and last name.

b)  Buildings should support a function enter that takes a person and a room
    number. The building should then keep track of anyone who enters/leaves the
    building and respond to some type of where_is(person) query with the room
    number that person is in. Ensure, naturally, that no one can be in more
    than one building at a time.

c)  Make the building class iterable over the people in it. That is, make it
    possible to write a for loop of the form:
        for person in building:
            ...

d)  Implement a class that represents an office building, an object that
    behaves the same as a building but only allows people to enter if they are
    on a list of employees passed in when the OfficeBuilding is instantiated.
    You may want to look up the super function in the Python documentation
    concerning classes.

e)  Implement a class that represents a house. The House class should implement
    enter to take only a Person object, and the House class should not support
    where_is at all. It should instead support at_home(Person), a function that
    returns a Boolean.

f)  Modify all buildings, houses included, to remember their location as an
    (x, y) tuple. Then make it possible to call some function that takes such
    a tuple and returns the building object at that tuple or None if no
    building exists at that location. You may choose whether any given location
    can only hold one building or multiple buildings, but you need to handle
    this corner case in some logical fashion.

g)  With a minimum of code duplication, modify the Building class so that
    bldg[roomnumber] = person accomplishes the same thing as
    bldg.enter(person, roomnumber). Be careful with how you do this if you
    chose to inherit any classes from Building (which you should have).
"""

class Person:
    
    def __init__(self, name, gender):
        if gender == 'M' or gender == 'F':
            self.gender = gender
        else:
            raise Exception('Invalid Gender')

        try:
            if name.split()[0][0].isupper() and name.split()[1][0].isupper():
                self.name = name
            else:
                raise Exception('Invalid Name')
        except IndexError:
            raise Exception('Invalid Name')

        self.inbuilding = None

    def leave(self):
        self.inbuilding.leave(self)

    def __repr__(self):
        return self.name

class Building:
    def __init__(self, location):
        self.people = {}
        self.loc = location
    
    def enter(self, person, room_no):
        if not person.inbuilding == None:
            person.leave()

        person.inbuilding = self
        
        self.people[person] = room_no
        
    def leave(self, person):
        del self.people[person]

    def where_is(self, person):
        if person in self.people:
            return self.people[person]
        else:
            return 'Not here'

    def __setitem__(self, room, person):
        self.enter(person, room)

    def __iter__(self):
        return iter(self.people)

class OfficeBuilding(Building):
    def __init__(self, location, employeelist):
        self.employees = employeelist
        Building.__init__(self, location)

    def enter(self, person, room_no):
        if person in self.employees:
            Building.enter(self, person, room_no)
        else:
            print 'Not an employee'

class Home(Building):
    def enter(self, person):
        Building.enter(self, person, 0)

    def where_is(self, person):
        pass

    def at_home(self, person):
        return person in self.people

    def __setitem__(self, room, person):
        print 'No room numbers here!'

class Client:
    def __init__(self):
        self.map = []

    def add_building(self, bldg):
        if self.bldg_at(bldg.loc) == None:
            self.map.append(bldg)
        else:
            print 'There is already a building at ' + str(bldg.loc)
            

    def bldg_at(self, location):
        for bldg in self.map:
            if bldg.loc == location:
                return bldg
        return None
