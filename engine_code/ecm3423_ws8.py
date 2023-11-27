import pygame

# import the scene class
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from BaseModel import DrawModelFromMesh

from shaders import *


class ExeterScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        #sun
        self.light = LightSource(self, position=[5., 20, 5.])


        #plane/jet
        plane = load_obj_file('models/TAL16.obj')
        self.plane = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([19,6,6]), scaleMatrix([1.2,1.2,1.2])) , mesh=mesh, shader=FlatShader()) for mesh in plane]

        #race_car
        race_car = load_obj_file('models/s15.obj')
        self.race_car = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([12,0.5,5]), scaleMatrix([1.2,1.2,1.2])) , mesh=mesh, shader=FlatShader()) for mesh in race_car]

        #trees
        yellow_tree_01 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_01 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([4,0,4]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_01]
        yellow_tree_02 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_02 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([4,0,9]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_02]
        yellow_tree_03 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_03 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([10,0,4]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_03]
        yellow_tree_04 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_04 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([10,0,9]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_04]
        yellow_tree_05 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_05 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([16,0,4]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_05]
        yellow_tree_06 = load_obj_file('models/GenTree-103_AE3D_03122023-F1.obj')
        self.yellow_tree_06 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([16,0,9]), scaleMatrix([0.21,0.21,0.21])) , mesh=mesh, shader=FlatShader()) for mesh in yellow_tree_06]


        # #trex
        trexy = load_obj_file('models/tyranosausus_rex.obj')
        self.trexy = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([7,0,7]), scaleMatrix([0.15,0.15,0.15])) , mesh=mesh, shader=FlatShader()) for mesh in trexy]


            #First row of buildings
        #buildings
        building_01 = load_obj_file('models/Building_03.obj')
        building_02 = load_obj_file('models/Building_02.obj')
        building_03 = load_obj_file('models/Building_04.obj')
        building_04 = load_obj_file('models/Building_01.obj')
        building_05 = load_obj_file('models/Building_04.obj')
        building_06 = load_obj_file('models/Building_03.obj')
        building_07 = load_obj_file('models/Building_01.obj')
        building_08 = load_obj_file('models/Building_02.obj')

        # self.building_01 = [DrawModelFromMesh(scene=self, M=translationMatrix([0,0,0]), mesh=mesh, shader=FlatShader()) for mesh in building_01]
        self.building_01 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_01]
        self.building_02 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([3,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_02]
        self.building_03 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([6,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_03]
        self.building_04 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([9,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_04]
        self.building_05 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([12,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_05]
        self.building_06 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([15,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_06]
        self.building_07 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([18,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_07]
        self.building_08 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([21,0,0]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_08]

            #Second row of buildings
        #buildings
        building_09 = load_obj_file('models/Building_02.obj')
        building_10 = load_obj_file('models/Building_04.obj')
        building_11 = load_obj_file('models/Building_03.obj')
        building_12 = load_obj_file('models/Building_01.obj')
        building_13 = load_obj_file('models/Building_04.obj')
        building_14 = load_obj_file('models/Building_02.obj')
        building_15 = load_obj_file('models/Building_03.obj')
        building_16 = load_obj_file('models/Building_01.obj')

        # self.building_01 = [DrawModelFromMesh(scene=self, M=translationMatrix([0,0,0]), mesh=mesh, shader=FlatShader()) for mesh in building_01]
        self.building_09 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_09]
        self.building_10 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([3,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_10]
        self.building_11 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([6,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_11]
        self.building_12 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([9,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_12]
        self.building_13 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([12,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_13]
        self.building_14 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([15,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_14]
        self.building_15 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([18,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_15]
        self.building_16 = [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([21,0,14]), scaleMatrix([0.4,0.4,0.4])) , mesh=mesh, shader=FlatShader()) for mesh in building_16]



        # self.building_01 = [DrawModelFromMesh(scene=self, M=translationMatrix([0,0,0]), mesh=mesh, shader=FlatShader()) for mesh in building_01]

        #floor
        floor = load_obj_file('models/rough_road.obj')
        self.floor = [DrawModelFromMesh(scene=self, M=translationMatrix([0,0,0]), mesh=mesh, shader=FlatShader()) for mesh in floor]
        

    def keyboard(self, event):
        '''
        Process additional keyboard events for this demo.
        '''
        Scene.keyboard(self, event)

        if event.key == pygame.K_1:
            print('--> using Flat shading')
            self.bunny.use_textures = True
            self.bunny.bind_shader('flat')


        elif event.key == pygame.K_2:
            print('--> using Texture shading')
            self.bunny.bind_shader('texture')


    def draw(self):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.camera.update()


        #plane
        for model in self.plane:
            model.draw()

        #race_car
        for model in self.race_car:
            model.draw()

        #draw tree
        for model in self.yellow_tree_01:
            model.draw()
        for model in self.yellow_tree_02:
            model.draw()
        for model in self.yellow_tree_03:
            model.draw()
        for model in self.yellow_tree_04:
            model.draw()
        for model in self.yellow_tree_05:
            model.draw()
        for model in self.yellow_tree_06:
            model.draw()

        #draw trex
        for model in self.trexy:
            model.draw()

        #draw buildings first row
        for model in self.building_01:
            model.draw()
        for model in self.building_02:
            model.draw()
        for model in self.building_03:
            model.draw()
        for model in self.building_04:
            model.draw()
        for model in self.building_05:
            model.draw()
        for model in self.building_06:
            model.draw()
        for model in self.building_07:
            model.draw()
        for model in self.building_08:
            model.draw()

        #draw buildings second row
        for model in self.building_09:
            model.draw()
        for model in self.building_10:
            model.draw()
        for model in self.building_11:
            model.draw()
        for model in self.building_12:
            model.draw()
        for model in self.building_13:
            model.draw()
        for model in self.building_14:
            model.draw()
        for model in self.building_15:
            model.draw()
        for model in self.building_16:
            model.draw()


        #draw floor
        for model in self.floor:
            model.draw()

        # # then we loop over all models in the list and draw them
        # for model in self.models:
        #     model.draw()

        # # also all models from the table
        # for model in self.table:
        #     model.draw()

        # # and for the box
        # for model in self.box:
        #     model.draw()

        # # for the bunny (it consists of a single mesh).
        # self.bunny.draw()

        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        pygame.display.flip()


if __name__ == '__main__':
    # initialises the scene object
    # scene = Scene(shaders='gouraud')
    # scene = ExeterScene()

    scene = ExeterScene()

    # starts drawing the scene
    scene.run()
