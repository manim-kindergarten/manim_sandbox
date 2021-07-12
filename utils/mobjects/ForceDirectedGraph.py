from manimlib import *
import math
# Not yet finished. 
class ForceDirectedGraph(VGroup):
    I = 2.5
    gdata  = [
            [.0,I,I,.0,.0,I],
            [I,.0,I,.0,.0,.0],
            [I,I,.0,I,.0,.0],
            [.0,.0,I,.0,I,.0],
            [.0,.0,.0,I,.0,I],
            [I,.0,.0,.0,I,.0]
        ]
    attaches = [Text(str(i))for i in range(6)]
    alpha = 1.0
    beta = 0.1
    k = 1.0
    eta = .8
    delta_t = 0.1

    def inverse(_):
        for i in range(len((_.gdata[0]))):
            for j in range(len((_.gdata[0]))):
                if(_.gdata[i][j] != 0):
                    _.gdata[i][j] = 0
                else:
                     _.gdata[i][j] = _.I
            

    def coulomb_force(_,a,b):
            dx = b.get_x() - a.get_x()
            dy = b.get_y() - a.get_y()
            ds2 = dx * dx + dy * dy
            ds = math.sqrt(ds2)
            ds3 = ds2 * ds
            if ds3 == 0.0:
                const = 0
            else:
                const   = _.beta / (ds2 * ds)
            return [-const * dx, -const * dy,.0]
        
    def hooke_force(_,xi, xj, dij):
        dx = xj.get_x() - xi.get_x()
        dy = xj.get_y() - xi.get_y()
        ds = math.sqrt(dx * dx + dy * dy)
        dl = ds - dij
        const = _.k*_.anchor.get_width() * dl / ds
        return [const * dx, const * dy,.0]

    def bouncing(_):
        def upd_edg(obj,dt):
            vg = VGroup()
            for i in range(_.node_num):
                for j in range(_.node_num):
                    # print(i*10+j)
                    if(_.gdata[i][j] != 0):
                        vg.add(Line(_.nodes[i].get_center(),_.nodes[j].get_center()))
            obj.become(vg)
        def adjust(obj,dt):
            for i in range(_.node_num):
                Fx = 0.0
                Fy = 0.0
                for j in range(_.node_num):
                    if(j==i):
                        continue
                    dij = _.gdata[i][j]*(_.anchor.get_width()/2)
                    Fij = 0.0
                    if(dij == .0):
                        # print("from {} to {} no dist, F = {} ".format(i, j,str(_.coulomb_force(obj[i], obj[j]))))
                        Fij = _.coulomb_force(obj[i], obj[j])
                    else:
                        # print("from {} to {} has dist, F = {} ".format(i, j,str(_.hooke_force(obj[i], obj[j],dij))))
                        Fij = _.hooke_force(obj[i], obj[j],dij)
                    Fx += Fij[0]
                    Fy += Fij[1]
                    
                _.v[i][0] = (_.v[i][0] + _.alpha * Fx * _.delta_t) * _.eta
                _.v[i][1] = (_.v[i][1] + _.alpha * Fy * _.delta_t) * _.eta
            for i in range(_.node_num):
                    obj[i].shift(_.v[i]*_.delta_t)
            _.nodes.move_to(_.anchor.get_center())
        _.edges.add_updater(upd_edg)
        _.nodes.add_updater(adjust)
        def update_attach(tgt):
            def anim(obj,dt):
                obj.next_to(_.nodes[tgt],RIGHT)
            return anim
        for isp in range(_.node_num):
            # print("isp = "+str(isp))
            _.attaches[isp].add_updater(update_attach(isp))


    def __init__(_, **kwargs):
        VGroup.__init__(_, **kwargs)
        _.anchor = Circle().set_opacity(0.0)
        _.add(_.anchor)
        _.v = []
        _.node_num = len(_.gdata[0])
        _.nodes = VGroup()
        _.edges = VGroup()
        # attaches = VGroup(attach[i] for i in attach)
        for i in range(_.node_num):
            _.add(_.attaches[i])
            _.nodes.add(Dot().move_to(np.array([random.random(),random.random(),0])))
        for i in range(_.node_num):
            # _.nodes.add(Dot().move_to(g[i+4].get_center()+0.5*LEFT))
            _.v.append(np.array([.0,.0,.0]))
        
        _.bouncing()

        _.add(_.edges,_.nodes)

class Test(Scene):
    def construct(_):
        a = ForceDirectedGraph()
        _.wait()
        _.add(a)
        _.wait(2)
        a.inverse()
        _.wait(2)
        a.scale(0.5)
        a.inverse()
        _.wait(2)
        a.inverse()
        a.bouncing()
        _.wait(2)
        a.inverse()
        _.wait(2)
        a.inverse()
        _.wait(2)