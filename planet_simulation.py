import pygame
import math
pygame.init()

WIDTH, HEIGHT =1500, 800
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE=(255,255,255)
YELLOW=(255,255,0)
BLUE=(100, 149, 237)
RED=(255,0,0) 
DARKRED=(128, 0, 0)
BROWN=(131, 76, 1)
PINK=(224, 191, 184)
GREEN=(8,143, 143)
DARKBLUE=(0, 0, 139)
YELLOWBROWN=(255, 213, 157)

FONT=pygame.font.SysFont("comicsans", 12)

class Planet:
    AU=149.6e6*1000 #distance from earth to sun in km (astronomical units)
    G=6.67428e-11
    SCALE=25/AU  #1 au=100 px
    TIMESTEP=3600*24 #ONE DAY


    def __init__(self, x, y, radius, colour, mass):
        self.x=x #no of metres away the planet is from sun
        self.y=y 
        self.radius=radius
        self.colour=colour
        self.mass=mass

        self.orbit=[]
        self.sun=False
        self.distance_to_sun=0

        self.x_vel=0
        self.y_vel=0

    def draw(self, win):
        x=self.x*self.SCALE + WIDTH/2
        y=self.y*self.SCALE + HEIGHT/2

        if len(self.orbit)>2:

            updated_points=[]
            for point in self.orbit:
                x,y=point
                x=x*self.SCALE+WIDTH/2
                y=y*self.SCALE+HEIGHT/2
                updated_points.append((x,y))
            pygame.draw.lines(win, self.colour, False, updated_points)

        pygame.draw.circle(win, self.colour, (x,y), self.radius)
        if not self.sun:
            distance_text=FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x-distance_text.get_width()/2,y-distance_text.get_width()))


    def attraction(self, other): #other here is other planet
        other_x, other_y=other.x, other.y
        distance_x=other_x-self.x 
        distance_y=other_y-self.y

        distance=math.sqrt(distance_x**2+distance_y**2)

        if other.sun:
            self.distance_to_sun=distance
        
        force=self.G*self.mass*other.mass/distance**2
        theta=math.atan2(distance_y, distance_x)
        force_x=math.cos(theta)*force
        force_y=math.sin(theta)*force

        return force_x, force_y
    
    def update_position(self, planets):
        total_fx=total_fy=0
        for planet in planets:
            if self==planet:
                continue
            fx, fy=self.attraction(planet)
            total_fx+=fx
            total_fy+=fy
    
        self.x_vel+=total_fx/self.mass*self.TIMESTEP
        self.y_vel+=total_fy/self.mass*self.TIMESTEP

        self.x+=self.x_vel*self.TIMESTEP
        self.y+=self.y_vel*self.TIMESTEP

        self.orbit.append((self.x, self.y))

def main():
    run=True
    clock=pygame.time.Clock()

    sun=Planet(0,0, 5, YELLOW, 1.98892 * 10 **30)
    sun.sun=True
    earth=Planet(-1*Planet.AU, 0, 0.5*8, BLUE, 5.9742 * 10**24)
    earth.y_vel=29.783*1000

    mars=Planet(1.52*Planet.AU, 0, 0.266*10, RED, 6.39 * 10**23)
    mars.y_vel=-24.077*1000

    mercury=Planet(-0.39*Planet.AU, 0, 0.1915*10, DARKRED, 3.30 * 10**23)
    mercury.y_vel=47.4*1000

    venus=Planet(0.72*Planet.AU, 0, 0.4745*10, PINK, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    jupiter=Planet(-5.2*Planet.AU, 0, 5.605*10, BROWN, 1.89813 * 10**27)
    jupiter.y_vel = 13.07 * 1000

    saturn=Planet(9.54*Planet.AU, 0, 4.725*10, YELLOWBROWN, 5.683 * 10**26)
    saturn.y_vel = -9.69 * 1000

    uranus=Planet(-19.2*Planet.AU, 0, 2.005*10, GREEN, 8.681 * 10**25)
    uranus.y_vel = 6.81 * 1000

    neptune=Planet(30.06*Planet.AU, 0, 1.94*10, DARKBLUE, 1.024 * 10**26)
    neptune.y_vel = -5.43 * 1000
    

    planets=[sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]


    while run:
        clock.tick(60) #run this loop at max 60 times per second
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        
        pygame.display.update()

    pygame.quit()

main()

