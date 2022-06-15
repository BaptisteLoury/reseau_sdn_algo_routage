from mininet.topo import Topo

class MininetTopo(Topo):

    def __init__(self, **params):
        Topo.__init__(*self,**params)

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1', ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='10.0.0.3')
        h4 = self.addHost('h4', ip='10.0.0.4')
        h5 = self.addHost('h5', ip='10.0.0.5')
        h6 = self.addHost('h6', ip='10.0.0.6')

        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)
        self.addLink(s3, h4)
        self.addLink(s4, h5)
        self.addLink(s4, h6)

topos = { 'topo':(lambda: MininetTopo())}

locations = {
    'c0':(700,120),
    's1':(450,150),
    's2':(200,350),
    's3':(450,350),
    's4':(700,350),
    'h1':(150,500),
    'h2':(250,500),
    'h3':(400,500),
    'h4':(500,500),
    'h5':(650,500),
    'h6':(750,500),
}