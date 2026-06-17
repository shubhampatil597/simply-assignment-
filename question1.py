import simpy
def customer(env, server):
with server.request() as req:
yield req
print("Waiting time :", env.now - arrival)
yield env.timeout(2)
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)
for i in range(5):
env.process(customer(env, server))  # create customer (arrival)
env.run()