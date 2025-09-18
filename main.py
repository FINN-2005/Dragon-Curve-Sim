from classses import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES, pygame.SRCALPHA)
        self.clock = pygame.Clock()
        
        self.vertices = cp.array([[-1,0,1], [1,0,1]], dtype='float32')
        self.angle = 0
        self.first = True
        v = cp.asnumpy(self.vertices).tolist()
        self.xy = v[-1][0], v[-1][1]
        self.scale = 0.4
        self.is_rotating = False
        
    def update(self):
        # if not self.is_rotating:              # uncomment this to rotate automatically
        #     self.mouse_pressed()              # otherise, click to rotate
            
        verts = self.vertices.copy()
        fps = int(self.clock.get_fps())
        if fps:
            self.scale *= pow((1/sqrt(2)), (1/fps))
        
        self.rotate(verts)
        self.draw(verts)        
                
    def rotate(self, verts):
        if self.is_rotating:
            x,y = self.xy
            verts = verts @ translate(-x, -y)
            verts = verts @ rotate(radians(-self.angle))
            verts = verts @ translate(x, y)
            if self.angle < 90: self.angle += self.dt
            else: 
                self.angle = 0
                self.is_rotating = False
                v = cp.asnumpy(verts).tolist()
                self.xy = v[0][0], v[0][1]
                self.vertices = cp.vstack([self.vertices, verts])
            self.draw(verts)

    def draw(self, verts):
        verts = verts @ scale(self.scale, self.scale)
        verts = verts @ origin_to_center()

        verts = cp.asnumpy(verts)
        verts = verts.tolist()
        for i in range(0, len(verts) - 1, 2):
            pygame.draw.line(self.screen, 'black', verts[i][:2], verts[i+1][:2], 2)   
                
    def mouse_pressed(self):
        if not self.is_rotating:
            self.is_rotating = True
        
    def run(self):
        self.running = True
        while self.running:
            self.dt = 100 * self.clock.tick(FPS)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed()
                    
            self.screen.fill('bisque')
            self.update()
            pygame.display.set_caption(f'FPS: {self.clock.get_fps()}')
            pygame.display.flip()


Game().run()
            