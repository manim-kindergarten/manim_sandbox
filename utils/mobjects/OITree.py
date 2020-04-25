# from: @Micoael_Primo
from manimlib.imports import *


class Edge():
    def __init__(self, _nxt, _to):
        self.nxt = _nxt
        self.to = _to
        


class TreeScene(Scene):
    
    def init(self):
        '''
        Initilize the tree.
        '''
        self.cnt = 0
        self.edgnum = 21
        self.treeroot = 1
        self.factor = 1
        self.shiftup = 2
        self.radius = 0.3
        self.verbose = False

        self.lines = VMobject()
        self.tree = VMobject() 
        self.ids = VMobject()
        self.treeMobject = VGroup()
        self.edgemk = VMobject()

        self.edg = [Edge(0,0)]
        self.head = [0]*self.edgnum
        self.dep = [0]*self.edgnum
        self.sidecnt = [(0,0)]
        self.fa = [0]*self.edgnum
        self.pos = [np.array([0,self.shiftup,0])]
        self.out = [0]*self.edgnum
        self.dfsord=[0]
        self.hasone=[False]*self.edgnum
        self.omega = [2*PI]*self.edgnum
        self.tau = [0]*self.edgnum
        self.size=[1]*self.edgnum
        self.edgeQ = [(0,0)]

        for i in range(self.edgnum):
            x=Edge(0,0)
            self.edg.append(x)
        for i in range(self.edgnum):
            x=np.array([0,self.shiftup,0])
            self.pos.append(x)
        
    
    def add_edge(self,u,v):
        '''
        Add an edge from u to v.
        '''
        self.edgeQ.append((u,v));

    def remove_edge(self,u,v):
        '''
        Remove an edge from u to v.
        '''
        self.edgeQ.remove((u,v))
    
    def apply_edge(self):
        '''
        (private)
        Finally apply the edge.
        Appies the edge
        '''
        for (u,v) in self.edgeQ:
            if u==v:
                continue
            self.adde(u,v)

    def adde(self, u, v):
        '''
        (private)
        Add an edge applied on arraies inside.
        '''
        if self.verbose:
            print("Added edge  from and to"+str(u)+" "+str(v))
        self.hasone[u] = True
        self.hasone[v] = True

        self.out[u]=self.out[u]+1
        self.cnt = self.cnt+1

        self.edg[self.cnt].nxt = self.head[u]
        self.edg[self.cnt].to = v
        self.edg[self.cnt].top = 0
        self.edg[self.head[u]].top = self.cnt
        self.edg[self.cnt].bot = self.head[u]
        self.head[u] = self.cnt


    def dfs(self, x,layer,fat):
        '''
        (private)
        Get the basic arguments of the tree.
        '''
        self.dfsord.append(x)
        self.dep[x] = layer

        self.fa[x] = fat
        i = self.head[x]
        if i==0:
            self.size[x]=1
        while i != int(0):
            v = self.edg[i].to
            if v != fat:
                self.dfs(self.edg[i].to,layer+1,x)
            self.size[x]=self.size[x]+self.size[self.edg[i].to]
            i = self.edg[i].nxt

    def getpos(self,v):
        '''
        (private)
        Get the x-y crood position between of a tree.
        '''
        if v!= self.treeroot:
            u=self.fa[v]
            self.pos[v] = self.pos[u]+2*np.array([math.cos(self.tau[v]+self.omega[v]/2),math.sin(self.tau[v]+self.omega[v]/2),0])  
        yita = self.tau[v]
        i = self.head[v]
        while i != int(0):
            w = self.edg[i].to
            self.omega[w] = self.size[w]/self.size[1]*-self.factor*PI
            self.tau[w] = yita
            yita = yita+self.omega[w]
            if w!=self.fa[v]:
                self.getpos(self.edg[i].to)
            i = self.edg[i].nxt
            if self.verbose:
                print(i)

    def getxy(self):
        '''
        (private)
        Get the position between of a tree.
        '''
        self.getpos(self.treeroot)
        for i in range(1,self.edgnum):
            if self.hasone[i]:
                p=Circle(fill_color=GREEN,radius=0.25,fill_opacity=0.8,color=GREEN)
                p.move_to(self.pos[i])
                self.tree.add(p)
            else:
                p=Circle(fill_color=GREEN,radius=0.25,fill_opacity=0.8,color=GREEN)
                p.move_to(8*DOWN)
                self.tree.add(p)
        return self.tree

    def get_id(self):
        '''
        (private)
        Get the id between of a tree.
        '''
        for i in range(1,self.edgnum):
            if self.hasone[i]==True:
                ics=TextMobject(str(i))
                ics.move_to(self.pos[i]).shift((self.radius+0.1)*DOWN).scale(0.6)
                self.ids.add(ics)
        return self.ids

    def get_nodes(self):
        '''
        (private)
        Get the node (circle around the txts) of a tree.
        '''
        return self.tree
    
    def get_connection(self,x,fa):
        '''
        (private)
        Get the lines between of a tree.
        '''
        ln = Line(self.pos[self.fa[x]],self.pos[self.fa[x]],color=BLUE)
        ln = Line(self.pos[self.fa[x]],self.pos[x],color=BLUE)
        self.lines.add(ln)
        txt=TextMobject(str(len(self.lines)-1),color=WHITE)
        txt.move_to(ln).scale(0.5)
        self.edgemk.add(txt)
        self.sidecnt.append((fa,x))
        i = self.head[x]
        while i != int(0):
            w = self.edg[i].to
            if w != self.fa[x]:
                self.get_connection(self.edg[i].to,self.fa[x])
            i = self.edg[i].nxt
        return self.lines

    def highlight_point(self,id):
        """
        Focuses on a node to stress
        """
        if self.hasone[id]:
            self.play(FocusOn(self.pos[id]))
        else:
            p=Circle(fill_color=YELLOW,radius=0.25,fill_opacity=0.9,color=YELLOW)
            p.move_to(8*DOWN)
    
    def highlight_edge(self,frm,to):
        """
        Focuses on an edge to stress

        """
        for i in range(0,len(self.sidecnt)):
            u = self.sidecnt[i][0]
            v = self.sidecnt[i][1]
            if u!=0 and v!=0:
                if frm==u and to==v:
                    self.play(FocusOn(self.lines[i-1]))
                    break
    
    def get_instance_of_id(self,x):
        """
        Returns a instance of node which you can apply methods on.

        """
        return self.tree[x-1]

    def get_instance_of_edge(self,x):
        '''
        Returns a instance of edge which you can apply methods on.
        
        '''
        for i in range(0,len(self.sidecnt)):
            u = self.sidecnt[i][0]
            v = self.sidecnt[i][1]
            if u!=0 and v!=0:
                if frm==u and to==v:
                    return (self.lines[i-1])
                    break
    
    def get_arguments(self):
        '''
        (private)
        Get the datas of a tree.
        '''
        self.apply_edge()
        self.dfs(self.treeroot,self.treeroot,0)
        self.treeMobject.add(self.getxy())
        self.treeMobject.add(self.get_nodes())
        self.treeMobject.add(self.get_id())
        self.treeMobject.add(self.get_connection(self.treeroot,0))

    def restart(self):
        '''
        (private)
        Restart the tree. Clear all the mobjects and datas.
        '''
        self.cnt = 0
        self.edg = [Edge(0,0)]
        self.head = [0]*self.edgnum
        self.dep = [0]*self.edgnum
        self.sidecnt = [(0,0)]
        self.fa = [0]*self.edgnum
        self.pos = [np.array([0,self.shiftup,0])]
        self.out = [0]*self.edgnum
        self.dfsord=[0]
        self.hasone=[False]*self.edgnum
        self.omega = [2*PI]*self.edgnum
        self.tau = [0]*self.edgnum
        self.size=[1]*self.edgnum
        for i in range(self.edgnum):
            x=Edge(0,0)
            self.edg.append(x)
        for i in range(self.edgnum):
            x=np.array([0,self.shiftup,0])
            self.pos.append(x)
        self.lines = VMobject()
        self.tree = VMobject() 
        self.ids = VMobject()
        self.treeMobject = VGroup()

    def draw_tree(self):
        '''
        Show up the tree onto the screen.
        '''
        self.apply_edge()
        self.dfs(self.treeroot,self.treeroot,0)
        self.treeMobject.add(self.getxy())
        self.treeMobject.add(self.get_nodes())
        self.treeMobject.add(self.get_id())
        self.treeMobject.add(self.get_connection(self.treeroot,0))
        self.play(Write(self.treeMobject))

    def update_transform(self):
        '''
        Update the tree on the screen, which uses the latest data to 
        reposition and rebuild the tree.

        '''

        utter = self.treeMobject.copy()
        self.remove(self.treeMobject)
        self.restart()
        self.get_arguments()
        self.play(Transform(utter,self.treeMobject))
        self.add(self.treeMobject)
        self.remove(utter)
        #self.play(Write(self.treeMobject))
    
    def dynamic_add_edge(self,frm,to):
        '''
        Dynamic add an edge onto the screen while play a short animation.
        TODO: The animation is not smooth...
        '''
        self.add_edge(frm,to)
        self.update_transform()

    def dynamic_remove_edge(self,frm,to):
        '''
        Dynamic remove an edge onto the screen while play a short animation.
        TODO: The animation is not smooth...
        '''
        self.remove_edge(frm,to)
        self.update_transform()



class Demonstrate(TreeScene):
    def construct(_):
        _.init()
        _.draw_tree()
        _.dynamic_add_edge(1,2)
        _.dynamic_add_edge(2,1)
        _.dynamic_add_edge(1,3)
        _.dynamic_add_edge(3,1)
        _.dynamic_add_edge(1,5)
        _.dynamic_add_edge(5,1)
        _.dynamic_add_edge(3,4)
        _.dynamic_add_edge(4,3)
        #change the root
        _.treeroot = 3
        #update
        _.update_transform()
