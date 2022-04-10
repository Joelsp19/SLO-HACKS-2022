from Functions import *
import enum
import random


class Direction(enum.Enum):
    UP = 1
    DOWN = 2


wall_dim = [400, 10]
wall_offset = 25
spike_height = 10
spike_offset = 10 + wall_offset

class GravityDash:
    def __init__(self, canvas):
        self.stride = 50
        self.size = [500,200,10]
        self.canvas = canvas
        self.direction = Direction.UP
        self.char = canvas.create_rectangle(self.size[0],self.size[1], self.size[0]+10, self.size[1]+10, fill="red")
        self.create_walls()
        self.spike_list = []
        self.spike_speed = 20
        self.bounds = self.size[0]
    def create_walls(self):
        wall_location = [self.size[0] - wall_offset,200-wall_dim[1]]
        diff = self.stride + self.size[2] * 2
        color = "black"
        create_wall(self.canvas, wall_location[0],wall_location[1],wall_dim[0],wall_dim[1],color)
        create_wall(self.canvas, wall_location[0], wall_location[1]+diff, wall_dim[0], wall_dim[1],color)

    def create_spikes(self):

        diff = self.stride - spike_height

        x = random.randint(0, 3)
        if (x==0):
            self.spike_list.append(create_spike(self.canvas, self.size[0]+ wall_dim[0] - spike_offset, self.size[1]+ wall_dim[1] + diff, spike_height, "black", 0))
        elif (x==1):
            self.spike_list.append(create_spike(self.canvas, self.size[0]+ wall_dim[0] - spike_offset, self.size[1]+ wall_dim[1], spike_height, "black", 1))

    def spike_move(self):
        x = -1 * self.spike_speed
        y = 0
        for spike in self.spike_list:
            print(self.canvas.coords(spike)[0])
            if(self.canvas.coords(spike)[0] > self.bounds):
                self.canvas.move(spike, x, y)

    def up(self, event):
        if(self.direction!=Direction.UP):
            x = 0
            y = -1 * self.stride
            self.canvas.move(self.char, x, y)
            self.direction = Direction.UP

    def down(self, event):
        if(self.direction!=Direction.DOWN):
            x = 0
            y = self.stride
            self.canvas.move(self.char, x, y)
            self.direction = Direction.DOWN