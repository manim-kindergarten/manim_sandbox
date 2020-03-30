from manimlib.imports import *
# From @author:Micoael_Primo
class PictureX(Scene):
    # I drew this frame by frame.
    # It may look like a bit squished after demostrating...
    # I twicked some attrs of manim to make it a real square-like star.
    # A bit like Neither star?

    # This is a stupid way to realize, as you can see,
    # enum every possible point on axis y and get the corrspounding x
    # at the x axis 

    def construct(_):
        ROD_LEN=2.5
        ln1=Line(np.array([-4,0,0]),np.array([4,0,0]),color=DARK_BLUE)
        ln2=Line(np.array([0,3,0]),np.array([0,-3,0]),color=DARK_BLUE)
        OFFSET_X = -ROD_LEN
        OFFSET_Y = -ROD_LEN
        _.add(Rectangle(width=2000,height=2000,fill_color=WHITE,fill_opacity=1.0))
        _.play(Write(ln1))
        _.play(Write(ln2))
        
        
        def getCroodWithArg(x):
            # First part of the animation
            return np.array([(ROD_LEN*ROD_LEN-x*x)**1/2+OFFSET_X,OFFSET_Y,0])

        def getCroodWithInverse(x):
            # Second part of the animation
            return np.array([2*ROD_LEN-((ROD_LEN*ROD_LEN-x*x))**1/2,0,0])

        def getCroodUP(x):
            # Third part of the animation
            return np.array([ROD_LEN-(ROD_LEN*ROD_LEN-(ROD_LEN-x)**2)**1/2,ROD_LEN,0])

        def getCroodUPL(x):
            # Final part of the animation
            return np.array([(ROD_LEN*ROD_LEN-(ROD_LEN-x)**2)**1/2,ROD_LEN,0])

        onScrGroup = VGroup()
        
        # Assuume the framerate is 60 fps
        FRAME_RATE = 60
        # So the frame interval is 1/60
        WAIT_INTERVAL = 1/FRAME_RATE
        # Each animation lasts for 120 frames
        PIECE_OF_THE_ANIMATION =120
        # So the delta is ROD's len divide by piece of the animation
        single = ROD_LEN/PIECE_OF_THE_ANIMATION

        for i in range(PIECE_OF_THE_ANIMATION):
            # Make an indicator for rendering purpose
            # Render frame by frame
            # Next part to Ln 98.
            print("Progressing G1 "+ str(i)+" of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = ROD_LEN-i*single
            line = Line(np.array([OFFSET_X,xCrood+OFFSET_Y,0]),getCroodWithArg(xCrood),color=GREEN).shift(ROD_LEN*UP+ROD_LEN*RIGHT)
            onScrGroup.add(line)
            _.add(onScrGroup)
            _.wait(WAIT_INTERVAL)
            onScrGroup.remove(line)
            _.remove(onScrGroup)

        for i in range(PIECE_OF_THE_ANIMATION+1):
            print("ProgressingG2 "+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = ROD_LEN-i*single
            line = Line(np.array([0,xCrood,0]),getCroodUPL(xCrood),color=YELLOW_E).shift(ROD_LEN*DOWN)
            onScrGroup.add(line)
            _.add(onScrGroup)
            _.wait(WAIT_INTERVAL)
            onScrGroup.remove(line)
            _.remove(onScrGroup)

        for i in range(PIECE_OF_THE_ANIMATION):
            print("ProgressingG3 "+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = i*single
            line = Line(np.array([ROD_LEN,xCrood,0]),getCroodUP(xCrood),color=BLUE).shift(ROD_LEN*LEFT+ROD_LEN*DOWN)
            onScrGroup.add(line)
            _.add(onScrGroup)
            _.wait(WAIT_INTERVAL)
            onScrGroup.remove(line)
            _.remove(onScrGroup)
        i=0
        for i in range(PIECE_OF_THE_ANIMATION):
            print("Progressing G4"+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            yCrood = i*single
            line = Line(np.array([2*ROD_LEN,yCrood,0]),getCroodWithInverse(yCrood),color=RED).shift(2*ROD_LEN*LEFT)
            onScrGroup.add(line)
            _.add(onScrGroup)
            _.wait(WAIT_INTERVAL)
            onScrGroup.remove(line)
            _.remove(onScrGroup)

        

    

        for i in range(PIECE_OF_THE_ANIMATION):

            print("Progressing A1"+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = ROD_LEN-i*single
            line = Line(np.array([OFFSET_X,xCrood+OFFSET_Y,0]),getCroodWithArg(xCrood),color=GREEN).shift(ROD_LEN*UP+ROD_LEN*RIGHT)
            onScrGroup.add(line)
            _.add(line)
            _.wait(WAIT_INTERVAL)
            # leave a copy of line every 10 frames
            if i%10!=0:
                _.remove(line)

        i=0
        

        for i in range(PIECE_OF_THE_ANIMATION):
            print("Progressing A2"+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = ROD_LEN-i*single
            line = Line(np.array([0,xCrood,0]),getCroodUPL(xCrood),color=YELLOW_E).shift(ROD_LEN*DOWN)
            onScrGroup.add(line)
            _.add(line)
            _.wait(WAIT_INTERVAL)
            if i%10!=0:
                _.remove(line)

        for i in range(PIECE_OF_THE_ANIMATION):
            print("ProgressingA3"+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            xCrood = i*single
            line = Line(np.array([ROD_LEN,xCrood,0]),getCroodUP(xCrood),color=BLUE).shift(ROD_LEN*LEFT+ROD_LEN*DOWN)
            onScrGroup.add(line)
            _.add(line)
            _.wait(WAIT_INTERVAL)
            if i%10!=0:
                _.remove(line)

        for i in range(PIECE_OF_THE_ANIMATION):
            print("Progressing A4"+ str(i)+"of "+str(PIECE_OF_THE_ANIMATION))
            yCrood = i*single
            line = Line(np.array([2*ROD_LEN,yCrood,0]),getCroodWithInverse(yCrood),color=RED).shift(2*ROD_LEN*LEFT)
            onScrGroup.add(line)
            _.add(line)
            _.wait(WAIT_INTERVAL)
            print(np.array([OFFSET_X,xCrood+OFFSET_Y,0]))
            print(+getCroodWithArg(xCrood))
            print("----")
            if i%10!=0:
                _.remove(line)
        
        _.wait(1)
        _.play(FadeOut(ln1),FadeOut(ln2))

        _.wait(2)
