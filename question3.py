import simpy

def customer(env, server):
    with server.request() as req:
        yield req
        yield env.timeout(2)

def arrival(env, server):
    for i in range(8):
        env.process(customer(env, server))
        yield env.timeout(1)

env = simpy.Environment()

server = simpy.Resource(env, capacity=1)

env.process(arrival(env, server))

env.run()