class Person:
    def __init__(self, name, luck, status):
        self.name = name
        self.luck = luck
        self.status = status
        self.decisions = []
    
    def make_choice(self):
        pass
    
class Death:
    def __init__(self, orders):
        self.orders = orders
    
    def setOrder(self):
        pass
    
    def attempt_to_take(self):
        pass
    
class Vision:
    def __init__(self, name, luck, status, decisions):
        self.name = name
        self.luck = luck
        self.status = status
        self.decisions = decisions
    
    def make_choice(self):
        pass

    def show(self):
        pass
              
class Simulation:
    def __init__(self):
        pass
    
    def start(self):
        pass

class Event:
    def __init__(self, name, description, choices):
        self.name = name
        self.description = description
        self.choices = choices
        
    def trigger(self, person):
        print("Event: ", self.name)
        print("Event Description: ", self.description)
        print("Variants:")
        for i, choice in enumerate(self.choices):
            print(i,") ",choice)
            #person.luck += random.randint(-100,100)
        
        
        userInput = input("Your choice...")
  








event1 = Event(
    name="Highway Pile-Up",
    description="You're driving on a busy highway when a vision shows a logging truck losing its load, causing a massive crash. The logs are about to roll free in seconds.",
    choices=[
        "Slam on the brakes and pull over immediately.",
        "Speed up to pass the truck before the logs fall.",
        "Stay in your lane and hope the vision is wrong.",
        "Warn other drivers by honking and flashing lights."
    ]
)

event2 = Event(
    name="Elevator Malfunction",
    description="You're in a crowded elevator when you notice the cables fraying in your mind's eye. The elevator jerks slightly as it starts to ascend.",
    choices=[
        "Hit the emergency stop button and demand everyone exit.",
        "Stay calm and ride it to your floor, trusting maintenance.",
        "Pry open the doors and climb out now.",
        "Distract everyone by faking a panic attack to stop the elevator."
    ]
)

event3 = Event(
    name="Gas Leak at the Cafe",
    description="While sipping coffee, you smell gas and see a vision of an explosion triggered by the kitchen's faulty stove. The staff seem unaware.",
    choices=[
        "Yell 'Gas leak!' and evacuate the cafe.",
        "Quietly leave without alerting anyone.",
        "Inform the manager calmly about the smell.",
        "Ignore it, assuming it's just your imagination."
    ]
)

event4 = Event(
    name="Construction Site Collapse",
    description="Walking past a construction site, you foresee a crane dropping its load of steel beams onto the sidewalk where you're standing.",
    choices=[
        "Run back the way you came to avoid the drop zone.",
        "Duck into a nearby shop for cover.",
        "Keep walking, believing you can outrun the collapse.",
        "Shout a warning to the construction workers above."
    ]
)

event5 = Event(
    name="Roller Coaster Derailment",
    description="Strapped into a roller coaster, a vision shows the track buckling at the next loop, sending cars plummeting. The ride is about to start.",
    choices=[
        "Scream to stop the ride and demand to get off.",
        "Stay silent and brace for the worst.",
        "Try to unbuckle your restraint and jump out.",
        "Warn the person next to you to spread panic."
    ]
)

event6 = Event(
    name="Mall Escalator Trap",
    description="Riding an escalator in a busy mall, you see it suddenly speeding up and jamming, crushing people at the top.",
    choices=[
        "Jump over the side railing to the floor below.",
        "Push through the crowd to get off at the top.",
        "Stay put and hope the escalator stabilizes.",
        "Press the emergency stop button if you can reach it."
    ]
)

event7 = Event(
    name="Fireworks Factory Mishap",
    description="Touring a fireworks factory, you envision a spark igniting a chain reaction of explosions. You're near a storage room.",
    choices=[
        "Sprint for the nearest exit without warning others.",
        "Pull the fire alarm to evacuate everyone.",
        "Hide behind heavy machinery for protection.",
        "Assume it's a false alarm and continue the tour."
    ]
)

event8 = Event(
    name="Subway Surge",
    description="Waiting on a subway platform, you see a vision of a power surge causing the third rail to electrify the platform.",
    choices=[
        "Climb onto the tracks to avoid the platform.",
        "Rush back up the stairs to the street.",
        "Warn everyone to stay away from the edge.",
        "Stand still, doubting the vision's accuracy."
    ]
)

event9 = Event(
    name="Gym Equipment Failure",
    description="Lifting weights at the gym, you foresee a cable snapping on a nearby machine, whipping through the air toward you.",
    choices=[
        "Drop your weights and dive to the floor.",
        "Yell at the person using the machine to stop.",
        "Move to another part of the gym quickly.",
        "Keep lifting, thinking it's just nerves."
    ]
)

event10 = Event(
    name="Bridge Collapse",
    description="Driving across a suspension bridge, you see it swaying and snapping in a vision, plunging cars into the river below.",
    choices=[
        "Stop the car and run back on foot.",
        "Accelerate to cross the bridge faster.",
        "Stay in the car and call emergency services.",
        "Dismiss the vision and keep driving normally."
    ]
)

event11 = Event(
    name="Kitchen Fire",
    description="Cooking dinner, you smell smoke and see a vision of a grease fire engulfing the kitchen due to an unattended pan.",
    choices=[
        "Turn off the stove and cover the pan with a lid.",
        "Grab a fire extinguisher and spray the flames.",
        "Run out of the house and call 911.",
        "Ignore the smoke, thinking it's just steam."
    ]
)

event12 = Event(
    name="Airplane Turbulence",
    description="On a flight, you foresee severe turbulence causing overhead bins to open and heavy luggage to fall, injuring passengers.",
    choices=[
        "Warn the flight attendants to secure the bins.",
        "Buckle up tightly and cover your head.",
        "Try to move to a safer seat away from bins.",
        "Relax, assuming turbulence is normal."
    ]
)

event13 = Event(
    name="Chemical Spill",
    description="At a science lab, you see a vision of a chemical spill releasing toxic fumes after a vial is dropped.",
    choices=[
        "Put on a gas mask and seal the lab door.",
        "Evacuate the lab and pull the alarm.",
        "Try to clean the spill before it spreads.",
        "Stay at your station, doubting the vision."
    ]
)

event14 = Event(
    name="Amusement Park Flood",
    description="At a water park, you foresee a wave pool malfunction flooding the area, trapping people in strong currents.",
    choices=[
        "Climb to higher ground immediately.",
        "Warn the lifeguards to shut down the pool.",
        "Help others get out of the pool area.",
        "Stay in the pool, thinking it's safe."
    ]
)

event15 = Event(
    name="Hotel Glass Fall",
    description="In a high-rise hotel lobby, you see a vision of a massive glass chandelier crashing down from the ceiling.",
    choices=[
        "Run out of the lobby to the street.",
        "Warn everyone to clear the area.",
        "Hide under a sturdy table nearby.",
        "Stand still, believing the chandelier is secure."
    ]
)


events = [event1,
          event2,
          event3,
          event4,
          event5,
          event6,
          event7,
          event8,
          event9,
          event10,
          event11,
          event12,
          event13,
          event14,
          event15
          ]

person1 = Person("Thomas",80,"alive")

for elem in events:
    elem.trigger(person1)