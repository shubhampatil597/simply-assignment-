import simpy

def customer(env, server):
    arrive = env.now

    with server.request() as req:
        yield req
        print("Wait:", env.now - arrive)
        yield env.timeout(3)

env = simpy.Environment()

server = simpy.Resource(env, capacity=2)

for i in range(5):
    env.process(customer(env, server))

env.run()